"""Pre-generate article TTS audio after publishing (run by .github/workflows/tts-pack.yml).

1. Collect every Korean text that needs TTS (the same set the site build lists in /data/tts.json).
2. Wait until the live site has deployed that list, then fetch each missing text from https://pocketkorean.com/api/tts
   (the worker holds the Google key; nothing secret is needed here).
3. Append the MP3s to one new pack file in media/tts/ and record [pack, offset, length] in media/tts/index.json.
The next site build points the listen buttons at those slices, so audio plays instantly everywhere.
"""
import json, os, sys, time, urllib.parse, urllib.request
sys.path.insert(0, os.path.dirname(__file__))
import articles, say

SITE = os.environ.get('SITE', 'https://pocketkorean.com')
DIR = os.path.join(say.ROOT, 'media', 'tts')

def get(url, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'pocketkorean-tts-pack'}), timeout=60) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            if e.code in (400, 404): return e.code, b''
        except Exception:
            pass
        time.sleep(3 * (i + 1))
    return 0, b''

def main():
    articles.build()
    texts = sorted(articles.TTS)
    idx = say.tts_index()
    missing = [t for t in texts if say.tts_key(t) not in idx]
    print(f'{len(texts)} TTS texts, {len(missing)} without audio')
    if not missing: return
    want = {say.tts_key(t) for t in missing}
    for _ in range(40):                       # wait for the deploy that lists these texts (up to ~20 min)
        st, body = get(f'{SITE}/data/tts.json?ts={int(time.time())}')
        live = set(json.loads(body or b'[]')) if st == 200 else set()
        if want <= live: break
        print(f'waiting for deploy: {len(want - live)} texts not live yet'); time.sleep(30)
    os.makedirs(DIR, exist_ok=True)
    name = time.strftime('%Y%m%d-%H%M%S') + '.mp3'
    pack, done = bytearray(), 0
    for t in missing:
        st, mp3 = get(f'{SITE}/api/tts?t={urllib.parse.quote(t)}')
        if st != 200 or not mp3:
            print('skip', st, t); continue
        idx[say.tts_key(t)] = [f'/media/tts/{name}', len(pack), len(mp3)]
        pack += mp3; done += 1
    if not done: return
    open(os.path.join(DIR, name), 'wb').write(pack)
    json.dump(idx, open(os.path.join(DIR, 'index.json'), 'w'), separators=(',', ':'), sort_keys=True)
    print(f'packed {done} texts into media/tts/{name} ({len(pack) // 1024} KB)')

if __name__ == '__main__':
    main()
