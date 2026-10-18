"""Build the blog from content/blog/*.md.

Each post is a Markdown file with front matter, for example:

---
title: How to learn TOPIK vocabulary
lang: en            # en, es, vi, th, id, zh-hk, zh-tw
date: 2026-10-19
description: One or two sentences for search results and the post list.
cover: /assets/blog/my-image.jpg   # optional
draft: false                       # true = not published
---
Your text in Markdown...

Run:  python3 tools/blog.py   (Cloudflare Pages runs this on every deploy)
"""
import os, re, sys, glob, json, shutil, datetime
sys.path.insert(0, os.path.dirname(__file__))
import yaml, markdown
from layout import LANGS, URL, BY_URL, BASE, E, T, page, cta_box

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'content', 'blog')

def read_post(fp):
    raw = open(fp, encoding='utf-8').read()
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)$', raw, re.S)
    meta, body = (yaml.safe_load(m.group(1)) or {}, m.group(2)) if m else ({}, raw)
    if meta.get('draft'): return None
    lang = str(meta.get('lang') or 'en').strip().lower()
    d = BY_URL.get(lang) or ('yue' if lang in ('yue', 'zh-hk') else 'tw' if lang in ('tw', 'zh-tw') else None)
    if not d: print('skip (unknown lang):', fp, lang); return None
    name = os.path.splitext(os.path.basename(fp))[0]
    slug = str(meta.get('slug') or re.sub(r'^\d{4}-\d{2}-\d{2}-', '', name)).strip().lower()
    slug = re.sub(r'[^\w\-]+', '-', slug, flags=re.U).strip('-') or name
    date = meta.get('date') or name[:10]
    if isinstance(date, (datetime.date, datetime.datetime)): date = date.strftime('%Y-%m-%d')
    date = str(date)[:10]
    # body may be Markdown or HTML (the editor can save either); Markdown passes HTML through.
    html_body = markdown.markdown(body, extensions=['extra', 'sane_lists'])
    text = re.sub(r'<[^>]+>', ' ', html_body)
    desc = str(meta.get('description') or re.sub(r'\s+', ' ', text).strip()[:160])
    return dict(d=d, slug=slug, title=str(meta.get('title') or slug), date=date, desc=desc,
                cover=meta.get('cover') or '', html=html_body, src=os.path.relpath(fp, ROOT))

def card(p, d):
    u = URL[p['d']]
    img = f'<img src="{E(p["cover"])}" alt="" loading="lazy">' if p['cover'] else ''
    return (f'<a class="postcard" href="/{u}/blog/{p["slug"]}/">{img}<div><small>{p["date"]}</small>'
            f'<h3>{E(p["title"])}</h3><p>{E(p["desc"])}</p><span>{T("read_more", d)} →</span></div></a>')

def build():
    posts = [p for p in (read_post(f) for f in sorted(glob.glob(os.path.join(SRC, '*.md')))) if p]
    posts.sort(key=lambda p: p['date'], reverse=True)
    by = {d: [p for p in posts if p['d'] == d] for d, *_ in LANGS}
    urls = []
    for d, u, h, n in LANGS:
        out = os.path.join(ROOT, u, 'blog')
        if os.path.isdir(out): shutil.rmtree(out)
        os.makedirs(out, exist_ok=True)
        mine = by[d]
        if mine:
            lst = f'<div class="postlist">{"".join(card(p, d) for p in mine)}</div>'
        else:
            lst = f'<p class="note">{T("no_posts", d)}</p><div class="postlist">{"".join(card(p, d) for p in by["en"][:12])}</div>'
        body = f'<h1>{T("blog_h", d)}</h1><p class="lead">{T("blog_p", d)}</p>{lst}{cta_box(d)}'
        open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(
            page(d, 'blog/', f'{T("blog_h", d)} | Pocket Korean', T('blog_p', d), body))
        urls.append(f'{BASE}/{u}/blog/')
        for p in mine:
            pd = os.path.join(out, p['slug']); os.makedirs(pd, exist_ok=True)
            cover = f'<img class="cover" src="{E(p["cover"])}" alt="">' if p['cover'] else ''
            body = (f'<p class="crumbs"><a href="/{u}/blog/">{T("blog_h", d)}</a></p><article class="post">'
                    f'<h1>{E(p["title"])}</h1><p class="date">{p["date"]}</p>{cover}{p["html"]}</article>{cta_box(d)}'
                    f'<p><a class="btn ghost" href="/{u}/blog/">← {T("all_posts", d)}</a></p>')
            canon = f'{BASE}/{u}/blog/{p["slug"]}/'
            img = (BASE + p['cover']) if str(p['cover']).startswith('/') else (p['cover'] or None)
            open(os.path.join(pd, 'index.html'), 'w', encoding='utf-8').write(
                page(d, f'blog/{p["slug"]}/', f'{p["title"]} | Pocket Korean', p['desc'], body, alts=False,
                     canonical=canon, image=img, og_type='article'))
            urls.append(canon)
        # latest posts on the language home page
        home = os.path.join(ROOT, u, 'index.html')
        if os.path.exists(home):
            s = open(home, encoding='utf-8').read()
            show = (mine or by['en'])[:3]
            block = (f'<section><h2>{T("latest_posts", d)}</h2><div class="postlist">{"".join(card(p, d) for p in show)}</div>'
                     f'<p><a class="btn ghost" href="/{u}/blog/">{T("all_posts", d)} →</a></p></section>') if show else ''
            s2 = re.sub(r'<!--BLOG-->.*?<!--/BLOG-->', f'<!--BLOG-->{block}<!--/BLOG-->', s, flags=re.S)
            if s2 != s: open(home, 'w', encoding='utf-8').write(s2)
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f'<url><loc>{x}</loc></url>' for x in urls] + ['</urlset>']
    open(os.path.join(ROOT, 'sitemap-blog.xml'), 'w', encoding='utf-8').write('\n'.join(sm))
    print(f'blog: {len(posts)} posts, {len(urls)} pages')

if __name__ == '__main__':
    build()
