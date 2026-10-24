"""Listen buttons for German text on the Pocket German pages (Life in Germany posts, the tips and quiz of the word posts).

mark(html, g) finds German words and sentences in rendered HTML and puts a small speaker button after each one.
Audio comes from:
  1. german/media/tts/ packs (pre-generated: index.json {hash: [file, offset, length]}), when the text is there;
  2. otherwise /api/tts?l=de&t=… (the worker speaks only texts listed in /german/data/tts.json, German voice).
pack(texts) makes new packs with Google TTS — run it where a key is available:  GOOGLE_TTS_KEY_FILE=… python3 tools/german_say.py
"""
import base64, hashlib, html as H, json, os, re, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TTSDIR = os.path.join(ROOT, 'german', 'media', 'tts')
TEXTS = set()          # every text marked during this build (→ /german/data/tts.json)
LEX = NOUN = None
VERBISH = set()
SPK = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M11 5 6 9H3v6h3l5 4z" fill="currentColor"/><path d="M15.5 8.5a5 5 0 0 1 0 7"/></svg>'
EN_ONLY = set('the and to of is you your for with on at it this that are be can will have has was were they their them he she we our not or but if when what which who how why do does did a an my me us from by about into more most very just only also then than there here these those some any all one two get got make made'.split())
LAT = r"A-Za-zÄÖÜäöüßẞ"
RUN = re.compile(rf"[{LAT}][{LAT}\-’']*(?:[ ,]+[{LAT}][{LAT}\-’']*)*[.!?…]?")

def h16(t): return hashlib.sha1(t.encode()).hexdigest()[:16]

def lexicon(words):
    """words: iterable of app word dicts (de, ex, rel)."""
    global LEX, NOUN
    LEX, NOUN = set(), set()
    tok = lambda s: re.findall(rf"[{LAT}]+", s or '')
    for w in words:
        de = w.get('de', '')
        for t in tok(de) + tok(w.get('ex', '')): LEX.add(t.lower())
        for r in w.get('rel') or []:
            for t in tok(r.get('de') if isinstance(r, dict) else r): LEX.add(t.lower())
        m = re.match(r'(der|die|das)\s+([A-ZÄÖÜ]\w+)', de)
        if m: NOUN.add(m.group(2).lower())
        else:
            for t in tok(de): VERBISH.add(t.lower())

def STRICT(g): return g not in ('ko', 'ja', 'zh')   # Latin-script page languages: only clear German gets a button
def is_german(run, g):
    s = run.strip(' ,')
    toks = re.findall(rf"[{LAT}]+", s)
    if not toks or len(toks) > 18 or len(s) > 200: return False
    low = [t.lower() for t in toks]
    if any(t in EN_ONLY for t in low) or re.search(r"\w['’](s|t|re|ll|ve|m|d)\b", s): return False
    if any(t.isupper() and len(t) > 1 for t in toks): return False          # DB, ZDF, CET …
    known = sum(t in LEX for t in low) / len(low)
    signal = bool(re.search('[ÄÖÜäöüß]', s)) or bool(re.match(r'(der|die|das|ein|eine|einen)\s+[A-ZÄÖÜ]', s, re.I)) \
        or any(t[0].isupper() and t.lower() in NOUN for t in toks[1:]) or (toks[0][0].isupper() and low[0] in NOUN)
    # German nouns are capitalised: a lower-case token that is only known as a noun is English (star, plan, parade …)
    if any(t[0].islower() and t.lower() in NOUN and t.lower() not in VERBISH for t in toks): return False
    if len(toks) == 1:
        if STRICT(g): return signal and known == 1
        # on Korean/Japanese pages Latin text is nearly always German: accept capitalised words (nouns) too
        return len(toks[0]) >= 4 and (low[0] in LEX or toks[0][0].isupper() or signal)
    if STRICT(g) and not signal: return known == 1 and len(toks) >= 3 and re.search(r'[.!?]$', s) is not None
    return known >= (0.8 if STRICT(g) else 0.5) or (not STRICT(g) and signal)

def button(t):
    TEXTS.add(t)
    idx = index()
    tp = idx.get(h16(t))
    attr = f' data-tp="{tp[0]},{tp[1]},{tp[2]}"' if tp else ''
    return f'<button type="button" class="say xs" data-tts="{H.escape(t)}"{attr} aria-label="listen">{SPK}</button>'

_IDX = None
def index():
    global _IDX
    if _IDX is None:
        try: _IDX = json.load(open(os.path.join(TTSDIR, 'index.json')))
        except (OSError, ValueError): _IDX = {}
    return _IDX

SKIP = {'a', 'button', 'script', 'style', 'code', 'time', 'h1', 'figcaption', 'th', 'svg'}
def mark(html_, g):
    """Return html_ with speaker buttons after German runs."""
    if LEX is None: return html_
    from bs4 import BeautifulSoup, NavigableString
    soup = BeautifulSoup(html_, 'html.parser')
    for node in list(soup.find_all(string=True)):
        if not isinstance(node, NavigableString) or not node.strip(): continue
        par = node.parent; bad = False
        while par is not None and par.name != '[document]':
            if par.name in SKIP or 'src' in (par.get('class') or []) or 'nosay' in (par.get('class') or []) or 'say' in (par.get('class') or []) or par.get('lang') == 'de':
                bad = True; break
            par = par.parent
        if bad: continue
        text = str(node); out, last, hit = [], 0, False
        for m in RUN.finditer(text):
            if m.end() < len(text) and (text[m.end()].isalnum() or text[m.end()] in '@/'): continue   # wetter.com, a@b, a/b
            run = m.group(0).rstrip(' ,’\'-')
            if not is_german(run, g): continue
            hit = True
            out.append(H.escape(text[last:m.start()]))
            out.append(f'<span lang="de">{H.escape(run)}</span>{button(run)}')
            last = m.start() + len(run)
        if not hit: continue
        out.append(H.escape(text[last:]))
        node.replace_with(BeautifulSoup(''.join(out), 'html.parser'))
    return str(soup)

def pack(texts, key):
    """Synthesize texts missing from the index into a new pack file."""
    os.makedirs(TTSDIR, exist_ok=True)
    idx = index()
    todo = sorted(t for t in texts if h16(t) not in idx)
    if not todo: return 0
    n = len([f for f in os.listdir(TTSDIR) if f.endswith('.mp3')])
    name = f'p{n:03d}.mp3'; buf = bytearray()
    for t in todo:
        body = json.dumps({'input': {'text': t}, 'voice': {'languageCode': 'de-DE', 'name': 'de-DE-Neural2-G'},
                           'audioConfig': {'audioEncoding': 'MP3', 'speakingRate': 0.92}}).encode()
        r = urllib.request.urlopen(urllib.request.Request(f'https://texttospeech.googleapis.com/v1/text:synthesize?key={key}', data=body,
                                                          headers={'content-type': 'application/json'}), timeout=60)
        a = base64.b64decode(json.load(r)['audioContent'])
        idx[h16(t)] = [name, len(buf), len(a)]; buf += a
    open(os.path.join(TTSDIR, name), 'wb').write(bytes(buf))
    json.dump(idx, open(os.path.join(TTSDIR, 'index.json'), 'w'), separators=(',', ':'))
    return len(todo)

if __name__ == '__main__':
    texts = json.load(open(os.path.join(ROOT, 'german', 'data', 'tts_texts.json')))
    key = open(os.environ['GOOGLE_TTS_KEY_FILE']).read().strip()
    print('new clips:', pack(texts, key))
