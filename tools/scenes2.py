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
