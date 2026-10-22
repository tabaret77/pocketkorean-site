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
