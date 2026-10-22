"""Rich scene covers with cute characters (1600x1000 SVG). Original drawings."""
import random, math, cute
INK = '#4A2E2A'
DEFS = ('<filter id="sh"><feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#141838" flood-opacity=".18"/></filter>'
        '<filter id="soft"><feGaussianBlur stdDeviation="6"/></filter>')

def svg(bg_defs, inner):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000"><defs>{DEFS}{bg_defs}</defs>{inner}</svg>'

def P(fn, x, y, s=1.0, **kw):
    return f'<svg x="{x}" y="{y}" width="{300*s:.0f}" height="{420*s:.0f}" viewBox="0 0 300 420" overflow="visible">{fn(0, 0, 1, **kw)}</svg>'

def tag(x, y, text, bg='#FFFFFF', size=52, fg=INK):
    w = 56 + size * 1.02 * len(text)
    return (f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w:.0f}" height="{size*1.6:.0f}" rx="{size*.8:.0f}" fill="{bg}" stroke="{INK}" stroke-width="5"/>'
            f'<text x="{x+w/2:.0f}" y="{y+size*1.15:.0f}" text-anchor="middle" font-family="Nanum Myeongjo" font-weight="800" font-size="{size}" fill="{fg}">{text}</text></g>')

def bubble(x, y, text, size=54, tail='down-right', bg='#FFFFFF'):
    w = 80 + size * 1.0 * len(text); h = size * 1.9
    tx = {'down-right': (x + w - 90, y + h, x + w - 30, y + h + 50, x + w - 150), 'down-left': (x + 60, y + h, x + 30, y + h + 50, x + 130)}[tail]
    return (f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w:.0f}" height="{h:.0f}" rx="40" fill="{bg}" stroke="{INK}" stroke-width="5"/>'
            f'<path d="M{tx[0]:.0f} {tx[1]-3:.0f} L{tx[2]:.0f} {tx[3]:.0f} L{tx[4]:.0f} {tx[1]-3:.0f}Z" fill="{bg}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
            f'<rect x="{min(tx[0],tx[4])-2:.0f}" y="{tx[1]-8:.0f}" width="{abs(tx[0]-tx[4])+4:.0f}" height="8" fill="{bg}"/>'
            f'<text x="{x+w/2:.0f}" y="{y+h*.66:.0f}" text-anchor="middle" font-family="Nanum Myeongjo" font-weight="800" font-size="{size}" fill="{INK}">{text}</text></g>')

def sparkle(x, y, r, c='#FFD84A'):
    return f'<path d="M{x} {y-r} Q{x+r*.18} {y-r*.18} {x+r} {y} Q{x+r*.18} {y+r*.18} {x} {y+r} Q{x-r*.18} {y+r*.18} {x-r} {y} Q{x-r*.18} {y-r*.18} {x} {y-r}Z" fill="{c}" stroke="{INK}" stroke-width="3"/>'

# ---------- TOPIK vocabulary: climbing a staircase of books ----------
def topik_vocab():
    R = random.Random(3)
    d = '<linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE1C7"/><stop offset=".55" stop-color="#CFE8FF"/><stop offset="1" stop-color="#E3F7F0"/></linearGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#sk)"/>', '<circle cx="1320" cy="230" r="150" fill="#FFF3C4" opacity=".8"/>']
    for _ in range(18):
        s.append(f'<circle cx="{R.uniform(0,1600):.0f}" cy="{R.uniform(0,500):.0f}" r="{R.uniform(3,7):.0f}" fill="#FFFFFF" opacity=".8"/>')
    s.append('<path d="M0 900 Q800 850 1600 900 L1600 1000 L0 1000Z" fill="#9BD08A"/>')
    cols = [('#F2555A', '#C93E44'), ('#FF9F43', '#D97B22'), ('#FFD84A', '#D9B21E'), ('#12A57A', '#0B7F5D'), ('#2446F0', '#1632C4'), ('#7C5CFF', '#5B3FD6')]
    for i, (c, c2) in enumerate(cols):
        x = 220 + i * 190; h = 110 + i * 105; y = 905 - h
        s.append(f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="190" height="{h}" rx="10" fill="{c}" stroke="{INK}" stroke-width="5"/>'
                 f'<rect x="{x}" y="{y}" width="190" height="34" rx="10" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/><rect x="{x+12}" y="{y+40}" width="166" height="8" fill="{c2}"/>'
                 f'<text x="{x+95}" y="{y+108}" text-anchor="middle" font-family="Nanum Myeongjo" font-weight="800" font-size="56" fill="#FFFFFF">{i+1}급</text></g>')
    # flag on top
    s.append(f'<path d="M1270 270 V380" stroke="{INK}" stroke-width="6"/><path d="M1270 272 L1380 300 L1270 330Z" fill="#F2555A" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>')
    s.append(P(cute.boy, 560, 400, .95, mood='happy', vest='#12A57A', vest_sh='#0B7F5D'))
    s.append(P(cute.girl, 1170, 140, .82, mood='talk', cardigan='#FFFFFF', skirt='#7C5CFF', skirt_sh='#5B3FD6'))
    s.append(tag(150, 560, '사랑', '#FFF6D1') + tag(420, 330, '경험', '#E3F7F0') + tag(840, 150, '분석하다', '#EFEAFF'))
    s.append(sparkle(380, 520, 22) + sparkle(800, 300, 18, '#FF9C9C') + sparkle(1120, 120, 24) + sparkle(1480, 420, 20, '#7C5CFF'))
    return svg(d, ''.join(s))

# ---------- Read hangul in an hour: chalkboard lesson ----------
def hangul():
    d = '<linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF4E0"/><stop offset="1" stop-color="#F6E3C6"/></linearGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#wall)"/>', '<rect y="860" width="1600" height="140" fill="#D9B48A"/><rect y="860" width="1600" height="10" fill="#B88E62"/>']
    s.append(f'<g filter="url(#sh)"><rect x="150" y="90" width="1000" height="560" rx="18" fill="#B47A48" stroke="{INK}" stroke-width="6"/><rect x="180" y="120" width="940" height="500" rx="8" fill="#2F6B55"/></g>')
    s.append('<rect x="180" y="120" width="940" height="500" fill="#FFFFFF" opacity=".04"/>')
    chalk = 'font-family="Nanum Myeongjo" font-weight="800" fill="#F4F7EF"'
    s.append(f'<text x="290" y="420" {chalk} font-size="210">ㄱ</text><text x="500" y="400" {chalk} font-size="120">+</text><text x="610" y="420" {chalk} font-size="210">ㅏ</text><text x="810" y="400" {chalk} font-size="120">=</text>')
    s.append(f'<text x="920" y="430" font-family="Nanum Myeongjo" font-weight="800" font-size="230" fill="#FFD84A">가</text>')
    s.append(f'<path d="M300 500 q260 60 760 -6" stroke="#F4F7EF" stroke-width="5" fill="none" stroke-dasharray="14 12" opacity=".7"/><text x="640" y="580" text-anchor="middle" {chalk} font-size="46" opacity=".85">g + a = ga</text>')
    s.append('<rect x="190" y="606" width="920" height="22" rx="6" fill="#8A5A34"/><rect x="300" y="596" width="60" height="14" rx="4" fill="#FFFFFF"/><rect x="380" y="598" width="44" height="12" rx="4" fill="#FFD84A"/>')
    # toy blocks on the floor
    blocks = [(150, 760, 'ㄴ', '#F2555A'), (270, 790, 'ㄷ', '#2446F0'), (210, 670, 'ㅁ', '#12A57A'), (1440, 780, 'ㅗ', '#FF9F43'), (1330, 800, 'ㅂ', '#7C5CFF'), (1390, 690, 'ㅎ', '#1E8DE0')]
    for x, y, ch, c in blocks:
        s.append(f'<g filter="url(#sh)"><path d="M{x} {y} l60 -24 l60 24 l-60 24Z" fill="#FFFFFF" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/><path d="M{x} {y} v90 l60 24 v-90Z" fill="{c}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/><path d="M{x+60} {y+24} v90 l60 -24 v-90Z" fill="{c}" stroke="{INK}" stroke-width="4" stroke-linejoin="round" opacity=".8"/>'
                 f'<text x="{x+30}" y="{y+86}" text-anchor="middle" font-family="Nanum Myeongjo" font-weight="800" font-size="52" fill="#FFFFFF">{ch}</text></g>')
    # teacher girl with a pointer
    s.append(f'<path d="M1150 560 L1000 380" stroke="#8A5A34" stroke-width="10" stroke-linecap="round"/>')
    s.append(P(cute.girl, 1120, 450, 1.05, mood='talk', hair='#2B1E1A', hair_hi='#5A4038', cardigan='#FFD84A', cardigan_sh='#D9B21E', skirt='#2446F0', skirt_sh='#1632C4', ribbon='#F2555A'))
    s.append(sparkle(1080, 160, 22) + sparkle(1220, 300, 16, '#FF9C9C'))
    return svg(d, ''.join(s))

# ---------- -아요/-어요: puzzle pieces snapping together ----------
def ayo():
    d = '<radialGradient id="bgm" cx=".5" cy=".45" r=".75"><stop offset="0" stop-color="#F2FFF9"/><stop offset="1" stop-color="#BFEBD9"/></radialGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#bgm)"/>']
    def piece(x, y, w, h, c, text, knob='right'):
        k = f'L{x+w} {y+h*.32} C{x+w+60} {y+h*.2} {x+w+60} {y+h*.8} {x+w} {y+h*.68}' if knob == 'right' else f'L{x+w} {y+h}'
        notch = f'L{x} {y+h*.68} C{x+60} {y+h*.8} {x+60} {y+h*.2} {x} {y+h*.32}' if knob == 'notch' else ''
        path = f'M{x} {y} L{x+w} {y} {k} L{x+w} {y+h} L{x} {y+h} {notch}Z'
        return (f'<g filter="url(#sh)"><path d="{path}" fill="{c}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
                f'<text x="{x+w/2+(20 if knob=="notch" else 0)}" y="{y+h*.66}" text-anchor="middle" font-family="Nanum Myeongjo" font-weight="800" font-size="{h*.5:.0f}" fill="{INK}">{text}</text></g>')
    s.append(piece(170, 190, 300, 220, '#FFFFFF', '먹-') + piece(530, 190, 360, 220, '#FFD84A', '-어요', 'notch'))
    s.append(f'<text x="960" y="345" font-family="Nanum Myeongjo" font-weight="800" font-size="120" fill="{INK}">=</text>')
    s.append(f'<g filter="url(#sh)"><rect x="1070" y="170" width="420" height="260" rx="40" fill="#12A57A" stroke="{INK}" stroke-width="6"/><text x="1280" y="345" text-anchor="middle" font-family="Nanum Myeongjo" font-weight="800" font-size="130" fill="#FFFFFF">먹어요</text></g>')
    s.append(sparkle(1500, 150, 26) + sparkle(1060, 460, 18, '#FF9C9C'))
    # small piece examples
    s.append(tag(190, 520, '가요', '#FFF6D1', 46) + tag(390, 560, '해요', '#FFFFFF', 46) + tag(220, 640, '좋아요', '#EFEAFF', 46))
    s.append(P(cute.boy, 700, 470, 1.1, mood='happy', vest='#12A57A', vest_sh='#0B7F5D'))
    s.append(P(cute.girl, 1080, 500, 1.0, mood='talk', cardigan='#FFFFFF', skirt='#FF9F43', skirt_sh='#D97B22'))
    s.append(bubble(1130, 440, '맛있어요!', 46, 'down-left'))
    return svg(d, ''.join(s))

# ---------- 괜찮아요: four-panel comic ----------
def gwaenchana():
    d = '<linearGradient id="bgv" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F3EEFF"/><stop offset="1" stop-color="#E2D9FF"/></linearGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#bgv)"/>']
    panels = [(80, 70, '괜찮아요?', '#FFE9E8'), (830, 70, '괜찮아요', '#E4F2FD'), (80, 520, '괜찮아요!', '#E3F7F0'), (830, 520, '괜찮네요', '#FFF6D1')]
    for i, (x, y, txt, c) in enumerate(panels):
        s.append(f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="690" height="410" rx="26" fill="{c}" stroke="{INK}" stroke-width="6"/></g>')
        s.append(f'<circle cx="{x+40}" cy="{y+40}" r="22" fill="{INK}"/><text x="{x+40}" y="{y+50}" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="800" font-size="26" fill="#fff">{i+1}</text>')
    # 1 bump: girl helps boy who fell
    s.append(P(cute.boy, 120, 170, .7, mood='happy', vest='#F2555A', vest_sh='#C93E44') + P(cute.girl, 420, 150, .72, mood='talk'))
    s.append(bubble(380, 95, '괜찮아요?', 40, 'down-left'))
    # 2 offered food: no thanks
    s.append(f'<g transform="translate(900 300)"><ellipse cx="80" cy="60" rx="80" ry="22" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/><path d="M20 50 Q80 -10 140 50Z" fill="#F7C9A9" stroke="{INK}" stroke-width="5"/></g>')
    s.append(P(cute.boy, 1120, 150, .72, mood='smile', vest='#2446F0', vest_sh='#1632C4'))
    s.append(f'<g transform="translate(1300 330)"><circle r="34" fill="#FFE9DA" stroke="{INK}" stroke-width="4"/><path d="M-20 -10 h40 M-20 6 h40" stroke="{INK}" stroke-width="4" stroke-linecap="round"/></g>')
    s.append(bubble(900, 100, '괜찮아요', 40, 'down-right'))
    # 3 bandage, thumbs up
    s.append(P(cute.girl, 260, 610, .72, mood='happy', cardigan='#FFFFFF', skirt='#12A57A', skirt_sh='#0B7F5D'))
    s.append(f'<g transform="translate(480 760) rotate(-30)"><rect x="-40" y="-14" width="80" height="28" rx="14" fill="#F7C9A9" stroke="{INK}" stroke-width="4"/><rect x="-12" y="-14" width="24" height="28" fill="#FFFFFF" stroke="{INK}" stroke-width="3"/></g>')
    s.append(bubble(500, 545, '괜찮아요!', 40, 'down-left'))
    # 4 tasting: not bad
    s.append(P(cute.girl, 900, 610, .72, mood='smile', hair='#2B1E1A', hair_hi='#5A4038', cardigan='#FFD84A', cardigan_sh='#D9B21E'))
    s.append(f'<g transform="translate(1250 760)"><path d="M-60 0 h120 l-14 70 h-92Z" fill="#FFFFFF" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/><path d="M-50 10 h100" stroke="#F2555A" stroke-width="10"/><path d="M-20 -14 q10 -20 0 -40 M10 -14 q10 -20 0 -40" stroke="#C8CDE4" stroke-width="5" fill="none"/></g>')
    s.append(bubble(1140, 545, '괜찮네요', 40, 'down-left'))
    return svg(d, ''.join(s))

# ---------- Slang: chat on a phone, laughing ----------
def slang():
    R = random.Random(8)
    d = '<linearGradient id="bgs" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5B3FD6"/><stop offset="1" stop-color="#F2555A"/></linearGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#bgs)"/>']
    for _ in range(40):
        s.append(f'<circle cx="{R.uniform(0,1600):.0f}" cy="{R.uniform(0,1000):.0f}" r="{R.uniform(2,6):.0f}" fill="#FFFFFF" opacity="{R.uniform(.2,.6):.2f}"/>')
    s.append(f'<g filter="url(#sh)"><rect x="560" y="90" width="460" height="860" rx="64" fill="#141838"/><rect x="584" y="140" width="412" height="780" rx="40" fill="#F4F6FC"/><rect x="740" y="108" width="100" height="14" rx="7" fill="#2E3466"/></g>')
    msgs = [('헐 대박', 'l', '#FFFFFF'), ('ㅋㅋㅋㅋㅋ', 'r', '#FFD84A'), ('킹받네', 'l', '#FFFFFF'), ('갓생 산다', 'r', '#FFD84A'), ('국룰이지', 'l', '#FFFFFF'), ('꿀잼!!', 'r', '#FFD84A')]
    for i, (t, side, c) in enumerate(msgs):
        y = 180 + i * 118; w = 70 + 46 * len(t)
        x = 610 if side == 'l' else 970 - w
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="84" rx="30" fill="{c}" stroke="{INK}" stroke-width="4"/><text x="{x+w/2}" y="{y+56}" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="700" font-size="40" fill="{INK}">{t}</text>')
    s.append(P(cute.girl, 1080, 520, 1.15, mood='happy', hair='#2B1E1A', hair_hi='#5A4038', cardigan='#FFFFFF', skirt='#7C5CFF', skirt_sh='#5B3FD6', ribbon='#FFD84A'))
    s.append(P(cute.boy, 170, 520, 1.15, mood='talk', vest='#FF9F43', vest_sh='#D97B22'))
    for x, y, t, c in [(150, 200, '신조어', '#FFD84A'), (1150, 220, 'ㅋㅋ', '#FFFFFF'), (1240, 380, '대박', '#FF9C9C')]:
        s.append(tag(x, y, t, c, 56))
    s.append(sparkle(470, 150, 26) + sparkle(1480, 160, 22, '#FF9C9C') + sparkle(1110, 470, 18))
    return svg(d, ''.join(s))

# ---------- Café order ----------
def cafe():
    d = '<linearGradient id="bgc" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F6E6D2"/><stop offset="1" stop-color="#EAD2B6"/></linearGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#bgc)"/>']
    # menu board
    s.append(f'<g filter="url(#sh)"><rect x="980" y="50" width="560" height="300" rx="20" fill="#2E2A2A" stroke="{INK}" stroke-width="6"/></g>')
    s.append(f'<text x="1260" y="112" text-anchor="middle" font-family="Nanum Myeongjo" font-weight="800" font-size="46" fill="#FFD84A">메뉴</text>')
    for i, (n, p) in enumerate([('아메리카노', '4,500'), ('카페라떼', '5,000'), ('녹차라떼', '5,500')]):
        s.append(f'<text x="1020" y="{180+i*62}" font-family="Noto Sans CJK KR" font-weight="700" font-size="38" fill="#F4F7EF">{n}</text><text x="1500" y="{180+i*62}" text-anchor="end" font-family="Noto Sans CJK KR" font-weight="700" font-size="40" fill="#F4F7EF">{p}</text>')
    # pendant lamps
    for x in (300, 620):
        s.append(f'<path d="M{x} 0 V120" stroke="{INK}" stroke-width="4"/><path d="M{x-60} 180 Q{x} 90 {x+60} 180Z" fill="#12A57A" stroke="{INK}" stroke-width="5"/><ellipse cx="{x}" cy="190" rx="26" ry="12" fill="#FFE98A"/>')
    # barista behind the counter
    s.append(P(cute.boy, 760, 380, 1.0, mood='smile', shirt='#FFFFFF', vest='#2E2A2A', vest_sh='#141010', hair='#5A3328', hair_hi='#8C5A45'))
    s.append(f'<g filter="url(#sh)"><rect x="0" y="690" width="1600" height="80" fill="#8A5A34" stroke="{INK}" stroke-width="6"/><rect x="0" y="770" width="1600" height="230" fill="#B47A48"/></g>')
    # cups on the counter
    s.append(f'<g transform="translate(1280 560)"><path d="M0 40 h100 l-12 92 h-76Z" fill="#FFFFFF" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/><rect x="-6" y="28" width="112" height="16" rx="6" fill="{INK}"/><path d="M8 80 h84 l-6 40 h-72Z" fill="#7A4A35"/><path d="M60 28 l20 -40" stroke="#F2555A" stroke-width="8" stroke-linecap="round"/></g>')
    s.append(f'<g transform="translate(1430 600)"><path d="M0 0 h90 l-10 90 h-70Z" fill="#FFFFFF" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/><path d="M90 20 q30 10 0 40" stroke="{INK}" stroke-width="5" fill="none"/></g>')
    # customer girl with a speech bubble
    s.append(P(cute.girl, 210, 470, 1.2, mood='talk', cardigan='#E3F7F0', cardigan_sh='#A9DCC9', skirt='#2446F0', skirt_sh='#1632C4'))
    s.append(bubble(110, 260, '아이스 아메리카노 주세요', 46, 'down-right'))
    s.append(f'<g transform="translate(60 520)"><path d="M40 160 h80 l-10 120 h-60Z" fill="#B47A48" stroke="{INK}" stroke-width="5"/><circle cx="60" cy="130" r="40" fill="#5E9C72" stroke="{INK}" stroke-width="5"/><circle cx="100" cy="110" r="36" fill="#7FB28A" stroke="{INK}" stroke-width="5"/></g>')
    return svg(d, ''.join(s))

# ---------- Survival Korean: taxi and convenience store street ----------
def survival():
    R = random.Random(11)
    d = '<linearGradient id="bgt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9FD3F7"/><stop offset="1" stop-color="#E4F2FD"/></linearGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#bgt)"/>']
    s.append(f'<g filter="url(#sh)"><rect x="880" y="200" width="680" height="560" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>'
             f'<rect x="860" y="190" width="720" height="90" rx="10" fill="#12A57A" stroke="{INK}" stroke-width="6"/></g>')
    s.append(f'<text x="1220" y="255" text-anchor="middle" font-family="Nanum Myeongjo" font-weight="800" font-size="54" fill="#FFFFFF">편의점 24</text>')
    for i in range(8):
        s.append(f'<path d="M{880+i*85} 280 h85 l-10 40 h-65Z" fill="{"#FFFFFF" if i%2 else "#12A57A"}" stroke="{INK}" stroke-width="4"/>')
    s.append(f'<rect x="920" y="360" width="260" height="400" fill="#CFE6F7" stroke="{INK}" stroke-width="5"/><rect x="1220" y="360" width="300" height="250" fill="#CFE6F7" stroke="{INK}" stroke-width="5"/>')
    for i in range(3):
        s.append(f'<rect x="1240" y="{390+i*70}" width="260" height="10" fill="#B47A48"/>' + ''.join(f'<rect x="{1250+j*40}" y="{356+i*70}" width="26" height="34" rx="4" fill="{R.choice(["#F2555A","#FFD84A","#2446F0","#12A57A"])}"/>' for j in range(6)))
    s.append('<rect y="760" width="1600" height="240" fill="#B9BFCF"/><rect y="760" width="1600" height="30" fill="#E3E6EE"/>')
    for x in range(40, 1600, 220):
        s.append(f'<rect x="{x}" y="890" width="120" height="16" rx="8" fill="#FFFFFF" opacity=".8"/>')
    # taxi
    s.append(f'<g transform="translate(120 560)" filter="url(#sh)"><path d="M60 180 l60 -110 h300 l90 110 h70 a20 20 0 0 1 20 20 v80 H0 v-80 a20 20 0 0 1 20 -20Z" fill="#FF9F43" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
             f'<path d="M150 90 h120 v90 h-170Z M300 90 h110 l70 90 h-180Z" fill="#CFE6F7" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
             f'<rect x="230" y="30" width="110" height="40" rx="8" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/><text x="285" y="62" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="28" fill="{INK}">TAXI</text>'
             f'<circle cx="140" cy="280" r="48" fill="{INK}"/><circle cx="140" cy="280" r="20" fill="#C8CDE4"/><circle cx="470" cy="280" r="48" fill="{INK}"/><circle cx="470" cy="280" r="20" fill="#C8CDE4"/></g>')
    s.append(P(cute.girl, 700, 420, 1.15, mood='talk', cardigan='#FFFFFF', skirt='#F2555A', skirt_sh='#C93E44'))
    s.append(f'<g transform="translate(940 690) rotate(-14)"><rect x="-50" y="-32" width="100" height="64" rx="10" fill="#2446F0" stroke="{INK}" stroke-width="5"/><rect x="-36" y="-14" width="30" height="20" rx="4" fill="#FFD84A"/></g>')
    s.append(bubble(380, 250, '카드 돼요?', 60, 'down-right'))
    return svg(d, ''.join(s))

# ---------- K-pop comeback stage ----------
def comeback():
    R = random.Random(2)
    d = ('<linearGradient id="bgk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#140F3A"/><stop offset="1" stop-color="#3A1E6E"/></linearGradient>'
         '<linearGradient id="beam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE98A" stop-opacity=".55"/><stop offset="1" stop-color="#FFE98A" stop-opacity="0"/></linearGradient>')
    s = ['<rect width="1600" height="1000" fill="url(#bgk)"/>']
    for x, r in [(380, -14), (800, 0), (1220, 14)]:
        s.append(f'<path d="M{x-30} 0 L{x+30} 0 L{x+260} 760 L{x-260} 760Z" fill="url(#beam)" transform="rotate({r} {x} 0)"/>')
    s.append(f'<g filter="url(#sh)"><rect x="420" y="90" width="760" height="300" rx="22" fill="#0B0A24" stroke="#7C5CFF" stroke-width="8"/></g>')
    s.append(f'<text x="800" y="290" text-anchor="middle" font-family="Nanum Myeongjo" font-weight="800" font-size="190" fill="#FFFFFF" style="filter:drop-shadow(0 0 18px #FF5FA2)">컴백</text>')
    s.append(tag(1220, 140, '10월', '#FFD84A', 56))
    s.append('<path d="M0 760 H1600 V1000 H0Z" fill="#0B0A24"/><path d="M200 760 H1400 L1500 820 H100Z" fill="#2B2560"/>')
    s.append(P(cute.boy, 470, 380, 1.0, mood='happy', shirt='#FFFFFF', vest='#141838', vest_sh='#000000', hair='#E9E3F7', hair_hi='#FFFFFF'))
    s.append(P(cute.girl, 830, 380, 1.0, mood='talk', hair='#F07A96', hair_hi='#FFC2D1', cardigan='#141838', cardigan_sh='#000000', skirt='#FFFFFF', skirt_sh='#D9DDEA', ribbon='#FFD84A'))
    for x in (690, 1050):
        s.append(f'<path d="M{x} 640 l-20 -60" stroke="{INK}" stroke-width="6"/><circle cx="{x-22}" cy="574" r="14" fill="#C8CDE4" stroke="{INK}" stroke-width="4"/>')
    for i in range(22):
        x = 30 + i * 72 + R.uniform(-10, 10); y = 880 + R.uniform(-20, 30); c = R.choice(['#FF5FA2', '#FFD84A', '#5CF2B5', '#7DA8FF'])
        s.append(f'<circle cx="{x:.0f}" cy="{y+40:.0f}" r="34" fill="#1A1640"/><path d="M{x:.0f} {y+10:.0f} l{R.uniform(-14,14):.0f} -80" stroke="#C8CDE4" stroke-width="6"/><circle cx="{x:.0f}" cy="{y-70:.0f}" r="16" fill="{c}" style="filter:drop-shadow(0 0 10px {c})"/>')
    for _ in range(30):
        s.append(sparkle(int(R.uniform(40, 1560)), int(R.uniform(20, 700)), int(R.uniform(6, 12)), R.choice(['#FFD84A', '#FF9C9C', '#FFFFFF'])))
    return svg(d, ''.join(s))

# ---------- 존댓말 vs 반말: family dinner table ----------
def jondaen():
    d = '<linearGradient id="bgj" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF4E0"/><stop offset="1" stop-color="#F3DFC2"/></linearGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#bgj)"/>']
    s.append(f'<g filter="url(#sh)"><rect x="560" y="110" width="480" height="320" rx="10" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/><path d="M800 110 V430 M560 270 H1040" stroke="{INK}" stroke-width="5"/></g>')
    s.append('<rect x="580" y="130" width="200" height="120" fill="#CFE6F7"/><rect x="820" y="130" width="200" height="120" fill="#CFE6F7"/><circle cx="700" cy="190" r="34" fill="#FFF3C4"/>')
    s.append(P(cute.boy, 160, 330, 1.15, mood='happy', hair='#CFCAC6', hair_hi='#F2EEEA', vest='#A0785A', vest_sh='#7E5B42', legs='#4A4A5A', glasses=True))
    s.append(P(cute.girl, 1100, 330, 1.15, mood='talk'))
    s.append(f'<g filter="url(#sh)"><path d="M120 760 H1480 L1540 820 H60Z" fill="#B47A48" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/><rect x="60" y="820" width="1480" height="40" fill="#8A5A34" stroke="{INK}" stroke-width="6"/></g>')
    for x in (520, 760, 1000):
        s.append(f'<g transform="translate({x} 700)"><path d="M0 0 h120 q0 60 -60 64 q-60 -4 -60 -64Z" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/><path d="M8 0 q52 -40 104 0Z" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/><circle cx="40" cy="-10" r="5" fill="#E9E3D9"/><circle cx="70" cy="-14" r="5" fill="#E9E3D9"/></g>')
    s.append(f'<path d="M640 760 l60 -70 M650 760 l70 -66" stroke="#B9852E" stroke-width="6" stroke-linecap="round"/>')
    s.append(bubble(1010, 160, '진지 드셨어요?', 52, 'down-right', '#FFFFFF'))
    s.append(bubble(170, 160, '밥 먹었어?', 52, 'down-left', '#FFF6D1'))
    s.append(tag(660, 560, '존댓말 vs 반말', '#EFEAFF', 44))
    return svg(d, ''.join(s))

# ---------- 10 drama lines: watching a drama at home ----------
def drama_lines():
    R = random.Random(6)
    d = ('<linearGradient id="bgd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2A2F5C"/><stop offset="1" stop-color="#1A1E44"/></linearGradient>'
         '<radialGradient id="tvg" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="#7DA8FF" stop-opacity=".45"/><stop offset="1" stop-color="#7DA8FF" stop-opacity="0"/></radialGradient>')
    s = ['<rect width="1600" height="1000" fill="url(#bgd)"/>', '<ellipse cx="800" cy="380" rx="700" ry="380" fill="url(#tvg)"/>']
    s.append(f'<g filter="url(#sh)"><rect x="330" y="70" width="940" height="560" rx="26" fill="#0B0D24" stroke="#000" stroke-width="6"/></g>')
    s.append('<svg x="356" y="96" width="888" height="508" viewBox="0 0 888 508"><rect width="888" height="508" fill="#F6C9B8"/><rect y="0" width="888" height="300" fill="#FFE1C7"/>'
             '<circle cx="700" cy="120" r="70" fill="#FFF3C4"/><rect x="0" y="300" width="888" height="208" fill="#E9A88F"/>'
             + P(cute.girl, 150, 70, 1.05, mood='talk') + P(cute.boy, 470, 80, 1.0, mood='smile', vest='#141838', vest_sh='#000') + '</svg>')
    s.append(f'<rect x="560" y="520" width="480" height="78" rx="12" fill="#000" opacity=".6"/><text x="800" y="575" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="700" font-size="46" fill="#FFFFFF">밥 먹었어?</text>')
    s.append(f'<g filter="url(#sh)"><path d="M140 780 Q140 700 240 700 H1360 Q1460 700 1460 780 V900 H140Z" fill="#7C5CFF" stroke="{INK}" stroke-width="6"/><rect x="100" y="760" width="120" height="180" rx="40" fill="#6A4AE8" stroke="{INK}" stroke-width="6"/><rect x="1380" y="760" width="120" height="180" rx="40" fill="#6A4AE8" stroke="{INK}" stroke-width="6"/></g>')
    # two viewers from behind (heads)
    for x, hair in [(560, '#2C2220'), (880, '#5A3328')]:
        s.append(f'<circle cx="{x+80}" cy="700" r="90" fill="{hair}" stroke="{INK}" stroke-width="5"/><path d="M{x+20} 760 Q{x+80} 730 {x+140} 760 L{x+160} 820 H{x}Z" fill="{"#5B8DEF" if x==560 else "#FFF1CF"}" stroke="{INK}" stroke-width="5"/>')
    s.append(f'<g transform="translate(1180 760)"><path d="M0 0 h120 l-16 110 h-88Z" fill="#F2555A" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>' + ''.join(f'<circle cx="{R.uniform(10,110):.0f}" cy="{R.uniform(-30,0):.0f}" r="14" fill="#FFF8E0" stroke="{INK}" stroke-width="3"/>' for _ in range(8)) + '</g>')
    s.append(tag(80, 120, '드라마 대사', '#FFD84A', 50))
    return svg(d, ''.join(s))

# ---------- Residence card: at the immigration office ----------
def residence():
    d = '<linearGradient id="bgr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#EAF3FB"/><stop offset="1" stop-color="#D6E6F5"/></linearGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#bgr)"/>']
    s.append(f'<g filter="url(#sh)"><rect x="1150" y="80" width="360" height="170" rx="16" fill="#141838" stroke="{INK}" stroke-width="5"/></g>'
             f'<text x="1330" y="140" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="700" font-size="34" fill="#9FB3E8">번호</text><text x="1330" y="222" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="800" font-size="80" fill="#5CF2B5">0127</text>')
    s.append(P(cute.boy, 980, 300, 1.0, mood='smile', shirt='#FFFFFF', vest='#2446F0', vest_sh='#1632C4', hair='#2C2220'))
    s.append(f'<g filter="url(#sh)"><rect x="700" y="640" width="900" height="360" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/><rect x="700" y="640" width="900" height="40" fill="#C8CDE4" stroke="{INK}" stroke-width="6"/></g>'
             f'<rect x="900" y="740" width="500" height="110" rx="16" fill="#2446F0"/><text x="1150" y="815" text-anchor="middle" font-family="Nanum Myeongjo" font-weight="800" font-size="56" fill="#FFFFFF">출입국 민원</text>')
    # the card, big and tilted
    s.append(f'<g transform="translate(120 140) rotate(-6)" filter="url(#sh)"><rect width="640" height="400" rx="30" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>'
             f'<rect width="640" height="96" rx="30" fill="#2446F0" stroke="{INK}" stroke-width="6"/><rect y="60" width="640" height="36" fill="#2446F0"/>'
             f'<text x="40" y="66" font-family="Nanum Myeongjo" font-weight="800" font-size="48" fill="#FFFFFF">외국인등록증</text>'
             f'<rect x="40" y="130" width="180" height="230" rx="16" fill="#E8ECFF" stroke="{INK}" stroke-width="4"/>'
             f'<svg x="40" y="130" width="180" height="230" viewBox="0 0 180 230">{cute.girl(-62, 40, .97, "smile")}</svg>'
             + ''.join(f'<rect x="260" y="{150+i*56}" width="{w}" height="26" rx="13" fill="{c}"/>' for i, (w, c) in enumerate([(320, '#C8CDE4'), (260, '#C8CDE4'), (300, '#C8CDE4'), (200, '#FFD84A')])) +
             '<circle cx="560" cy="330" r="34" fill="none" stroke="#F2555A" stroke-width="5" opacity=".7"/></g>')
    s.append(P(cute.girl, 300, 560, 1.0, mood='happy', cardigan='#FFFFFF', skirt='#12A57A', skirt_sh='#0B7F5D'))
    s.append(f'<g transform="translate(600 820) rotate(-10)"><rect x="-56" y="-40" width="112" height="80" rx="10" fill="#7A2329" stroke="{INK}" stroke-width="5"/><text y="12" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="800" font-size="22" fill="#FFD84A">PASSPORT</text></g>')
    s.append(sparkle(860, 140, 24) + sparkle(120, 600, 18, '#FF9C9C'))
    return svg(d, ''.join(s))

SCENES = {'learn-topik-vocabulary-level-by-level': topik_vocab, 'read-hangul-in-an-hour': hangul, 'ayo-eoyo-polite-ending': ayo,
          'gwaenchanayo-meaning': gwaenchana, 'korean-slang-online-2026': slang, 'ordering-at-a-korean-cafe': cafe,
                    'jondaenmal-vs-banmal': jondaen, '10-lines-every-k-drama': drama_lines}
