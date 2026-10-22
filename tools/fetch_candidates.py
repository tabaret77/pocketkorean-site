#!/usr/bin/env python3
"""Download cover photo candidates (free licences that allow commercial use) for review.
Sources: Wikimedia Commons and Openverse (Flickr etc.). Writes media/candidates/<topic>/NN.jpg + credits.json.
Runs in GitHub Actions (.github/workflows/fetch-candidates.yml), commits to the media-candidates branch."""
import json, os, re, time, urllib.parse, urllib.request, html
from fetch_media import get, strip, OK, BAD, API, UA

ROOT = os.path.join(os.path.dirname(__file__), '..', 'media', 'candidates')
OV_OK = {'by', 'by-sa', 'cc0', 'pdm'}

def commons(q, n):
    p = {'action': 'query', 'format': 'json', 'generator': 'search', 'gsrnamespace': 6, 'gsrsearch': q + ' filetype:bitmap', 'gsrlimit': 20,
         'prop': 'imageinfo', 'iiprop': 'url|size|extmetadata', 'iiurlwidth': 1600, 'iiextmetadatafilter': 'LicenseShortName|Artist|ObjectName'}
    d = get(API + '?' + urllib.parse.urlencode(p)); out = []
    for pg in sorted((d.get('query') or {}).get('pages', {}).values(), key=lambda x: x.get('index', 99)):
        ii = (pg.get('imageinfo') or [{}])[0]; md = ii.get('extmetadata') or {}
        lic = strip((md.get('LicenseShortName') or {}).get('value'))
        if not OK.search(lic) or BAD.search(lic) or ii.get('width', 0) < 1000: continue
        out.append({'src': 'commons', 'title': pg['title'], 'url': ii.get('thumburl') or ii['url'], 'page': ii.get('descriptionurl'),
                    'author': strip((md.get('Artist') or {}).get('value'))[:80], 'license': lic})
        if len(out) >= n: break
    return out

def openverse(q, n):
    u = 'https://api.openverse.org/v1/images/?' + urllib.parse.urlencode({'q': q, 'license_type': 'commercial,modification', 'page_size': 20, 'mature': 'false'})
    try: d = get(u)
    except Exception: return []
    out = []
    for r in d.get('results', []):
        if r.get('license') not in OV_OK or (r.get('width') or 0) < 1000: continue
        lic = ('CC ' + r['license'].upper() + ' ' + (r.get('license_version') or '')).strip() if r['license'] not in ('cc0', 'pdm') else ('CC0' if r['license'] == 'cc0' else 'Public domain')
        out.append({'src': 'openverse/' + (r.get('source') or ''), 'title': r.get('title') or '', 'url': r['url'], 'page': r.get('foreign_landing_url'),
                    'author': (r.get('creator') or '')[:80], 'license': lic})
        if len(out) >= n: break
    return out

def main():
    topics = json.load(open(os.path.join(os.path.dirname(__file__), 'candidates.json')))
    for t, qs in topics.items():
        dd = os.path.join(ROOT, t); os.makedirs(dd, exist_ok=True); cred = []; seen = set(); i = 0
        for q in qs:
            for c in commons(q, 4) + openverse(q, 4):
                if c['url'] in seen: continue
                seen.add(c['url'])
                try: b = get(c['url'], binary=True)
                except Exception: continue
                if len(b) < 30000: continue
                i += 1; fn = f'{i:02d}.jpg'; open(os.path.join(dd, fn), 'wb').write(b)
                c.update(file=fn, query=q); cred.append(c); time.sleep(0.5)
        json.dump(cred, open(os.path.join(dd, 'credits.json'), 'w'), ensure_ascii=False, indent=1)
        print(t, i)

if __name__ == '__main__':
    main()
