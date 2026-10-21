#!/usr/bin/env python3
"""Fetch freely licensed photos from Wikimedia Commons into media/library/<group>/.

Only licences that allow commercial use and need nothing more than attribution
(public domain, CC0, CC BY, CC BY-SA) are kept. Every file gets a credits entry
(title, author, licence, source page) in media/library/credits.json.
Runs in GitHub Actions (see .github/workflows/fetch-media.yml).
"""
import json, os, re, time, html, urllib.parse, urllib.request

ROOT = os.path.join(os.path.dirname(__file__), '..', 'media', 'library')
UA = 'PocketKoreanMediaBot/1.0 (https://pocketkorean.com; hello@pocketkorean.com)'
API = 'https://commons.wikimedia.org/w/api.php'
OK = re.compile(r'^(public domain|pd\b|cc0|cc[- ]by(-sa)?[- ]?\d(\.\d)?)', re.I)
BAD = re.compile(r'\b(nc|nd|fair use|non-free)\b', re.I)

def get(url, binary=False):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                d = r.read()
                return d if binary else json.loads(d)
        except Exception as e:
            time.sleep(2 + 3 * i)
    raise RuntimeError('failed ' + url)

def strip(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s or '')).strip()

def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')[:60]

def search(q, width, n):
    p = {'action': 'query', 'format': 'json', 'generator': 'search', 'gsrnamespace': 6,
         'gsrsearch': q + ' filetype:bitmap', 'gsrlimit': 40, 'prop': 'imageinfo',
         'iiprop': 'url|size|mime|extmetadata', 'iiurlwidth': width,
         'iiextmetadatafilter': 'LicenseShortName|LicenseUrl|Artist|Credit|ImageDescription|Restrictions'}
    d = get(API + '?' + urllib.parse.urlencode(p))
    pages = sorted((d.get('query') or {}).get('pages', {}).values(), key=lambda x: x.get('index', 99))
    out = []
    for pg in pages:
        ii = (pg.get('imageinfo') or [{}])[0]
        m = ii.get('extmetadata') or {}
        lic = strip((m.get('LicenseShortName') or {}).get('value'))
        if not lic or not OK.search(lic) or BAD.search(lic):
            continue
        if ii.get('mime') not in ('image/jpeg', 'image/png'):
            continue
        if (ii.get('width') or 0) < 1000:
            continue
        out.append({
            'title': pg['title'],
            'query': q,
            'file_url': ii.get('url'),
            'thumb_url': ii.get('thumburl') or ii.get('url'),
            'source_page': ii.get('descriptionurl'),
            'author': strip((m.get('Artist') or {}).get('value'))[:200],
            'credit': strip((m.get('Credit') or {}).get('value'))[:200],
            'license': lic,
            'license_url': strip((m.get('LicenseUrl') or {}).get('value')),
            'description': strip((m.get('ImageDescription') or {}).get('value'))[:300],
            'restrictions': strip((m.get('Restrictions') or {}).get('value')),
        })
        if len(out) >= n:
            break
    return out

def main():
    cfg = json.load(open(os.path.join(ROOT, 'queries.json')))
    cpath = os.path.join(ROOT, 'credits.json')
    credits = json.load(open(cpath)) if os.path.exists(cpath) else []
    have = {c['title'] for c in credits}
    xp = os.path.join(ROOT, 'excluded.json')
    if os.path.exists(xp): have |= set(json.load(open(xp)))  # reviewed and removed (off-topic, logos, ads)
    for group, qs in cfg['groups'].items():
        os.makedirs(os.path.join(ROOT, group), exist_ok=True)
        for q in qs:
            try:
                items = search(q, cfg.get('width', 1600), cfg.get('per_query', 6))
            except Exception as e:
                print('search failed', q, e); continue
            for k, it in enumerate(items, 1):
                if it['title'] in have:
                    continue
                ext = '.png' if it['thumb_url'].lower().endswith('.png') else '.jpg'
                k2 = k
                while any(os.path.exists(os.path.join(ROOT, group, f"{slug(q)}-{k2}{e}")) for e in ('.jpg', '.png')):
                    k2 += 1
                name = f"{slug(q)}-{k2}{ext}"
                path = os.path.join(ROOT, group, name)
                try:
                    data = get(it['thumb_url'], binary=True)
                except Exception as e:
                    print('download failed', it['title'], e); continue
                open(path, 'wb').write(data)
                it['group'] = group
                it['file'] = f'media/library/{group}/{name}'
                it['attribution'] = f"{it['author'] or 'Unknown author'} / {it['license']} / Wikimedia Commons"
                credits.append(it); have.add(it['title'])
                print('ok', it['file'], it['license'])
                time.sleep(0.5)
    json.dump(credits, open(cpath, 'w'), ensure_ascii=False, indent=1)
    # human-readable list
    with open(os.path.join(ROOT, 'CREDITS.md'), 'w') as f:
        f.write('# Photo credits (Wikimedia Commons)\n\nUse each photo with the attribution shown. CC BY-SA photos: keep the same licence for edited versions.\n\n')
        for c in credits:
            f.write(f"- `{c['file']}` — {c['title']} — {c['author'] or 'Unknown'} — {c['license']} — {c['source_page']}\n")
    print('total', len(credits))

if __name__ == '__main__':
    main()
