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

def read(fp):
    raw = open(fp, encoding='utf-8').read()
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)$', raw, re.S)
    meta, body = (yaml.safe_load(m.group(1)) or {}, m.group(2)) if m else ({}, raw)
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
    text = re.sub(r'<[^>]+>', ' ', html_body)
    desc = str(meta.get('description') or re.sub(r'\s+', ' ', text).strip()[:160])
    return dict(d=d, sec=sec, cat=cat, slug=slug, title=str(meta.get('title') or slug), date=date, desc=desc,
                cover=str(meta.get('cover') or ''), credit=str(meta.get('cover_credit') or ''),
                phrase=str(meta.get('phrase') or ''), pmean=str(meta.get('phrase_meaning') or ''),
                html=html_body, legacy='/blog/' in fp.replace(os.sep, '/'), name=name)

def url(p): return f'/{URL[p["d"]]}/{p["sec"]}/{p["slug"]}/'

def acard(p, d, lead=False):
    ph = (f'<img src="{E(p["cover"])}" alt="" loading="lazy">' + (f'<small>{E(p["credit"])}</small>' if p['credit'] else '')) if p['cover'] \
        else f'<span class="gfx" lang="ko">{E(p["phrase"] or "가")}</span>'
    phrase = (f'<span class="phrase"><b>{T("phrase_story", d)}:</b> <b lang="ko">{E(p["phrase"])}</b>'
              f'{" = " + E(p["pmean"]) if p["pmean"] else ""}</span>') if p['phrase'] else ''
    return (f'<a class="acard{" lead" if lead else ""}" href="{url(p)}"><div class="ph">{ph}</div><div class="bd">'
            f'<span class="cat">{E(T(CATS[p["cat"]][1], d))}</span><h3>{E(p["title"])}</h3><p>{E(p["desc"])}</p>{phrase}</div></a>')

def placeholder(d, cat, href=None):
    """empty-state card for a category (photo + category name), used until articles exist"""
    ph = CATPHOTO.get(cat)
    img = f'<img src="{ph[0]}" alt="" loading="lazy"><small>{E(ph[1])}</small>' if ph else ''
    sec = CATS[cat][0]
    return (f'<a class="acard" href="{href or L(d, sec + "/" + cat + "/")}"><div class="ph">{img}</div><div class="bd">'
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
                extra = (f'<div class="grid g4" style="margin-top:28px"><a class="tile" href="{L(d, "topik/")}" style="--bg-t:#FFF4CC;--fg-t:#8A5E00"><small>TOPIK</small><b>{T("nav_topik", d)}</b><span>{T("dict_bylevel", d)}</span></a>'
                         f'<a class="tile" href="{L(d, "grammar/")}" style="--bg-t:#E8FBF2;--fg-t:#0B6B43"><small>{T("nav_grammar", d)}</small><b>{T("grammar_h", d)}</b><span>{T("q_grammar_d", d)}</span></a>'
                         f'<a class="tile" href="{L(d, "dictionary/")}" style="--bg-t:#E6EAFF;--fg-t:#1F3BD1"><small>{T("sec_dict", d)}</small><b>{T("dict_search", d)}</b><span>{T("dict_hint", d)}</span></a>'
                         f'<a class="tile" href="{L(d, "level-test/")}" style="--bg-t:#FFE6E6;--fg-t:#B42323"><small>{T("lt_nav", d)}</small><b>{T("lt_cta", d)}</b><span>{T("q_level_d", d)}</span></a></div>')
            body = phead(d, T(key, d), T(key, d), T(key + '_p', d), col, chips(d, sec)) + f'<div class="wrap" style="padding-top:36px;padding-bottom:64px">{listing(secposts)}{extra}</div>'
            write(f'/{u}/{sec}/', page(d, f'{sec}/', f'{T(key, d)} | Pocket Korean', T(key + '_p', d), body, wide=True, cur=sec))
            urls.append(f'{BASE}/{u}/{sec}/')
            for c, ck in cats:
                cp = [p for p in secposts if p['cat'] == c]
                crumbs = f'<p class="crumbs"><a href="{L(d, sec + "/")}">{T(key, d)}</a></p>'
                body = phead(d, T(key, d), T(ck, d), T(key + '_p', d), col, chips(d, sec, c), crumbs) + f'<div class="wrap" style="padding-top:36px;padding-bottom:64px">{listing(cp, c)}</div>'
                write(f'/{u}/{sec}/{c}/', page(d, f'{sec}/{c}/', f'{T(ck, d)} – {T(key, d)} | Pocket Korean', T(key + '_p', d), body, wide=True, cur=sec))
                urls.append(f'{BASE}/{u}/{sec}/{c}/')
        for p in mine:
            key, col = SEC[p['sec']][1], SEC[p['sec']][2]
            cover = (f'<img class="cover" src="{E(p["cover"])}" alt="">' + (f'<p class="credit">{E(p["credit"])}</p>' if p['credit'] else '')) if p['cover'] else ''
            phrase = (f'<div class="phrasebox"><b>{T("phrase_story", d)}:</b> <b lang="ko">{E(p["phrase"])}</b>{" = " + E(p["pmean"]) if p["pmean"] else ""}'
                      f'<a style="margin-left:auto" href="{L(d, "dictionary/")}?q={E(p["phrase"])}">{T("dict_search", d)} →</a></div>') if p['phrase'] else ''
            rel = [q for q in mine if q['sec'] == p['sec'] and q is not p][:3]
            more = (f'<section style="margin-top:48px"><h2 style="font-size:26px">{T("more", d)}</h2><div class="grid">{"".join(acard(q, d) for q in rel)}</div></section>') if rel else ''
            body = (f'<div class="wrap" style="padding-top:36px;padding-bottom:64px"><p class="crumbs"><a href="{L(d, p["sec"] + "/")}">{T(key, d)}</a> › '
                    f'<a href="{L(d, p["sec"] + "/" + p["cat"] + "/")}">{T(CATS[p["cat"]][1], d)}</a></p><article class="post">'
                    f'<h1>{E(p["title"])}</h1><p class="meta">{p["date"]}</p>{cover}{phrase}{p["html"]}</article>{cta_box(d)}{more}</div>')
            canon = BASE + url(p)
            img = (BASE + p['cover']) if p['cover'].startswith('/') else (p['cover'] or None)
            write(url(p), page(d, f'{p["sec"]}/{p["slug"]}/', f'{p["title"]} | Pocket Korean', p['desc'], body, alts=False,
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
    t_html = (f'<div class="grid">{"".join(acard(p, d, lead=i == 0) for i, p in enumerate(today))}</div>' if today
              else f'<div class="grid">{"".join(placeholder(d, c) for c, _ in SEC["korea-today"][3])}</div>')
    life = pick('life-travel', 4)
    l_html = (f'<div class="grid g4">{"".join(acard(p, d) for p in life)}</div>' if life
              else f'<div class="grid g4">{"".join(placeholder(d, c) for c in ("transport", "food", "living", "festivals"))}</div>')
    learn = pick('learn', 4)
    le_html = f'<div class="grid" style="margin-top:20px">{"".join(acard(p, d) for p in learn)}</div>' if learn else ''
    dl = ([p for p in mine if p['cat'] == 'drama-lines'] or [p for p in en if p['cat'] == 'drama-lines'])[:1]
    if dl:
        p = dl[0]
        dr = (f'<div class="drama"><div class="l"><span class="pill">{T("drama_h", d)}</span><p class="line" lang="ko">“{E(p["phrase"] or p["title"])}”</p>'
              f'<p class="tr">{E(p["pmean"])}</p><p style="color:#E1E4FA">{E(p["desc"])}</p><a class="btn yellow" href="{url(p)}">{T("read_more", d)} →</a></div>'
              f'<div class="r"><span class="kicker">{T("cat_drama", d)}</span><a class="wl" href="{L(d, "words/drama-lines/")}"><span>{T("see_all", d)}</span><span>→</span></a></div></div>')
    else:
        dr = (f'<div class="drama"><div class="l"><span class="pill">{T("drama_h", d)}</span><p class="line" lang="ko">“괜찮아요?”</p>'
              f'<p class="tr">{T("no_articles", d)}</p><a class="btn yellow" href="{L(d, "words/drama-lines/")}">{T("cat_drama", d)} →</a></div>'
              f'<div class="r"><span class="kicker">{T("words_in_line", d)}</span><a class="wl" href="{L(d, "dictionary/")}?q=괜찮다"><b lang="ko">괜찮다</b><span class="tag">T1</span></a></div></div>')
    for name, html in (('TODAY', t_html), ('LIFE', l_html), ('LEARN', le_html), ('DRAMA', dr)):
        s = re.sub(rf'<!--{name}-->.*?<!--/{name}-->', lambda m: f'<!--{name}-->{html}<!--/{name}-->', s, flags=re.S)
    open(fp, 'w', encoding='utf-8').write(s)

if __name__ == '__main__':
    build()
