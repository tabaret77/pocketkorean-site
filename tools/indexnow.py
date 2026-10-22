"""IndexNow: tell Bing, Yandex and other IndexNow engines about new article URLs right after they go live.
The key is public by design (it is served as /<key>.txt to prove we own the site)."""
import json, os, sys, time, urllib.request
KEY = '57db4ffcea862a591d850d5c1109729a'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://pocketkorean.com'

def write_key():
    open(os.path.join(ROOT, KEY + '.txt'), 'w').write(KEY)

def live(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'pocketkorean-indexnow'}), timeout=30) as r:
            return r.status == 200
    except Exception:
        return False

def submit(urls):
    urls = sorted(set(urls))
    if not urls: return print('no new URLs')
    for _ in range(40):                     # wait for the deploy (up to ~20 min)
        if live(f'{SITE}/{KEY}.txt') and live(urls[-1]): break
        time.sleep(30)
    body = json.dumps({'host': 'pocketkorean.com', 'key': KEY, 'keyLocation': f'{SITE}/{KEY}.txt', 'urlList': urls[:10000]}).encode()
    req = urllib.request.Request('https://api.indexnow.org/indexnow', data=body, method='POST', headers={'Content-Type': 'application/json; charset=utf-8'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r: print('IndexNow', r.status, len(urls), 'URLs')
    except urllib.error.HTTPError as e:
        print('IndexNow', e.code, e.read()[:200])

if __name__ == '__main__':
    # args: changed article files (content/articles/*.md) -> their live URLs
    sys.path.insert(0, os.path.dirname(__file__))
    import articles
    urls = []
    for f in sys.argv[1:]:
        if f.endswith('.md') and os.path.exists(f):
            p = articles.read(f)
            if p: urls.append(SITE + articles.url(p))
    submit(urls)
