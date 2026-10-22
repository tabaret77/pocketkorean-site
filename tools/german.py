"""Pocket German section of pocketkorean.com.

  /german/           Korean      /german/en/   English      /german/ja/   Japanese
  each: index (search, intro, today's words + sentence of the day, Life in Germany grid, app features),
        dictionary/, today/, life/ (+ life/<slug>/ articles), app/ (web trial)
  /german/app/       the Pocket German web app (trial: A1 + topic words; see german_app.py)
  /german/data/      search index, word shards, pictures and the daily data used by /german/assets/pg.js

Source data: /home/claude/pgsrc (copied from the app: data/, data_en/, data_ja/, help2*/).
Articles: content/german/<lang>/<slug>.md  (front matter: title, date, summary, cover; body in Markdown)
Run: python3 tools/german.py   (after german_audio.py has built german/app/audio)
"""
import datetime, hashlib, html, json, os, re, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layout import PG_LOGO, PG_NAME, PG_BASE, PG_MENU, E, LOGO

SRC = '/home/claude/pgsrc'
OUT = '/home/claude/pocketkorean-site'
G = f'{OUT}/german'
BASE = 'https://pocketkorean.com'
GL = ['ko', 'en', 'ja']
DP = {'ko': 'data', 'en': 'data_en', 'ja': 'data_ja'}
HELP = {'ko': 'help2', 'en': 'help2_en', 'ja': 'help2_ja'}
APPFILE = {'ko': 'index.html', 'en': 'index_en.html', 'ja': 'index_ja.html'}
WEBAPP = {'ko': '/german/web/', 'en': '/german/web/index_en.html', 'ja': '/german/web/index_ja.html'}
LVS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
LVNAME = {'ko': ['입문', '초급', '중급', '중상급', '고급', '최상급'],
          'en': ['Beginner', 'Elementary', 'Intermediate', 'Upper intermediate', 'Advanced', 'Proficient'],
          'ja': ['入門', '初級', '中級', '中上級', '上級', '最上級']}
POS = {'명사': ('noun', '名詞'), '동사': ('verb', '動詞'), '형용사': ('adjective', '形容詞'), '표현': ('expression', '表現'), '부사': ('adverb', '副詞'),
       '속담': ('proverb', 'ことわざ'), '전치사': ('preposition', '前置詞'), '대명사': ('pronoun', '代名詞'), '감탄사': ('interjection', '間投詞'),
       '접속사': ('conjunction', '接続詞'), '수사': ('numeral', '数詞'), '관사': ('article', '冠詞')}
def pos_label(p, g):
    if g == 'ko': return p
    return '/'.join(POS.get(x, (x, x))[0 if g == 'en' else 1] for x in p.split('/'))

S = {
 'ko': dict(
   htitle='포켓독일어 · 그림과 발음으로 외우는 독일어 단어 17,780개',
   hdesc='A1부터 C2까지 독일어 단어 17,780개를 그림, 원어민 발음, 예문, 어원과 함께. 매일 바뀌는 오늘의 단어와 오늘의 한 문장, 웹에서 바로 써 보는 포켓독일어.',
   kick='A1–C2 · 17,780단어', h1='독일어 단어를<br>주머니에 넣고 다니세요',
   lead='단어 카드 한 장에 뜻과 그림, 원어민 발음, 예문, 어원까지. 하루 10분 미션으로 A1에서 C2까지 차근차근 올라가요.',
   ph='독일어·한국어로 찾기 (예: Haus, 집)', go='찾기', try_='웹에서 체험하기', soon='App Store 곧 출시',
   free='웹 체험판에서는 A1 단어와 주제별 단어를 무료로 볼 수 있어요.',
   tw='오늘의 단어', ts='오늘의 한 문장', tw_more='단어 카드로 보기', pat='문장 패턴', listen='듣기',
   life='독일 이야기', life_p='독일에서 살며 만나는 문화와 생활, 그리고 그 속의 독일어.', life_empty='첫 이야기를 준비하고 있어요. 곧 이곳에서 만나요.', more='더 보기',
   feat='앱에서는 이렇게 공부해요',
   feats=[('study', '그림이 있는 단어 카드', '관사 색, 복수형, 예문, 어원, 관련 어휘까지 카드 한 장에.'),
          ('mission', '하루 10분 미션', '새 단어와 복습할 단어를 섞은 오늘의 미션. 80점을 넘으면 성공이에요.'),
          ('testmc', '여러 가지 퀴즈', '그림 보고 맞히기, der·die·das 고르기, 철자 쓰기, 짝 맞추기까지.'),
          ('stats', '진도와 기억 상태', '레벨별 진도와 목표 레벨까지 남은 거리를 한눈에 보여 줘요.')],
   dict_t='독일어 단어 사전', dict_p='A1부터 C2까지 17,780개 단어를 독일어나 한국어로 찾아보세요.', dict_hint='찾고 싶은 단어를 입력하세요.',
   n_found='{n}개 단어', none='「{q}」에 맞는 단어가 없어요.', loading='불러오는 중…',
   forms='형태', ex='예문', ety='어원', rel='관련 어휘', tip='알아 두면 좋아요',
   in_app='이 단어의 발음은 앱에서 들을 수 있어요.',
   today_t='오늘의 단어 · 오늘의 한 문장', today_p='매일 새로운 주제의 단어 10개와 문장 하나가 바뀌어요. 앱의 ‘오늘의 한 문장’과 같은 문장이에요.',
   app_t='포켓독일어 웹 체험판', app_p='A1 단어와 주제별 단어를 웹에서 바로 써 보세요. 모든 레벨과 미션 기록은 앱에서 열려요.', app_open='체험판 열기',
   langs='언어', pk='Pocket Korean', foot='포켓독일어는 Pocket Korean을 만든 팀이 만들었어요.', read='읽기', date_fmt='{y}년 {m}월 {d}일'),
 'en': dict(
   htitle='Pocket German · 17,780 German words with pictures and native audio',
   hdesc='17,780 German words from A1 to C2 with pictures, native audio, examples and word origins. A new topic and a new sentence every day, and an app you can try on the web.',
   kick='A1–C2 · 17,780 words', h1='German words<br>that fit in your pocket',
   lead='One card per word: meaning, picture, native audio, an example and where the word comes from. Ten minutes a day takes you from A1 to C2.',
   ph='Search in German or English (e.g. Haus, house)', go='Search', try_='Try it on the web', soon='Coming soon to the App Store',
   free='The web version opens all A1 words and the topic word lists for free.',
   tw="Today's words", ts='Sentence of the day', tw_more='See them as cards', pat='Pattern', listen='Listen',
   life='Life in Germany', life_p='Culture and everyday life in Germany, and the German you meet along the way.', life_empty='The first stories are on their way.', more='More',
   feat='How the app helps you learn',
   feats=[('study', 'Picture word cards', 'Article colours, plurals, examples, origins and related words on one card.'),
          ('mission', 'A 10-minute daily mission', 'New words mixed with the ones due for review. Score 80 to pass.'),
          ('testmc', 'Quizzes of every kind', 'Name the picture, pick der, die or das, spell it, match the pairs.'),
          ('stats', 'Progress you can see', 'Level progress and how far you are from your goal level.')],
   dict_t='German dictionary', dict_p='Look up 17,780 words from A1 to C2 in German or English.', dict_hint='Type a word to start.',
   n_found='{n} words', none='No words match “{q}”.', loading='Loading…',
   forms='Forms', ex='Example', ety='Origin', rel='Related words', tip='Good to know',
   in_app='You can hear this word in the app.',
   today_t="Today's words · Sentence of the day", today_p='Ten words on a new topic and one new sentence, every day. It is the same sentence as in the app.',
   app_t='Pocket German on the web', app_p='Try A1 and the topic word lists right in your browser. Every level and your mission history open in the app.', app_open='Open the web version',
   langs='Language', pk='Pocket Korean', foot='Pocket German is made by the team behind Pocket Korean.', read='Read', date_fmt='{mon} {d}, {y}'),
 'ja': dict(
   htitle='ポケットドイツ語 · 絵と音声で覚えるドイツ語単語 17,780語',
   hdesc='A1からC2までのドイツ語単語17,780語を、イラスト・ネイティブ音声・例文・語源とともに。毎日変わる今日の単語と今日のひとこと、ウェブですぐ試せるポケットドイツ語。',
   kick='A1–C2 · 17,780語', h1='ドイツ語の単語を、<br>いつもポケットに',
   lead='1枚の単語カードに意味、イラスト、ネイティブ音声、例文、語源まで。1日10分のミッションでA1からC2まで一歩ずつ。',
   ph='ドイツ語か日本語で検索（例: Haus, 家）', go='検索', try_='ウェブで試す', soon='App Store 近日公開',
   free='ウェブ版ではA1の単語とテーマ別単語を無料で使えます。',
   tw='今日の単語', ts='今日のひとこと', tw_more='カードで見る', pat='文型', listen='聞く',
   life='ドイツ暮らし', life_p='ドイツで暮らして出会う文化と生活、そしてその中のドイツ語。', life_empty='最初の記事を準備しています。もうすぐ公開します。', more='もっと見る',
   feat='アプリではこう学びます',
   feats=[('study', 'イラスト付き単語カード', '冠詞の色、複数形、例文、語源、関連語まで1枚に。'),
          ('mission', '1日10分のミッション', '新しい単語と復習する単語を混ぜた今日のミッション。80点で合格です。'),
          ('testmc', 'いろいろなクイズ', '絵を見て答える、der・die・das を選ぶ、つづりを書く、ペアを合わせる。'),
          ('stats', '進み具合と記憶の状態', 'レベルごとの進み具合と目標レベルまでの距離がひと目で。')],
   dict_t='ドイツ語単語辞典', dict_p='A1からC2までの17,780語をドイツ語か日本語で検索できます。', dict_hint='単語を入力してください。',
   n_found='{n}語', none='「{q}」に合う単語がありません。', loading='読み込み中…',
   forms='変化形', ex='例文', ety='語源', rel='関連語', tip='ポイント',
   in_app='この単語の発音はアプリで聞けます。',
   today_t='今日の単語 · 今日のひとこと', today_p='毎日、新しいテーマの単語10語とひとことが入れ替わります。アプリの「今日のひとこと」と同じ文です。',
   app_t='ポケットドイツ語 ウェブ版', app_p='A1とテーマ別単語をブラウザですぐ試せます。すべてのレベルとミッションの記録はアプリで使えます。', app_open='ウェブ版を開く',
   langs='言語', pk='Pocket Korean', foot='ポケットドイツ語は Pocket Korean のチームが作っています。', read='読む', date_fmt='{y}年{m}月{d}日'),
}
HL = {'ko': 'ko', 'en': 'en', 'ja': 'ja'}
FONTS = {'ko': 'Noto+Sans+KR:wght@400;500;700', 'en': 'Atkinson+Hyperlegible:wght@400;700', 'ja': 'Noto+Sans+JP:wght@400;500;700'}
MON = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
def fdate(g, d):
    return S[g]['date_fmt'].format(y=d.year, m=d.month, d=d.day, mon=MON[d.month - 1])

def write(path, s):
    p = f'{G}/{path}'
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w').write(s)
def jdump(path, obj): write(path, json.dumps(obj, ensure_ascii=False, separators=(',', ':')))
def ver(path):
    return hashlib.md5(open(f'{G}/{path}', 'rb').read()).hexdigest()[:8]
def shard(i):
    """FNV-1a, low byte as two hex digits (pg.js uses the same)"""
    h = 0x811c9dc5
    for c in i.encode():
        h = ((h ^ c) * 0x01000193) & 0xffffffff
    return f'{h & 255:02x}'

# ---------- data ----------
W = {g: {} for g in GL}
for g in GL:
    for lv in LVS:
        for w in json.load(open(f'{SRC}/{DP[g]}/{lv}.json')):
            W[g][w['id']] = w
TOP = json.load(open(f'{SRC}/data/topics.json'))
DAILY = {g: json.load(open(f'{SRC}/{DP[g]}/daily.json')) for g in GL}
PICS, PMAP = {}, {}
for f in ['ill', 'ill_B1', 'ill_B2', 'ill_C1', 'ill_C2']:
    j = json.load(open(f'{SRC}/data/{f}.json')); PICS.update(j['pics']); PMAP.update(j['map'])
try:
    AUD = json.load(open(f'{G}/web/audio/idx2.json'))['m']
except OSError:
    AUD = {}
NWORDS = len(W['ko'])

def art(de):
    m = re.match(r'(der|die|das)\s', de)
    return m.group(1) if m else ''
def word_html(de):
    a = art(de)
    return f'<b class="a-{a}">{a}</b> {E(de[len(a) + 1:])}' if a else E(de)
def pic_svg(i):
    k = PMAP.get(i); p = k and PICS.get(k)
    return f'<svg viewBox="0 0 100 100" aria-hidden="true">{p}</svg>' if p else ''

def day_index(d, n):
    """same as the app: (day of year + year*7) % n"""
    return (d.timetuple().tm_yday + d.year * 7) % n

def data_files():
    # pictures, sharded like the words: {id: svg body}
    pics = {}
    for i, k in PMAP.items():
        if k in PICS: pics.setdefault(shard(i), {})[i] = PICS[k]
    for h, v in pics.items(): jdump(f'data/pic/{h}.json', v)
    for g in GL:
        idx = [[i, w['de'], w['ko'], w['lv']] for i, w in W[g].items()]
        jdump(f'data/{g}/idx.json', idx)
        sh = {}
        for i, w in W[g].items():
            sh.setdefault(shard(i), {})[i] = {k: w[k] for k in ('de', 'lv', 'forms', 'ko', 'ex', 'exk', 'ety', 'rel', 'tip') if w.get(k)} | {'pos': pos_label(w.get('pos', ''), g)}
        for h, v in sh.items(): jdump(f'data/{g}/w/{h}.json', v)
        today = {'t': [{'k': t['key'], 'e': t.get('emoji', ''), 'n': t['name'].get(g) or t['name']['ko'],
                        'w': [[i, W[g][i]['de'], W[g][i]['ko'], W[g][i]['lv']] for i in t['ids'] if i in W[g]]} for t in TOP['topics']],
                 'd': [[x['de'], x['ko'], x.get('pat', ''), x.get('note', ''), x.get('tag', ''), x.get('lv', '')] for x in DAILY[g]]}
        jdump(f'data/{g}/today.json', today)

# ---------- page shell ----------
CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'german.css')).read()
JS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'german.js')).read()

def url(g, p=''): return p if p.startswith('/') else f'{PG_BASE[g]}{p}'

def page(g, rel, title, desc, body, cur=None, alts=True):
    s = S[g]
    canon = f'{BASE}{url(g, rel)}'
    links = ''.join(f'<link rel="alternate" hreflang="{HL[x]}" href="{BASE}{url(x, rel)}">' for x in GL) + \
        f'<link rel="alternate" hreflang="x-default" href="{BASE}{url("en", rel)}">' if alts else ''
    first = next((p for p, t in PG_MENU[g] if cur and p.split('#')[0] == cur), None)
    nav = ''.join(f'<a href="{url(g, p)}"{" aria-current=\"page\"" if p == first else ""}>{E(t)}</a>' for p, t in PG_MENU[g])
    lsw = ''.join(f'<a href="{url(x, rel if alts else "")}" lang="{x}"{" aria-current=\"true\"" if x == g else ""}>{n}</a>'
                  for x, n in (('ko', '한국어'), ('en', 'English'), ('ja', '日本語')))
    pk = '/ja/' if g == 'ja' else '/en/'
    return f'''<!doctype html><html lang="{HL[g]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{canon}">{links}
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{canon}">
<meta property="og:image" content="{BASE}/german/assets/og.png"><meta property="og:site_name" content="{E(PG_NAME[g])}">
<link rel="icon" href="/german/assets/icon.svg" type="image/svg+xml"><meta name="theme-color" content="#151515">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800&amp;family={FONTS[g]}&amp;display=swap">
<link rel="stylesheet" href="/german/assets/pg-{CSSV}.css"></head>
<body class="pg" data-g="{g}" data-base="{url(g)}">
<header class="pgtop"><div class="pgw pgbar">
<a class="pgbrand" href="{url(g)}">{PG_LOGO}<span>{E(PG_NAME[g])}</span></a>
<nav class="pgnav" aria-label="{E(PG_NAME[g])}">{nav}</nav>
<div class="pgact"><nav class="pglang" aria-label="{s["langs"]}">{lsw}</nav><a class="pgpk" href="{pk}">{LOGO}<span>Pocket Korean</span></a></div>
</div></header>
<main id="main">{body}</main>
<footer class="pgfoot"><div class="pgw"><div class="pgfb"><a class="pgbrand" href="{url(g)}">{PG_LOGO}<span>{E(PG_NAME[g])}</span></a><p>{E(s["foot"])}</p></div>
<nav>{"".join(f'<a href="{url(g, p)}">{E(t)}</a>' for p, t in PG_MENU[g])}</nav>
<p class="pgcopy">© 2026 {E(PG_NAME[g])} · <a href="{pk}">Pocket Korean</a> · <a href="/privacy/">Privacy</a></p></div></footer>
<script src="/german/assets/pg-{JSV}.js" defer></script></body></html>'''

# ---------- blocks ----------
def search_form(g, big=False, q=''):
    s = S[g]
    return (f'<form class="pgsearch{" big" if big else ""}" role="search" action="{url(g, "dictionary/")}" method="get">'
            f'<label class="sr" for="pgq">{E(s["ph"])}</label><input id="pgq" name="q" type="search" value="{E(q)}" placeholder="{E(s["ph"])}" autocomplete="off" lang="{g}">'
            f'<button type="submit">{E(s["go"])}</button></form>')

def today_words(g, d, full=False):
    t = TOP['topics'][day_index(d, len(TOP['topics']))]
    ws = [W[g][i] for i in t['ids'] if i in W[g]]
    if full:
        def card(w):
            ex = f'<p class="wex" lang="de">{E(w["ex"])}</p><p class="wexk">{E(w.get("exk", ""))}</p>' if w.get('ex') else ''
            return (f'<li class="wcard"><span class="pic">{pic_svg(w["id"])}</span><div class="wb"><p class="wde" lang="de">{word_html(w["de"])}</p>'
                    f'<p class="wm">{E(w["ko"])}</p>{ex}<span class="lv l{w["lv"][0]}">{w["lv"]}</span></div></li>')
        items = ''.join(card(w) for w in ws)
    else:
        items = ''.join(f'<li><a href="{url(g, "dictionary/")}?q={E(w["de"])}"><span class="wde" lang="de">{word_html(w["de"])}</span>'
                        f'<span class="wm">{E(w["ko"])}</span><span class="lv l{w["lv"][0]}">{w["lv"]}</span></a></li>' for w in ws)
    name = t['name'].get(g) or t['name']['ko']
    return f'<div class="topic"><span class="emo" aria-hidden="true">{t.get("emoji", "")}</span><b>{E(name)}</b></div><ol class="{"wcards" if full else "wlist"}">{items}</ol>'

def today_sentence(g, d):
    n = day_index(d, len(DAILY[g])); x = DAILY[g][n]
    key = f'N{n:03d}'
    s = S[g]
    say = f'<button class="say" data-say="{key}" aria-label="{E(s["listen"])}">{SPK}</button>' if key in AUD else ''
    return (f'<p class="sde" lang="de">{E(x["de"])}{say}</p><p class="str">{E(x["ko"])}</p>'
            f'<div class="spat"><small>{E(s["pat"])}</small><p lang="de">{E(x.get("pat", ""))}</p></div>'
            f'<p class="snote">{E(x.get("note", ""))}</p><p class="stag"><span class="lv l{x.get("lv", "A")[0]}">{E(x.get("lv", ""))}</span> {E(x.get("tag", ""))}</p>')
SPK = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M11 5 6 9H3v6h3l5 4z" fill="currentColor"/><path d="M15.5 8.5a5 5 0 0 1 0 7M18.5 5.5a9 9 0 0 1 0 13"/></svg>'

# ---------- articles (content/german/<lang>/<slug>.md) ----------
def load_articles(g):
    out = []
    d = f'{OUT}/content/german/{g}'
    if not os.path.isdir(d): return out
    import markdown
    for f in sorted(os.listdir(d)):
        if not f.endswith('.md'): continue
        raw = open(f'{d}/{f}').read()
        meta, body = {}, raw
        m = re.match(r'---\n(.*?)\n---\n(.*)', raw, re.S)
        if m:
            body = m.group(2)
            for line in m.group(1).splitlines():
                if ':' in line:
                    k, v = line.split(':', 1); meta[k.strip()] = v.strip().strip('"')
        if meta.get('draft') == 'true': continue
        meta['slug'] = f[:-3]
        meta['html'] = markdown.markdown(body, extensions=['extra'])
        meta['dt'] = datetime.date.fromisoformat(meta.get('date', '2026-01-01'))
        out.append(meta)
    return sorted(out, key=lambda a: a['dt'], reverse=True)

def art_card(g, a):
    img = f'<img src="{E(a["cover"])}" alt="" loading="lazy">' if a.get('cover') else f'<span class="ph" aria-hidden="true">{PG_LOGO}</span>'
    return (f'<a class="acard" href="{url(g, "life/" + a["slug"] + "/")}"><span class="cov">{img}</span>'
            f'<span class="ab"><time datetime="{a["dt"]}">{fdate(g, a["dt"])}</time><b>{E(a.get("title", ""))}</b><span>{E(a.get("summary", ""))}</span></span></a>')

def art_grid(g, arts, n=None):
    s = S[g]
    if not arts:
        return f'<div class="aempty">{PG_LOGO}<p>{E(s["life_empty"])}</p></div>'
    return '<div class="agrid">' + ''.join(art_card(g, a) for a in arts[:n]) + '</div>'

# ---------- pages ----------
def home(g, d, arts):
    s = S[g]
    feats = ''.join(f'<li><figure><img src="/german/web/{HELP[g]}/{k}.jpg" alt="" loading="lazy" width="600" height="1200"></figure><h3>{E(t)}</h3><p>{E(p)}</p></li>' for k, t, p in s['feats'])
    body = f'''<section class="hero"><div class="pgw herow">
<div class="hcopy"><p class="kick">{E(s["kick"])}</p><h1>{s["h1"]}</h1><p class="lead">{E(s["lead"])}</p>
{search_form(g, True)}
<div class="hbtns"><a class="btn red" href="{WEBAPP[g]}">{E(s["try_"])}</a><span class="soon"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M16.4 12.6c0-2.4 2-3.6 2.1-3.7-1.2-1.7-3-1.9-3.6-2-1.5-.2-3 .9-3.8.9s-2-.9-3.3-.9c-1.7 0-3.3 1-4.2 2.5-1.8 3.1-.5 7.7 1.3 10.2.9 1.2 1.9 2.6 3.2 2.6 1.3-.1 1.8-.8 3.3-.8s2 .8 3.3.8c1.4 0 2.3-1.3 3.1-2.5 1-1.4 1.4-2.8 1.4-2.9 0 0-2.8-1.1-2.8-4.2zM14 5.2c.7-.8 1.2-2 1-3.2-1 0-2.3.7-3 1.5-.6.7-1.2 1.9-1.1 3.1 1.2.1 2.4-.6 3.1-1.4z"/></svg>{E(s["soon"])}</span></div>
<p class="free">{E(s["free"])}</p></div>
<div class="hart" aria-hidden="true"><svg class="hpk" viewBox="0 0 220 240"><g class="hk"><g transform="translate(110 88) rotate(-8)"><rect x="-40" y="-52" width="80" height="104" rx="11" fill="#DD0000"/><text x="0" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="64" fill="#FFCE00">Ä</text></g></g><path d="M18 120H202V168Q202 228 110 232Q18 228 18 168Z" fill="#fff"/><path class="hst" d="M32 134H188V166Q188 214 110 218Q32 214 32 166Z" fill="none" stroke="#151515" stroke-width="2.5" stroke-dasharray="6 6"/></svg>
<span class="flag"><i></i><i></i><i></i></span></div>
</div></section>
<section class="pgw today" id="today" data-today="{d.isoformat()}">
<article class="tcard words"><header><h2>{E(s["tw"])}</h2><time class="tdate" datetime="{d.isoformat()}">{fdate(g, d)}</time></header><div class="twb">{today_words(g, d)}</div>
<a class="tmore" href="{url(g, "today/")}#words">{E(s["tw_more"])}</a></article>
<article class="tcard sent"><header><h2>{E(s["ts"])}</h2></header><div class="tsb">{today_sentence(g, d)}</div></article>
</section>
<section class="pgw life"><header class="sh"><h2>{E(s["life"])}</h2><p>{E(s["life_p"])}</p>{f'<a href="{url(g, "life/")}">{E(s["more"])}</a>' if len(arts) > 6 else ""}</header>{art_grid(g, arts, 6)}</section>
<section class="feat"><div class="pgw"><h2>{E(s["feat"])}</h2><ul class="fl">{feats}</ul>
<div class="fcta"><a class="btn red" href="{WEBAPP[g]}">{E(s["try_"])}</a><span class="soon">{E(s["soon"])}</span></div></div></section>'''
    ld = ('<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@type': 'MobileApplication', 'name': PG_NAME[g],
          'operatingSystem': 'iOS', 'applicationCategory': 'EducationalApplication', 'inLanguage': HL[g], 'description': s['hdesc'],
          'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'}}, ensure_ascii=False) + '</script>')
    write(f'{g + "/" if g != "ko" else ""}index.html', page(g, '', s['htitle'], s['hdesc'], body + ld))

def phead(g, h1, p):
    return f'<section class="phead"><div class="pgw"><h1>{E(h1)}</h1><p>{E(p)}</p></div></section>'

def dictionary(g):
    s = S[g]
    labels = json.dumps({k: s[k] for k in ('n_found', 'none', 'loading', 'forms', 'ex', 'ety', 'rel', 'tip', 'in_app', 'listen', 'dict_hint')} |
                        {'lv': dict(zip(LVS, LVNAME[g]))}, ensure_ascii=False)
    body = (phead(g, s['dict_t'], s['dict_p']) +
            f'<section class="pgw dict" id="dict" data-l=\'{E(labels)}\'>{search_form(g)}<p class="dcount" aria-live="polite">{E(s["dict_hint"])}</p>'
            f'<div class="dgrid"><ol class="dres" id="dres"></ol><div class="dcard" id="dcard" hidden></div></div></section>')
    write(f'{g + "/" if g != "ko" else ""}dictionary/index.html', page(g, 'dictionary/', f'{s["dict_t"]} | {PG_NAME[g]}', s['dict_p'], body, cur='dictionary/'))

def today_page(g, d):
    s = S[g]
    body = (phead(g, s['today_t'], s['today_p']) +
            f'<section class="pgw todayp" data-today="{d.isoformat()}"><h2 id="words">{E(s["tw"])} <time class="tdate" datetime="{d.isoformat()}">{fdate(g, d)}</time></h2>'
            f'<div class="twb full">{today_words(g, d, full=True)}</div>'
            f'<h2 id="sentence">{E(s["ts"])}</h2><article class="tcard sent big"><div class="tsb">{today_sentence(g, d)}</div></article></section>')
    write(f'{g + "/" if g != "ko" else ""}today/index.html', page(g, 'today/', f'{s["today_t"]} | {PG_NAME[g]}', s['today_p'], body, cur='today/'))

def life(g, arts):
    s = S[g]
    body = phead(g, s['life'], s['life_p']) + f'<section class="pgw life">{art_grid(g, arts)}</section>'
    write(f'{g + "/" if g != "ko" else ""}life/index.html', page(g, 'life/', f'{s["life"]} | {PG_NAME[g]}', s['life_p'], body, cur='life/'))
    for a in arts:
        cover = f'<figure class="acov"><img src="{E(a["cover"])}" alt=""></figure>' if a.get('cover') else ''
        body = (f'<article class="pgw post"><p class="crumb"><a href="{url(g, "life/")}">{E(s["life"])}</a></p><h1>{E(a.get("title", ""))}</h1>'
                f'<time datetime="{a["dt"]}">{fdate(g, a["dt"])}</time>{cover}<div class="prose">{a["html"]}</div></article>'
                f'<section class="pgw life"><header class="sh"><h2>{E(s["life"])}</h2></header>{art_grid(g, [x for x in arts if x is not a], 3)}</section>')
        write(f'{g + "/" if g != "ko" else ""}life/{a["slug"]}/index.html',
              page(g, f'life/{a["slug"]}/', f'{a.get("title", "")} | {PG_NAME[g]}', a.get('summary', ''), body, cur='life/', alts=False))

def app_page(g):
    """/german[/en|/ja]/app/: a short page that opens the web trial in the right language"""
    s = S[g]
    target = f'/german/app/{APPFILE[g] if g != "ko" else ""}'
    body = (phead(g, s['app_t'], s['app_p']) +
            f'<section class="pgw appgo"><a class="btn red big" href="{target}">{E(s["app_open"])}</a><p class="free">{E(s["free"])}</p>'
            f'<ul class="fl small">{"".join(f"<li><figure><img src=/german/web/{HELP[g]}/{k}.jpg alt=\'\' loading=lazy></figure><h3>{E(t)}</h3></li>" for k, t, p in s["feats"])}</ul></section>')
    write(f'{g + "/" if g != "ko" else ""}app/index.html'.replace('ko/', ''), page(g, 'app/', f'{s["app_t"]} | {PG_NAME[g]}', s['app_p'], body, cur='app/'))

def assets():
    global CSSV, JSV
    write('assets/pg.css', CSS); write('assets/pg.js', JS)
    CSSV, JSV = ver('assets/pg.css'), ver('assets/pg.js')
    for f in os.listdir(f'{G}/assets'):
        if re.match(r'pg-[0-9a-f]{8}\.(css|js)$', f): os.remove(f'{G}/assets/{f}')
    shutil.copy(f'{G}/assets/pg.css', f'{G}/assets/pg-{CSSV}.css'); shutil.copy(f'{G}/assets/pg.js', f'{G}/assets/pg-{JSV}.js')
    write('assets/icon.svg', PG_LOGO.replace(' class="logo pglogo"', ' xmlns="http://www.w3.org/2000/svg"'))

def sitemap():
    urls = []
    for g in GL:
        for p in ['', 'dictionary/', 'today/', 'life/']:
            urls.append(f'{BASE}{url(g, p)}')
        urls += [f'{BASE}{url(g, "life/" + a["slug"] + "/")}' for a in load_articles(g)]
    open(f'{OUT}/sitemap-german.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                                                   + ''.join(f'<url><loc>{u}</loc></url>' for u in urls) + '</urlset>')
    si = f'{OUT}/sitemap-index.xml'
    s = open(si).read()
    if 'sitemap-german.xml' not in s:
        s = s.replace('</sitemapindex>', f'<sitemap><loc>{BASE}/sitemap-german.xml</loc></sitemap></sitemapindex>')
        open(si, 'w').write(s)

def main():
    import zoneinfo
    d = datetime.datetime.now(zoneinfo.ZoneInfo('Europe/Berlin')).date()
    assets(); data_files()
    for g in GL:
        arts = load_articles(g)
        home(g, d, arts); dictionary(g); today_page(g, d); life(g, arts)
    sitemap()
    print('german: ok', NWORDS, 'words')

if __name__ == '__main__':
    main()
