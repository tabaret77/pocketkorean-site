"""Images for Pocket German's 'Life in Germany' posts (daily news briefing + culture post), rendered with Chromium.

Usage from Python:
    from german_cards import news_cover, news_card, life_cover, life_card, render
    news_cover('ko', date(2026,10,22), hook='…', items=['…','…','…'], out='german/media/life/2026-10-22/news-ko-cover.jpg')
    news_card('ko', 1, date(...), headline='…', keyword='…', big='−17', big_unit='센트', big_label='…', note='…',
              side=[('…','…'), ('…','…')], out='…/news-ko-01.jpg')
    life_cover('ko', title='…', kicker='…', emoji='🥨', out='…')
    life_card('ko', heading='…', points=[('🥨','…','…'), …], out='…')        # 2–4 illustrated points
    render(html_body, width, height, out)                                     # anything else (charts, tables, maps)
Design: the news cards follow the 'B style' of Sarah's German news posts (navy, red NEWS box, yellow keyword, flag bar);
life cards use the Pocket German look (paper, index cards, black/red/gold). Footer: Pocket German wordmark.
"""
import asyncio, datetime, html, os

FONT = {'ko': "'Noto Sans CJK KR'", 'ja': "'Noto Sans CJK JP'", 'en': "'Noto Sans CJK KR'"}
WD = {'ko': '월화수목금토일', 'ja': '月火水木金土日'}
BRAND = {'ko': '포켓<b style="color:#FF5A4E">독일어</b>', 'en': 'Pocket <b style="color:#FF5A4E">German</b>', 'ja': 'ポケット<b style="color:#FF5A4E">ドイツ語</b>'}
TODAY = {'ko': '오늘의 독일 뉴스', 'en': 'Germany today', 'ja': '今日のドイツニュース'}
E = lambda s: html.escape(str(s))

def dstr(lang, d):
    if lang == 'en':
        return d.strftime('%a, %-d %B %Y')
    return f'{d.year}. {d.month}. {d.day} ({WD[lang][d.weekday()]})'

FLAG = '<div style="display:flex;width:120px;height:8px;margin:14px 0 0"><i style="flex:1;background:#111"></i><i style="flex:1;background:#DC0000"></i><i style="flex:1;background:#FFCC00"></i></div>'
LOGO = ('<svg viewBox="0 0 100 100" width="30" height="30"><rect width="100" height="100" rx="24" fill="#151515"/><g transform="rotate(-8 50 38)">'
        '<rect x="32" y="12" width="36" height="46" rx="6" fill="#DD0000"/><text x="50" y="47" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="30" fill="#FFCE00">Ä</text></g>'
        '<path d="M16 48H84V68Q84 88 50 90Q16 88 16 68Z" fill="#fff"/></svg>')

def foot(lang, dark=True):
    c = '#8A97B5' if dark else '#5E6878'
    return f'<div style="position:absolute;left:56px;bottom:30px;display:flex;align-items:center;gap:10px;font-size:20px;color:{c}">{LOGO}<span>{BRAND[lang]}</span><span style="margin-left:8px">pocketkorean.com/german</span></div>'

def page(lang, w, h, body, bg='#0F1E3D'):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>*{{box-sizing:border-box;margin:0}}'
            f'body{{width:{w}px;height:{h}px;overflow:hidden;background:{bg};font-family:{FONT[lang]},"Noto Color Emoji",sans-serif;position:relative}}'
            f'b{{font-weight:900}}</style></head><body>{body}</body></html>')

async def _shot(doc, w, h, out):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': w, 'height': h})
        await pg.set_content(doc); await pg.wait_for_timeout(300)
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
        await pg.screenshot(path=out, type='jpeg', quality=88)
        await b.close()

def render(doc, w, h, out):
    """doc: a full HTML document (or a body fragment, wrapped in a blank white page)."""
    if '<html' not in doc:
        doc = f'<!doctype html><html><head><meta charset="utf-8"><style>*{{box-sizing:border-box}}body{{margin:0;width:{w}px;height:{h}px;font-family:"Noto Sans CJK KR","Noto Color Emoji",sans-serif}}</style></head><body>{doc}</body></html>'
    asyncio.run(_shot(doc, w, h, out))
    return out

def news_cover(lang, d, hook, items, out, hook_red=''):
    """1200×800: TODAY box + date, big title, flag, light card with the hook (hook_red: words to colour red), then the other items."""
    hk = E(hook)
    if hook_red and hook_red in hook:
        hk = hk.replace(E(hook_red), f'<span style="color:#DC0000">{E(hook_red)}</span>')
    li = ''.join(f'<li style="display:flex;gap:14px;align-items:flex-start;margin:0 0 12px"><i style="flex:none;width:14px;height:14px;margin-top:12px;background:{"#DC0000" if i < 2 else "#FFCC00"}"></i><span>{E(t)}</span></li>' for i, t in enumerate(items))
    body = (f'<div style="padding:52px 56px">'
            f'<div style="display:flex;align-items:center;gap:16px"><span style="background:#DC0000;color:#fff;font-weight:900;font-size:24px;padding:4px 14px;letter-spacing:.06em">TODAY</span>'
            f'<span style="color:#B7C2DC;font-size:24px">{E(dstr(lang, d))}</span></div>'
            f'<h1 style="color:#fff;font-size:76px;font-weight:900;margin-top:22px;letter-spacing:-.02em">{TODAY[lang]}</h1>{FLAG}'
            f'<div style="margin-top:30px;background:#F5F6FA;border-radius:24px;padding:30px 34px;color:#0F1E3D">'
            f'<p style="font-size:42px;font-weight:900;line-height:1.3">{hk}</p></div>'
            f'<ul style="list-style:none;padding:0;margin-top:26px;color:#E7ECF7;font-size:28px;font-weight:700;line-height:1.5">{li}</ul></div>{foot(lang)}')
    return render(page(lang, 1200, 800, body), 1200, 800, out)

def news_card(lang, n, d, headline, out, keyword='', big='', big_unit='', big_label='', note='', side=()):
    """1200×800 summary card for news item n: headline (keyword in yellow), left big fact card, right 2–3 dark cards (line, sub)."""
    hl = E(headline)
    if keyword and keyword in headline:
        hl = hl.replace(E(keyword), f'<span style="color:#FFCC00">{E(keyword)}</span>')
    sd = ''.join(f'<div style="background:#1C2F57;border-radius:20px;padding:22px 26px"><p style="color:#FFCC00;font-size:30px;font-weight:900;line-height:1.25">{E(a)}</p>'
                 f'<p style="color:#B7C2DC;font-size:21px;margin-top:6px;line-height:1.4">{E(b)}</p></div>' for a, b in side)
    body = (f'<div style="padding:46px 56px">'
            f'<div style="display:flex;align-items:center;gap:16px"><span style="background:#DC0000;color:#fff;font-weight:900;font-size:22px;padding:4px 12px;letter-spacing:.06em">NEWS {n}</span>'
            f'<span style="color:#B7C2DC;font-size:22px">{TODAY[lang]} · {E(dstr(lang, d))}</span></div>'
            f'<h2 style="color:#fff;font-size:50px;font-weight:900;margin-top:20px;line-height:1.25;letter-spacing:-.02em">{hl}</h2>{FLAG}'
            f'<div style="display:grid;grid-template-columns:1.05fr 1fr;gap:22px;margin-top:30px">'
            f'<div style="background:#F5F6FA;border-radius:24px;padding:30px 32px;color:#0F1E3D;display:flex;flex-direction:column;justify-content:center;min-height:360px">'
            f'<p style="font-size:24px;color:#5E6B8A;font-weight:700">{E(big_label)}</p>'
            f'<p style="font-size:120px;font-weight:900;line-height:1.05;color:#DC0000;letter-spacing:-.03em">{E(big)}<span style="font-size:44px;color:#0F1E3D;margin-left:8px">{E(big_unit)}</span></p>'
            f'<p style="font-size:21px;color:#5E6B8A;margin-top:10px;line-height:1.45">{E(note)}</p></div>'
            f'<div style="display:flex;flex-direction:column;gap:16px;justify-content:center">{sd}</div></div></div>{foot(lang)}')
    return render(page(lang, 1200, 800, body), 1200, 800, out)

def life_cover(lang, title, out, kicker='', emoji='🇩🇪', emojis=()):
    """1200×630 cover in the Pocket German look: paper, big emoji on an index card, title."""
    ems = ''.join(f'<span style="position:absolute;font-size:{s}px;left:{x}px;top:{y}px;transform:rotate({r}deg)">{e}</span>'
                  for e, (x, y, s, r) in zip(emojis, [(70, 80, 70, -12), (980, 70, 64, 10), (1040, 430, 72, -8), (120, 470, 60, 12)]))
    body = (f'<div style="position:absolute;inset:0;background:radial-gradient(circle at 85% 15%,#fff 0,rgba(255,255,255,0) 40%),#F3F5F1"></div>{ems}'
            f'<div style="position:absolute;left:50%;top:70px;transform:translateX(-50%) rotate(-3deg);width:300px;height:220px;background:#fff;border-radius:8px 8px 18px 18px;'
            f'box-shadow:0 20px 40px -18px rgba(27,36,51,.45);display:grid;place-items:center;font-size:130px">'
            f'<i style="position:absolute;left:22px;top:0;bottom:0;width:2px;background:#D9483B;opacity:.4"></i>{emoji}</div>'
            f'<div style="position:absolute;left:0;right:0;top:330px;text-align:center;padding:0 80px">'
            f'<p style="font-size:24px;font-weight:700;color:#D9483B;letter-spacing:.04em">{E(kicker)}</p>'
            f'<h1 style="font-size:54px;font-weight:900;color:#1B2433;line-height:1.25;margin-top:10px;letter-spacing:-.02em">{E(title)}</h1></div>'
            f'<div style="position:absolute;left:540px;bottom:72px;display:flex;width:120px;height:8px"><i style="flex:1;background:#111"></i><i style="flex:1;background:#DC0000"></i><i style="flex:1;background:#FFCC00"></i></div>'
            f'{foot(lang, dark=False)}')
    return render(page(lang, 1200, 630, body, bg='#F3F5F1'), 1200, 630, out)

def life_card(lang, heading, points, out, h=560):
    """1200×560 illustrated summary: heading + 2–4 index cards, each (emoji, title, one line)."""
    n = len(points)
    cards = ''.join(f'<div style="position:relative;background:#fff;border-radius:8px 8px 18px 18px;box-shadow:0 18px 36px -20px rgba(27,36,51,.45);padding:26px 26px 26px 44px;transform:rotate({[-2,1.5,-1,2][i % 4]}deg)">'
                    f'<i style="position:absolute;left:24px;top:0;bottom:0;width:2px;background:#D9483B;opacity:.4"></i>'
                    f'<div style="font-size:64px">{e}</div><p style="font-size:30px;font-weight:900;color:#1B2433;margin-top:10px;line-height:1.25">{E(t)}</p>'
                    f'<p style="font-size:21px;color:#5E6878;margin-top:8px;line-height:1.45">{E(s)}</p></div>' for i, (e, t, s) in enumerate(points))
    body = (f'<div style="padding:50px 56px"><h2 style="font-size:44px;font-weight:900;color:#1B2433;letter-spacing:-.02em">{E(heading)}</h2>'
            f'<div style="display:flex;width:120px;height:8px;margin-top:14px"><i style="flex:1;background:#111"></i><i style="flex:1;background:#DC0000"></i><i style="flex:1;background:#FFCC00"></i></div>'
            f'<div style="display:grid;grid-template-columns:repeat({n},1fr);gap:24px;margin-top:40px">{cards}</div></div>{foot(lang, dark=False)}')
    return render(page(lang, 1200, h, body, bg='#F3F5F1'), 1200, h, out)
