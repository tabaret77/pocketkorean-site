import random, math

def operating(svg):
    """Operating room: a surgeon from behind under the lamp, heartbeat line rising into an arrow."""
    s = ['<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#06103A"/><stop offset=".6" stop-color="#0E2A8A"/><stop offset="1" stop-color="#1640C8"/></linearGradient>'
         '<radialGradient id="cone" cx=".5" cy="0" r="1"><stop offset="0" stop-color="#DDE9FF" stop-opacity=".55"/><stop offset="1" stop-color="#DDE9FF" stop-opacity="0"/></radialGradient>'
         '<linearGradient id="gown" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2C9BB0"/><stop offset="1" stop-color="#1B6F86"/></linearGradient></defs>'
         '<rect width="1600" height="1000" fill="url(#bg)"/>'
         '<g opacity=".35"><rect x="80" y="120" width="300" height="420" rx="10" fill="#1A3AA8"/><rect x="420" y="160" width="220" height="380" rx="10" fill="#1A3AA8"/></g>'
         '<path d="M1020 220 L700 1000 L1600 1000 L1600 520Z" fill="url(#cone)"/>'
         '<rect x="1130" y="0" width="16" height="120" fill="#9FB3E8"/>'
         '<ellipse cx="1138" cy="190" rx="190" ry="70" fill="#C7D5F5"/><ellipse cx="1138" cy="200" rx="160" ry="52" fill="#EAF2FF"/>']
    for i in range(18):
        a = i / 18 * math.tau
        s.append(f'<circle cx="{1138+110*math.cos(a):.0f}" cy="{200+32*math.sin(a):.0f}" r="13" fill="#FFFFFF" opacity=".95"/>')
    s.append('<ellipse cx="1138" cy="200" rx="260" ry="110" fill="#EAF2FF" opacity=".25" filter="url(#blur30)"/>')
    s.append('<g filter="url(#blur8)" opacity=".7"><path d="M780 1000 Q790 640 900 610 Q1010 640 1020 1000Z" fill="#16457A"/><ellipse cx="900" cy="560" rx="62" ry="70" fill="#0F2E57"/>'
             '<path d="M1380 1000 Q1390 660 1480 640 Q1570 660 1580 1000Z" fill="#16457A"/><ellipse cx="1480" cy="590" rx="58" ry="66" fill="#0F2E57"/></g>')
    s.append('<path d="M700 860 L1600 760 L1600 1000 L640 1000Z" fill="#9EC3E6" opacity=".85"/><path d="M700 860 L1600 760" stroke="#E6F2FF" stroke-width="6"/>')
    s.append('<g transform="translate(1040 430)">'
             '<path d="M-150 600 Q-160 250 -60 190 Q0 170 60 190 Q160 250 150 600Z" fill="url(#gown)"/>'
             '<path d="M-60 190 Q0 230 60 190" stroke="#14586B" stroke-width="5" fill="none"/>'
             '<path d="M-118 300 Q-200 230 -190 120" stroke="#2387A0" stroke-width="58" stroke-linecap="round" fill="none"/>'
             '<path d="M118 300 Q200 230 190 120" stroke="#2387A0" stroke-width="58" stroke-linecap="round" fill="none"/>'
             '<g transform="translate(-190 100) scale(-1 1)"><path d="M-26 40 Q-34 0 -30 -40 Q-28 -56 -18 -56 Q-10 -56 -10 -40 L-10 -62 Q-8 -76 2 -76 Q12 -76 12 -62 L12 -58 Q14 -70 24 -68 Q32 -66 32 -54 L32 -30 Q40 -40 46 -32 Q50 -26 44 -14 L30 30 Q24 44 0 46 Q-20 46 -26 40Z" fill="#7FD3E8"/></g><g transform="translate(190 100) scale(1 1)"><path d="M-26 40 Q-34 0 -30 -40 Q-28 -56 -18 -56 Q-10 -56 -10 -40 L-10 -62 Q-8 -76 2 -76 Q12 -76 12 -62 L12 -58 Q14 -70 24 -68 Q32 -66 32 -54 L32 -30 Q40 -40 46 -32 Q50 -26 44 -14 L30 30 Q24 44 0 46 Q-20 46 -26 40Z" fill="#7FD3E8"/></g>'
             '<ellipse cx="0" cy="110" rx="72" ry="84" fill="#20323F"/>'
             '<path d="M-76 96 Q-74 20 0 18 Q74 20 76 96 Q40 70 0 72 Q-40 70 -76 96Z" fill="#F2555A"/>'
             + ''.join(f'<circle cx="{x}" cy="{y}" r="7" fill="#FFD84A"/>' for x, y in [(-40, 50), (-10, 34), (24, 44), (50, 66), (-56, 76), (10, 62)]) +
             '<path d="M-20 92 Q-30 150 -10 180" stroke="#141c26" stroke-width="18" stroke-linecap="round" fill="none"/></g>')
    glow = 'style="filter:drop-shadow(0 0 12px #5CF2B5)"'
    s.append(f'<g transform="translate(60 -440)"><path d="M80 900 H300 l20 -40 l24 90 l26 -170 l28 160 l20 -40 H520 l40 -80 l60 30 l80 -150 l80 50 l120 -260" fill="none" stroke="#5CF2B5" stroke-width="8" stroke-linejoin="round" stroke-linecap="round" {glow}/>'
             f'<path d="M900 490 l-50 8 m50 -8 l-10 48" stroke="#5CF2B5" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none" {glow}/></g>')
    return svg(''.join(s))

def atrium(svg):
    """Department store atrium with skylight and indoor garden; a neatly dressed woman from behind."""
    R = random.Random(12)
    s = ['<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF7EA"/><stop offset="1" stop-color="#F3E3CC"/></linearGradient>'
         '<linearGradient id="floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E9D7BF"/><stop offset="1" stop-color="#CDB596"/></linearGradient>'
         '<radialGradient id="sun" cx=".55" cy="0" r=".9"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".9"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient></defs>'
         '<rect width="1600" height="1000" fill="url(#sky)"/>']
    for i in range(14):
        x = 100 + i * 110
        s.append(f'<path d="M{x} 0 Q{800+(x-800)*.55} 120 {800+(x-800)*.35} 210" stroke="#D9C3A2" stroke-width="5" fill="none"/>')
    s.append('<path d="M0 210 Q800 150 1600 210 L1600 240 Q800 180 0 240Z" fill="#E2CDAE"/><rect width="1600" height="700" fill="url(#sun)"/>')
    shop = ["#F7C9A9", "#CFE3D2", "#F3DDB2", "#E9C1C1"]
    for k, (y, h) in enumerate([(250, 120), (390, 130), (540, 140)]):
        s.append(f'<path d="M0 {y} L520 {y+30+k*10} L520 {y+h} L0 {y+h+20}Z" fill="#EADBC4"/><path d="M1600 {y} L1080 {y+30+k*10} L1080 {y+h} L1600 {y+h+20}Z" fill="#EADBC4"/>')
        for j in range(5):
            x = 30 + j * 98
            s.append(f'<rect x="{x}" y="{y+40+k*6}" width="70" height="{h-55}" rx="6" fill="{R.choice(shop)}" opacity=".9"/>')
            s.append(f'<rect x="{1600-x-70}" y="{y+40+k*6}" width="70" height="{h-55}" rx="6" fill="{R.choice(shop)}" opacity=".9"/>')
        s.append(f'<path d="M0 {y+h+20} L520 {y+h}" stroke="#B89A74" stroke-width="5"/><path d="M1600 {y+h+20} L1080 {y+h}" stroke="#B89A74" stroke-width="5"/>')
    s.append('<path d="M0 700 L520 680 L1080 680 L1600 700 L1600 1000 L0 1000Z" fill="url(#floor)"/>')
    s.append('<path d="M560 700 Q800 640 1040 700 L1000 760 Q800 720 600 760Z" fill="#B8956C"/>')
    for cx, cy, r, c in [(640, 560, 90, '#7FB28A'), (760, 500, 120, '#5E9C72'), (880, 530, 105, '#6FAA7E'), (980, 580, 80, '#88BC92'), (700, 620, 70, '#4E8A62'), (850, 620, 80, '#5E9C72')]:
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" filter="url(#paint)"/>')
    s.append('<rect x="752" y="560" width="14" height="150" fill="#7A5A3C"/><rect x="872" y="580" width="12" height="130" fill="#7A5A3C"/>')
    s.append('<rect x="560" y="760" width="480" height="120" fill="#FFFFFF" opacity=".18" filter="url(#blur30)"/>')
    for x, c in [(420, '#6B5A70'), (1080, '#4F5B7A'), (1450, '#8E6A5A')]:
        s.append(f'<g transform="translate({x} 640) scale(.45)" opacity=".75"><circle cx="40" cy="20" r="20" fill="#3A2E2E"/><path d="M14 46 Q40 36 66 46 L74 160 L6 160Z" fill="{c}"/><rect x="18" y="158" width="12" height="40" fill="#3A2E2E"/><rect x="48" y="158" width="12" height="40" fill="#3A2E2E"/></g>')
    pleats = ''.join(f'<path d="M{8+i*18} 340 L{30+i*12.5} 230" stroke="#5E4236" stroke-width="3"/>' for i in range(9))
    s.append('<g transform="translate(1180 560)">'
             '<ellipse cx="80" cy="420" rx="90" ry="14" fill="#8E7356" opacity=".35"/>'
             '<rect x="52" y="330" width="18" height="84" fill="#F1D9C6"/><rect x="92" y="330" width="18" height="84" fill="#F1D9C6"/>'
             '<path d="M46 410 h30 v12 h-32z M88 410 h30 v12 h-32z" fill="#3A2A22"/>'
             '<path d="M30 230 L130 230 L152 340 L8 340Z" fill="#7A5A4A"/>' + pleats +
             '<path d="M28 100 Q80 82 132 100 L140 240 Q80 252 20 240Z" fill="#F6EBD8"/><path d="M80 100 L80 240" stroke="#E3D2B6" stroke-width="3"/>'
             '<path d="M24 110 Q6 170 14 236" stroke="#F6EBD8" stroke-width="30" stroke-linecap="round" fill="none"/><path d="M136 110 Q156 170 150 230" stroke="#F6EBD8" stroke-width="30" stroke-linecap="round" fill="none"/>'
             '<path d="M44 40 Q80 4 116 40 L120 104 Q80 118 40 104Z" fill="#2E1E1A"/>'
             '<path d="M150 180 L170 300 L104 300 L116 180Z" fill="#FFFFFF" stroke="#D8C7AA" stroke-width="3"/><path d="M122 182 Q136 140 148 182" stroke="#3A2A22" stroke-width="5" fill="none"/></g>')
    return svg(''.join(s))

def maple(svg):
    """Maple tunnel walking path with a wooden fence and a stone wall."""
    R = random.Random(21)
    VP = (780, 560)
    s = ['<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9FD0F2"/><stop offset="1" stop-color="#E8F4FC"/></linearGradient>'
         '<linearGradient id="path" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#CFC6BD"/><stop offset="1" stop-color="#9C9087"/></linearGradient></defs>'
         '<rect width="1600" height="1000" fill="url(#sky)"/><path d="M0 600 L1600 600 L1600 1000 L0 1000Z" fill="#B88A5A"/>']
    s.append(f'<path d="M{VP[0]-18} {VP[1]} L{VP[0]+22} {VP[1]} L1180 1000 L380 1000Z" fill="url(#path)"/>')
    s.append(f'<path d="M{VP[0]+30} {VP[1]} L{VP[0]+60} {VP[1]-10} L1600 760 L1600 1000 L1240 1000Z" fill="#B7B1AA"/>')
    for i in range(140):
        t = R.random() ** .8
        x = VP[0] + 40 + (1600 - VP[0] - 40) * t + R.uniform(-30, 30)
        ytop = VP[1] - 10 + (760 - VP[1] + 10) * t; ybot = VP[1] + (1000 - VP[1]) * t
        y = R.uniform(ytop, ybot); w, h = 10 + 70 * t, 6 + 40 * t
        s.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{h/3:.0f}" fill="{R.choice(["#D6D1CB","#A39C94","#C3BDB6","#8F8881"])}" opacity=".9"/>')
    for _ in range(26):
        side = R.choice([-1, 1]); t = R.uniform(.05, 1)
        x = VP[0] + side * (40 + 760 * t) + R.uniform(-30, 30); yb = VP[1] + 440 * t
        s.append(f'<path d="M{x:.0f} {yb:.0f} Q{x+side*R.uniform(10,60):.0f} {yb-200*t-60:.0f} {x+side*R.uniform(40,140):.0f} {VP[1]-300*t-80:.0f}" stroke="#4A3226" stroke-width="{3+16*t:.0f}" fill="none" stroke-linecap="round"/>')
    cols = ['#E8381E', '#F25C1E', '#F7861E', '#FBB02A', '#FFD13A', '#C9221E', '#F0503A', '#E26A2C', '#D9301F', '#FFC23D']
    g = []
    for _ in range(1600):
        x, y = R.uniform(-80, 1680), R.uniform(-80, 760)
        dx, dy = (x - VP[0]) / 800, (y - VP[1] + 120) / 600
        d = math.hypot(dx, dy * 1.4)
        if d < .32 + R.uniform(-.05, .08): continue
        if y > 640 and abs(x - VP[0]) < 520: continue
        r = R.uniform(14, 46) * (0.6 + d)
        g.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.0f}" fill="{R.choice(cols)}" opacity="{R.uniform(.55,.95):.2f}"/>')
    s.append('<g filter="url(#paint)">' + ''.join(g) + '</g>')
    s.append('<g filter="url(#soft)">' + ''.join(f'<circle cx="{R.uniform(0,1600):.0f}" cy="{R.uniform(0,640):.0f}" r="{R.uniform(4,10):.0f}" fill="{R.choice(cols)}"/>' for _ in range(260)) + '</g>')
    s.append('<g filter="url(#paint)">' + ''.join(f'<circle cx="{R.uniform(1100,1600):.0f}" cy="{R.uniform(600,760):.0f}" r="{R.uniform(20,50):.0f}" fill="{R.choice(["#E8557A","#F07A96","#C93A62"])}" opacity=".85"/>' for _ in range(40)) + '</g>')
    posts = []
    for i in range(12):
        t = (i / 11) ** 1.6
        posts.append((VP[0] - 50 - (VP[0] + 40) * t, VP[1] + 40 + 420 * t, 40 + 260 * t, 4 + 30 * t))
    for x, yb, h, w in posts:
        s.append(f'<rect x="{x-w/2:.0f}" y="{yb-h:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{w/3:.0f}" fill="#7A4F34"/>')
    for k in (.25, .62):
        s.append('<path d="' + ' '.join(f'{"M" if j == 0 else "L"}{x:.0f} {yb-h*(1-k):.0f}' for j, (x, yb, h, w) in enumerate(posts)) + '" stroke="#8B5E3E" stroke-width="12" fill="none" stroke-linecap="round"/>')
    s.append(''.join(f'<ellipse cx="{R.uniform(380,1180):.0f}" cy="{R.uniform(700,1000):.0f}" rx="{R.uniform(4,11):.0f}" ry="{R.uniform(2,5):.0f}" fill="{R.choice(cols)}" opacity=".85"/>' for _ in range(220)))
    s.append(f'<g transform="translate({VP[0]-14} {VP[1]-8}) scale(.22)"><circle cx="20" cy="10" r="12" fill="#2A2A3A"/><rect x="6" y="24" width="28" height="60" rx="8" fill="#3A4A6A"/></g>'
             f'<g transform="translate({VP[0]+6} {VP[1]-6}) scale(.2)"><circle cx="20" cy="10" r="12" fill="#2A2A3A"/><rect x="6" y="24" width="28" height="60" rx="8" fill="#6A3A3A"/></g>')
    return svg(''.join(s))

def concert(svg):
    """Concert seen from the crowd: stage, LED screen, beams, a sea of light sticks. Performers only as tiny silhouettes."""
    R = random.Random(14)
    s = ['<defs><linearGradient id="bgk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0E0B2E"/><stop offset="1" stop-color="#2C1660"/></linearGradient>'
         '<linearGradient id="bm" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C8B6FF" stop-opacity=".5"/><stop offset="1" stop-color="#C8B6FF" stop-opacity="0"/></linearGradient>'
         '<linearGradient id="scr" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FF5FA2"/><stop offset=".5" stop-color="#7C5CFF"/><stop offset="1" stop-color="#2DD4FF"/></linearGradient></defs>'
         '<rect width="1600" height="1000" fill="url(#bgk)"/>']
    for x, r in [(300, -20), (620, -8), (980, 8), (1300, 20)]:
        s.append(f'<path d="M{x-20} 40 L{x+20} 40 L{x+300} 820 L{x-300} 820Z" fill="url(#bm)" transform="rotate({r} {x} 40)"/>')
    s.append('<rect x="460" y="150" width="680" height="380" rx="14" fill="url(#scr)"/><rect x="460" y="150" width="680" height="380" rx="14" fill="#000" opacity=".15"/>')
    for i in range(10):
        s.append(f'<circle cx="{560+i*60}" cy="{340+40*math.sin(i)}" r="{18+10*math.cos(i*1.7):.0f}" fill="#FFFFFF" opacity=".25"/>')
    s.append('<path d="M240 600 H1360 L1460 680 H140Z" fill="#1B1442"/><rect x="140" y="680" width="1320" height="30" fill="#120D33"/>')
    for x in (720, 790, 860):
        s.append(f'<g transform="translate({x} 520)" fill="#0B0820"><circle cx="0" cy="0" r="14"/><path d="M-16 18 Q0 10 16 18 L20 80 L-20 80Z"/></g>')
    s.append('<rect x="0" y="700" width="1600" height="300" fill="#0B0820"/>')
    cols = ['#FF5FA2', '#FFD84A', '#5CF2B5', '#7DA8FF', '#FFFFFF']
    for row in range(4):
        for i in range(30):
            x = i * 56 + (row % 2) * 28 + R.uniform(-8, 8); y = 760 + row * 60 + R.uniform(-10, 10); c = R.choice(cols)
            s.append(f'<circle cx="{x:.0f}" cy="{y+50:.0f}" r="{24+row*4}" fill="#151033"/>'
                     f'<path d="M{x:.0f} {y+30:.0f} l{R.uniform(-10,10):.0f} -60" stroke="#8A86B0" stroke-width="5"/>'
                     f'<circle cx="{x:.0f}" cy="{y-34:.0f}" r="{11+row*2}" fill="{c}" style="filter:drop-shadow(0 0 10px {c})"/>')
    for _ in range(70):
        x, y = R.uniform(0, 1600), R.uniform(0, 650)
        s.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{R.uniform(6,12):.0f}" height="{R.uniform(10,18):.0f}" fill="{R.choice(cols)}" transform="rotate({R.uniform(0,90):.0f} {x:.0f} {y:.0f})" opacity=".85"/>')
    return svg(''.join(s))

def street_night(svg):
    """Seoul side street at dusk: a glowing convenience store, an orange taxi, shop signs in hangul, wet road."""
    R = random.Random(15)
    s = ['<defs><linearGradient id="dsk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1B2556"/><stop offset=".6" stop-color="#5A4C8A"/><stop offset="1" stop-color="#F29E7A"/></linearGradient>'
         '<linearGradient id="rd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3A3657"/><stop offset="1" stop-color="#1A1830"/></linearGradient>'
         '<radialGradient id="glo" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFF4C2" stop-opacity=".8"/><stop offset="1" stop-color="#FFF4C2" stop-opacity="0"/></radialGradient></defs>'
         '<rect width="1600" height="1000" fill="url(#dsk)"/>']
    # back buildings with signs
    for x0, w, top in [(0, 220, 180), (210, 180, 260), (380, 200, 140), (1380, 220, 200)]:
        s.append(f'<rect x="{x0}" y="{top}" width="{w}" height="{700-top}" fill="#2A2650"/>')
        for wy in range(top + 24, 660, 40):
            for wx in range(x0 + 16, x0 + w - 20, 34):
                if R.random() < .5: s.append(f'<rect x="{wx}" y="{wy}" width="16" height="20" fill="#FFD98A" opacity="{R.uniform(.5,.9):.2f}"/>')
    signs = [(40, 300, '약국', '#12A57A'), (240, 340, '카페', '#F2555A'), (410, 220, '노래방', '#7C5CFF'), (1420, 290, '식당', '#FF9F43')]
    for x, y, t, c in signs:
        s.append(f'<rect x="{x}" y="{y}" width="{60+len(t)*46}" height="70" rx="10" fill="{c}" style="filter:drop-shadow(0 0 12px {c})"/><text x="{x+30+len(t)*23}" y="{y+50}" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="42" fill="#fff">{t}</text>')
    # convenience store, glowing
    s.append('<circle cx="1000" cy="520" r="420" fill="url(#glo)"/>')
    s.append('<rect x="640" y="300" width="740" height="400" fill="#F4F7EF"/><rect x="620" y="270" width="780" height="80" fill="#12A57A"/>'
             '<text x="1010" y="326" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="46" fill="#fff">편의점</text>'
             '<rect x="680" y="380" width="300" height="320" fill="#FFF8DC"/><rect x="1010" y="380" width="330" height="240" fill="#FFF8DC"/>')
    for i in range(3):
        s.append(f'<rect x="1030" y="{420+i*66}" width="290" height="8" fill="#C9A06A"/>' + ''.join(f'<rect x="{1040+j*36}" y="{388+i*66}" width="24" height="32" rx="4" fill="{R.choice(["#F2555A","#FFD84A","#2446F0","#12A57A","#FF9F43"])}"/>' for j in range(8)))
    s.append('<rect x="700" y="560" width="120" height="60" rx="6" fill="#FFD84A" opacity=".8"/><rect x="840" y="600" width="120" height="100" rx="6" fill="#F2555A" opacity=".5"/>')
    # sidewalk, road, reflections
    s.append('<rect y="700" width="1600" height="40" fill="#8E8AA8"/><rect y="740" width="1600" height="260" fill="url(#rd)"/>')
    for x, c in [(1000, '#FFF4C2'), (300, '#F2555A'), (80, '#12A57A'), (480, '#7C5CFF')]:
        s.append(f'<rect x="{x-40}" y="750" width="80" height="240" fill="{c}" opacity=".22" filter="url(#blur8)"/>')
    for x in range(40, 1600, 240):
        s.append(f'<rect x="{x}" y="880" width="130" height="12" rx="6" fill="#FFFFFF" opacity=".35"/>')
    # taxi
    s.append('<g transform="translate(140 600)"><path d="M70 160 l60 -96 h300 l90 96 h70 a20 20 0 0 1 20 20 v70 H0 v-70 a20 20 0 0 1 20 -20Z" fill="#FF9F43"/>'
             '<path d="M150 80 h120 v80 h-160Z M300 80 h110 l66 80 h-176Z" fill="#2A3460"/><rect x="230" y="26" width="110" height="40" rx="8" fill="#FFF4C2" style="filter:drop-shadow(0 0 10px #FFE98A)"/>'
             '<text x="285" y="56" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="26" fill="#3A2A22">TAXI</text>'
             '<circle cx="140" cy="250" r="44" fill="#141414"/><circle cx="140" cy="250" r="18" fill="#8E8AA8"/><circle cx="470" cy="250" r="44" fill="#141414"/><circle cx="470" cy="250" r="18" fill="#8E8AA8"/>'
             '<rect x="600" y="190" width="40" height="20" rx="6" fill="#FFF4C2" style="filter:drop-shadow(0 0 14px #FFF4C2)"/></g>')
    # street lamp
    s.append('<rect x="1470" y="360" width="12" height="380" fill="#141832"/><path d="M1440 350 h72 l-10 26 h-52z" fill="#FFF4C2" style="filter:drop-shadow(0 0 22px #FFE98A)"/>')
    return svg(''.join(s))

def desk(svg):
    """Top-down desk still life for a residence-card guide: passport, card, number ticket, pen, stamp, coffee."""
    s = ['<defs><linearGradient id="wd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E0B98C"/><stop offset="1" stop-color="#C99A68"/></linearGradient></defs>'
         '<rect width="1600" height="1000" fill="url(#wd)"/>']
    for y in range(40, 1000, 90):
        s.append(f'<path d="M0 {y} Q400 {y+14} 800 {y} T1600 {y}" stroke="#B88A5A" stroke-width="3" fill="none" opacity=".35"/>')
    sh = 'style="filter:drop-shadow(0 18px 18px rgba(60,30,10,.35))"'
    # application form
    s.append(f'<g transform="translate(860 90) rotate(6)" {sh}><rect width="560" height="740" rx="8" fill="#FFFFFF"/>'
             '<text x="40" y="90" font-family="Nanum Myeongjo" font-weight="800" font-size="46" fill="#141838">신청서</text>'
             + ''.join(f'<rect x="40" y="{150+i*70}" width="{[480,420,460,300,440,380,260,420][i]}" height="16" rx="8" fill="#DCE1EE"/>' for i in range(8)) +
             '<rect x="40" y="690" width="200" height="16" rx="8" fill="#FFD84A"/></g>')
    # passport
    s.append(f'<g transform="translate(560 520) rotate(-12)" {sh}><rect width="300" height="420" rx="18" fill="#7A2329"/>'
             '<circle cx="150" cy="170" r="56" fill="none" stroke="#E8C46A" stroke-width="6"/><path d="M110 170 h80 M150 130 v80" stroke="#E8C46A" stroke-width="5"/>'
             '<text x="150" y="300" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="800" font-size="34" fill="#E8C46A">PASSPORT</text></g>')
    # residence card, big
    s.append(f'<g transform="translate(140 140) rotate(-5)" {sh}><rect width="620" height="390" rx="28" fill="#FFFFFF"/>'
             '<rect width="620" height="92" rx="28" fill="#2446F0"/><rect y="60" width="620" height="32" fill="#2446F0"/>'
             '<text x="40" y="64" font-family="Nanum Myeongjo" font-weight="800" font-size="46" fill="#FFFFFF">외국인등록증</text>'
             '<rect x="40" y="128" width="170" height="220" rx="14" fill="#E8ECFF"/><circle cx="125" cy="210" r="42" fill="#B9C3E6"/><path d="M60 340 Q125 250 190 340Z" fill="#B9C3E6"/>'
             + ''.join(f'<rect x="250" y="{150+i*54}" width="{w}" height="24" rx="12" fill="{c}"/>' for i, (w, c) in enumerate([(320, '#DCE1EE'), (250, '#DCE1EE'), (290, '#DCE1EE'), (190, '#FFD84A')])) +
             '<circle cx="540" cy="320" r="34" fill="none" stroke="#F2555A" stroke-width="5" opacity=".7"/></g>')
    # number ticket
    s.append(f'<g transform="translate(1180 760) rotate(-8)" {sh}><rect width="230" height="150" rx="10" fill="#FFFDF4"/>'
             '<text x="115" y="50" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="700" font-size="30" fill="#5A5F80">번호표</text>'
             '<text x="115" y="122" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="800" font-size="64" fill="#141838">0127</text></g>')
    # pen, stamp, coffee
    s.append(f'<g transform="translate(900 860) rotate(-28)" {sh}><rect width="320" height="26" rx="13" fill="#141838"/><path d="M320 0 l40 13 l-40 13Z" fill="#E8C46A"/><rect x="40" y="-6" width="16" height="38" rx="6" fill="#E8C46A"/></g>')
    s.append(f'<g transform="translate(1440 120)" {sh}><circle r="100" fill="#FFFFFF"/><circle r="78" fill="#6B4430"/><circle r="78" fill="none" stroke="#8A5A40" stroke-width="10"/><ellipse cx="-20" cy="-20" rx="30" ry="14" fill="#C9906A" opacity=".5"/></g>')
    s.append(f'<g transform="translate(160 760)" {sh}><rect x="-50" y="0" width="100" height="70" rx="14" fill="#F2555A"/><rect x="-20" y="-80" width="40" height="90" rx="12" fill="#3A2A22"/></g>')
    return svg(''.join(s))

# ---- 2026-10-22 batch ----
def disguise_night(svg):
    """Seoul business district at night: glass towers, a black car, one tiny suited figure from behind, open handcuffs glinting."""
    R = random.Random(21)
    s = ['<defs><linearGradient id="dn_sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#070B22"/><stop offset=".7" stop-color="#1B2A5A"/><stop offset="1" stop-color="#6A3C6E"/></linearGradient>'
         '<linearGradient id="dn_gl" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#1E3C6E"/><stop offset="1" stop-color="#2F5C8E"/></linearGradient>'
         '<linearGradient id="dn_rd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1A1C34"/><stop offset="1" stop-color="#0A0B18"/></linearGradient>'
         '<radialGradient id="dn_lamp" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFE7B0" stop-opacity=".7"/><stop offset="1" stop-color="#FFE7B0" stop-opacity="0"/></radialGradient></defs>'
         '<rect width="1600" height="1000" fill="url(#dn_sky)"/>']
    for _ in range(60):
        s.append(f'<circle cx="{R.uniform(0,1600):.0f}" cy="{R.uniform(0,260):.0f}" r="{R.uniform(1,2.4):.1f}" fill="#fff" opacity="{R.uniform(.3,.8):.2f}"/>')
    # far skyline
    x = 0
    while x < 1600:
        w = R.uniform(70, 140); h = R.uniform(220, 420)
        s.append(f'<rect x="{x:.0f}" y="{700-h:.0f}" width="{w:.0f}" height="{h:.0f}" fill="#141C40"/>'); x += w + 6
    # main glass towers on the right
    for x0, w, top in [(820, 230, 120), (1080, 260, 40), (1360, 240, 170)]:
        s.append(f'<rect x="{x0}" y="{top}" width="{w}" height="{720-top}" fill="url(#dn_gl)"/>'
                 f'<path d="M{x0} {top} l{w} 0 l0 {720-top} Z" fill="#fff" opacity=".05"/>')
        for wy in range(top + 20, 700, 28):
            for wx in range(x0 + 12, x0 + w - 14, 24):
                if R.random() < .42: s.append(f'<rect x="{wx}" y="{wy}" width="14" height="16" fill="#FFE29A" opacity="{R.uniform(.4,.95):.2f}"/>')
    s.append('<rect x="1150" y="20" width="6" height="30" fill="#F2555A"/><circle cx="1153" cy="18" r="6" fill="#FF6B70" style="filter:drop-shadow(0 0 8px #FF6B70)"/>')
    # street
    s.append('<rect y="700" width="1600" height="300" fill="url(#dn_rd)"/><rect y="700" width="1600" height="26" fill="#2E3150"/>')
    for x in range(60, 1600, 220):
        s.append(f'<rect x="{x}" y="860" width="120" height="10" rx="5" fill="#fff" opacity=".25"/>')
    # street lamp
    s.append('<circle cx="1480" cy="430" r="200" fill="url(#dn_lamp)"/><rect x="1474" y="430" width="10" height="290" fill="#3A3D5C"/><rect x="1440" y="420" width="80" height="16" rx="8" fill="#FFE7B0"/>')
    # black car
    s.append('<g transform="translate(860 640)" style="filter:drop-shadow(0 16px 14px rgba(0,0,0,.5))">'
             '<path d="M0 110 v-40 q0 -20 20 -24 l90 -12 l70 -50 h190 l80 50 l80 14 q20 4 20 24 v38Z" fill="#0C0E1C"/>'
             '<path d="M190 34 l58 -42 h88 v42Z M346 34 v-42 h60 l58 42Z" fill="#3B5A8A" opacity=".75"/>'
             '<circle cx="110" cy="112" r="34" fill="#05060D"/><circle cx="110" cy="112" r="14" fill="#5C6080"/><circle cx="440" cy="112" r="34" fill="#05060D"/><circle cx="440" cy="112" r="14" fill="#5C6080"/>'
             '<rect x="530" y="66" width="22" height="12" rx="4" fill="#FFF2C0" style="filter:drop-shadow(0 0 14px #FFF2C0)"/></g>')
    s.append('<path d="M1412 760 l200 40 v-60Z" fill="#FFF2C0" opacity=".12"/>')
    # tiny figure from behind, dark suit, short hair
    s.append('<g transform="translate(1330 600)" fill="#06070F"><circle cx="0" cy="0" r="16"/><path d="M-22 22 q22 -8 44 0 l6 80 h-56Z"/><rect x="-18" y="100" width="14" height="70"/><rect x="4" y="100" width="14" height="70"/></g>')
    s.append('<ellipse cx="1330" cy="772" rx="40" ry="8" fill="#000" opacity=".4"/>')
    # handcuffs glinting on the pavement, right foreground
    s.append('<g transform="translate(1250 880) rotate(-12)" fill="none" stroke="#C9D2E8" stroke-width="12" style="filter:drop-shadow(0 0 10px #8FA8FF)">'
             '<ellipse cx="0" cy="0" rx="46" ry="34"/><ellipse cx="150" cy="10" rx="46" ry="34"/><circle cx="62" cy="2" r="9" stroke-width="6"/><circle cx="80" cy="5" r="9" stroke-width="6"/><circle cx="98" cy="8" r="9" stroke-width="6"/></g>')
    return svg(''.join(s))

def muse_stage(svg):
    """Dreamy fantasy stage: big moon, floating gold gallery frames, a birthday cake with candles, a sea of light sticks. Performers only tiny silhouettes."""
    R = random.Random(22)
    s = ['<defs><linearGradient id="ms_sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2A1E5C"/><stop offset=".55" stop-color="#8E6CC9"/><stop offset="1" stop-color="#F6B9C9"/></linearGradient>'
         '<radialGradient id="ms_moon" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFF7E0"/><stop offset=".7" stop-color="#FFE9B8"/><stop offset="1" stop-color="#FFE9B8" stop-opacity="0"/></radialGradient>'
         '<linearGradient id="ms_gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFE29A"/><stop offset="1" stop-color="#C9922E"/></linearGradient></defs>'
         '<rect width="1600" height="1000" fill="url(#ms_sky)"/>']
    s.append('<circle cx="1180" cy="270" r="230" fill="url(#ms_moon)"/><circle cx="1180" cy="270" r="160" fill="#FFF7E0"/>'
             '<circle cx="1130" cy="230" r="22" fill="#F2DDB0" opacity=".6"/><circle cx="1230" cy="320" r="14" fill="#F2DDB0" opacity=".6"/>')
    for _ in range(90):
        x, y = R.uniform(0, 1600), R.uniform(0, 520)
        s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{R.uniform(1.5,4):.1f}" fill="#FFF7E0" opacity="{R.uniform(.4,.9):.2f}"/>')
    # floating gallery frames with soft painted skies inside
    for x, y, w, h, rot, c1, c2 in [(760, 120, 200, 250, -8, '#7FB7FF', '#FFC6D9'), (1420, 110, 150, 190, 10, '#FFD38A', '#C79BFF'), (900, 430, 160, 120, 6, '#A6F0D0', '#7FB7FF')]:
        s.append(f'<g transform="rotate({rot} {x+w/2} {y+h/2})" style="filter:drop-shadow(0 14px 16px rgba(40,10,80,.4))">'
                 f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#ms_gold)"/>'
                 f'<rect x="{x+16}" y="{y+16}" width="{w-32}" height="{h-32}" fill="{c1}"/><path d="M{x+16} {y+h-16} q{(w-32)/2} -{h/3} {w-32} 0Z" fill="{c2}"/></g>')
    # stage
    s.append('<path d="M560 640 H1600 V700 H480Z" fill="#3B2470"/><rect x="480" y="700" width="1120" height="26" fill="#2A1852"/>')
    for x in (1300, 1350, 1400, 1450, 1500, 1550):
        s.append(f'<g transform="translate({x} 570)" fill="#1A0F3A"><circle cx="0" cy="0" r="12"/><path d="M-14 16 Q0 8 14 16 L17 70 L-17 70Z"/></g>')
    # birthday cake
    s.append('<g transform="translate(980 500)" style="filter:drop-shadow(0 16px 16px rgba(40,10,80,.45))">'
             '<rect x="0" y="60" width="220" height="80" rx="10" fill="#FFF3F6"/><path d="M0 74 q27 24 55 0 q27 24 55 0 q27 24 55 0 q27 24 55 0" fill="#FF9FC0"/>'
             '<rect x="30" y="0" width="160" height="66" rx="10" fill="#FFE1EA"/><path d="M30 12 q20 18 40 0 q20 18 40 0 q20 18 40 0 q20 18 40 0" fill="#C79BFF"/>'
             + ''.join(f'<rect x="{50+i*30}" y="-40" width="10" height="40" rx="3" fill="{c}"/><ellipse cx="{55+i*30}" cy="-52" rx="8" ry="13" fill="#FFD84A" style="filter:drop-shadow(0 0 10px #FFB84A)"/>' for i, c in enumerate(['#7FB7FF', '#FF9FC0', '#A6F0D0', '#FFD38A', '#C79BFF'])) +
             '<rect x="-20" y="140" width="260" height="14" rx="7" fill="#E9DAFF"/></g>')
    # crowd with light sticks (right two thirds, dark)
    s.append('<rect y="726" width="1600" height="274" fill="#140B30"/>')
    cols = ['#FFF7E0', '#FFC6D9', '#C79BFF', '#7FB7FF', '#FFD84A']
    for row in range(4):
        for i in range(30):
            x = i * 56 + (row % 2) * 28 + R.uniform(-8, 8); y = 780 + row * 56 + R.uniform(-8, 8)
            if x < 380 and R.random() < .7: continue
            c = R.choice(cols)
            s.append(f'<circle cx="{x:.0f}" cy="{y+48:.0f}" r="{24+row*4}" fill="#0E0724"/>'
                     f'<path d="M{x:.0f} {y+28:.0f} l{R.uniform(-10,10):.0f} -56" stroke="#7A70A8" stroke-width="5"/>'
                     f'<circle cx="{x:.0f}" cy="{y-32:.0f}" r="{11+row*2}" fill="{c}" style="filter:drop-shadow(0 0 10px {c})"/>')
    return svg(''.join(s))

def seongbuk_hill(svg):
    """Seongbuk-dong hillside at dusk: hanok roofs, the stone city wall, ginkgo trees, tall wooden standing sculptures, a loop bus, lantern light."""
    R = random.Random(23)
    s = ['<defs><linearGradient id="sb_sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3C3A78"/><stop offset=".55" stop-color="#C77A8A"/><stop offset="1" stop-color="#F7C08A"/></linearGradient>'
         '<radialGradient id="sb_lan" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFD98A" stop-opacity=".8"/><stop offset="1" stop-color="#FFD98A" stop-opacity="0"/></radialGradient></defs>'
         '<rect width="1600" height="1000" fill="url(#sb_sky)"/>']
    s.append('<circle cx="1260" cy="300" r="60" fill="#FFE7B8" opacity=".9"/>')
    s.append('<path d="M0 520 Q300 380 620 470 T1200 400 T1600 440 V1000 H0Z" fill="#5A4A7A"/>')
    # fortress wall along the ridge
    s.append('<path d="M560 520 Q900 430 1600 470 V520 Q900 480 560 560Z" fill="#B9A58E"/>')
    for i in range(30):
        t = i / 29; x = 560 + t * 1040; y = 520 - 70 * math.sin(t * math.pi * .9) + (t * 0)
        s.append(f'<rect x="{x:.0f}" y="{y-22:.0f}" width="22" height="22" fill="#A8937C"/>')
    s.append('<path d="M0 640 Q400 560 800 620 T1600 600 V1000 H0Z" fill="#3E3260"/>')
    # hanok roofs cluster (right half)
    for x, y, w in [(760, 600, 260), (1020, 580, 300), (1300, 610, 260), (900, 700, 300), (1220, 700, 340)]:
        s.append(f'<g style="filter:drop-shadow(0 10px 10px rgba(0,0,0,.35))"><rect x="{x+30}" y="{y+40}" width="{w-60}" height="80" fill="#EFE2C8"/>'
                 f'<rect x="{x+50}" y="{y+60}" width="40" height="50" fill="#FFD98A"/><rect x="{x+w-100}" y="{y+60}" width="40" height="50" fill="#FFD98A"/>'
                 f'<path d="M{x-20} {y+46} Q{x+w/2} {y+20} {x+w+20} {y+46} L{x+w-20} {y} Q{x+w/2} {y-16} {x+20} {y}Z" fill="#2B2B3E"/>'
                 f'<path d="M{x-20} {y+46} Q{x+w/2} {y+20} {x+w+20} {y+46}" stroke="#4A4A66" stroke-width="6" fill="none"/></g>')
    # tall slim wooden standing sculptures beside the wall
    for x, h in [(640, 190), (690, 230), (735, 170)]:
        s.append(f'<g fill="#7A4E2C"><ellipse cx="{x}" cy="{560-h}" rx="12" ry="16"/><rect x="{x-9}" y="{560-h+14}" width="18" height="{h-14}" rx="8"/></g>'
                 f'<rect x="{x-3}" y="{560-h+20}" width="5" height="{h-30}" fill="#A06A3E" opacity=".6"/>')
    # ginkgo trees
    for x, y, r in [(560, 640, 90), (1520, 560, 110), (1120, 520, 70), (820, 520, 60)]:
        s.append(f'<rect x="{x-8}" y="{y}" width="16" height="{r+40}" fill="#4A3424"/>')
        for _ in range(16):
            s.append(f'<circle cx="{x+R.uniform(-r*.7,r*.7):.0f}" cy="{y-r*.4+R.uniform(-r*.6,r*.5):.0f}" r="{R.uniform(r*.3,r*.5):.0f}" fill="{R.choice(["#F5C542","#F2B630","#FFD866"])}" opacity=".95"/>')
    # lanterns
    for x, y in [(980, 690), (1440, 700), (1180, 600)]:
        s.append(f'<circle cx="{x}" cy="{y}" r="80" fill="url(#sb_lan)"/><rect x="{x-10}" y="{y-14}" width="20" height="28" rx="6" fill="#FFE29A"/>')
    # lane + small green loop bus
    s.append('<path d="M480 1000 Q900 860 1600 880 V940 Q900 920 640 1000Z" fill="#6E6488"/>')
    s.append('<g transform="translate(1180 840)" style="filter:drop-shadow(0 8px 8px rgba(0,0,0,.4))"><rect x="0" y="0" width="200" height="70" rx="16" fill="#12A57A"/>'
             '<rect x="14" y="12" width="40" height="26" rx="4" fill="#DDF5EE"/><rect x="62" y="12" width="40" height="26" rx="4" fill="#DDF5EE"/><rect x="110" y="12" width="40" height="26" rx="4" fill="#DDF5EE"/><rect x="158" y="12" width="30" height="40" rx="4" fill="#DDF5EE"/>'
             '<circle cx="44" cy="72" r="14" fill="#1A1A2A"/><circle cx="160" cy="72" r="14" fill="#1A1A2A"/></g>')
    # falling ginkgo leaves
    for _ in range(26):
        x, y = R.uniform(300, 1600), R.uniform(80, 980)
        s.append(f'<path d="M{x:.0f} {y:.0f} q12 -14 24 0 q-12 6 -12 18 q0 -12 -12 -18Z" fill="#FFD23F" transform="rotate({R.uniform(0,360):.0f} {x:.0f} {y:.0f})"/>')
    for x in (1500, 1530):
        s.append(f'<g transform="translate({x} 830)" fill="#1E1834"><circle cx="0" cy="0" r="8"/><path d="M-9 10 h18 l3 40 h-24Z"/></g>')
    return svg(''.join(s))

def hoecnic_river(svg):
    """Han River park in golden late-autumn light: a picnic mat with trays of sliced raw fish, a ramen cup, skyline and bridge, tiny figures far away."""
    R = random.Random(24)
    s = ['<defs><linearGradient id="hr_sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6FA2D9"/><stop offset=".6" stop-color="#F3C48E"/><stop offset="1" stop-color="#F9DDB0"/></linearGradient>'
         '<linearGradient id="hr_riv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7FA8C9"/><stop offset="1" stop-color="#4C6F9A"/></linearGradient>'
         '<linearGradient id="hr_gr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9BA75A"/><stop offset="1" stop-color="#5D6A33"/></linearGradient></defs>'
         '<rect width="1600" height="1000" fill="url(#hr_sky)"/>']
    s.append('<circle cx="1300" cy="300" r="70" fill="#FFF1C9" opacity=".9"/>')
    x = 0
    while x < 1600:
        w = R.uniform(40, 110); h = R.uniform(60, 220)
        s.append(f'<rect x="{x:.0f}" y="{470-h:.0f}" width="{w:.0f}" height="{h:.0f}" fill="#8C8FB2" opacity=".75"/>'); x += w + 4
    s.append('<path d="M1060 470 l20 -260 l20 260Z" fill="#8C8FB2" opacity=".8"/><circle cx="1080" cy="230" r="14" fill="#8C8FB2"/>')
    s.append('<rect y="470" width="1600" height="150" fill="url(#hr_riv)"/>')
    # bridge with arches
    s.append('<rect y="430" width="1600" height="16" fill="#5E5A7E"/>')
    for x in range(0, 1600, 200):
        s.append(f'<path d="M{x} 446 q100 70 200 0" stroke="#5E5A7E" stroke-width="10" fill="none"/><rect x="{x-6}" y="446" width="12" height="70" fill="#5E5A7E"/>')
    for _ in range(14):
        s.append(f'<rect x="{R.uniform(0,1600):.0f}" y="{R.uniform(520,610):.0f}" width="{R.uniform(30,90):.0f}" height="4" rx="2" fill="#fff" opacity=".45"/>')
    s.append('<path d="M0 620 Q800 590 1600 620 V1000 H0Z" fill="url(#hr_gr)"/>')
    # tiny figures far away
    for x in (380, 410, 1450):
        s.append(f'<g transform="translate({x} 620)" fill="#3A3850"><circle cx="0" cy="0" r="7"/><path d="M-8 9 h16 l3 34 h-22Z"/></g>')
    # picnic mat (right)
    s.append('<g transform="translate(760 700)"><path d="M0 120 L120 0 H820 L840 260 H-40Z" fill="#F2F2F2" style="filter:drop-shadow(0 14px 12px rgba(0,0,0,.3))"/>'
             + ''.join(f'<path d="M{i*110} 260 L{120+i*100} 0" stroke="#5C9BD6" stroke-width="22" opacity=".55"/>' for i in range(8))
             + '<path d="M820 0 l40 -30 l-20 50Z" fill="#E6E6E6"/></g>')
    # sashimi trays
    for tx, ty in [(900, 760), (1150, 740)]:
        s.append(f'<g transform="translate({tx} {ty})" style="filter:drop-shadow(0 8px 6px rgba(0,0,0,.35))"><rect x="0" y="0" width="220" height="120" rx="14" fill="#1C1C24"/>'
                 '<path d="M14 92 q40 -40 80 -20 q40 -30 110 10 v20 h-190Z" fill="#E8F5E0"/>'
                 + ''.join(f'<path d="M{24+i*30} {80-(i%2)*10} q18 -40 34 -36 q-6 30 -22 46Z" fill="{c}" stroke="#fff" stroke-width="3"/>' for i, c in enumerate(['#FF9E8A', '#FFB39F', '#F7F2EC', '#FF9E8A', '#F7F2EC', '#FFB39F']))
                 + '<rect x="160" y="20" width="44" height="30" rx="6" fill="#7BC36B"/></g>')
    # ramen cup with steam
    s.append('<g transform="translate(1420 760)"><path d="M0 0 h90 l-12 110 h-66Z" fill="#F2555A"/><rect x="-6" y="-10" width="102" height="16" rx="6" fill="#fff"/>'
             '<path d="M30 -20 q-14 -30 4 -60 M60 -20 q-14 -30 4 -60" stroke="#fff" stroke-width="6" fill="none" opacity=".7"/></g>')
    # ice bag + chopsticks
    s.append('<g transform="translate(1300 880)"><path d="M0 0 q60 -30 120 0 l-10 50 h-100Z" fill="#CFE9FF" opacity=".85"/></g>'
             '<path d="M1080 900 l140 -40 M1086 912 l140 -40" stroke="#C9A06A" stroke-width="7"/>')
    return svg(''.join(s))

def boiler_room(svg):
    """A cosy one-room on a winter night: wall boiler control panel, bubble wrap on a frosted window, warm floor mat, socks and a steaming mug. No people."""
    s = ['<defs><linearGradient id="br_wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3A3352"/><stop offset="1" stop-color="#574868"/></linearGradient>'
         '<linearGradient id="br_win" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1C2A5C"/><stop offset="1" stop-color="#4B5F9A"/></linearGradient>'
         '<radialGradient id="br_glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFB86B" stop-opacity=".55"/><stop offset="1" stop-color="#FFB86B" stop-opacity="0"/></radialGradient></defs>'
         '<rect width="1600" height="1000" fill="url(#br_wall)"/>']
    # window with frost + bubble wrap + snow
    s.append('<rect x="780" y="110" width="400" height="440" rx="10" fill="#E9E2D6"/><rect x="800" y="130" width="360" height="400" fill="url(#br_win)"/>')
    R = random.Random(25)
    for _ in range(40):
        s.append(f'<circle cx="{R.uniform(805,1155):.0f}" cy="{R.uniform(135,525):.0f}" r="{R.uniform(2,5):.1f}" fill="#fff" opacity=".85"/>')
    for yy in range(140, 530, 26):
        for xx in range(810, 1160, 26):
            s.append(f'<circle cx="{xx + (13 if (yy//26)%2 else 0)}" cy="{yy}" r="10" fill="#fff" opacity=".16" stroke="#fff" stroke-opacity=".3"/>')
    s.append('<path d="M800 530 q60 -40 120 -10 q60 -30 120 0 q60 -30 120 -6 V530Z" fill="#fff" opacity=".35"/><rect x="976" y="130" width="10" height="400" fill="#E9E2D6"/>')
    # boiler control panel
    s.append('<g transform="translate(1260 220)" style="filter:drop-shadow(0 12px 12px rgba(0,0,0,.4))"><rect x="0" y="0" width="260" height="320" rx="24" fill="#F4F1EA"/>'
             '<rect x="26" y="28" width="208" height="100" rx="10" fill="#1E3A2C"/><text x="130" y="100" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="64" fill="#7DFFB8" style="filter:drop-shadow(0 0 8px #7DFFB8)">20℃</text>'
             + ''.join(f'<rect x="{26+(i%2)*110}" y="{150+(i//2)*72}" width="98" height="56" rx="12" fill="{c}"/><text x="{75+(i%2)*110}" y="{188+(i//2)*72}" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="30" fill="#fff">{t}</text>' for i, (t, c) in enumerate([('실내', '#F2555A'), ('온돌', '#FF9F43'), ('외출', '#2446F0'), ('온수', '#12A57A')])) +
             '</g>')
    # floor
    s.append('<path d="M0 700 H1600 V1000 H0Z" fill="#B97A4A"/>')
    for y in range(720, 1000, 46):
        s.append(f'<rect x="0" y="{y}" width="1600" height="3" fill="#9A6238" opacity=".5"/>')
    s.append('<ellipse cx="1100" cy="860" rx="560" ry="170" fill="url(#br_glow)"/>')
    # warm mat / rug
    s.append('<path d="M760 780 L1560 780 L1600 980 L700 980Z" fill="#E7D3B7"/><path d="M780 800 L1540 800 L1572 960 L740 960Z" fill="none" stroke="#C99B6A" stroke-width="6" stroke-dasharray="20 14"/>')
    # low table with mug and bill envelope
    s.append('<g style="filter:drop-shadow(0 14px 12px rgba(0,0,0,.35))"><rect x="960" y="700" width="420" height="40" rx="10" fill="#8A5530"/><rect x="990" y="740" width="22" height="90" fill="#6E4122"/><rect x="1330" y="740" width="22" height="90" fill="#6E4122"/></g>'
             '<g transform="translate(1040 620)"><rect x="0" y="0" width="70" height="80" rx="10" fill="#FFF6E8"/><path d="M70 18 q30 0 30 24 q0 24 -30 24" stroke="#FFF6E8" stroke-width="10" fill="none"/>'
             '<path d="M18 -12 q-14 -28 4 -56 M44 -12 q-14 -28 4 -56" stroke="#fff" stroke-width="6" fill="none" opacity=".6"/></g>'
             '<g transform="translate(1180 664) rotate(-6)"><rect x="0" y="0" width="150" height="36" rx="4" fill="#F7F2E6"/><path d="M0 0 l75 22 l75 -22" stroke="#D2C7B0" stroke-width="3" fill="none"/></g>')
    # thick socks on the floor
    s.append('<g transform="translate(1300 860) rotate(-10)"><path d="M0 0 h40 v60 q0 20 30 26 q20 6 16 26 h-70 q-16 0 -16 -20Z" fill="#F2555A"/><rect x="0" y="0" width="40" height="16" fill="#FFF0E0"/></g>'
             '<g transform="translate(1370 870) rotate(8)"><path d="M0 0 h40 v60 q0 20 30 26 q20 6 16 26 h-70 q-16 0 -16 -20Z" fill="#F2555A"/><rect x="0" y="0" width="40" height="16" fill="#FFF0E0"/></g>')
    return svg(''.join(s))

def ktx_platform(svg):
    """High-speed train platform in the evening: a white streamlined train nose, overhead departure board, a car-number marker on the floor, a suitcase. No people."""
    s = ['<defs><linearGradient id="kp_bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1E2550"/><stop offset="1" stop-color="#4A4A7A"/></linearGradient>'
         '<linearGradient id="kp_tr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#C9D0DE"/></linearGradient>'
         '<linearGradient id="kp_fl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8E8CA8"/><stop offset="1" stop-color="#5A5878"/></linearGradient></defs>'
         '<rect width="1600" height="1000" fill="url(#kp_bg)"/>']
    # canopy with lights
    s.append('<path d="M0 0 H1600 V90 L0 160Z" fill="#14183A"/>')
    for x in range(80, 1600, 180):
        s.append(f'<rect x="{x}" y="{150 - x*0.04:.0f}" width="110" height="10" rx="5" fill="#FFF4D0" style="filter:drop-shadow(0 0 12px #FFF4D0)"/>')
    # departure board
    s.append('<g transform="translate(860 200)" style="filter:drop-shadow(0 10px 12px rgba(0,0,0,.45))"><rect x="0" y="0" width="620" height="230" rx="12" fill="#0A0D1E"/><rect x="0" y="0" width="620" height="46" rx="12" fill="#2446F0"/>'
             '<text x="24" y="33" font-family="Noto Sans CJK KR" font-weight="900" font-size="28" fill="#fff">열차 출발 안내</text>'
             + ''.join(f'<text x="24" y="{96+i*52}" font-family="Noto Sans CJK KR" font-weight="700" font-size="32" fill="{c}">{a}</text><text x="250" y="{96+i*52}" font-family="Noto Sans CJK KR" font-weight="700" font-size="32" fill="{c}">{b}</text><text x="470" y="{96+i*52}" font-family="Noto Sans CJK KR" font-weight="700" font-size="32" fill="{c}">{d}</text>'
                       for i, (a, b, d, c) in enumerate([('KTX 101', '부산행', '18:30', '#FFD84A'), ('KTX 405', '목포행', '18:42', '#E6E9FF'), ('KTX 211', '동대구행', '18:55', '#E6E9FF')])) +
             '</g>')
    # train: long body going to the left horizon, nose on the right
    s.append('<path d="M300 480 L1180 470 Q1420 470 1560 640 L1560 700 L300 700Z" fill="url(#kp_tr)" style="filter:drop-shadow(0 18px 18px rgba(0,0,0,.4))"/>'
             '<path d="M300 610 L1500 600 L1540 640 L300 648Z" fill="#2446F0"/>'
             '<path d="M1220 492 Q1380 500 1470 590 L1290 586Z" fill="#1A2448"/>')
    for x in range(340, 1150, 120):
        s.append(f'<rect x="{x}" y="520" width="80" height="50" rx="10" fill="#2A3460"/>')
    s.append('<circle cx="1520" cy="668" r="10" fill="#FFF4C0" style="filter:drop-shadow(0 0 10px #FFF4C0)"/>')
    # platform floor with yellow safety line
    s.append('<path d="M0 700 H1600 V1000 H0Z" fill="url(#kp_fl)"/><rect y="700" width="1600" height="18" fill="#DCD9EA"/>')
    s.append('<path d="M0 740 H1600 V762 H0Z" fill="#FFD84A"/>')
    for x in range(0, 1600, 40):
        s.append(f'<circle cx="{x+20}" cy="751" r="4" fill="#C9A21A"/>')
    # car-number marker on the floor
    s.append('<g transform="translate(1100 840) skewX(-20)"><rect x="0" y="0" width="200" height="80" rx="8" fill="#2446F0"/><text x="100" y="58" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="48" fill="#fff">5호차</text></g>')
    # rolling suitcase
    s.append('<g transform="translate(1400 780)" style="filter:drop-shadow(0 12px 10px rgba(0,0,0,.4))"><rect x="20" y="-70" width="10" height="70" fill="#9AA0B8"/><rect x="70" y="-70" width="10" height="70" fill="#9AA0B8"/><rect x="14" y="-80" width="72" height="14" rx="6" fill="#9AA0B8"/>'
             '<rect x="0" y="0" width="100" height="150" rx="16" fill="#F2555A"/><rect x="24" y="20" width="8" height="110" rx="4" fill="#D53E44"/><rect x="68" y="20" width="8" height="110" rx="4" fill="#D53E44"/>'
             '<circle cx="18" cy="158" r="10" fill="#222"/><circle cx="82" cy="158" r="10" fill="#222"/></g>')
    return svg(''.join(s))

def stick_gifts(svg):
    """Shop counter for 11 November: plain red and pink stick-biscuit gift boxes (no logos), a heart bundle, a plate of white garaetteok, a calendar showing 11.11. No people."""
    R = random.Random(27)
    s = ['<defs><linearGradient id="sg_bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5A2A4A"/><stop offset="1" stop-color="#9A4A5E"/></linearGradient>'
         '<radialGradient id="sg_glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFE2B0" stop-opacity=".6"/><stop offset="1" stop-color="#FFE2B0" stop-opacity="0"/></radialGradient></defs>'
         '<rect width="1600" height="1000" fill="url(#sg_bg)"/><circle cx="1150" cy="420" r="560" fill="url(#sg_glow)"/>']
    # shelves of boxes on the right
    for row, y in enumerate([150, 330]):
        s.append(f'<rect x="700" y="{y+130}" width="900" height="16" fill="#E9C9A0"/>')
        for i in range(10):
            x = 720 + i * 86; c = ['#E8323C', '#FF7FA8', '#F2555A', '#FFB0C8', '#C9243A'][(i + row) % 5]
            h = 120 - (i % 3) * 8
            s.append(f'<rect x="{x}" y="{y+130-h}" width="70" height="{h}" rx="4" fill="{c}" style="filter:drop-shadow(0 6px 6px rgba(0,0,0,.3))"/>'
                     f'<rect x="{x+10}" y="{y+150-h}" width="50" height="10" rx="5" fill="#fff" opacity=".7"/>'
                     + ''.join(f'<rect x="{x+16+k*12}" y="{y+176-h}" width="5" height="{h-60}" rx="2" fill="#7A3A1A"/>' for k in range(4)))
    # counter
    s.append('<rect x="0" y="640" width="1600" height="360" fill="#C98E5E"/><rect x="0" y="640" width="1600" height="26" fill="#E3AE7C"/>')
    # a glass of upright chocolate-dipped sticks
    s.append('<g transform="translate(900 470)" style="filter:drop-shadow(0 14px 12px rgba(0,0,0,.35))">'
             + ''.join(f'<g transform="rotate({k*5} 60 170)"><rect x="{55}" y="-20" width="10" height="190" rx="5" fill="#F6E1B8"/><rect x="54" y="-20" width="12" height="110" rx="6" fill="{["#5A2A14","#F7EFE6","#FF8FB0"][abs(k)%3]}"/></g>' for k in range(-4, 5)) +
             '<path d="M0 90 h120 l-12 100 h-96Z" fill="#DDEBFF" opacity=".55" stroke="#fff" stroke-width="4"/><path d="M14 120 h92" stroke="#FF3D6E" stroke-width="10"/></g>')
    # gift box with heart
    s.append('<g transform="translate(1100 520)" style="filter:drop-shadow(0 14px 12px rgba(0,0,0,.35))"><rect x="0" y="40" width="200" height="140" rx="8" fill="#FF7FA8"/><rect x="-10" y="20" width="220" height="40" rx="8" fill="#FF9FC0"/>'
             '<rect x="90" y="20" width="20" height="160" fill="#E8323C"/><path d="M100 20 q-50 -50 -60 -10 q10 20 60 10 q50 10 60 -10 q-10 -40 -60 10" fill="#E8323C"/>'
             '<path d="M60 120 q-20 -30 0 -40 q10 -6 20 6 q10 -12 20 -6 q20 10 0 40 l-20 20Z" fill="#fff" opacity=".85"/></g>')
    # plate of garaetteok
    s.append('<g transform="translate(1300 700)"><ellipse cx="90" cy="60" rx="140" ry="40" fill="#F4F4F4" style="filter:drop-shadow(0 10px 8px rgba(0,0,0,.3))"/>'
             + ''.join(f'<rect x="{-10+k*36}" y="{20+(k%2)*6}" width="30" height="36" rx="10" fill="#FFFDF5" stroke="#E6E0D0" stroke-width="2"/>' for k in range(6)) +
             '<ellipse cx="200" cy="40" rx="24" ry="10" fill="#E8A92E"/></g>')
    # calendar 11.11
    s.append('<g transform="translate(1440 180) rotate(4)" style="filter:drop-shadow(0 10px 10px rgba(0,0,0,.35))"><rect x="0" y="0" width="140" height="160" rx="10" fill="#fff"/><rect x="0" y="0" width="140" height="44" rx="10" fill="#E8323C"/>'
             '<text x="70" y="32" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="26" fill="#fff">11월</text>'
             '<text x="70" y="128" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="72" fill="#3A1A2A">11</text></g>')
    for _ in range(30):
        x, y = R.uniform(500, 1600), R.uniform(40, 620)
        s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{R.uniform(2,5):.1f}" fill="#FFE9B0" opacity="{R.uniform(.3,.8):.2f}"/>')
    return svg(''.join(s))

def pharmacy_counter(svg):
    """Neighbourhood pharmacy: a glowing green 약 sign, shelves of plain boxes, a counter with medicine pouches, prescription, thermometer, tissues and tea. No people."""
    R = random.Random(28)
    s = ['<defs><linearGradient id="ph_bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E9F4EF"/><stop offset="1" stop-color="#C7DDD5"/></linearGradient></defs>'
         '<rect width="1600" height="1000" fill="url(#ph_bg)"/>']
    # window at left top showing dusk street (kept calm), sign
    # green glowing 약 sign on the right
    s.append('<g transform="translate(1340 70)"><rect x="0" y="0" width="200" height="200" rx="28" fill="#12A57A" style="filter:drop-shadow(0 0 24px #3CE0A8)"/>'
             '<text x="100" y="146" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="130" fill="#fff">약</text></g>')
    # shelves with plain boxes
    for y in (140, 300, 460):
        s.append(f'<rect x="700" y="{y+110}" width="600" height="14" fill="#9C7A58"/>')
        x = 712
        while x < 1280:
            w = R.choice([50, 60, 70]); h = R.choice([70, 84, 96]); c = R.choice(['#FFFFFF', '#FFE3E3', '#E3ECFF', '#FFF2C8', '#DDF5EE'])
            s.append(f'<rect x="{x}" y="{y+110-h}" width="{w}" height="{h}" rx="4" fill="{c}" stroke="#B9C4C0" stroke-width="2"/><rect x="{x+8}" y="{y+120-h}" width="{w-16}" height="8" rx="4" fill="{R.choice(["#F2555A","#2446F0","#12A57A","#FF9F43"])}" opacity=".7"/>')
            x += w + 10
    # counter
    s.append('<rect x="0" y="650" width="1600" height="350" fill="#F7F3EC"/><rect x="0" y="650" width="1600" height="30" fill="#12A57A"/>')
    # prescription paper
    s.append('<g transform="translate(760 700) rotate(-5)" style="filter:drop-shadow(0 8px 8px rgba(0,0,0,.2))"><rect x="0" y="0" width="200" height="250" fill="#fff"/>'
             '<text x="100" y="44" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="30" fill="#2E3B66">처방전</text>'
             + ''.join(f'<rect x="20" y="{70+k*30}" width="{R.choice([120,150,160])}" height="8" rx="4" fill="#C9D2E0"/>' for k in range(5)) + '</g>')
    # medicine pouches strip
    s.append('<g transform="translate(1000 720)">' + ''.join(f'<g transform="translate({k*84} {k*6})"><rect x="0" y="0" width="80" height="110" rx="6" fill="#fff" stroke="#CFD8E0" stroke-width="3"/>'
             f'<circle cx="26" cy="64" r="11" fill="#FFFFFF" stroke="#C0C8D0" stroke-width="2"/><ellipse cx="52" cy="70" rx="14" ry="8" fill="#FFB0B0"/><circle cx="40" cy="88" r="9" fill="#FFE07A"/><rect x="10" y="12" width="60" height="10" rx="5" fill="#12A57A" opacity=".6"/></g>' for k in range(3)) + '</g>')
    # thermometer
    s.append('<g transform="translate(1270 900) rotate(-20)"><rect x="0" y="0" width="160" height="22" rx="11" fill="#fff" stroke="#BFC9C5" stroke-width="3"/><rect x="10" y="8" width="90" height="6" rx="3" fill="#F2555A"/><circle cx="8" cy="11" r="10" fill="#F2555A"/></g>')
    # tissue box
    s.append('<g transform="translate(1340 700)" style="filter:drop-shadow(0 8px 8px rgba(0,0,0,.2))"><rect x="0" y="40" width="180" height="110" rx="10" fill="#7FB7FF"/><path d="M70 40 q20 -50 40 -40 q20 10 0 40Z" fill="#fff"/></g>')
    # tea mug
    s.append('<g transform="translate(1520 760)"><rect x="0" y="0" width="64" height="76" rx="10" fill="#FFF6E8" stroke="#E0D2BC" stroke-width="3"/><path d="M64 16 q26 0 26 22 q0 22 -26 22" stroke="#FFF6E8" stroke-width="10" fill="none"/>'
             '<path d="M20 -10 q-12 -24 4 -48 M42 -10 q-12 -24 4 -48" stroke="#9FB8AE" stroke-width="5" fill="none" opacity=".7"/></g>')
    return svg(''.join(s))
