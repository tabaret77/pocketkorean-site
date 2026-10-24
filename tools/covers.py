"""Original cover illustrations for articles (1600x1000 JPG) in the site's manuscript-paper style.
No text other than Korean (covers are shared by all 12 languages). Rendered with Playwright.
usage: npm i --prefix /tmp/pkfonts @fontsource/nanum-myeongjo@5 && python3 tools/covers.py [cover-key ...]  -> media/covers/<cover-key>.jpg"""
import asyncio, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cute, weather_scene, scenes3
from playwright.async_api import async_playwright
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.environ.get('PK_FONTS', '/tmp/pkfonts/node_modules')   # npm i --prefix /tmp/pkfonts @fontsource/nanum-myeongjo@5
OUT = os.path.join(ROOT, 'media', 'covers')
MEDIA = os.path.join(ROOT, 'media') + '/'
C = dict(ink='#141838', blue='#2446F0', yellow='#FFD84A', coral='#F2555A', sky='#1E8DE0', mint='#12A57A', violet='#7C5CFF',
         coral_l='#FFE9E8', sky_l='#E4F2FD', mint_l='#E3F7F0', violet_l='#EFEAFF', blue_l='#E8ECFF', yellow_l='#FFF6D1')

HEAD = f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="file://{FONTS}/@fontsource/nanum-myeongjo/800.css">
<link rel="stylesheet" href="file://{FONTS}/@fontsource/nanum-myeongjo/korean-800.css">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1600px;height:1000px;overflow:hidden;position:relative;font-family:"Noto Sans CJK KR",sans-serif;color:{C['ink']}}}
.bg{{position:absolute;inset:0;background-color:var(--bg);background-image:linear-gradient(rgba(20,24,56,.07) 2px,transparent 2px),linear-gradient(90deg,rgba(20,24,56,.07) 2px,transparent 2px);background-size:80px 80px}}
.my{{font-family:"Nanum Myeongjo",serif;font-weight:800}}
.cell{{display:inline-grid;place-items:center;width:var(--s,200px);height:var(--s,200px);background:#fff;box-shadow:inset 0 0 0 5px var(--line,{C['coral']});margin-right:-5px;font-family:"Nanum Myeongjo",serif;font-weight:800;font-size:calc(var(--s,200px)*.66);line-height:1}}
.bubble{{position:absolute;background:#fff;border:6px solid {C['ink']};border-radius:48px;padding:34px 56px;font-weight:700;white-space:nowrap}}
.abs{{position:absolute}}
.chip{{position:absolute;background:#fff;border:5px solid {C['ink']};border-radius:28px;padding:16px 34px;font-weight:700;font-size:58px;white-space:nowrap}}
</style></head><body>'''

def page(bg, inner): return HEAD + f'<div class="bg" style="--bg:{bg}"></div>' + inner + '</body></html>'

def person(x, y, s, body, head='#F2C4A8', hair=C['ink']):
    return (f'<svg class="abs" style="left:{x}px;top:{y}px" width="{220*s}" height="{300*s}" viewBox="0 0 220 300">'
            f'<path d="M20 300c0-80 40-120 90-120s90 40 90 120z" fill="{body}"/><circle cx="110" cy="100" r="62" fill="{head}"/>'
            f'<path d="M48 96c0-44 28-66 62-66s62 22 62 66c-18-20-44-28-62-28s-44 8-62 28z" fill="{hair}"/>'
            f'<circle cx="88" cy="108" r="6" fill="{C["ink"]}"/><circle cx="132" cy="108" r="6" fill="{C["ink"]}"/>'
            f'<path d="M92 134q18 14 36 0" fill="none" stroke="{C["ink"]}" stroke-width="6" stroke-linecap="round"/></svg>')

COVERS = {}

# 1 read hangul in an hour: letters building a syllable
COVERS['read-hangul-in-an-hour'] = page(C['mint_l'], f'''
<div class="abs" style="left:150px;top:330px;display:flex;align-items:center;gap:36px">
 <span class="cell" style="--line:{C['mint']}">ㄱ</span><b style="font-size:120px">+</b>
 <span class="cell" style="--line:{C['mint']}">ㅏ</span><b style="font-size:120px">=</b>
 <span class="cell" style="--s:280px;--line:{C['coral']};background:{C['yellow']}">가</span></div>
''' + ''.join(f'<span class="abs my" style="left:{x}px;top:{y}px;font-size:{s}px;color:{c};transform:rotate({r}deg)">{j}</span>'
              for x, y, s, c, r, j in [(120, 60, 150, C['blue'], -12, 'ㄴ'), (420, 90, 120, C['coral'], 10, 'ㄷ'), (760, 50, 140, C['violet'], -6, 'ㅁ'),
                                       (1100, 80, 130, C['mint'], 14, 'ㅗ'), (1380, 120, 150, C['blue'], -10, 'ㅂ'), (200, 760, 140, C['violet'], 8, 'ㅅ'),
                                       (560, 790, 120, C['blue'], -14, 'ㅇ'), (900, 770, 150, C['coral'], 6, 'ㅎ'), (1250, 740, 140, C['mint'], -8, 'ㅜ')]))

# 2 -아요/-어요 polite ending
COVERS['ayo-eoyo-polite-ending'] = page(C['mint_l'], f'''
<div class="abs my" style="left:130px;top:150px;font-size:230px;line-height:1">-아요<br><span style="color:{C['mint']}">-어요</span></div>
<div class="chip" style="left:900px;top:170px;font-size:80px">가<span style="background:{C['yellow']}">요</span></div>
<div class="chip" style="left:1180px;top:330px;font-size:80px">먹<span style="background:{C['yellow']}">어요</span></div>
<div class="chip" style="left:930px;top:520px;font-size:80px">해<span style="background:{C['yellow']}">요</span></div>
<div class="chip" style="left:1180px;top:700px;font-size:80px">좋<span style="background:{C['yellow']}">아요</span></div>''')

# 3 괜찮아요: one word, four situations
def icon(kind):
    if kind == 'smile': return f'<circle cx="60" cy="60" r="50" fill="{C["yellow"]}"/><circle cx="42" cy="50" r="7" fill="{C["ink"]}"/><circle cx="78" cy="50" r="7" fill="{C["ink"]}"/><path d="M38 72q22 20 44 0" fill="none" stroke="{C["ink"]}" stroke-width="7" stroke-linecap="round"/>'
    if kind == 'band': return f'<g transform="rotate(-35 60 60)"><rect x="10" y="40" width="100" height="40" rx="20" fill="#F2C4A8" stroke="{C["ink"]}" stroke-width="5"/><rect x="42" y="40" width="36" height="40" fill="#fff" stroke="{C["ink"]}" stroke-width="5"/></g>'
    if kind == 'no': return f'<path d="M30 100V50a10 10 0 0 1 20 0v-14a10 10 0 0 1 20 0v6a10 10 0 0 1 20 0v40c0 18-12 28-30 28H50c-12 0-20-6-20-10z" fill="#F2C4A8" stroke="{C["ink"]}" stroke-width="5"/>'
    return f'<path d="M30 104V58h18l20-36c10 0 14 8 12 18l-4 18h22c8 0 12 6 10 12l-8 28c-2 6-6 8-12 8z" fill="#F2C4A8" stroke="{C["ink"]}" stroke-width="5"/><rect x="14" y="58" width="18" height="48" rx="4" fill="{C["blue"]}"/>'
COVERS['gwaenchanayo-meaning'] = page(C['violet_l'], f'''
<div class="bubble my" style="left:330px;top:300px;font-size:200px;padding:40px 80px;border-radius:70px">괜찮아요</div>
<svg class="abs" style="left:520px;top:600px" width="120" height="90"><path d="M10 0l100 0-90 80z" fill="#fff" stroke="{C['ink']}" stroke-width="6"/></svg>
<div class="abs" style="left:520px;top:582px;width:100px;height:14px;background:#fff"></div>
''' + ''.join(f'<svg class="abs" style="left:{x}px;top:{y}px" width="190" height="190" viewBox="0 0 120 120"><circle cx="60" cy="60" r="58" fill="#fff"/>{icon(k)}</svg>'
              for x, y, k in [(110, 90, 'smile'), (1300, 120, 'band'), (120, 720, 'no'), (1290, 690, 'up')]))

# 4 존댓말 vs 반말
COVERS['jondaenmal-vs-banmal-v3'] = page(C['violet_l'], f'<svg class="abs" style="left:80px;top:420px" width="460" height="600" viewBox="0 0 300 420">{cute.boy(0, 0, 1, "happy", hair="#CFCAC6", hair_hi="#F2EEEA", vest="#A0785A", vest_sh="#7E5B42", legs="#4A4A5A", glasses=True)}</svg>'
 + f'<svg class="abs" style="left:1100px;top:470px" width="400" height="530" viewBox="0 0 300 420">{cute.girl(0, 0, 1, "talk")}</svg>' + f'''
<div class="bubble" style="left:110px;top:150px;font-size:76px">진지 드셨어요?</div>
<div class="bubble" style="left:900px;top:250px;font-size:76px;background:{C['yellow']}">밥 먹었어?</div>
<div class="abs my" style="left:700px;top:600px;font-size:150px;color:{C['violet']}">↔</div>''')

# 5 slang
COVERS['korean-slang-online-2026'] = page(C['violet_l'], f'''
<div class="abs" style="left:560px;top:80px;width:480px;height:920px;border-radius:70px;background:{C['ink']}"></div>
<div class="abs" style="left:590px;top:130px;width:420px;height:900px;border-radius:44px;background:#fff"></div>
<div class="chip" style="left:620px;top:200px;background:{C['blue_l']}">헐 대박</div>
<div class="chip" style="left:720px;top:330px;background:{C['yellow']}">ㅋㅋㅋㅋ</div>
<div class="chip" style="left:620px;top:460px;background:{C['blue_l']}">킹받네</div>
<div class="chip" style="left:760px;top:590px;background:{C['yellow']}">갓생</div>
<div class="chip" style="left:620px;top:720px;background:{C['blue_l']}">국룰이지</div>
<div class="abs my" style="left:120px;top:170px;font-size:170px;color:{C['violet']};transform:rotate(-8deg)">꿀잼</div>
<div class="abs my" style="left:1140px;top:560px;font-size:150px;color:{C['coral']};transform:rotate(7deg)">신조어</div>''')

# 6 drama lines: TV with a subtitle
COVERS['10-lines-every-k-drama-v3'] = page(C['violet_l'], f'''
<div class="abs" style="left:250px;top:120px;width:1100px;height:660px;border-radius:40px;background:{C['ink']}"></div>
<div class="abs" style="left:290px;top:160px;width:1020px;height:580px;border-radius:20px;background:linear-gradient(180deg,#3B4C9B,#1E2556)"></div>
<div class="abs" style="left:290px;top:160px;width:1020px;height:580px;border-radius:20px;overflow:hidden"><svg width="1020" height="580" viewBox="0 0 1020 580">{cute.girl(170, 90, 1.25, 'talk')}{cute.boy(560, 100, 1.2, 'smile')}</svg></div>
<div class="abs" style="left:290px;top:600px;width:1020px;text-align:center"><span style="background:rgba(0,0,0,.6);color:#fff;font-size:76px;font-weight:700;padding:6px 30px;border-radius:12px">밥 먹었어?</span></div>
<div class="abs" style="left:700px;top:780px;width:200px;height:80px;background:{C['ink']}"></div><div class="abs" style="left:560px;top:850px;width:480px;height:30px;border-radius:15px;background:{C['ink']}"></div>''')

# 7 cafe order
COVERS['ordering-at-a-korean-cafe'] = page(C['sky_l'], f'''
<svg class="abs" style="left:260px;top:260px" width="460" height="640" viewBox="0 0 230 320"><path d="M30 60h170l-20 250H50z" fill="#fff" stroke="{C['ink']}" stroke-width="6"/>
<path d="M44 150h142l-8 100H52z" fill="{C['sky']}"/><rect x="18" y="40" width="194" height="30" rx="8" fill="{C['ink']}"/><path d="M140 40l20-40" stroke="{C['coral']}" stroke-width="10" stroke-linecap="round"/>
<rect x="70" y="190" width="30" height="30" rx="6" fill="#fff" opacity=".8"/><rect x="120" y="180" width="30" height="30" rx="6" fill="#fff" opacity=".8"/></svg>
<div class="bubble" style="left:720px;top:200px;font-size:84px">아이스 아메리카노<br>한 잔 주세요</div>
<div class="abs my" style="left:900px;top:640px;font-size:200px;color:{C['sky']}">주세요</div>''')

# 8 residence card
COVERS['residence-card-korea-guide-v3'] = page(C['sky_l'], f'''
<div class="abs" style="left:300px;top:200px;width:1000px;height:620px;border-radius:44px;background:#fff;box-shadow:inset 0 0 0 6px {C['ink']},30px 30px 0 {C['sky']}"></div>
<div class="abs" style="left:300px;top:200px;width:1000px;height:140px;border-radius:44px 44px 0 0;background:{C['ink']};color:#fff;font-size:76px;font-weight:700;padding:26px 60px">외국인등록증</div>
<div class="abs" style="left:380px;top:400px;width:260px;height:330px;border-radius:24px;background:{C['blue_l']};overflow:hidden"><svg width="260" height="330" viewBox="0 0 260 330">{cute.boy(-30, 40, 1.07)}</svg></div>
''' + ''.join(f'<div class="abs" style="left:720px;top:{y}px;width:{w}px;height:36px;border-radius:18px;background:{c}"></div>' for y, w, c in [(420, 480, '#C8CDE4'), (500, 380, '#C8CDE4'), (580, 440, '#C8CDE4'), (660, 300, C['yellow'])]))

# 9 weather words
def wx(kind, x, y, label):
    s = {'sun': f'<circle cx="100" cy="100" r="50" fill="{C["yellow"]}"/>' + ''.join(f'<rect x="94" y="10" width="12" height="30" rx="6" fill="{C["yellow"]}" transform="rotate({a} 100 100)"/>' for a in range(0, 360, 45)),
         'cloud': f'<path d="M40 140h120a32 32 0 0 0 0-64 46 46 0 0 0-88-10 36 36 0 0 0-32 74z" fill="#fff" stroke="{C["ink"]}" stroke-width="6"/>',
         'rain': f'<path d="M40 110h120a32 32 0 0 0 0-64 46 46 0 0 0-88-10 36 36 0 0 0-32 74z" fill="#fff" stroke="{C["ink"]}" stroke-width="6"/>' + ''.join(f'<path d="M{a} 130l-10 30" stroke="{C["sky"]}" stroke-width="10" stroke-linecap="round"/>' for a in (70, 105, 140)),
         'snow': f'<path d="M40 110h120a32 32 0 0 0 0-64 46 46 0 0 0-88-10 36 36 0 0 0-32 74z" fill="#fff" stroke="{C["ink"]}" stroke-width="6"/>' + ''.join(f'<circle cx="{a}" cy="{b}" r="9" fill="{C["sky"]}"/>' for a, b in ((70, 145), (105, 165), (140, 145)))}[kind]
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:320px;text-align:center"><svg width="260" height="200" viewBox="0 0 200 180">{s}</svg>'
            f'<div class="my" style="font-size:96px;margin-top:6px">{label}</div></div>')
COVERS['weather-words-in-korean-v2'] = HEAD + weather_scene.scene() + '</body></html>'

# 10 autumn & winter festivals
leaf = lambda x, y, r, c, s: f'<svg class="abs" style="left:{x}px;top:{y}px;transform:rotate({r}deg)" width="{s}" height="{s}" viewBox="0 0 100 100"><path d="M50 4l10 24 22-10-8 24 22 6-20 14 8 22-22-8-4 24-8-22-8 22-4-24-22 8 8-22-20-14 22-6-8-24 22 10z" fill="{c}"/><path d="M50 50v50" stroke="{c}" stroke-width="5"/></svg>'
COVERS['korea-autumn-winter-festival-guide'] = page(C['sky_l'], ''.join(leaf(x, y, r, c, s) for x, y, r, c, s in [(80, 80, -20, C['coral'], 220), (380, 600, 15, '#F28C28', 180), (1250, 90, 30, '#F28C28', 240), (1350, 640, -10, C['coral'], 200), (700, 760, 40, C['yellow'], 150), (980, 60, -35, C['yellow'], 140)])
    + ''.join(f'<svg class="abs" style="left:{x}px;top:{y}px" width="300" height="300" viewBox="0 0 100 100">' + ''.join(f'<path d="M50 50L{50+44*__import__("math").cos(a/6.283*6.283)} {50+44*__import__("math").sin(a)}" stroke="{c}" stroke-width="3" stroke-linecap="round"/>' for a in [i*0.524 for i in range(12)]) + '</svg>' for x, y, c in [(1000, 330, C['violet']), (250, 300, C['blue'])])
    + f'<div class="abs" style="left:520px;top:330px;display:flex"><span class="cell" style="--s:280px;--line:{C["coral"]}">단</span><span class="cell" style="--s:280px;--line:{C["coral"]}">풍</span></div>')

# 11 현백 코어 (style trend)
COVERS['hyunbaek-core-trend'] = page(C['coral_l'], f'''
<svg class="abs" style="left:230px;top:250px" width="560" height="660" viewBox="0 0 280 330"><path d="M90 90V60a50 50 0 0 1 100 0v30" fill="none" stroke="{C['ink']}" stroke-width="12"/>
<rect x="20" y="90" width="240" height="230" rx="18" fill="#fff" stroke="{C['ink']}" stroke-width="8"/><rect x="20" y="230" width="240" height="20" fill="{C['coral']}"/></svg>
<svg class="abs" style="left:430px;top:500px" width="300" height="300" viewBox="0 0 150 150">''' + ''.join(f'<circle cx="{75+55*__import__("math").cos(i*0.4+0.6)}" cy="{40+60*__import__("math").sin(i*0.4+0.6)}" r="10" fill="#fff" stroke="{C["ink"]}" stroke-width="3"/>' for i in range(8)) + f'''</svg>
<div class="abs my" style="left:860px;top:300px;font-size:190px;line-height:1.15">현백<br><span style="color:{C['coral']}">코어</span></div>''')

# 12 100일의 거짓말: a countdown calendar and premiere
COVERS['100-days-of-deception-ratings'] = page(C['coral_l'], f'''
<div class="abs" style="left:200px;top:200px;width:560px;height:620px;border-radius:40px;background:#fff;box-shadow:inset 0 0 0 6px {C['ink']}"></div>
<div class="abs" style="left:200px;top:200px;width:560px;height:150px;border-radius:40px 40px 0 0;background:{C['coral']}"></div>
<div class="abs" style="left:300px;top:150px;width:28px;height:110px;border-radius:14px;background:{C['ink']}"></div><div class="abs" style="left:630px;top:150px;width:28px;height:110px;border-radius:14px;background:{C['ink']}"></div>
<div class="abs" style="left:200px;top:400px;width:560px;text-align:center;font-size:300px;font-weight:900;line-height:1">100</div>
<div class="abs my" style="left:200px;top:700px;width:560px;text-align:center;font-size:90px">일</div>
<div class="abs" style="left:880px;top:330px;display:flex"><span class="cell">첫</span></div><div class="abs" style="left:1100px;top:330px;display:flex"><span class="cell">방</span><span class="cell">송</span></div>''')

# 13 Doctor X ratings: rising chart and a medical cross
COVERS['doctor-x-kim-ji-won-ratings'] = page(C['coral_l'], ''.join(
    f'<div class="abs" style="left:{x}px;top:{900-h}px;width:150px;height:{h}px;border-radius:20px 20px 0 0;background:{c}"></div>'
    for x, h, c in [(180, 300, '#F6A6A8'), (380, 400, '#F48487'), (580, 520, C['coral']), (780, 650, C['coral'])]) + f'''
<svg class="abs" style="left:1060px;top:140px" width="380" height="380" viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" fill="#fff" stroke="{C['ink']}" stroke-width="3"/><path d="M38 18h24v20h20v24H62v20H38V62H18V38h20z" fill="{C['coral']}"/></svg>
<div class="abs my" style="left:1000px;top:600px;font-size:170px">시청률</div>
<svg class="abs" style="left:200px;top:120px" width="800" height="420" viewBox="0 0 800 420"><path d="M20 380L230 290 430 190 640 40" fill="none" stroke="{C['ink']}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/><path d="M600 30l50 4-10 48" fill="none" stroke="{C['ink']}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></svg>''')

# 14 TOPIK vocabulary level by level: a staircase of levels
COVERS['learn-topik-vocabulary-level-by-level'] = page(C['mint_l'], ''.join(
    f'<div class="abs" style="left:{120+i*230}px;top:{780-i*110}px;width:230px;height:{220+i*110}px;background:{c};border-radius:18px 18px 0 0;box-shadow:inset 0 0 0 5px {C["ink"]}">'
    f'<div class="my" style="text-align:center;font-size:80px;margin-top:26px;color:{C["ink"]}">{i+1}급</div></div>'
    for i, c in enumerate(['#fff', '#fff', C['blue_l'], C['blue_l'], C['violet_l'], C['violet_l']])) + f'''
<div class="chip" style="left:150px;top:560px;font-size:60px">사랑</div><div class="chip" style="left:620px;top:330px;font-size:60px">경험</div><div class="chip" style="left:1090px;top:110px;font-size:60px">분석하다</div>''')

# 15 K-pop comeback race: a stage with light sticks
COVERS['october-kpop-comeback-race'] = page('#1D2250', ''.join(
    f'<div class="abs" style="left:{x}px;top:0;width:0;height:0;border-left:{w}px solid transparent;border-right:{w}px solid transparent;border-top:760px solid rgba(255,216,74,.32);transform:rotate({r}deg);transform-origin:top center"></div>'
    for x, w, r in [(300, 160, -18), (800, 180, 0), (1300, 160, 18)]) + f"""
<div class="abs" style="left:0;top:700px;width:1600px;height:300px;background:#141838"></div>
<div class="abs" style="left:380px;top:250px;display:flex"><span class="cell" style="--s:260px;--line:{C['yellow']}">컴</span><span class="cell" style="--s:260px;--line:{C['yellow']}">백</span></div>
""" + ''.join(f'<div class="abs" style="left:{x}px;top:{y}px;width:16px;height:120px;border-radius:8px;background:#9AA0B8;transform:rotate({r}deg)"><div style="position:absolute;left:-22px;top:-50px;width:60px;height:60px;border-radius:50%;background:{c};box-shadow:0 0 40px {c}"></div></div>'
              for x, y, r, c in [(120, 820, -15, C['coral']), (330, 860, 10, C['yellow']), (560, 830, -8, C['sky']), (790, 870, 12, C['mint']), (1010, 830, -12, C['violet']), (1230, 860, 8, C['coral']), (1450, 820, -10, C['yellow'])])
    + f'<div class="abs my" style="left:1000px;top:330px;font-size:120px;color:#fff">10월</div>')

# 16 survival Korean: taxi, café and convenience store
COVERS['survival-korean-taxi-cafe-convenience-store'] = page(C['sky_l'], f"""
<svg class="abs" style="left:110px;top:520px" width="620" height="330" viewBox="0 0 310 165"><path d="M30 90l30-50h150l40 50h30a10 10 0 0 1 10 10v30H10v-30a10 10 0 0 1 10-10z" fill="#F2A33A" stroke="{C['ink']}" stroke-width="5"/>
<path d="M75 50h55v40H50zM145 50h60l30 40h-90z" fill="{C['sky_l']}" stroke="{C['ink']}" stroke-width="4"/><rect x="120" y="22" width="60" height="20" rx="4" fill="#fff" stroke="{C['ink']}" stroke-width="4"/>
<circle cx="75" cy="135" r="24" fill="{C['ink']}"/><circle cx="235" cy="135" r="24" fill="{C['ink']}"/></svg>
<svg class="abs" style="left:880px;top:430px" width="620" height="460" viewBox="0 0 310 230"><rect x="10" y="50" width="290" height="175" fill="#fff" stroke="{C['ink']}" stroke-width="5"/>
<rect x="10" y="20" width="290" height="40" fill="{C['mint']}" stroke="{C['ink']}" stroke-width="5"/><rect x="30" y="90" width="110" height="135" fill="{C['sky_l']}" stroke="{C['ink']}" stroke-width="4"/>
<rect x="165" y="90" width="115" height="70" fill="{C['sky_l']}" stroke="{C['ink']}" stroke-width="4"/><text x="155" y="48" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="24" fill="#fff">24</text></svg>
<div class="bubble" style="left:420px;top:150px;font-size:100px">카드 돼요?</div>""")

# ---- editorial photo covers: a free-licence photo, darkened, with the key Korean phrase set large ----
PHOTO = {
 '100-days-of-deception-ratings-v2': (MEDIA + 'photos/gyeongseong-night.png', '첫 방송', '100일의 거짓말', C['coral'], 'center'),
 'doctor-x-kim-ji-won-ratings-v2': (MEDIA + 'photos/operating-room-ill.png', '시청률', '닥터X 18.5%', C['coral'], 'center'),
 'hyunbaek-core-trend-v2': (MEDIA + 'photos/atrium-ill.png', '현백 코어', '백화점 스타일', C['coral'], 'center'),
 'october-kpop-comeback-race-p1': (MEDIA + 'photos/concert-ill.png', '컴백', '10월의 K-pop', C['yellow'], 'center'),
 'survival-korean-taxi-cafe-convenience-store-p1': (MEDIA + 'photos/street-night-ill.png', '카드 돼요?', '택시와 편의점에서', C['sky'], 'center'),
 'residence-card-korea-guide-p1': (MEDIA + 'photos/desk-ill.png', '외국인등록증', '신청부터 받기까지', C['sky'], 'center'),
 'korea-autumn-winter-festival-guide-v2': (MEDIA + 'photos/maple-tunnel-ill.png', '단풍 구경', '가을과 겨울 축제', C['sky'], 'center'),
 'love-in-disguise-premiere-p1': (MEDIA + 'photos/disguise-night-ill.png', '유죄', '나의 유죄인간 5.6%', C['coral'], 'center'),
 'nmixx-strange-muse-birthday-wish-p1': (MEDIA + 'photos/muse-stage-ill.png', '소원', '엔믹스 멜론 5위', C['yellow'], 'center'),
 'seongbuk-art-week-2026-p1': (MEDIA + 'photos/seongbuk-hill-ill.png', '집', '성북아트위크', C['coral'], 'center'),
 'hoe-cnic-han-river-raw-fish-picnic-p1': (MEDIA + 'photos/hoecnic-river-ill.png', '회크닉', '한강에서 회 한 접시', C['coral'], 'center'),
 'korean-winter-heating-boiler-guide-p1': (MEDIA + 'photos/boiler-room-ill.png', '난방', '첫 한국 겨울 보일러', C['sky'], 'center'),
 'ktx-booking-after-srt-merger-p1': (MEDIA + 'photos/ktx-platform-ill.png', '승차권', 'SRT 통합 후 KTX 예매', C['sky'], 'center'),
 'pepero-day-november-11-p1': (MEDIA + 'photos/stick-gifts-ill.png', '빼빼로데이', '11월 11일의 선물', C['sky'], 'center'),
 'korean-phrases-pharmacy-clinic-p1': (MEDIA + 'photos/pharmacy-counter-ill.png', '아파요', '약국과 병원에서', C['sky'], 'center'),
 'take-charge-of-my-heart-netflix-top-10-p1': (MEDIA + 'photos/heart-rooftop-ill.png', '충전', '나를 충전해줘', C['coral'], 'center'),
 'nct-wish-i-spy-first-week-sales-p1': (MEDIA + 'photos/dome-crowd-ill.png', '초동', 'NCT WISH 155만 장', C['yellow'], 'center'),
 'hanbok-culture-week-2026-p1': (MEDIA + 'photos/palace-hanbok-ill.png', '한복', '한복문화주간', C['coral'], 'center'),
 'colour-puffer-jackets-trend-p1': (MEDIA + 'photos/puffer-street-ill.png', '패딩', '올겨울은 컬러 패딩', C['coral'], 'center'),
 'korea-rubbish-sorting-food-waste-p1': (MEDIA + 'photos/recycle-corner-ill.png', '분리수거', '종량제 봉투와 음식물', C['sky'], 'center'),
 'seoul-late-night-n-buses-p1': (MEDIA + 'photos/nbus-stop-ill.png', '막차', '서울 심야버스', C['sky'], 'center'),
 'suneung-csat-day-customs-p1': (MEDIA + 'photos/exam-gate-ill.png', '수능', '11월 19일 시험의 날', C['sky'], 'center'),
 'korean-phrases-clothes-shopping-p1': (MEDIA + 'photos/boutique-ill.png', '입어 봐도 돼요?', '옷 가게에서', C['sky'], 'center'),
 'between-steps-ratings-high-p1': (MEDIA + 'photos/robot-lab-ill.png', '연애박사', '반환점에서 자체 최고 시청률', C['coral'], 'center'),
 'a2o-lite-neon-three-wins-p1': (MEDIA + 'photos/music-stage-ill.png', '1위', '데뷔 일주일 만에 음방 3관왕', C['coral'], 'center'),
 'hansik-day-first-korean-food-day-p1': (MEDIA + 'photos/hansik-pond-ill.png', '한식', '첫 번째 한식의 날', C['coral'], 'center'),
 'tamjo-birdwatching-young-koreans-p1': (MEDIA + 'photos/magpie-persimmon-ill.png', '탐조', '스마트폰 들고 새 보러 가요', C['coral'], 'center'),
 'korea-phone-number-sim-plan-p1': (MEDIA + 'photos/phone-shop-ill.png', '개통', '유심, 약정, 알뜰폰', C['sky'], 'center'),
 'korea-express-bus-guide-p1': (MEDIA + 'photos/rest-stop-ill.png', '고속버스', '우등, 프리미엄, 휴게소', C['sky'], 'center'),
 'g-star-2026-busan-game-show-p1': (MEDIA + 'photos/game-hall-ill.png', '전시회', '11월 부산 게임 전시회', C['sky'], 'center'),
 'korean-phrases-hair-salon-p1': (MEDIA + 'photos/hair-salon-ill.png', '다듬어 주세요', '미용실에서', C['sky'], 'center'),
}  # slug -> (photo path, big phrase, small line, accent colour, object-position)
def photo_page(photo, big, small, accent, pos='center'):
    return HEAD + f"""<img src="file://{photo}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{pos}">
<div class="abs" style="inset:0;background:linear-gradient(90deg,rgba(14,17,40,.86) 0%,rgba(14,17,40,.55) 45%,rgba(14,17,40,0) 75%)"></div>
<div class="abs" style="left:110px;bottom:120px;color:#fff">
 <div style="width:96px;height:10px;background:{accent};margin-bottom:34px"></div>
 <div class="my" style="font-size:{200 if len(big) <= 4 else 150}px;line-height:1.05;letter-spacing:-.02em;text-shadow:0 4px 30px rgba(0,0,0,.35)">{big}</div>
 <div style="font-size:52px;font-weight:700;margin-top:26px;color:#E6E9FF">{small}</div>
</div></body></html>"""

for _k, _f in scenes3.SCENES.items(): COVERS[_k + '-s1'] = HEAD + _f() + '</body></html>'

for _k in ['10-lines-every-k-drama', '100-days-of-deception-ratings', 'doctor-x-kim-ji-won-ratings', 'hyunbaek-core-trend', 'jondaenmal-vs-banmal', 'korea-autumn-winter-festival-guide', 'residence-card-korea-guide']: COVERS.pop(_k, None); PHOTO.pop(_k, None)

def only_ok(slug):
    import sys
    a = sys.argv[1:]
    return not a or slug in a

async def main():
    os.makedirs(OUT, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1600, 'height': 1000})
        for slug, (ph, big, small, acc, pos) in PHOTO.items(): COVERS[slug] = photo_page(ph, big, small, acc, pos)
        for slug, (ph, *_r) in PHOTO.items():   # text-free version for list thumbnails
            if not only_ok(slug): continue
            im = Image.open(ph).convert('RGB'); im.thumbnail((1600, 1000)); im.save(f'{OUT}/{slug}-t.jpg', quality=86, optimize=True, progressive=True)
        only = sys.argv[1:]
        for slug, html in COVERS.items():
            if only and slug not in only: continue
            f = f'/tmp/cover-{slug}.html'
            open(f, 'w').write(html)
            await pg.goto('file://' + f); await pg.wait_for_timeout(400)
            png = f[:-5] + '.png'
            await pg.screenshot(path=png)
            Image.open(png).convert('RGB').save(f'{OUT}/{slug}.jpg', quality=86, optimize=True, progressive=True)
            print(slug)
        await b.close()

if __name__ == '__main__':
    asyncio.run(main())
    import subprocess, os
    iv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imgvariants.py')
    if os.path.exists(iv): subprocess.run(['python3', iv, 'media/covers'])
