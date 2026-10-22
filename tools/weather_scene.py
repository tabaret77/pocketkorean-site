import random, math, cute
INK = '#4A2E2A'
def scene():
    R = random.Random(5)
    s = ['<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000"><defs>'
         '<linearGradient id="sky" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8FD3FF"/><stop offset=".42" stop-color="#BFE3F7"/><stop offset=".62" stop-color="#AEB9D6"/><stop offset="1" stop-color="#6E7BA8"/></linearGradient>'
         '<linearGradient id="ground" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9BD08A"/><stop offset="1" stop-color="#6FB27A"/></linearGradient>'
         '<radialGradient id="glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFE98A" stop-opacity=".9"/><stop offset="1" stop-color="#FFE98A" stop-opacity="0"/></radialGradient>'
         '<filter id="sh"><feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#141838" flood-opacity=".18"/></filter></defs>'
         '<rect width="1600" height="1000" fill="url(#sky)"/>']
    # sun with a face
    s.append('<circle cx="250" cy="230" r="230" fill="url(#glow)"/>')
    for i in range(12):
        a = i / 12 * math.tau
        s.append(f'<path d="M{250+120*math.cos(a):.0f} {230+120*math.sin(a):.0f} L{250+160*math.cos(a+.08):.0f} {230+160*math.sin(a+.08):.0f} L{250+160*math.cos(a-.08):.0f} {230+160*math.sin(a-.08):.0f}Z" fill="#FFC93C"/>')
    s.append(f'<circle cx="250" cy="230" r="100" fill="#FFD84A" stroke="{INK}" stroke-width="6"/>'
             f'<path d="M210 222 q12 -14 24 0 M266 222 q12 -14 24 0" stroke="{INK}" stroke-width="6" fill="none" stroke-linecap="round"/>'
             f'<path d="M232 252 q18 18 36 0" stroke="{INK}" stroke-width="6" fill="none" stroke-linecap="round"/><ellipse cx="196" cy="250" rx="14" ry="8" fill="#FF9C9C"/><ellipse cx="304" cy="250" rx="14" ry="8" fill="#FF9C9C"/>')
    # clouds (cute, with faces) and rain / snow
    def cloud(x, y, sc, col, face=True, sad=False):
        o = f'<g transform="translate({x} {y}) scale({sc})" filter="url(#sh)"><path d="M0 80 Q-10 30 40 30 Q50 -10 100 0 Q140 -30 180 10 Q230 0 230 50 Q260 60 250 90 Q240 110 210 110 L30 110 Q-10 110 0 80Z" fill="{col}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
        if face:
            o += f'<circle cx="95" cy="62" r="7" fill="{INK}"/><circle cx="150" cy="62" r="7" fill="{INK}"/>'
            o += (f'<path d="M110 90 q12 -10 24 0" stroke="{INK}" stroke-width="5" fill="none" stroke-linecap="round"/>' if sad else f'<path d="M110 82 q12 10 24 0" stroke="{INK}" stroke-width="5" fill="none" stroke-linecap="round"/>')
        return o + '</g>'
    s.append(cloud(560, 120, 1.0, '#FFFFFF'))
    s.append(cloud(1000, 90, 1.15, '#D5DBEA', sad=True))
    s.append(cloud(1300, 210, .95, '#E9EDF7'))
    for _ in range(46):
        x, y = R.uniform(1010, 1290), R.uniform(240, 640)
        s.append(f'<path d="M{x:.0f} {y:.0f} q-6 14 0 20 q6 -6 0 -20Z" fill="#4AA3F0" opacity=".85"/>')
    for _ in range(30):
        x, y, r = R.uniform(1320, 1580), R.uniform(330, 620), R.uniform(9, 15)
        arms = ''.join(f'<path d="M0 0 L{r*math.cos(i*math.pi/3):.1f} {r*math.sin(i*math.pi/3):.1f}"/>' for i in range(6))
        s.append(f'<g transform="translate({x:.0f} {y:.0f}) rotate({R.uniform(0,60):.0f})" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round">{arms}</g>')
    # Seoul skyline with Namsan tower
    s.append('<path d="M0 760 Q240 700 480 740 Q700 690 900 730 Q1150 680 1380 726 Q1500 704 1600 720 L1600 1000 L0 1000Z" fill="#7FA6D9" opacity=".55"/>')
    sky = []
    xx = 0
    while xx < 1600:
        w = R.choice([60, 80, 100, 120]); h = R.choice([90, 130, 170, 210, 250])
        sky.append(f'<rect x="{xx}" y="{800-h}" width="{w-8}" height="{h+40}" rx="6" fill="{R.choice(["#5E7FB8","#6B8CC4","#5373AE"])}"/>')
        for wy in range(800 - h + 18, 820, 30):
            for wx in range(xx + 12, xx + w - 18, 22):
                if R.random() < .5: sky.append(f'<rect x="{wx}" y="{wy}" width="10" height="14" rx="2" fill="#FFF4C2" opacity=".85"/>')
        xx += w
    s.append(''.join(sky))
    s.append('<path d="M300 840 Q360 700 460 690 Q560 700 620 840Z" fill="#4E8A62"/>'
             '<rect x="452" y="470" width="16" height="230" fill="#E9EDF7" stroke="#4A2E2A" stroke-width="4"/><path d="M430 520 h60 l-8 40 h-44z" fill="#F2555A" stroke="#4A2E2A" stroke-width="4"/><rect x="457" y="420" width="6" height="56" fill="#4A2E2A"/>')
    s.append('<path d="M0 840 Q400 800 800 830 Q1200 860 1600 820 L1600 1000 L0 1000Z" fill="url(#ground)"/>')
    # character with yellow umbrella
    s.append(f'<g transform="translate(1116 430)"><path d="M150 -10 L150 444" stroke="{INK}" stroke-width="7"/>'
             f'<path d="M-40 70 Q150 -150 340 70 Q300 50 270 76 Q240 50 210 76 Q180 50 150 76 Q120 50 90 76 Q60 50 30 76 Q0 50 -40 70Z" fill="#FFD84A" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
             f'<path d="M150 -10 Q90 0 30 76 M150 -10 Q210 0 270 76" stroke="#E6B82A" stroke-width="4" fill="none"/></g>')
    s.append('<svg x="1050" y="560" width="300" height="420" viewBox="0 0 300 420">' + cute.girl(0, 0, 1, 'talk', cardigan='#FFFFFF', cardigan_sh='#D9E4F5', skirt='#5B8DEF', skirt_sh='#3D6CCB', ribbon='#F2555A') + '</svg>')
    # label tags
    def tag(x, y, text, bg='#FFFFFF'):
        w = 60 + 54 * len(text)
        return (f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="84" rx="42" fill="{bg}" stroke="{INK}" stroke-width="5"/>'
                f'<text x="{x+w/2}" y="{y+60}" text-anchor="middle" font-family="Nanum Myeongjo" font-weight="800" font-size="52" fill="{INK}">{text}</text></g>')
    s.append(tag(370, 330, '맑음', '#FFF6D1') + tag(640, 270, '흐림') + tag(1080, 330, '비', '#E4F2FD') + tag(1440, 640, '눈', '#FFFFFF'))
    # speech bubble
    s.append(f'<g filter="url(#sh)"><path d="M560 470 h500 a40 40 0 0 1 40 40 v66 a40 40 0 0 1 -40 40 h-40 l60 52 l-110 -52 h-410 a40 40 0 0 1 -40 -40 v-66 a40 40 0 0 1 40 -40Z" fill="#FFFFFF" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
             f'<text x="810" y="564" text-anchor="middle" font-family="Nanum Myeongjo" font-weight="800" font-size="56" fill="{INK}">오늘 날씨 어때요?</text></g>')
    s.append('</svg>')
    return ''.join(s)
