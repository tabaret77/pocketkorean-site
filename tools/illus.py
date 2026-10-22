"""Hand-built scene illustrations (SVG -> PNG 1600x1000) used as cover backgrounds. Original drawings; no real faces."""
import asyncio, random, math, sys, os
from playwright.async_api import async_playwright
OUTD = os.environ.get('ILL_OUT', os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media', 'photos'))

GRAIN = '''<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="3"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .07 0"/></filter>
<filter id="soft"><feGaussianBlur stdDeviation="2"/></filter><filter id="blur8"><feGaussianBlur stdDeviation="8"/></filter><filter id="blur30"><feGaussianBlur stdDeviation="30"/></filter>
<filter id="paint"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="3" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="18"/></filter>'''
def svg(inner): return f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000"><defs>{GRAIN}</defs>{inner}<rect width="1600" height="1000" filter="url(#grain)"/></svg>'

# ---------- 1. Gyeongseong, rainy night, 1930s ----------
def gyeongseong():
    R = random.Random(4)
    s = ['''<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0B1030"/><stop offset=".55" stop-color="#262B58"/><stop offset="1" stop-color="#5C4668"/></linearGradient>
<linearGradient id="road" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3A3454"/><stop offset="1" stop-color="#14162E"/></linearGradient>
<radialGradient id="lamp" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFD98A" stop-opacity=".9"/><stop offset=".35" stop-color="#FFB86B" stop-opacity=".35"/><stop offset="1" stop-color="#FFB86B" stop-opacity="0"/></radialGradient></defs>
<rect width="1600" height="1000" fill="url(#sky)"/>
<path d="M600 520 C700 420 790 380 870 400 C950 380 1010 330 1090 360 C1170 390 1230 450 1320 520Z" fill="#1A1E44"/>
<g fill="#151937"><rect x="760" y="440" width="300" height="140"/><rect x="840" y="410" width="140" height="40"/><path d="M860 410 Q910 330 960 410Z"/><rect x="905" y="320" width="10" height="30"/></g>''']
    # left buildings (perspective toward VP 930,600)
    for x0, w, top, col in [(0, 260, 140, '#1E2148'), (240, 200, 260, '#252A55'), (420, 150, 360, '#2C3060'), (560, 110, 430, '#30346A'), (660, 80, 480, '#343873')]:
        s.append(f'<rect x="{x0}" y="{top}" width="{w}" height="{640-top}" fill="{col}"/><rect x="{x0-6}" y="{top-10}" width="{w+12}" height="12" fill="#12142E"/>')
        for wy in range(top + 30, 600, 46):
            for wx in range(x0 + 18, x0 + w - 24, 38):
                if R.random() < .45: s.append(f'<rect x="{wx}" y="{wy}" width="18" height="24" fill="#FFD27A" opacity="{R.uniform(.5,.95):.2f}"/>')
    # right buildings
    for x0, w, top, col in [(1000, 90, 470, '#343873'), (1080, 130, 400, '#2E3266'), (1200, 170, 300, '#262A57'), (1360, 240, 120, '#1C1F45')]:
        s.append(f'<rect x="{x0}" y="{top}" width="{w}" height="{640-top}" fill="{col}"/><rect x="{x0-6}" y="{top-10}" width="{w+12}" height="12" fill="#12142E"/>')
        for wy in range(top + 30, 600, 46):
            for wx in range(x0 + 16, x0 + w - 22, 36):
                if R.random() < .45: s.append(f'<rect x="{wx}" y="{wy}" width="16" height="22" fill="#FFD27A" opacity="{R.uniform(.5,.95):.2f}"/>')
    # vertical neon sign
    s.append('<g><rect x="1300" y="180" width="56" height="300" rx="6" fill="#2A0F2A" stroke="#F2555A" stroke-width="4"/>' +
             ''.join(f'<text x="1328" y="{232+i*62}" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="44" fill="#FF8A8E" style="filter:drop-shadow(0 0 10px #F2555A)">{c}</text>' for i, c in enumerate('경성다방')) + '</g>')
    # road
    s.append('<path d="M0 640 H1600 V1000 H0Z" fill="url(#road)"/>')
    s.append('<path d="M880 640 L980 640 L1500 1000 L300 1000Z" fill="#2B2848" opacity=".7"/>')
    for x in (905, 955):  # tram rails
        s.append(f'<path d="M{x} 640 L{(x-930)*14+930} 1000" stroke="#8C86B0" stroke-width="3" opacity=".55"/>')
    # tram
    s.append('''<g transform="translate(700 520)"><rect x="0" y="20" width="230" height="110" rx="14" fill="#B33A3F"/><rect x="0" y="95" width="230" height="35" fill="#7A2329"/>
<path d="M30 20 Q115 -4 200 20Z" fill="#5A1A20"/><line x1="115" y1="8" x2="150" y2="-60" stroke="#222" stroke-width="3"/>''' +
             ''.join(f'<rect x="{14+i*42}" y="38" width="30" height="40" rx="4" fill="#FFE2A0"/>' for i in range(5)) + '</g>')
    # reflections
    for x, c in [(1328, '#F2555A'), (720, '#FFD27A'), (820, '#FFD27A'), (1150, '#FFD98A')]:
        s.append(f'<rect x="{x-14}" y="650" width="28" height="340" fill="{c}" opacity=".18" filter="url(#blur8)"/>')
    # street lamp + glow
    s.append('<circle cx="1150" cy="430" r="230" fill="url(#lamp)"/><rect x="1144" y="430" width="12" height="400" fill="#0E0F22"/><path d="M1124 410 h52 l-10 36 h-32z" fill="#FFE7A8"/><rect x="1120" y="398" width="60" height="14" fill="#0E0F22"/>')
    # woman from behind (cloche hat, long coat), holding an envelope behind her back
    s.append('''<g transform="translate(1020 600)">
<ellipse cx="60" cy="300" rx="70" ry="12" fill="#000" opacity=".35"/>
<path d="M30 70 Q60 52 90 70 L112 270 Q60 286 8 270Z" fill="#8E2F3C"/><path d="M60 72 L60 270" stroke="#6E2230" stroke-width="3"/>
<rect x="34" y="268" width="14" height="30" fill="#E8D3C2"/><rect x="72" y="268" width="14" height="30" fill="#E8D3C2"/><rect x="30" y="292" width="22" height="9" rx="3" fill="#1A1220"/><rect x="70" y="292" width="22" height="9" rx="3" fill="#1A1220"/>
<path d="M36 34 Q60 0 84 34 Q92 44 96 48 Q60 56 24 48 Q28 44 36 34Z" fill="#1E1B2E"/><path d="M34 52 Q60 70 86 52 L84 66 Q60 76 36 66Z" fill="#2B2236"/>
<rect x="76" y="168" width="36" height="24" rx="2" fill="#F4E9D6" transform="rotate(-12 94 180)"/><path d="M78 172 l17 10 16 -12" stroke="#B9A88D" stroke-width="2" fill="none" transform="rotate(-12 94 180)"/></g>''')
    # man in fedora and trench coat, a few steps behind in the shadow
    s.append('''<g transform="translate(880 650) scale(.78)" opacity=".92"><path d="M30 60 Q60 46 90 60 L106 250 Q60 262 14 250Z" fill="#1A1B33"/><rect x="34" y="248" width="14" height="40" fill="#11122A"/><rect x="70" y="248" width="14" height="40" fill="#11122A"/>
<ellipse cx="60" cy="40" rx="48" ry="9" fill="#0E0F22"/><path d="M38 40 Q40 10 60 12 Q80 10 82 40Z" fill="#0E0F22"/></g>''')
    # rain
    for _ in range(420):
        x, y, l = R.uniform(-100, 1600), R.uniform(0, 1000), R.uniform(18, 46)
        s.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x-l*.25:.0f}" y2="{y+l:.0f}" stroke="#C8CCF0" stroke-width="1.4" opacity="{R.uniform(.15,.45):.2f}"/>')
    return svg(''.join(s))

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scenes2
SCENES = {'gyeongseong-night': gyeongseong, 'operating-room-ill': lambda: scenes2.operating(svg), 'atrium-ill': lambda: scenes2.atrium(svg), 'maple-tunnel-ill': lambda: scenes2.maple(svg), 'concert-ill': lambda: scenes2.concert(svg), 'street-night-ill': lambda: scenes2.street_night(svg), 'desk-ill': lambda: scenes2.desk(svg), 'disguise-night-ill': lambda: scenes2.disguise_night(svg), 'muse-stage-ill': lambda: scenes2.muse_stage(svg), 'seongbuk-hill-ill': lambda: scenes2.seongbuk_hill(svg), 'hoecnic-river-ill': lambda: scenes2.hoecnic_river(svg), 'boiler-room-ill': lambda: scenes2.boiler_room(svg), 'ktx-platform-ill': lambda: scenes2.ktx_platform(svg), 'stick-gifts-ill': lambda: scenes2.stick_gifts(svg), 'pharmacy-counter-ill': lambda: scenes2.pharmacy_counter(svg)}

async def main(names):
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1600, 'height': 1000})
        for n in names or SCENES:
            await pg.set_content('<html><body style="margin:0">' + SCENES[n]() + '</body></html>'); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f'{OUTD}/{n}.png'); print(n)
        await b.close()
if __name__ == '__main__': asyncio.run(main(sys.argv[1:]))
