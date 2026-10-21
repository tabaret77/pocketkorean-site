"""Shared page layout for pocketkorean.com (used by the data generator and by articles.py)."""
import html, re
from strings import S

BASE = 'https://pocketkorean.com'
APP = 'https://app.pocketkorean.com'
# (data code, url code, hreflang, name)
LANGS = [('en', 'en', 'en', 'English'), ('es', 'es', 'es', 'Español'), ('vi', 'vi', 'vi', 'Tiếng Việt'),
         ('th', 'th', 'th', 'ภาษาไทย'), ('id', 'id', 'id', 'Bahasa Indonesia'),
         ('yue', 'zh-hk', 'zh-HK', '廣東話（香港）'), ('tw', 'zh-tw', 'zh-TW', '國語（台灣）'),
         ('ja', 'ja', 'ja', '日本語'), ('zh', 'zh-cn', 'zh-CN', '简体中文'), ('pt', 'pt', 'pt-BR', 'Português (Brasil)'),
         ('ru', 'ru', 'ru', 'Русский'), ('mn', 'mn', 'mn', 'Монгол')]
URL = {d: u for d, u, h, n in LANGS}
HL = {d: h for d, u, h, n in LANGS}
BY_URL = {u: d for d, u, h, n in LANGS}

# Site structure. Each section has categories; articles (content/articles) pick one section + one category.
# (slug, string key, colour class)
SECTIONS = [
    ('korea-today', 'sec_today', 'coral', [('k-drama', 'cat_kdrama'), ('k-pop', 'cat_kpop'), ('culture', 'cat_culture'), ('trends', 'cat_trends')]),
    ('life-travel', 'sec_life', 'sky', [('living', 'cat_living'), ('places', 'cat_places'), ('food', 'cat_food'), ('transport', 'cat_transport'),
                                         ('festivals', 'cat_festivals'), ('survival-korean', 'cat_survival')]),
    ('learn', 'sec_learn', 'mint', [('topik-guide', 'cat_topik'), ('grammar-lessons', 'cat_grammar'), ('topic-words', 'cat_topicwords'), ('hangul', 'cat_hangul')]),
    ('words', 'sec_words', 'yellow', [('word-of-the-day', 'cat_wod'), ('drama-lines', 'cat_drama'), ('phrases', 'cat_phrases'), ('slang', 'cat_slang'),
                                      ('polite-casual', 'cat_polite')]),
]
SEC = {s[0]: s for s in SECTIONS}
# each section's hangul badge (what the section is called in Korean) and colour
BADGE = {'korea-today': ('오늘', 'coral'), 'life-travel': ('생활', 'sky'), 'learn': ('공부', 'mint'), 'words': ('단어', 'violet'),
         'dictionary': ('사전', 'blue'), 'name': ('이름', 'yellow'), 'level-test': ('실력', 'blue'), 'app': ('앱', 'blue'), 'about': ('소개', 'violet')}
def badge(key, big=False):
    k, c = BADGE.get(key, ('한', 'blue'))
    return f'<span class="badge b-{c}{" big" if big else ""}" lang="ko" aria-hidden="true">{k}</span>'
CATS = {c: (s[0], k) for s in SECTIONS for c, k in s[3]}

import hashlib, os as _os
def _ver(f):
    try: return hashlib.md5(open(_os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), 'assets', f), 'rb').read()).hexdigest()[:8]
    except OSError: return '1'
CSSV, JSV = _ver('site.css'), _ver('site.js')

def E(s): return html.escape(str(s or ''), quote=True)
def T(k, l, **kw):
    v = S[k].get(l) or S[k]['en']
    return v.format(**kw) if kw else v
def clean(s): return re.sub(r'</?(b|i|em|strong|small|span)[^>]*>', '', str(s or ''))

LOGO = ('<svg class="logo" viewBox="0 0 100 100" aria-hidden="true"><rect width="100" height="100" rx="24" fill="#2D4BFF"/>'
        '<g transform="rotate(-8 50 40)"><rect x="33" y="14" width="34" height="42" rx="5" fill="#FF6B6B"/>'
        '<text x="50" y="40" text-anchor="middle" font-family="serif" font-weight="800" font-size="20" fill="#fff">가</text></g>'
        '<path d="M18 40H82V64Q82 86 50 88Q18 86 18 64Z" fill="#fff"/>'
        '<path d="M24 46H76V63Q76 80 50 82Q24 80 24 63Z" fill="none" stroke="#2D4BFF" stroke-width="2" stroke-dasharray="3 3"/></svg>')

ICON = {
    'search': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
    'menu': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    'globe': '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 2.5 15.3 0 18M12 3c-2.5 2.7-2.5 15.3 0 18"/></svg>',
    'ig': '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".6" fill="currentColor"/></svg>',
    'yt': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="2.5" y="5.5" width="19" height="13" rx="4"/><path d="M10 9.5v5l4.5-2.5z" fill="currentColor"/></svg>',
    'tt': '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M14 3v11.5a3.5 3.5 0 1 1-3.5-3.5"/><path d="M14 3c.5 2.5 2.5 4.5 5 4.5"/></svg>',
    'speaker': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M11 5 6 9H3v6h3l5 4z" fill="currentColor"/><path d="M15.5 8.5a5 5 0 0 1 0 7M18.5 5.5a9 9 0 0 1 0 13"/></svg>',
}
# social accounts: fill in when they exist (empty = hidden)
SOCIAL = {'ig': '', 'yt': '', 'tt': ''}

def L(d, path=''):
    return f'/{URL[d]}/{path}'

def nav_cols(d):
    cols = []
    colour = {'coral': '#FF6B6B', 'sky': '#3DA0FF', 'mint': '#3DD598', 'yellow': '#FFD43B'}
    for slug, key, col, cats in SECTIONS:
        links = f'<a href="{L(d, slug + "/")}">{T("all_in", d)}</a>' + ''.join(f'<a href="{L(d, slug + "/" + c + "/")}">{T(k, d)}</a>' for c, k in cats)
        if slug == 'learn':
            links += f'<a href="{L(d, "topik/")}">{T("nav_topik", d)}</a><a href="{L(d, "grammar/")}">{T("nav_grammar", d)}</a>'
        cols.append((T(key, d), colour[col], links))
    cols.append((T('sec_dict', d), '#2D4BFF',
                 f'<a href="{L(d, "dictionary/")}">{T("dict_search", d)}</a><a href="{L(d, "topik/")}">{T("dict_bylevel", d)}</a>'
                 f'<a href="{L(d, "grammar/")}">{T("nav_grammar", d)}</a><a class="star" href="{L(d, "name/")}">{T("name_nav", d)} ★</a>'))
    cols.append(('Pocket Korean', '#9B6CFF',
                 f'<a href="{L(d, "level-test/")}">{T("lt_nav", d)}</a><a href="{L(d, "app/")}">{T("app_nav", d)}</a>'
                 f'<a href="{L(d, "about/")}">{T("about_nav", d)}</a><a href="/privacy/">{T("privacy", d)}</a>'))
    return cols

def page(d, rel, title, desc, body, alts=True, canonical=None, image=None, og_type='website', wide=False, cur=None):
    """rel: path inside the language folder ('' = language home). alts=False for pages that exist in one language only.
    wide=True: body brings its own full-width sections; otherwise it is wrapped in a content column."""
    u = URL[d]
    canon = canonical or f'{BASE}/{u}/{rel}'
    links = ''
    if alts:
        for dd, uu, hh, nn in LANGS:
            links += f'<link rel="alternate" hreflang="{hh}" href="{BASE}/{uu}/{rel}">'
        links += f'<link rel="alternate" hreflang="x-default" href="{BASE}/en/{rel}">'
    opts = ''.join(f'<option value="/{uu}/{rel if alts else ""}"{" selected" if dd == d else ""} lang="{hh}">{nn}</option>' for dd, uu, hh, nn in LANGS)
    img = image or f'{BASE}/icon-512.png'
    ld = ''
    if rel == '':
        ld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite",'
              f'"name":"Pocket Korean","alternateName":["PocketKorean","Pocket Korean – 11,000 Words, Grammar & TOPIK"],"url":"{BASE}/","inLanguage":"{HL[d]}",'
              f'"potentialAction":{{"@type":"SearchAction","target":"{BASE}/{u}/dictionary/?q={{q}}","query-input":"required name=q"}}'
              '}</script>')
    social = ''.join(f'<a class="sns" href="{E(v)}" aria-label="{n}" rel="noopener">{ICON[k]}</a>'
                     for k, n in (('ig', 'Instagram'), ('yt', 'YouTube'), ('tt', 'TikTok')) if (v := SOCIAL.get(k)))
    top = [(s[0], s[1]) for s in SECTIONS] + [('dictionary', 'sec_dict'), ('level-test', 'lt_nav')]
    navlinks = ''.join(f'<a href="{L(d, p + "/")}"{" aria-current=\"page\"" if cur == p else ""}>{T(k, d)}</a>' for p, k in top)
    mega = ''.join(f'<div class="col" style="--c:{c}"><p>{E(h)}</p>{ls}</div>' for h, c, ls in nav_cols(d))
    foot = ''.join(f'<div><p>{E(h)}</p>{ls}</div>' for h, c, ls in nav_cols(d))
    main = body if wide else f'<div class="wrap legacy">{body}</div>'
    return f'''<!doctype html><html lang="{HL[d]}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canon}">{links}
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:site_name" content="Pocket Korean"><meta property="og:type" content="{og_type}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{E(img)}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/icon-180.png">
<meta name="theme-color" content="#2446F0">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800&amp;family=Atkinson+Hyperlegible:wght@400;700&amp;family=Nanum+Myeongjo:wght@700;800&amp;family=Noto+Sans+KR:wght@400;500;700&amp;display=swap">
<link rel="stylesheet" href="/assets/site-{CSSV}.css">{ld}
</head><body data-lang="{d}" data-u="{u}">
<a class="sr" href="#main">Skip to content</a>
<div class="util"><div class="wrap"><p>{T('util_tag', d)}</p><div class="r">{social}{'<span class="sep" aria-hidden="true"></span>' if social else ''}
<label for="langsel" style="display:inline-flex;align-items:center;gap:6px">{ICON['globe']}<span class="sr">{T('choose_lang', d)}</span></label>
<select id="langsel" onchange="location.href=this.value">{opts}</select></div></div></div>
<header class="top" id="top"><div class="wrap bar">
<a class="brand" href="/{u}/">{LOGO}<span>Pocket Korean</span></a>
<nav class="main" aria-label="Main">{navlinks}</nav>
<div class="acts"><a class="iconbtn" href="{L(d, 'dictionary/')}" aria-label="{T('dict_search', d)}">{ICON['search']}</a>
<button class="iconbtn" id="menubtn" aria-expanded="false" aria-controls="mega" aria-label="{T('menu', d)}">{ICON['menu']}</button>
<a class="btn sm" href="{L(d, 'app/')}">{T('nav_app', d)}</a></div></div>
<nav class="mega" id="mega" aria-label="{T('menu', d)}"><div class="wrap cols">{mega}</div>
<div class="strip"><div class="wrap"><div class="chips"><b>{T('popular', d)}</b>
<a class="chip" href="{L(d, 'learn/topik-guide/')}">{T('cat_topik', d)}</a><a class="chip" href="{L(d, 'grammar/')}">{T('nav_grammar', d)}</a>
<a class="chip" href="{L(d, 'words/slang/')}">{T('cat_slang', d)}</a><a class="chip" href="{L(d, 'name/')}">{T('name_nav', d)}</a></div>
<a class="btn sm" href="{L(d, 'level-test/')}">{T('lt_cta', d)}</a></div></div></nav>
</header>
<main id="main">{main}</main>
<footer class="site"><div class="wrap"><div class="cols">{foot}</div>
<div class="bottom"><span>© 2026 Pocket Korean <a style="margin-left:14px" href="/privacy/">{T('privacy', d)}</a></span><span id="credits"></span></div></div></footer>
<script src="/assets/site-{JSV}.js" defer></script>
</body></html>'''

def cta_box(d):
    return (f'<div class="cta"><div><h2>{T("cta_box_h", d)}</h2><p>{T("cta_box_p", d)}</p></div>'
            f'<a class="btn" href="{APP}/?lang={d}">{T("cta_app", d)}</a></div>')

def phead(d, kicker, h1, lead, colour='blue', chips='', crumbs='', key=None):
    b = badge(key, True) if key else ''
    k = f'<p class="kicker">{E(kicker)}</p>' if kicker and kicker != h1 else ''
    return (f'<section class="phead c-{colour}"><div class="wrap">{crumbs}<div class="ph-t">{b}<div>{k}<h1>{E(h1)}</h1></div></div>'
            f'<p class="lead">{E(lead)}</p>{chips}</div></section>')
