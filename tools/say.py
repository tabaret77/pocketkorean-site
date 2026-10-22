"""Listen buttons for Korean text in articles.

Every run of Korean in an article body becomes tappable. Audio comes from:
  1. the app's native recordings (11,000+ dictionary words and their example sentences), when the text matches;
  2. otherwise Google Cloud TTS through /api/tts (the worker only speaks texts listed in /data/tts.json).
"""
import glob, hashlib, html as H, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_AUDIO = None

def audio_map():
    """text -> (pack-slice list, which) from the English word buckets (audio is the same in every language)."""
    global _AUDIO
    if _AUDIO is None:
        _AUDIO = {}
        for f in glob.glob(os.path.join(ROOT, 'data', 'en', 'w', '*.json')):
            for de, lst in json.load(open(f, encoding='utf-8')).items():
                for w in lst:
                    a = w.get('a')
                    if not a: continue
                    _AUDIO.setdefault(norm(w['de']), (a, 'w'))
                    if w.get('ex') and len(a) > 4 and a[3] >= 0:
                        _AUDIO.setdefault(norm(w['ex']), (a, 'ex'))
    return _AUDIO

def norm(s):
    return re.sub(r'\s+', ' ', s).strip().rstrip('.!?').strip()

HANGUL = '가-힣'
JAMO = 'ㄱ-ㅎㅏ-ㅣ'
RUN = re.compile(rf'[{HANGUL}{JAMO}][{HANGUL}{JAMO}0-9 ~/,.!?…·\'"‘’“”-]*')

def speech(run):
    """Text to speak for a run, or '' when it should not get a button (grammar endings, fragments)."""
    t = run.strip()
    if '~' in t:                       # sentence patterns with a blank: skip
        return ''
    t = re.sub(r'\((?:으|이|을|를|은|는|과|와)\)', '', t)          # (으)ㄹ, (이)
    t = re.sub(r'(?<![\w가-힣])([가-힣]{1,2})/[가-힣]{1,2}(?![\w가-힣])', r'\1', t)   # 이/가 -> 이
    t = t.replace('~', ' ').replace('…', ' ')
    t = re.sub(r'\s+', ' ', t).strip(' ,/·-(\'"‘’“”')
    if re.search(f'[{JAMO}]', t) or not re.search(f'[{HANGUL}]', t):
        return ''
    if len(t) > 180:
        return ''
    return t

def attrs(t, tts):
    hit = audio_map().get(norm(t))
    if hit:
        a, which = hit
        return f' data-pa="{H.escape(json.dumps(a))}" data-which="{which}"'
    tts.add(t)
    return f' data-t="{H.escape(t)}"'

SPK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
       '<path d="M11 5 6 9H3v6h3l5 4z" fill="currentColor"/><path d="M15.5 8.5a5 5 0 0 1 0 7"/></svg>')

def button(t, tts, label='Listen'):
    return f'<button type="button" class="say-b" lang="ko"{attrs(t, tts)} aria-label="{H.escape(label)}: {H.escape(t)}">{SPK}</button>'

SKIP = {'h1', 'h2', 'h3', 'code', 'pre', 'button', 'script', 'style'}

def add(body, tts):
    """Wrap Korean runs in an article's HTML. Links keep working: a small button follows a Korean link instead."""
    out, stack, link_txt = [], [], None
    for part in re.split(r'(<[^>]+>)', body):
        if part.startswith('<'):
            m = re.match(r'<(/?)([a-zA-Z0-9]+)', part)
            if m:
                tag = m.group(2).lower()
                if m.group(1):
                    if tag in stack:
                        while stack and stack.pop() != tag: pass
                    if tag == 'a' and link_txt is not None:
                        out.append(part)
                        t = speech(H.unescape(link_txt))
                        if t and not any(s in SKIP for s in stack):
                            out.append(button(t, tts))
                        link_txt = None
                        continue
                elif not part.endswith('/>') and tag not in ('br', 'img', 'hr', 'input'):
                    stack.append(tag)
                    if tag == 'a': link_txt = ''
            out.append(part)
            continue
        if link_txt is not None:
            link_txt += part
            out.append(part)
            continue
        if any(s in SKIP for s in stack) or not re.search(f'[{HANGUL}]', part):
            out.append(part)
            continue
        raw = H.unescape(part)
        pos, buf = 0, []
        for m in RUN.finditer(raw):
            run = m.group(0)
            core = run.rstrip(' ,(/-\'"‘“')       # keep sentence-final . ! ? inside
            t = speech(core)
            if m.start() > 0 and raw[m.start() - 1] in '-–‑[(':   # grammar ending like -아요, pronunciation [자밉], (으)
                t = ''
            if not t:
                continue
            s, e = m.start(), m.start() + len(core)
            buf.append(H.escape(raw[pos:s], quote=False))
            buf.append(f'<span class="say" role="button" tabindex="0" lang="ko"{attrs(t, tts)}>{H.escape(core, quote=False)}</span>')
            pos = e
        buf.append(H.escape(raw[pos:], quote=False))
        out.append(''.join(buf))
    return ''.join(out)

def tts_key(t):
    return hashlib.sha1(t.encode('utf-8')).hexdigest()[:16]

def write_allow(tts):
    os.makedirs(os.path.join(ROOT, 'data'), exist_ok=True)
    json.dump(sorted({tts_key(t) for t in tts}), open(os.path.join(ROOT, 'data', 'tts.json'), 'w'), separators=(',', ':'))
