"""Shared page layout for pocketkorean.com (used by the data generator and by blog.py)."""
import html, re
from strings import S

BASE = 'https://pocketkorean.com'
APP = 'https://app.pocketkorean.com'
# (data code, url code, hreflang, name)
LANGS = [('en', 'en', 'en', 'English'), ('es', 'es', 'es', 'Español'), ('vi', 'vi', 'vi', 'Tiếng Việt'),
         ('th', 'th', 'th', 'ภาษาไทย'), ('id', 'id', 'id', 'Bahasa Indonesia'),
         ('yue', 'zh-hk', 'zh-HK', '廣東話（香港）'), ('tw', 'zh-tw', 'zh-TW', '國語（台灣）')]
URL = {d: u for d, u, h, n in LANGS}
HL = {d: h for d, u, h, n in LANGS}
BY_URL = {u: d for d, u, h, n in LANGS}

def E(s): return html.escape(str(s or ''), quote=True)
def T(k, l, **kw): return S[k][l].format(**kw) if kw else S[k][l]
def clean(s): return re.sub(r'</?(b|i|em|strong|small|span)[^>]*>', '', str(s or ''))

LOGO = ('<svg class="logo" viewBox="0 0 100 100" aria-hidden="true"><rect width="100" height="100" rx="22" fill="#0047A0"/>'
        '<g transform="rotate(-8 50 40)"><rect x="33" y="14" width="34" height="42" rx="5" fill="#CD2E3A"/>'
        '<text x="50" y="40" text-anchor="middle" font-family="serif" font-weight="800" font-size="20" fill="#fff">가</text></g>'
        '<path d="M18 40H82V64Q82 86 50 88Q18 86 18 64Z" fill="#fff"/>'
        '<path d="M24 46H76V63Q76 80 50 82Q24 80 24 63Z" fill="none" stroke="#0047A0" stroke-width="1.6" stroke-dasharray="3 3"/></svg>')

def page(d, rel, title, desc, body, alts=True, canonical=None, image=None, og_type='website'):
    """rel: path inside the language folder ('' = language home). alts=False for pages that exist in one language only."""
    u = URL[d]
    canon = canonical or f'{BASE}/{u}/{rel}'
    links = ''
    if alts:
        for dd, uu, hh, nn in LANGS:
            links += f'<link rel="alternate" hreflang="{hh}" href="{BASE}/{uu}/{rel}">'
        links += f'<link rel="alternate" hreflang="x-default" href="{BASE}/en/{rel}">'
    langmenu = ''.join(f'<a href="/{uu}/{rel if alts else ""}"{" aria-current=\"true\"" if dd == d else ""} lang="{hh}">{nn}</a>'
                       for dd, uu, hh, nn in LANGS)
    img = image or f'{BASE}/icon-512.png'
    ld = ''
    if rel == '':
        ld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite",'
              f'"name":"Pocket Korean","alternateName":["PocketKorean","Pocket Korean – 11,000 Words, Grammar & TOPIK"],"url":"{BASE}/","inLanguage":"{HL[d]}"'
              '}</script>')
    return f'''<!doctype html><html lang="{HL[d]}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canon}">{links}
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:site_name" content="Pocket Korean"><meta property="og:type" content="{og_type}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{E(img)}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/icon-180.png">
<meta name="theme-color" content="#0047A0"><link rel="stylesheet" href="/assets/site.css">{ld}
</head><body>
<header class="top"><div class="wrap">
<a class="brand" href="/{u}/">{LOGO}<span>Pocket <b>Korean</b></span></a>
<nav><a href="/{u}/topik/">{T('nav_topik', d)}</a><a href="/{u}/grammar/">{T('nav_grammar', d)}</a><a href="/{u}/blog/">{T('nav_blog', d)}</a>
<a class="btn sm" href="{APP}/?lang={d}">{T('nav_app', d)}</a></nav></div></header>
<main class="wrap">{body}</main>
<footer><div class="wrap"><details class="langs"><summary>🌐 {T('choose_lang', d)}</summary><div>{langmenu}</div></details>
<p><a href="/privacy/">{T('privacy', d)}</a> · © 2026 Pocket Korean</p></div></footer>
</body></html>'''

def cta_box(d):
    return (f'<aside class="cta"><div><h2>{T("cta_box_h", d)}</h2><p>{T("cta_box_p", d)}</p></div>'
            f'<a class="btn" href="{APP}/?lang={d}">{T("cta_app", d)}</a></aside>')
