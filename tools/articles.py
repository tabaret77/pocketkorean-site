"""Build the article sections from content/articles/*.md (Pages CMS) — runs on every Cloudflare deploy.

Front matter of an article:
---
title: Why convenience stores show up in every K-drama
lang: en                  # en, es, vi, th, id, zh-hk, zh-tw
section: korea-today      # korea-today | life-travel | learn | words
category: culture         # see SECTIONS in layout.py
date: 2026-10-21
description: One or two sentences for the card and search results.
cover: /media/uploads/xyz.jpg      # optional
cover_credit: Photo: Name / CC BY 2.0   # required when the photo needs credit
phrase: 편의점             # optional "phrase from this story"
phrase_meaning: convenience store
draft: false
---
Markdown text…

Writes: /{lang}/{section}/, /{lang}/{section}/{category}/, /{lang}/{section}/{slug}/, fills the home page slots,
sitemap-articles.xml and _redirects (old /blog/ URLs).
"""
import os, re, sys, glob, json, shutil, datetime
sys.path.insert(0, os.path.dirname(__file__))
import yaml, markdown
from layout import LANGS, URL, BY_URL, BASE, APP, E, T, page, cta_box, phead, L, SECTIONS, SEC, CATS, ICON

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRCS = [os.path.join(ROOT, 'content', 'articles'), os.path.join(ROOT, 'content', 'blog')]
CATPHOTO = json.load(open(os.path.join(ROOT, 'data', 'catphoto.json'))) if os.path.exists(os.path.join(ROOT, 'data', 'catphoto.json')) else {}
COL = {'coral': '#B42323', 'sky': '#0B5A9A', 'mint': '#0B6B43', 'yellow': '#8A5E00'}

from urllib.parse import quote, unquote
try:
    _SPELL = {r[1].replace('/', '-') for r in json.load(open(os.path.join(ROOT, 'data', 'en', 'dict.json')))}
except Exception:
    _SPELL = set()
def _wordlink(m):
    w = unquote(m.group(2)).strip().replace('/', '-')
    return f'href="/{m.group(1)}/word/{quote(w)}/"' if w in _SPELL else m.group(0)

def read(fp):
    raw = open(fp, encoding='utf-8').read()
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)$', raw, re.S)
    if not m: return None
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except Exception:  # e.g. an unquoted colon in a value: fall back to simple "key: value" lines
        meta = {}
        for line in m.group(1).splitlines():
            k, _, v = line.partition(':')
            if k.strip() and _:
                v = v.strip().strip('"').strip("'")
                meta[k.strip()] = {'true': True, 'false': False}.get(v.lower(), v)
    body = m.group(2)
    if meta.get('draft'): return None
    lang = str(meta.get('lang') or 'en').strip().lower()
    d = BY_URL.get(lang) or {'yue': 'yue', 'tw': 'tw', 'zh': 'zh', 'zh-hans': 'zh', 'pt-br': 'pt'}.get(lang)
    if not d: print('skip (unknown lang):', fp, lang); return None
    sec = str(meta.get('section') or 'learn').strip()
    cat = str(meta.get('category') or '').strip()
    if sec not in SEC: print('skip (unknown section):', fp, sec); return None
    if cat not in [c for c, _ in SEC[sec][3]]: cat = SEC[sec][3][0][0]
    name = os.path.splitext(os.path.basename(fp))[0]
    slug = str(meta.get('slug') or re.sub(r'^\d{4}-\d{2}-\d{2}-', '', name)).strip().lower()
    slug = re.sub(r'[^\w\-]+', '-', slug, flags=re.U).strip('-') or name
    if slug in CATS: slug += '-1'
    date = meta.get('date') or name[:10]
    if isinstance(date, (datetime.date, datetime.datetime)): date = date.strftime('%Y-%m-%d')
    date = str(date)[:10]
    html_body = markdown.markdown(body, extensions=['extra', 'sane_lists'])
    html_body = re.sub(r'href="/([a-z-]+)/dictionary/\?q=([^"&#]+)"', _wordlink, html_body)
    text = re.sub(r'<[^>]+>', ' ', html_body)
    desc = str(meta.get('description') or re.sub(r'\s+', ' ', text).strip()[:160])
    return dict(d=d, sec=sec, cat=cat, slug=slug, title=str(meta.get('title') or slug), date=date, desc=desc,
                cover=str(meta.get('cover') or ''), credit=str(meta.get('cover_credit') or ''),
                phrase=str(meta.get('phrase') or ''), pmean=str(meta.get('phrase_meaning') or ''),
                off=str(meta.get('official_url') or '').strip(), offl=str(meta.get('official_label') or '').strip(),
                html=html_body, legacy='/blog/' in fp.replace(os.sep, '/'), name=name)

OFFICIAL = {'en': ('Official page', 'Poster, trailer and episode info'), 'es': ('Página oficial', 'Póster, tráiler e información de episodios'),
 'vi': ('Trang chính thức', 'Poster, trailer và thông tin các tập'), 'th': ('หน้าเว็บทางการ', 'โปสเตอร์ ตัวอย่าง และข้อมูลแต่ละตอน'),
 'id': ('Halaman resmi', 'Poster, trailer, dan info episode'), 'yue': ('官方網頁', '海報、預告片同每集資料'), 'tw': ('官方網頁', '海報、預告片與每集資訊'),
 'ja': ('公式ページ', 'ポスター、予告編、各話の情報'), 'zh': ('官方网页', '海报、预告片和每集信息'), 'pt': ('Página oficial', 'Pôster, trailer e informações dos episódios'),
 'ru': ('Официальная страница', 'Постер, трейлер и информация о сериях'), 'mn': ('Албан ёсны хуудас', 'Постер, трейлер, ангийн мэдээлэл')}

def official(p, d):
    if not p['off'].startswith('http'): return ''
    h, sub = OFFICIAL.get(d, OFFICIAL['en'])
    host = re.sub(r'^https?://(www\.)?', '', p['off']).split('/')[0]
    return (f'<a class="official" href="{E(p["off"])}" target="_blank" rel="noopener"><span><b>{h}</b>'
            f'<small>{E(p["offl"] or host)}</small><small>{sub}</small></span><span aria-hidden="true" class="ext">↗</span></a>')

def url(p): return f'/{URL[p["d"]]}/{p["sec"]}/{p["slug"]}/'

def acard(p, d, lead=False):
    ph = (f'<img src="{E(p["cover"])}" alt="" loading="lazy">' + (f'<small>{E(p["credit"])}</small>' if p['credit'] else '')) if p['cover'] \
        else f'<span class="gfx" lang="ko">{E(p["phrase"] or "가")}</span>'
    phrase = (f'<span class="phrase"><b>{T("phrase_story", d)}:</b> <b lang="ko">{E(p["phrase"])}</b>'
              f'{" = " + E(p["pmean"]) if p["pmean"] else ""}</span>') if p['phrase'] else ''
    return (f'<a class="acard c-{p["sec"]}{" lead" if lead else ""}" href="{url(p)}"><div class="ph">{ph}</div><div class="bd">'
            f'<span class="cat">{E(T(CATS[p["cat"]][1], d))}</span><h3>{E(p["title"])}</h3><p>{E(p["desc"])}</p>{phrase}</div></a>')

def _ph(p):
    return (f'<img src="{E(p["cover"])}" alt="" loading="lazy">' + (f'<small>{E(p["credit"])}</small>' if p['credit'] else '')) if p['cover'] \
        else f'<span class="gfx" lang="ko">{E(p["phrase"] or "가")}</span>'

def lead_story(p, d):
    phrase = (f'<span class="phrase"><b lang="ko">{E(p["phrase"])}</b>{E(p["pmean"])}</span>') if p['phrase'] else ''
    return (f'<a class="lead-story c-{p["sec"]}" href="{url(p)}"><div class="ph">{_ph(p)}</div>'
            f'<h3>{E(p["title"])}</h3><p>{E(p["desc"])}</p>{phrase}</a>')

def row(p, d):
    return (f'<a class="row c-{p["sec"]}" href="{url(p)}"><div class="ph">{_ph(p)}</div><div>'
            f'<span class="cat">{E(T(CATS[p["cat"]][1], d))}</span><h3>{E(p["title"])}</h3><p>{E(p["desc"])}</p></div></a>')

def placeholder(d, cat, href=None):
    """empty-state card for a category (photo + category name), used until articles exist"""
    ph = CATPHOTO.get(cat)
    img = f'<img src="{ph[0]}" alt="" loading="lazy"><small>{E(ph[1])}</small>' if ph else ''
    sec = CATS[cat][0]
    return (f'<a class="acard soon c-{sec}" href="{href or L(d, sec + "/" + cat + "/")}"><div class="ph">{img}</div><div class="bd">'
            f'<span class="cat">{E(T(SEC[sec][1], d))}</span><h3>{E(T(CATS[cat][1], d))}</h3><p>{T("no_articles", d)}</p></div></a>')

def chips(d, sec, cur=None):
    s = SEC[sec]
    out = f'<a class="chip{" on" if cur is None else ""}" href="{L(d, sec + "/")}">{T("all_in", d)}</a>'
    out += ''.join(f'<a class="chip{" on" if cur == c else ""}" href="{L(d, sec + "/" + c + "/")}">{E(T(k, d))}</a>' for c, k in s[3])
    if sec == 'learn':
        out += f'<a class="chip" href="{L(d, "topik/")}">{T("nav_topik", d)}</a><a class="chip" href="{L(d, "grammar/")}">{T("nav_grammar", d)}</a>'
    return f'<div class="chips">{out}</div>'

def write(path, html):
    fp = os.path.join(ROOT, path.strip('/'), 'index.html')
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, 'w', encoding='utf-8').write(html)

def build():
    posts = []
    for src in SRCS:
        for f in sorted(glob.glob(os.path.join(src, '*.md'))):
            p = read(f)
            if p: posts.append(p)
    posts.sort(key=lambda p: p['date'], reverse=True)
    urls = []; redirects = []
    have = {(p['d'], p['sec'], p['slug']) for p in posts}
    full = lambda p: all((dd, p['sec'], p['slug']) in have for dd, *_ in LANGS)
    for d, u, h, n in LANGS:
        mine = [p for p in posts if p['d'] == d]
        en = [p for p in posts if p['d'] == 'en']
        # clean old output
        for sec, *_ in SECTIONS:
            if os.path.isdir(os.path.join(ROOT, u, sec)): shutil.rmtree(os.path.join(ROOT, u, sec))
        if os.path.isdir(os.path.join(ROOT, u, 'blog')): shutil.rmtree(os.path.join(ROOT, u, 'blog'))
        for sec, key, col, cats in SECTIONS:
            secposts = [p for p in mine if p['sec'] == sec] or [p for p in en if p['sec'] == sec]
            def listing(items, cat=None):
                if items:
                    return f'<div class="grid">{"".join(acard(p, d, lead=(i == 0 and cat is None and len(items) > 2)) for i, p in enumerate(items))}</div>'
                cs = [cat] if cat else [c for c, _ in cats]
                return f'<div class="grid">{"".join(placeholder(d, c) for c in cs)}</div>'
            extra = ''
            if sec == 'learn':
                extra = (f'<div class="lessons" style="margin-top:44px"><a class="lesson" href="{L(d, "topik/")}"><img class="topik-mark sm" src="/assets/topik-mark.svg" width="92" height="24" alt="TOPIK"><span></span><span>{T("dict_bylevel", d)}</span></a>'
                         f'<a class="lesson" href="{L(d, "grammar/")}"><b>{T("grammar_h", d)}</b><span></span><span>{T("q_grammar_d", d)}</span></a>'
                         f'<a class="lesson" href="{L(d, "dictionary/")}"><b>{T("dict_search", d)}</b><span></span><span>{T("dict_hint", d)}</span></a>'
                         f'<a class="lesson" href="{L(d, "level-test/")}"><b>{T("lt_cta", d)}</b><span></span><span>{T("q_level_d", d)}</span></a></div>')
            body = phead(d, T(key, d), T(key, d), T(key + '_p', d), col, chips(d, sec), key=sec) + f'<div class="wrap" style="padding-top:36px;padding-bottom:64px">{listing(secposts)}{extra}</div>'
            write(f'/{u}/{sec}/', page(d, f'{sec}/', f'{T(key, d)} | Pocket Korean', T(key + '_p', d), body, wide=True, cur=sec))
            urls.append(f'{BASE}/{u}/{sec}/')
            for c, ck in cats:
                cp = [p for p in secposts if p['cat'] == c]
                crumbs = f'<p class="crumbs"><a href="{L(d, sec + "/")}">{T(key, d)}</a></p>'
                body = phead(d, T(key, d), T(ck, d), T(key + '_p', d), col, chips(d, sec, c), crumbs, key=sec) + f'<div class="wrap" style="padding-top:36px;padding-bottom:64px">{listing(cp, c)}</div>'
                write(f'/{u}/{sec}/{c}/', page(d, f'{sec}/{c}/', f'{T(ck, d)} – {T(key, d)} | Pocket Korean', T(key + '_p', d), body, wide=True, cur=sec))
                urls.append(f'{BASE}/{u}/{sec}/{c}/')
        for p in mine:
            key, col = SEC[p['sec']][1], SEC[p['sec']][2]
            cover = (f'<img class="cover" src="{E(p["cover"])}" alt="">' + (f'<p class="credit">{E(p["credit"])}</p>' if p['credit'] else '')) if p['cover'] else ''
            phrase = (f'<div class="phrasebox"><b>{T("phrase_story", d)}:</b> <b lang="ko">{E(p["phrase"])}</b>{" = " + E(p["pmean"]) if p["pmean"] else ""}'
                      f'<a class="more" style="margin-left:auto" href="{L(d, "dictionary/")}?q={E(p["phrase"])}">{T("dict_search", d)}</a></div>') if p['phrase'] else ''
            rel = [q for q in mine if q['sec'] == p['sec'] and q is not p][:3]
            more = (f'<div class="box"><span class="kicker">{T("more", d)}</span><div class="rows">{"".join(row(q, d) for q in rel)}</div></div>') if rel else ''
            body = (f'<div class="wrap layout2"><div class="main"><p class="crumbs"><a href="{L(d, p["sec"] + "/")}">{T(key, d)}</a> › '
                    f'<a href="{L(d, p["sec"] + "/" + p["cat"] + "/")}">{T(CATS[p["cat"]][1], d)}</a></p><article class="post">'
                    f'<h1>{E(p["title"])}</h1><p class="meta">{p["date"]}</p>{cover}{phrase}{official(p, d)}{p["html"]}</article></div>'
                    f'<aside class="sticky">{cta_box(d)}{more}</aside></div>')
            canon = BASE + url(p)
            img = (BASE + p['cover']) if p['cover'].startswith('/') else (p['cover'] or None)
            write(url(p), page(d, f'{p["sec"]}/{p["slug"]}/', f'{p["title"]} | Pocket Korean', p['desc'], body, alts=full(p),
                               canonical=canon, image=img, og_type='article', wide=True, cur=p['sec']))
            urls.append(canon)
            if p['legacy']: redirects.append(f'/{u}/blog/{p["slug"]}/ {url(p)} 301')
        redirects.append(f'/{u}/blog/ /{u}/learn/ 301')
        redirects.append(f'/{u}/blog/* /{u}/learn/ 301')
        home_slots(d, mine or [], en)
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f'<url><loc>{x}</loc></url>' for x in urls] + ['</urlset>']
    open(os.path.join(ROOT, 'sitemap-articles.xml'), 'w', encoding='utf-8').write('\n'.join(sm))
    open(os.path.join(ROOT, '_redirects'), 'w').write('\n'.join(redirects) + '\n')
    if os.path.exists(os.path.join(ROOT, 'sitemap-blog.xml')): os.remove(os.path.join(ROOT, 'sitemap-blog.xml'))
    print(f'articles: {len(posts)} posts, {len(urls)} pages')

def home_slots(d, mine, en):
    u = URL[d]
    fp = os.path.join(ROOT, u, 'index.html')
    if not os.path.exists(fp): return
    s = open(fp, encoding='utf-8').read()
    pick = lambda sec, k: ([p for p in mine if p['sec'] == sec] or [p for p in en if p['sec'] == sec])[:k]
    today = pick('korea-today', 4)
    t_html = (f'<div class="news">{lead_story(today[0], d)}<div class="rows">{"".join(row(p, d) for p in today[1:])}</div></div>' if today
              else f'<div class="grid">{"".join(placeholder(d, c) for c, _ in SEC["korea-today"][3])}</div>')
    life = pick('life-travel', 4)
    l_html = (f'<div class="grid g4">{"".join(acard(p, d) for p in life)}</div>' if life
              else f'<div class="grid g4">{"".join(placeholder(d, c) for c in ("transport", "food", "living", "festivals"))}</div>')
    learn = pick('learn', 4)
    le_html = f'<div class="grid" style="margin-top:20px">{"".join(acard(p, d) for p in learn)}</div>' if learn else ''
    dl = ([p for p in mine if p['cat'] == 'drama-lines'] or [p for p in en if p['cat'] == 'drama-lines'])[:1]
    if dl:
        p = dl[0]
        others = [q for q in (mine or en) if q['sec'] == 'words' and q is not p][:3] or [q for q in en if q['sec'] == 'words' and q is not p][:3]
        wl = ''.join(f'<a class="wl" href="{url(q)}"><b lang="ko">{E(q["phrase"] or q["title"])}</b><span class="tag">{E(T(CATS[q["cat"]][1], d))}</span></a>' for q in others)
        dr = (f'<div class="drama"><div class="l"><span class="pill">{T("drama_h", d)}</span><p class="line" lang="ko">“{E(p["phrase"] or p["title"])}”</p>'
              f'<p class="tr">{E(p["pmean"])}</p><p style="color:#E1E4FA">{E(p["desc"])}</p><a class="btn yellow" href="{url(p)}">{T("read_more", d)}</a></div>'
              f'<div class="r"><span class="kicker">{T("sec_words", d)}</span>{wl}<a class="more" style="color:#fff" href="{L(d, "words/")}">{T("see_all", d)}</a></div></div>')
    else:
        dr = (f'<div class="drama"><div class="l"><span class="pill">{T("drama_h", d)}</span><p class="line" lang="ko">“괜찮아요?”</p>'
              f'<p class="tr">{T("no_articles", d)}</p><a class="btn yellow" href="{L(d, "words/drama-lines/")}">{T("cat_drama", d)}</a></div>'
              f'<div class="r"><span class="kicker">{T("words_in_line", d)}</span><a class="wl" href="{L(d, "dictionary/")}?q=괜찮다"><b lang="ko">괜찮다</b><span class="tag">T1</span></a></div></div>')
    for name, html in (('TODAY', t_html), ('LIFE', l_html), ('LEARN', le_html), ('DRAMA', dr)):
        s = re.sub(rf'<!--{name}-->.*?<!--/{name}-->', lambda m: f'<!--{name}-->{html}<!--/{name}-->', s, flags=re.S)
    open(fp, 'w', encoding='utf-8').write(s)

if __name__ == '__main__':
    build()
