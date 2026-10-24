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

# ======================= 2026-10-22 batch =======================
F = 'font-family="Nanum Myeongjo" font-weight="800"'

def _leaf(x, y, r, c, rot=0):
    return (f'<g transform="translate({x} {y}) rotate({rot})"><path d="M0 {-r} C{r*.9} {-r*.6} {r*.9} {r*.4} 0 {r} C{-r*.9} {r*.4} {-r*.9} {-r*.6} 0 {-r}Z" fill="{c}" stroke="{INK}" stroke-width="3"/>'
            f'<path d="M0 {-r*.8} V{r*1.3}" stroke="{INK}" stroke-width="3"/></g>')

def _ginkgo(x, y, r, rot=0, c='#FFC93C'):
    return (f'<g transform="translate({x} {y}) rotate({rot})"><path d="M0 0 L{-r} {-r*.8} Q0 {-r*1.4} {r} {-r*.8}Z" fill="{c}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
            f'<path d="M0 0 v{r*.6}" stroke="{INK}" stroke-width="3"/></g>')

def _heart(x, y, r, c='#F2555A'):
    return f'<path transform="translate({x} {y}) scale({r/20})" d="M0 6 C-14 -10 -26 4 0 22 C26 4 14 -10 0 6Z" fill="{c}" stroke="{INK}" stroke-width="{60/r:.1f}"/>'

# ---------- TOPIK II writing question 54: exam desk ----------
def topik54():
    d = '<linearGradient id="q54bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#EEF2FF"/><stop offset="1" stop-color="#DCE3FA"/></linearGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#q54bg)"/>']
    # board with outline
    s.append(f'<g filter="url(#sh)"><rect x="90" y="70" width="820" height="360" rx="18" fill="#B47A48" stroke="{INK}" stroke-width="6"/><rect x="116" y="96" width="768" height="308" rx="8" fill="#2F6B55"/></g>')
    for i, w in enumerate(['서론', '본론', '결론']):
        x = 160 + i * 250
        s.append(f'<rect x="{x}" y="170" width="190" height="120" rx="20" fill="none" stroke="#F4F7EF" stroke-width="5" stroke-dasharray="12 8"/>'
                 f'<text x="{x+95}" y="252" text-anchor="middle" {F} font-size="64" fill="#F4F7EF">{w}</text>')
        if i < 2:
            s.append(f'<path d="M{x+198} 230 h44 m-16 -14 l16 14 l-16 14" stroke="#FFD84A" stroke-width="6" fill="none" stroke-linecap="round"/>')
    s.append(f'<text x="500" y="370" text-anchor="middle" {F} font-size="44" fill="#FFD84A">54번 · 600~700자</text>')
    # clock
    s.append(f'<g filter="url(#sh)"><circle cx="1360" cy="190" r="120" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/></g>'
             f'<path d="M1360 190 L1360 70 A120 120 0 0 1 1480 190Z" fill="#FFD84A" opacity=".55"/>'
             + ''.join(f'<rect x="1356" y="80" width="8" height="18" fill="{INK}" transform="rotate({a} 1360 190)"/>' for a in range(0, 360, 30)) +
             f'<path d="M1360 190 V100 M1360 190 L1420 220" stroke="{INK}" stroke-width="8" stroke-linecap="round"/><circle cx="1360" cy="190" r="10" fill="{INK}"/>')
    s.append(tag(1250, 340, '25분', '#FFFFFF', 46))
    # girl writing, desk in front
    s.append(P(cute.girl, 960, 380, 1.1, mood='talk', cardigan='#FFFFFF', skirt='#2446F0', skirt_sh='#1632C4'))
    s.append(f'<g filter="url(#sh)"><rect x="560" y="760" width="1000" height="40" rx="10" fill="#D9A46C" stroke="{INK}" stroke-width="6"/><rect x="600" y="800" width="920" height="200" fill="#C08A55" stroke="{INK}" stroke-width="6"/></g>')
    # manuscript paper (원고지)
    grid = ''.join(f'<rect x="{640+c*36}" y="{652+r*36}" width="30" height="30" fill="none" stroke="#E46A6E" stroke-width="2"/>' for r in range(3) for c in range(12))
    s.append(f'<g transform="rotate(-4 840 700)" filter="url(#sh)"><rect x="620" y="630" width="470" height="140" rx="6" fill="#FFFDF5" stroke="{INK}" stroke-width="4"/>{grid}'
             + ''.join(f'<text x="{655+i*36}" y="676" text-anchor="middle" {F} font-size="24" fill="{INK}">{ch}</text>' for i, ch in enumerate('현대 사회에서는')) + '</g>')
    s.append(f'<g transform="translate(1130 720) rotate(-35)"><rect x="0" y="-10" width="190" height="20" fill="#FFD84A" stroke="{INK}" stroke-width="4"/><path d="M190 -10 l34 10 l-34 10Z" fill="#F7D9B5" stroke="{INK}" stroke-width="4"/><rect x="-24" y="-10" width="26" height="20" fill="#F2555A" stroke="{INK}" stroke-width="4"/></g>')
    s.append(tag(110, 520, '주장', '#FFF6D1') + tag(150, 650, '따라서', '#E3F7F0', 48))
    s.append(sparkle(960, 110, 24) + sparkle(560, 520, 18, '#FF9C9C') + sparkle(1530, 420, 20, '#7C5CFF'))
    return svg(d, ''.join(s))

# ---------- -고 싶다: daydreaming in a café ----------
def go_sipda():
    d = '<linearGradient id="gsbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF1E6"/><stop offset="1" stop-color="#FFE0CC"/></linearGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#gsbg)"/>', '<rect y="840" width="1600" height="160" fill="#D9B48A"/><rect y="840" width="1600" height="10" fill="#B88E62"/>']
    # window
    s.append(f'<g filter="url(#sh)"><rect x="1220" y="80" width="300" height="340" rx="20" fill="#CFE8FF" stroke="{INK}" stroke-width="6"/></g><path d="M1370 80 V420 M1220 250 H1520" stroke="{INK}" stroke-width="6"/><circle cx="1450" cy="150" r="34" fill="#FFF3C4"/>')
    # thought clouds
    def cloud(cx, cy, inner, label, bg):
        return (f'<g filter="url(#sh)"><ellipse cx="{cx}" cy="{cy}" rx="170" ry="130" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/></g>{inner}'
                + tag(cx - (56 + 40 * 1.02 * len(label)) / 2, cy + 150, label, bg, 40))
    plane = f'<g transform="translate(260 210) rotate(-15)"><path d="M-90 0 Q-90 -16 -60 -16 H70 Q100 -16 100 0 Q100 16 70 16 H-60 Q-90 16 -90 0Z" fill="#E8ECFF" stroke="{INK}" stroke-width="5"/><path d="M-10 -14 L-40 -80 H-10 L40 -14Z M-10 14 L-40 80 H-10 L40 14Z" fill="#2446F0" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/><path d="M-80 -14 L-96 -50 H-76 L-56 -14Z" fill="#F2555A" stroke="{INK}" stroke-width="4"/></g>'
    bowl = (f'<g transform="translate(640 210)"><path d="M-100 -10 H100 Q96 70 0 76 Q-96 70 -100 -10Z" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>'
            + ''.join(f'<rect x="{x}" y="{y}" width="56" height="20" rx="10" fill="#F2555A" stroke="{INK}" stroke-width="3" transform="rotate({r} {x} {y})"/>' for x, y, r in [(-80, -26, 10), (-20, -34, -12), (30, -24, 18), (-50, -46, -5)]) +
            '<path d="M-30 -60 q10 -20 0 -40 M10 -60 q10 -20 0 -40" stroke="#C8CDE4" stroke-width="5" fill="none"/></g>')
    bed = (f'<g transform="translate(1010 220)"><rect x="-110" y="-10" width="220" height="60" rx="14" fill="#7C5CFF" stroke="{INK}" stroke-width="5"/><rect x="-120" y="-60" width="24" height="130" rx="8" fill="#B47A48" stroke="{INK}" stroke-width="5"/>'
           f'<rect x="-92" y="-36" width="70" height="34" rx="14" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/><text x="60" y="-30" {F} font-size="44" fill="#7C5CFF">z z</text></g>')
    s.append(cloud(260, 210, plane, '가고 싶어요', '#E8ECFF') + cloud(640, 210, bowl, '먹고 싶어요', '#FFE9E8') + cloud(1010, 220, bed, '쉬고 싶어요', '#EFEAFF'))
    s.append(''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/>' for x, y, r in [(700, 480, 16), (680, 530, 11), (980, 470, 16), (1000, 520, 11)]))
    # girl and boy at café table
    s.append(P(cute.girl, 520, 520, 1.0, mood='smile', cardigan='#FFD84A', cardigan_sh='#D9B21E', skirt='#12A57A', skirt_sh='#0B7F5D'))
    s.append(P(cute.boy, 900, 520, 1.0, mood='talk', vest='#F2555A', vest_sh='#C93E44'))
    s.append(f'<g filter="url(#sh)"><ellipse cx="840" cy="880" rx="300" ry="34" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/><rect x="826" y="900" width="28" height="100" fill="#B47A48" stroke="{INK}" stroke-width="5"/></g>')
    s.append(f'<g transform="translate(720 820)"><path d="M0 0 h70 l-8 56 h-54Z" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/><rect x="0" y="10" width="70" height="14" fill="#B47A48"/></g>')
    s.append(bubble(1180, 520, '보고 싶어요', 46, 'down-left'))
    s.append(sparkle(140, 470, 22) + sparkle(1540, 600, 18, '#FF9C9C') + sparkle(820, 60, 22))
    return svg(d, ''.join(s))

# ---------- Kimjang words: making kimchi together ----------
def kimjang():
    d = '<linearGradient id="kjbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF4E0"/><stop offset="1" stop-color="#FCE3C4"/></linearGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#kjbg)"/>', '<rect y="800" width="1600" height="200" fill="#E7C795"/>']
    # hanok-ish window lattice
    s.append(f'<g filter="url(#sh)"><rect x="1180" y="70" width="340" height="300" rx="10" fill="#FFF8E8" stroke="{INK}" stroke-width="6"/></g>'
             + ''.join(f'<path d="M{1180+i*68} 70 V370" stroke="#B47A48" stroke-width="5"/>' for i in range(1, 5)) + ''.join(f'<path d="M1180 {70+i*60} H1520" stroke="#B47A48" stroke-width="5"/>' for i in range(1, 5)))
    # characters behind tub
    s.append(P(cute.girl, 380, 330, 1.05, mood='happy', cardigan='#FFFFFF', skirt='#F2555A', skirt_sh='#C93E44'))
    s.append(P(cute.boy, 820, 340, 1.05, mood='talk', vest='#12A57A', vest_sh='#0B7F5D'))
    # big red tub
    s.append(f'<g filter="url(#sh)"><path d="M300 700 H1180 L1120 960 H360Z" fill="#E8434A" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/><ellipse cx="740" cy="700" rx="440" ry="60" fill="#C93E44" stroke="{INK}" stroke-width="7"/></g>')
    # cabbage halves in tub
    for cx, rot in [(520, -10), (700, 6), (880, -4), (1020, 12)]:
        s.append(f'<g transform="translate({cx} 680) rotate({rot})"><path d="M-100 0 Q-80 -46 0 -44 Q90 -40 104 0 Q90 40 0 44 Q-80 46 -100 0Z" fill="#9FD46A" stroke="{INK}" stroke-width="5"/>'
                 f'<path d="M-60 0 Q-40 -30 20 -30 Q90 -26 96 0 Q90 26 20 30 Q-40 30 -60 0Z" fill="#FFF6C8" stroke="{INK}" stroke-width="4"/>'
                 f'<path d="M-40 -14 Q30 -24 90 -8 M-44 0 H94 M-40 14 Q30 24 90 8" stroke="#E7DFA0" stroke-width="4" fill="none"/>'
                 f'<path d="M-20 -18 q30 10 60 -4 M0 16 q30 -10 60 4" stroke="#E8434A" stroke-width="9" fill="none" stroke-linecap="round" opacity=".85"/></g>')
    # red gloves (hands) on tub rim
    s.append(f'<ellipse cx="560" cy="650" rx="38" ry="26" fill="#F2555A" stroke="{INK}" stroke-width="5"/><ellipse cx="960" cy="650" rx="38" ry="26" fill="#F2555A" stroke="{INK}" stroke-width="5"/>')
    # chilli flakes bowl + radish
    s.append(f'<g filter="url(#sh)"><path d="M1260 820 h220 q-10 110 -110 112 q-100 -2 -110 -112Z" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/><ellipse cx="1370" cy="820" rx="110" ry="22" fill="#D63A2E" stroke="{INK}" stroke-width="5"/></g>')
    s.append(f'<g transform="translate(170 880) rotate(-15)" filter="url(#sh)"><path d="M-6 -24 Q-50 -80 -30 -100 M0 -24 Q0 -90 30 -100 M6 -24 Q40 -70 70 -70" stroke="#12A57A" stroke-width="16" fill="none" stroke-linecap="round"/>'
             f'<path d="M-50 -20 Q0 -36 50 -20 Q70 40 10 90 Q0 100 -10 90 Q-70 40 -50 -20Z" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/><path d="M-46 -12 Q0 -24 46 -12 Q50 10 44 20 Q0 6 -44 20 Q-50 10 -46 -12Z" fill="#CDEBA4"/></g>')
    s.append(tag(90, 90, '김장', '#FFD84A', 70) + tag(1210, 420, '고춧가루', '#FFE9E8', 44) + tag(90, 260, '배추', '#E3F7F0', 52) + tag(1300, 580, '무', '#FFFFFF', 48))
    s.append(bubble(700, 150, '너무 짜요?', 46, 'down-right'))
    s.append(sparkle(620, 110, 22) + sparkle(1120, 520, 18, '#FF9C9C'))
    return svg(d, ''.join(s))

# ---------- Batchim: the 7 final sounds ----------
def batchim():
    d = '<linearGradient id="bcbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF4E0"/><stop offset="1" stop-color="#F6E3C6"/></linearGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#bcbg)"/>', '<rect y="860" width="1600" height="140" fill="#D9B48A"/><rect y="860" width="1600" height="10" fill="#B88E62"/>']
    s.append(f'<g filter="url(#sh)"><rect x="80" y="70" width="1080" height="560" rx="18" fill="#B47A48" stroke="{INK}" stroke-width="6"/><rect x="108" y="98" width="1024" height="504" rx="8" fill="#2F6B55"/></g>')
    chalk = f'{F} fill="#F4F7EF"'
    s.append(f'<text x="620" y="180" text-anchor="middle" {chalk} font-size="54">받침 소리 7개</text>')
    for i, ch in enumerate('ㄱㄴㄷㄹㅁㅂㅇ'):
        x = 150 + i * 135
        s.append(f'<rect x="{x}" y="220" width="115" height="130" rx="16" fill="none" stroke="#FFD84A" stroke-width="5"/><text x="{x+57}" y="315" text-anchor="middle" {chalk} font-size="84">{ch}</text>')
    s.append(f'<text x="300" y="480" text-anchor="middle" {chalk} font-size="96">꽃</text><path d="M380 450 h90 m-20 -18 l20 18 l-20 18" stroke="#FFD84A" stroke-width="6" fill="none"/><text x="590" y="480" text-anchor="middle" {F} font-size="80" fill="#FFD84A">[꼳]</text>')
    s.append(f'<text x="300" y="580" text-anchor="middle" {chalk} font-size="96">옷</text><path d="M380 550 h90 m-20 -18 l20 18 l-20 18" stroke="#FFD84A" stroke-width="6" fill="none"/><text x="590" y="580" text-anchor="middle" {F} font-size="80" fill="#FFD84A">[옫]</text>')
    # flower + shirt doodles in chalk
    s.append('<g transform="translate(860 470)" stroke="#F4F7EF" stroke-width="5" fill="none">' + ''.join(f'<circle cx="{30*math.cos(a*math.pi/2.5):.0f}" cy="{30*math.sin(a*math.pi/2.5):.0f}" r="22"/>' for a in range(5)) + '<circle r="14" fill="#FFD84A" stroke="none"/><path d="M0 50 V120"/></g>')
    s.append('<path transform="translate(980 500)" d="M0 0 l40 -20 q20 18 40 0 l40 20 l-14 34 l-20 -8 v70 h-52 v-70 l-20 8Z" stroke="#F4F7EF" stroke-width="5" fill="none" stroke-linejoin="round"/>')
    # pointer and boy
    s.append(f'<path d="M1240 560 L1100 300" stroke="#8A5A34" stroke-width="10" stroke-linecap="round"/>')
    s.append(P(cute.boy, 1190, 430, 1.05, mood='talk', vest='#7C5CFF', vest_sh='#5B3FD6', glasses=True))
    s.append(tag(130, 700, '받침', '#FFD84A', 60) + tag(420, 760, '발음', '#E3F7F0', 50))
    s.append(sparkle(1250, 130, 24) + sparkle(1520, 380, 18, '#FF9C9C') + sparkle(760, 700, 20, '#7C5CFF'))
    return svg(d, ''.join(s))

# ---------- 화이팅: cheering at the school gate before 수능 ----------
def hwaiting():
    R = random.Random(22)
    d = '<linearGradient id="hwbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#CFE8FF"/><stop offset=".7" stop-color="#FFF1DA"/><stop offset="1" stop-color="#FFE6C2"/></linearGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#hwbg)"/>', '<rect y="840" width="1600" height="160" fill="#C9B79A"/>']
    # school gate pillars + building
    s.append(f'<g filter="url(#sh)"><rect x="560" y="120" width="900" height="420" fill="#F4EBDD" stroke="{INK}" stroke-width="6"/></g>'
             + ''.join(f'<rect x="{600+i*140}" y="{170+j*130}" width="90" height="80" fill="#BFDDF5" stroke="{INK}" stroke-width="4"/>' for i in range(6) for j in range(2)) +
             f'<g filter="url(#sh)"><rect x="80" y="300" width="90" height="560" fill="#B9A894" stroke="{INK}" stroke-width="6"/><rect x="1430" y="300" width="90" height="560" fill="#B9A894" stroke="{INK}" stroke-width="6"/></g>')
    # ginkgo tree
    s.append(f'<rect x="300" y="420" width="40" height="440" fill="#8A5A34" stroke="{INK}" stroke-width="5"/>'
             + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFC93C" stroke="{INK}" stroke-width="6"/>' for x, y, r in [(240, 360, 110), (400, 360, 110), (320, 250, 130), (320, 400, 100)])
             + '<circle cx="320" cy="330" r="120" fill="#FFC93C"/><circle cx="280" cy="250" r="40" fill="#FFE07A"/>')
    for _ in range(14):
        s.append(_ginkgo(R.uniform(60, 1560), R.uniform(520, 960), R.uniform(14, 22), R.uniform(-60, 60)))
    # banner
    s.append(f'<g filter="url(#sh)"><rect x="560" y="40" width="900" height="130" rx="14" fill="#F2555A" stroke="{INK}" stroke-width="6"/><text x="1010" y="135" text-anchor="middle" {F} font-size="84" fill="#FFFFFF">수능 화이팅!</text></g>')
    s.append(P(cute.girl, 620, 470, 1.0, mood='happy', cardigan='#FFFFFF', skirt='#2446F0', skirt_sh='#1632C4', ribbon='#F2555A'))
    s.append(P(cute.boy, 960, 480, 1.0, mood='talk', vest='#FF9F43', vest_sh='#D97B22'))
    # 찹쌀떡 box + 엿
    s.append(f'<g transform="translate(1260 760)" filter="url(#sh)"><rect width="200" height="110" rx="12" fill="#FFF6D1" stroke="{INK}" stroke-width="5"/>'
             + ''.join(f'<ellipse cx="{45+i*55}" cy="55" rx="24" ry="20" fill="#FFFFFF" stroke="{INK}" stroke-width="3"/>' for i in range(3)) + '</g>')
    s.append(f'<g transform="translate(420 800) rotate(-15)" filter="url(#sh)"><rect width="140" height="40" rx="20" fill="#C98A3A" stroke="{INK}" stroke-width="5"/><rect x="20" y="8" width="100" height="10" rx="5" fill="#E8B46A"/></g>')
    s.append(bubble(1150, 330, '화이팅!', 56, 'down-left') + bubble(260, 520, '꼭 붙어라!', 46, 'down-right'))
    s.append(tag(1220, 640, '힘내세요', '#E3F7F0', 44))
    s.append(sparkle(540, 260, 22) + sparkle(1540, 230, 20, '#FF9C9C') + sparkle(880, 420, 18))
    return svg(d, ''.join(s))

# ---------- Confession lines: bus stop at night, first snow ----------
def confession():
    R = random.Random(14)
    d = '<linearGradient id="cfbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#28306B"/><stop offset="1" stop-color="#7A6AB8"/></linearGradient><radialGradient id="cflamp" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFF3C4" stop-opacity=".9"/><stop offset="1" stop-color="#FFF3C4" stop-opacity="0"/></radialGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#cfbg)"/>']
    # city silhouettes
    for i in range(10):
        x = i * 170; h = R.uniform(180, 380)
        s.append(f'<rect x="{x}" y="{840-h:.0f}" width="150" height="{h:.0f}" fill="#3A3F7E"/>' + ''.join(f'<rect x="{x+20+c*44}" y="{860-h+r*50:.0f}" width="22" height="26" fill="#FFE59A" opacity="{R.choice([.2,.7,.9])}"/>' for c in range(3) for r in range(int(h//70))))
    s.append('<rect y="840" width="1600" height="160" fill="#EDEFF8"/>')
    # streetlight with glow
    s.append(f'<circle cx="300" cy="200" r="230" fill="url(#cflamp)"/><rect x="290" y="200" width="20" height="640" fill="#2B2F55" stroke="{INK}" stroke-width="4"/><path d="M250 190 h100 l-20 30 h-60Z" fill="#FFE59A" stroke="{INK}" stroke-width="5"/>')
    # bus stop sign
    s.append(f'<rect x="1440" y="420" width="16" height="420" fill="#2B2F55"/><g filter="url(#sh)"><rect x="1380" y="330" width="136" height="110" rx="14" fill="#2446F0" stroke="{INK}" stroke-width="5"/><text x="1448" y="402" text-anchor="middle" {F} font-size="40" fill="#FFFFFF">정류장</text></g>')
    s.append(P(cute.boy, 560, 440, 1.05, mood='talk', vest='#F2555A', vest_sh='#C93E44', hair='#2C2220'))
    s.append(P(cute.girl, 920, 450, 1.0, mood='happy', cardigan='#FFFFFF', skirt='#7C5CFF', skirt_sh='#5B3FD6'))
    # gift box in boy's hand
    s.append(f'<g transform="translate(790 720) rotate(8)" filter="url(#sh)"><rect x="-40" y="-36" width="80" height="72" rx="8" fill="#FF9C9C" stroke="{INK}" stroke-width="5"/><path d="M0 -36 V36 M-40 0 H40" stroke="#FFD84A" stroke-width="10"/></g>')
    s.append(_heart(880, 420, 26) + _heart(840, 360, 18, '#FF9C9C') + _heart(1200, 440, 20))
    for _ in range(55):
        s.append(f'<circle cx="{R.uniform(0,1600):.0f}" cy="{R.uniform(0,980):.0f}" r="{R.uniform(3,8):.0f}" fill="#FFFFFF" opacity="{R.uniform(.5,.95):.2f}"/>')
    s.append(bubble(420, 250, '좋아해', 58, 'down-right') + bubble(980, 230, '우리 사귈래?', 50, 'down-left'))
    s.append(tag(1050, 860, '오늘부터 1일', '#FFE9E8', 46))
    s.append(sparkle(1300, 120, 24) + sparkle(160, 120, 18, '#FFD84A'))
    return svg(d, ''.join(s))

# ---------- Making plans: park bench under maple trees ----------
def plans():
    R = random.Random(8)
    d = '<linearGradient id="mpbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#BFE3FF"/><stop offset="1" stop-color="#FFF0D6"/></linearGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#mpbg)"/>', '<path d="M0 760 Q800 720 1600 770 L1600 1000 L0 1000Z" fill="#B9D98A"/>']
    for cx, cy, r, c in [(200, 260, 230, '#E8434A'), (1420, 240, 240, '#FF9F43'), (1100, 200, 170, '#F2555A')]:
        s.append(f'<rect x="{cx-18}" y="{cy}" width="36" height="{760-cy}" fill="#8A5A34" stroke="{INK}" stroke-width="5"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" stroke="{INK}" stroke-width="6"/>')
    for _ in range(16):
        s.append(_leaf(R.uniform(60, 1560), R.uniform(560, 980), R.uniform(14, 20), R.choice(['#E8434A', '#FF9F43', '#FFC93C']), R.uniform(-80, 80)))
    # characters then bench in front
    s.append(P(cute.girl, 520, 420, 1.0, mood='talk', cardigan='#FFD84A', cardigan_sh='#D9B21E', skirt='#2446F0', skirt_sh='#1632C4'))
    s.append(P(cute.boy, 860, 430, 1.0, mood='happy', vest='#12A57A', vest_sh='#0B7F5D'))
    s.append(f'<g filter="url(#sh)"><rect x="420" y="700" width="760" height="34" rx="10" fill="#B47A48" stroke="{INK}" stroke-width="5"/><rect x="420" y="760" width="760" height="34" rx="10" fill="#B47A48" stroke="{INK}" stroke-width="5"/>'
             f'<rect x="470" y="794" width="26" height="110" fill="#5C3A22"/><rect x="1104" y="794" width="26" height="110" fill="#5C3A22"/></g>')
    # phones
    for x, r in [(640, -10), (960, 10)]:
        s.append(f'<g transform="translate({x} 680) rotate({r})" filter="url(#sh)"><rect x="-30" y="-52" width="60" height="104" rx="12" fill="#2B2F55" stroke="{INK}" stroke-width="4"/><rect x="-22" y="-42" width="44" height="80" rx="6" fill="#E8F6FF"/><rect x="-16" y="-34" width="30" height="10" rx="5" fill="#FFD84A"/><rect x="-12" y="-16" width="26" height="10" rx="5" fill="#9BD08A"/></g>')
    # calendar
    cal = ''.join(f'<rect x="{1240+c*44}" y="{560+r*40}" width="36" height="32" rx="4" fill="#FFFFFF" stroke="#C8CDE4" stroke-width="2"/>' for r in range(3) for c in range(6))
    s.append(f'<g filter="url(#sh)"><rect x="1220" y="480" width="300" height="220" rx="14" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/><rect x="1220" y="480" width="300" height="60" rx="14" fill="#F2555A" stroke="{INK}" stroke-width="5"/>'
             f'<text x="1370" y="526" text-anchor="middle" {F} font-size="38" fill="#FFFFFF">토요일</text></g>{cal}<circle cx="1478" cy="616" r="28" fill="none" stroke="#F2555A" stroke-width="6"/>')
    s.append(bubble(330, 250, '시간 돼?', 56, 'down-right') + bubble(840, 230, '단풍 보러 갈까?', 46, 'down-left'))
    s.append(tag(1230, 760, '콜!', '#FFD84A', 60))
    s.append(sparkle(760, 120, 22) + sparkle(120, 620, 18, '#FF9C9C'))
    return svg(d, ''.join(s))

# ---------- Texting shortcuts: chat bubbles from a phone at night ----------
def texting():
    R = random.Random(5)
    d = '<linearGradient id="txbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2E3570"/><stop offset="1" stop-color="#5B4A9E"/></linearGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#txbg)"/>']
    for _ in range(30):
        s.append(f'<circle cx="{R.uniform(0,1600):.0f}" cy="{R.uniform(0,400):.0f}" r="{R.uniform(2,5):.0f}" fill="#FFFFFF" opacity=".7"/>')
    s.append('<circle cx="1420" cy="140" r="70" fill="#FFF3C4"/><circle cx="1450" cy="120" r="62" fill="#2E3570"/>')
    # lamp glow
    s.append('<defs><radialGradient id="txglow"><stop offset="0" stop-color="#FFE59A" stop-opacity=".45"/><stop offset="1" stop-color="#FFE59A" stop-opacity="0"/></radialGradient></defs><circle cx="360" cy="560" r="320" fill="url(#txglow)"/>')
    # character (standing behind bed head)
    s.append(P(cute.girl, 220, 420, 1.05, mood='happy', cardigan='#FF9C9C', cardigan_sh='#E07A7E', skirt='#7C5CFF', skirt_sh='#5B3FD6'))
    # bed
    s.append(f'<g filter="url(#sh)"><rect x="60" y="760" width="900" height="120" rx="20" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/><path d="M60 780 Q500 700 960 790 V880 H60Z" fill="#7FB8F0" stroke="{INK}" stroke-width="6"/><rect x="60" y="880" width="900" height="40" fill="#B47A48" stroke="{INK}" stroke-width="6"/></g>')
    # big phone
    s.append(f'<g filter="url(#sh)"><rect x="560" y="300" width="280" height="500" rx="40" fill="#1B1E3A" stroke="{INK}" stroke-width="7"/><rect x="580" y="340" width="240" height="420" rx="20" fill="#E8F6FF"/></g>'
             + ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="40" rx="20" fill="{c}"/>' for x, y, w, c in [(596, 370, 150, '#FFFFFF'), (660, 430, 150, '#FFD84A'), (596, 490, 120, '#FFFFFF'), (690, 550, 120, '#FFD84A')]))
    # floating chat bubbles
    s.append(bubble(900, 140, 'ㄱㅅㄱㅅ', 60, 'down-left', '#FFF6D1') + bubble(1150, 380, 'ㅊㅋㅊㅋ', 60, 'down-left', '#E3F7F0'))
    s.append(bubble(940, 600, 'ㄹㅇ', 60, 'down-left') + bubble(1260, 650, 'ㅇㅈ', 60, 'down-left', '#EFEAFF'))
    s.append(tag(80, 120, '초성', '#FFD84A', 64))
    s.append(_heart(500, 260, 22) + sparkle(1500, 420, 22) + sparkle(870, 860, 18, '#FF9C9C') + sparkle(420, 160, 20, '#FFD84A'))
    return svg(d, ''.join(s))

# ---------- Honorific verbs: family dinner with grandma ----------
def honorific():
    d = '<linearGradient id="hnbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF4E0"/><stop offset="1" stop-color="#F8DFC0"/></linearGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#hnbg)"/>', '<rect y="800" width="1600" height="200" fill="#E2B57C"/>']
    # hanji sliding doors
    s.append(f'<g filter="url(#sh)"><rect x="1150" y="70" width="380" height="460" fill="#FFFBF0" stroke="#8A5A34" stroke-width="10"/></g>'
             + ''.join(f'<path d="M{1150+i*76} 70 V530" stroke="#8A5A34" stroke-width="4"/>' for i in range(1, 5)) + ''.join(f'<path d="M1150 {70+i*92} H1530" stroke="#8A5A34" stroke-width="4"/>' for i in range(1, 5)))
    # grandma (girl with grey hair) and grandchild (boy bowing slightly)
    s.append(P(cute.girl, 300, 390, 1.0, mood='happy', hair='#C9C4C0', hair_hi='#EDEAE6', cardigan='#9B7BD8', cardigan_sh='#7A5CB8', skirt='#5A4A7A', skirt_sh='#45385E', ribbon='#F2555A'))
    s.append(f'<g transform="rotate(8 1000 800)">{P(cute.boy, 880, 400, 1.0, mood="smile", vest="#12A57A", vest_sh="#0B7F5D")}</g>')
    # 밥상 low table
    s.append(f'<g filter="url(#sh)"><rect x="220" y="740" width="1100" height="50" rx="16" fill="#B5462E" stroke="{INK}" stroke-width="6"/><rect x="260" y="790" width="40" height="120" fill="#8A3422" stroke="{INK}" stroke-width="5"/><rect x="1240" y="790" width="40" height="120" fill="#8A3422" stroke="{INK}" stroke-width="5"/></g>')
    for x, c in [(420, '#FFFFFF'), (600, '#E8F0C8'), (900, '#FFD8B0'), (1100, '#FFFFFF')]:
        s.append(f'<path d="M{x-60} 730 h120 q-6 40 -60 42 q-54 -2 -60 -42Z" fill="{c}" stroke="{INK}" stroke-width="4"/>')
    s.append(f'<ellipse cx="420" cy="722" rx="56" ry="18" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/><path d="M395 700 q8 -18 0 -36 M430 700 q8 -18 0 -36" stroke="#C8CDE4" stroke-width="5" fill="none"/>'
             f'<ellipse cx="600" cy="726" rx="50" ry="12" fill="#6BA34A"/><ellipse cx="900" cy="726" rx="50" ry="12" fill="#E8434A"/>')
    s.append(f'<path d="M1180 738 L1290 724 M1180 748 L1290 740" stroke="#C0C0C8" stroke-width="6" stroke-linecap="round"/>')
    s.append(bubble(640, 190, '진지 드셨어요?', 50, 'down-right') + bubble(110, 230, '많이 드세요', 46, 'down-right'))
    s.append(tag(1140, 600, '안녕히 주무세요', '#EFEAFF', 38))
    s.append(sparkle(1540, 600, 20) + sparkle(700, 120, 22, '#FF9C9C'))
    return svg(d, ''.join(s))

SCENES_1022 = {'topik-writing-question-54': topik54, 'go-sipda-want-to': go_sipda, 'kimjang-kimchi-making-words': kimjang,
               'batchim-seven-final-sounds': batchim, 'hwaiting-meaning': hwaiting, 'k-drama-confession-lines': confession,
               'making-plans-with-friends': plans, 'korean-texting-abbreviations': texting, 'korean-honorific-verbs': honorific}
SCENES.update(SCENES_1022)


# ================= 2026-10-23 batch =================
def _bg(id_, top, bot):
    return f'<linearGradient id="{id_}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bot}"/></linearGradient>'

def _clock(cx, cy, r):
    return (f'<g filter="url(#sh)"><circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>'
            + ''.join(f'<rect x="{cx-3}" y="{cy-r+8}" width="6" height="14" fill="{INK}" transform="rotate({a} {cx} {cy})"/>' for a in range(0, 360, 30))
            + f'<path d="M{cx} {cy} V{cy-r*.6} M{cx} {cy} L{cx+r*.45} {cy+r*.2}" stroke="{INK}" stroke-width="7" stroke-linecap="round"/></g>')

def topik_reading():
    """Exam classroom: desk with an answer booklet and OMR card, wall clock, sand timer; a worried student; tags 읽기 지문 빈칸."""
    d = _bg('trbg', '#E4F2FD', '#CFE6F7')
    s = ['<rect width="1600" height="1000" fill="url(#trbg)"/>', '<rect y="780" width="1600" height="220" fill="#C9A47A"/>']
    s.append(f'<g filter="url(#sh)"><rect x="80" y="70" width="620" height="300" rx="16" fill="#2F5A48" stroke="#8A5A34" stroke-width="14"/></g>'
             f'<text x="390" y="200" text-anchor="middle" {F} font-size="72" fill="#FFFFFF">읽기 70분</text><text x="390" y="290" text-anchor="middle" {F} font-size="48" fill="#CFE8DA">1번 ~ 50번</text>')
    s.append(_clock(1360, 170, 110))
    s.append(P(cute.girl, 620, 330, 1.1, mood='talk', cardigan='#9BC8FF', cardigan_sh='#6EA6E8'))
    s.append(f'<g filter="url(#sh)"><rect x="380" y="700" width="900" height="44" rx="12" fill="#D8A86E" stroke="{INK}" stroke-width="6"/><rect x="430" y="744" width="30" height="200" fill="#8A5A34"/><rect x="1200" y="744" width="30" height="200" fill="#8A5A34"/></g>')
    s.append(f'<g transform="translate(560 610) rotate(-6)" filter="url(#sh)"><rect x="0" y="0" width="230" height="100" rx="6" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/>'
             + ''.join(f'<rect x="20" y="{16+k*16}" width="{180-k*20}" height="7" rx="3" fill="#C8CDE4"/>' for k in range(5)) + '</g>')
    s.append(f'<g transform="translate(860 620) rotate(5)" filter="url(#sh)"><rect x="0" y="0" width="200" height="90" rx="6" fill="#FFF6D1" stroke="{INK}" stroke-width="4"/>'
             + ''.join(f'<circle cx="{24+c*30}" cy="{22+r*24}" r="8" fill="{"#141838" if (r+c)%3==0 else "none"}" stroke="#F2555A" stroke-width="2"/>' for r in range(3) for c in range(6)) + '</g>')
    s.append(f'<g transform="translate(1110 560)" filter="url(#sh)"><path d="M0 0 H90 L50 70 L90 140 H0 L40 70Z" fill="#FFF6D1" stroke="{INK}" stroke-width="5"/><path d="M14 10 H76 L45 60Z" fill="#F2A03A"/><path d="M45 100 L80 134 H10Z" fill="#F2A03A"/></g>')
    s.append(bubble(980, 330, '시간이 부족해요!', 46, 'down-left'))
    s.append(tag(1240, 480, '지문', '#FFD84A', 54) + tag(120, 560, '읽기', '#FFFFFF', 54) + tag(160, 700, '빈칸', '#E3F7F0', 54))
    s.append(sparkle(860, 70, 22) + sparkle(1530, 420, 18, '#FF9C9C'))
    return svg(d, ''.join(s))

def past_tense():
    """Monday café: one friend shows weekend photos on a phone; bubbles 주말에 뭐 했어요? / 영화를 봤어요!"""
    d = _bg('ptbg', '#FFF0D6', '#F7D9B4')
    s = ['<rect width="1600" height="1000" fill="url(#ptbg)"/>', '<rect y="790" width="1600" height="210" fill="#B47A48"/>']
    s.append(f'<g filter="url(#sh)"><rect x="1140" y="60" width="380" height="300" rx="20" fill="#BFE3FF" stroke="#8A5A34" stroke-width="12"/></g><path d="M1330 60 V360 M1140 210 H1520" stroke="#8A5A34" stroke-width="8"/>'
             + ''.join(_leaf(1180 + i * 70, 120 + (i % 2) * 140, 16, c, i * 30) for i, c in enumerate(['#E8434A', '#FF9F43', '#FFC93C', '#E8434A', '#FF9F43'])))
    s.append(f'<g filter="url(#sh)"><rect x="80" y="80" width="300" height="180" rx="14" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/></g><text x="230" y="150" text-anchor="middle" {F} font-size="44" fill="{INK}">월요일</text><text x="230" y="220" text-anchor="middle" {F} font-size="36" fill="#F2555A">MONDAY</text>')
    s.append(P(cute.girl, 340, 400, 1.0, mood='happy', cardigan='#FFD84A', cardigan_sh='#D9B21E'))
    s.append(P(cute.boy, 900, 400, 1.0, mood='talk', vest='#7C5CFF', vest_sh='#5A3FD0'))
    s.append(f'<g transform="translate(640 560) rotate(-12)" filter="url(#sh)"><rect x="0" y="0" width="120" height="200" rx="18" fill="#2B2F55" stroke="{INK}" stroke-width="5"/><rect x="10" y="16" width="100" height="160" rx="8" fill="#E8F6FF"/>'
             f'<rect x="18" y="26" width="40" height="40" rx="4" fill="#FF9F43"/><rect x="62" y="26" width="40" height="40" rx="4" fill="#E8434A"/><rect x="18" y="72" width="84" height="60" rx="4" fill="#7C5CFF"/><path d="M50 92 l20 12 l-20 12z" fill="#fff"/></g>')
    s.append(f'<g filter="url(#sh)"><rect x="300" y="740" width="1000" height="40" rx="12" fill="#8A5A34" stroke="{INK}" stroke-width="5"/></g>')
    for x in (440, 1120):
        s.append(f'<path d="M{x-40} 690 h80 l-8 50 h-64z" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/><path d="M{x+40} 700 q24 4 18 24 q-6 14 -24 10" fill="none" stroke="{INK}" stroke-width="4"/><path d="M{x-14} 676 q-8 -16 4 -30 M{x+10} 676 q-8 -16 4 -30" stroke="#C8B49A" stroke-width="4" fill="none"/>')
    s.append(bubble(110, 300, '주말에 뭐 했어요?', 46, 'down-right') + bubble(880, 270, '영화를 봤어요!', 50, 'down-left', '#FFF6D1'))
    s.append(tag(1220, 520, '했어요', '#FFFFFF', 50) + tag(1250, 650, '갔어요', '#E3F7F0', 50))
    s.append(sparkle(780, 120, 22) + sparkle(1560, 440, 18, '#FF9C9C'))
    return svg(d, ''.join(s))

def hobby():
    """Cosy living room: a knitter, a gamer and a camera; books and hiking boots; bubble 취미가 뭐예요?"""
    d = _bg('hbbg', '#EFEAFF', '#DCD2FA')
    s = ['<rect width="1600" height="1000" fill="url(#hbbg)"/>', '<rect y="800" width="1600" height="200" fill="#C89A74"/>']
    # bookshelf
    s.append(f'<g filter="url(#sh)"><rect x="1230" y="120" width="300" height="680" fill="#B47A48" stroke="{INK}" stroke-width="6"/></g>')
    for k, y in enumerate((200, 360, 520)):
        s.append(f'<rect x="1240" y="{y+120}" width="280" height="14" fill="#8A5A34"/>' + ''.join(f'<rect x="{1250+i*38}" y="{y+120-(90+(i*13)%30)}" width="32" height="{90+(i*13)%30}" fill="{["#F2555A","#2446F0","#FFD84A","#12A57A","#7C5CFF","#FF9F43","#FFFFFF"][(i+k)%7]}" stroke="{INK}" stroke-width="3"/>' for i in range(7)))
    # sofa
    s.append(f'<g filter="url(#sh)"><rect x="160" y="560" width="900" height="200" rx="40" fill="#F2777C" stroke="{INK}" stroke-width="6"/><rect x="120" y="520" width="90" height="260" rx="40" fill="#E05A60" stroke="{INK}" stroke-width="6"/><rect x="1010" y="520" width="90" height="260" rx="40" fill="#E05A60" stroke="{INK}" stroke-width="6"/></g>')
    s.append(P(cute.girl, 230, 360, 1.0, mood='happy', cardigan='#FFFFFF', cardigan_sh='#E0DCE8', skirt='#12A57A', skirt_sh='#0B7F5D'))
    s.append(P(cute.boy, 640, 370, 1.0, mood='talk', vest='#2446F0', vest_sh='#1632C4'))
    # knitting: yarn ball and needles + scarf
    s.append(f'<g filter="url(#sh)"><circle cx="300" cy="840" r="46" fill="#FFD84A" stroke="{INK}" stroke-width="5"/><path d="M262 820 q38 30 76 -6 M262 850 q38 26 76 -8" stroke="#D9B21E" stroke-width="5" fill="none"/></g>'
             f'<path d="M330 680 L420 610 M350 690 L440 630" stroke="#8A5A34" stroke-width="7" stroke-linecap="round"/><rect x="330" y="640" width="90" height="70" rx="8" fill="#12A57A" stroke="{INK}" stroke-width="4"/>')
    # game controller
    s.append(f'<g transform="translate(740 650)" filter="url(#sh)"><path d="M0 30 Q0 0 40 0 H120 Q160 0 160 30 L170 80 Q170 100 150 100 Q130 100 120 80 H40 Q30 100 10 100 Q-10 100 -10 80Z" fill="#3A3F66" stroke="{INK}" stroke-width="5"/><circle cx="125" cy="35" r="9" fill="#F2555A"/><circle cx="145" cy="55" r="9" fill="#FFD84A"/><path d="M30 45 h30 M45 30 v30" stroke="#FFFFFF" stroke-width="8"/></g>')
    # camera on the floor and hiking boots
    s.append(f'<g transform="translate(1100 860)" filter="url(#sh)"><rect x="0" y="0" width="140" height="90" rx="14" fill="#2B2F55" stroke="{INK}" stroke-width="5"/><circle cx="70" cy="45" r="28" fill="#9BD0FF" stroke="{INK}" stroke-width="5"/><rect x="16" y="-14" width="36" height="16" rx="4" fill="#2B2F55"/></g>')
    s.append(f'<g transform="translate(1300 860)"><path d="M0 0 h50 v60 h50 q20 0 20 20 v10 H0Z" fill="#8A5A34" stroke="{INK}" stroke-width="4"/><path d="M130 0 h50 v60 h50 q20 0 20 20 v10 H130Z" fill="#8A5A34" stroke="{INK}" stroke-width="4"/></g>')
    s.append(bubble(460, 150, '취미가 뭐예요?', 56, 'down-left'))
    s.append(tag(60, 380, '뜨개질', '#E3F7F0', 50) + tag(960, 400, '게임', '#FFD84A', 50) + tag(1260, 30, '독서', '#FFFFFF', 50))
    s.append(sparkle(1120, 250, 22) + sparkle(100, 160, 18, '#FF9C9C'))
    return svg(d, ''.join(s))

def consonants():
    """Classroom whiteboard showing ㄱ ㅋ ㄲ; one character blows on a fluttering tissue; tags 달 탈 딸; bubble 된소리!"""
    d = _bg('csbg', '#E3F7F0', '#CDEDE2')
    s = ['<rect width="1600" height="1000" fill="url(#csbg)"/>', '<rect y="820" width="1600" height="180" fill="#C9A47A"/>']
    s.append(f'<g filter="url(#sh)"><rect x="380" y="60" width="1100" height="420" rx="18" fill="#FFFFFF" stroke="#8A9AA8" stroke-width="14"/></g>')
    for i, (j, c) in enumerate([('ㄱ', '#2446F0'), ('ㅋ', '#F2555A'), ('ㄲ', '#12A57A')]):
        x = 520 + i * 330
        s.append(f'<text x="{x+80}" y="330" text-anchor="middle" {F} font-size="230" fill="{c}">{j}</text>')
    s.append(f'<text x="770" y="440" text-anchor="middle" {F} font-size="40" fill="#8A9AA8">예사소리 · 거센소리 · 된소리</text>'.replace('770', '930'))
    s.append(f'<rect x="1300" y="470" width="120" height="16" rx="6" fill="#8A9AA8"/><rect x="1320" y="456" width="40" height="16" rx="4" fill="#2446F0"/>')
    s.append(P(cute.boy, 140, 420, 1.05, mood='talk', vest='#F2555A', vest_sh='#C8434A'))
    # tissue fluttering in front of the mouth
    s.append(f'<g transform="translate(470 520) rotate(-25)" filter="url(#sh)"><path d="M0 0 Q30 -10 60 0 Q70 40 50 90 Q30 80 10 90 Q-6 40 0 0Z" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/></g>'
             f'<path d="M430 560 q20 -10 30 -2 M432 590 q24 -8 34 4" stroke="#7FB7FF" stroke-width="5" fill="none" stroke-linecap="round"/>')
    s.append(P(cute.girl, 1160, 470, 1.0, mood='happy', cardigan='#FFD84A', cardigan_sh='#D9B21E'))
    s.append(bubble(1020, 520, '된소리!', 54, 'down-right', '#FFF6D1'))
    # mask prop on the floor
    s.append(f'<g transform="translate(860 840)" filter="url(#sh)"><ellipse cx="80" cy="60" rx="80" ry="64" fill="#FF9F43" stroke="{INK}" stroke-width="5"/><ellipse cx="50" cy="50" rx="18" ry="12" fill="{INK}"/><ellipse cx="110" cy="50" rx="18" ry="12" fill="{INK}"/><path d="M50 90 q30 20 60 0" stroke="{INK}" stroke-width="6" fill="none"/></g>')
    s.append(tag(560, 640, '달', '#FFFFFF', 60) + tag(720, 700, '탈', '#FFE9E8', 60) + tag(1040, 820, '딸', '#E4F2FD', 60))
    s.append(sparkle(320, 120, 24) + sparkle(1540, 600, 18, '#FF9C9C'))
    return svg(d, ''.join(s))

def autumn_blues():
    """By a window in autumn: a character with a mug of tea gazing at falling leaves; bubble 나 가을 타나 봐; tags 쓸쓸하다 산책."""
    R = random.Random(41)
    d = _bg('abbg', '#F8E4CC', '#EFC9A4')
    s = ['<rect width="1600" height="1000" fill="url(#abbg)"/>', '<rect y="820" width="1600" height="180" fill="#B47A48"/>']
    s.append(f'<g filter="url(#sh)"><rect x="760" y="70" width="740" height="560" rx="20" fill="#9EC8EC" stroke="#8A5A34" stroke-width="16"/></g>')
    s.append('<rect x="776" y="420" width="708" height="194" fill="#C8B080"/>')
    for cx, cy, r, c in [(950, 330, 140, '#E8434A'), (1300, 300, 170, '#FF9F43')]:
        s.append(f'<rect x="{cx-14}" y="{cy}" width="28" height="{614-cy}" fill="#6A4A34"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" stroke="{INK}" stroke-width="5"/>')
    s.append('<path d="M1130 70 V630 M760 350 H1500" stroke="#8A5A34" stroke-width="12"/>')
    for _ in range(14):
        s.append(_leaf(R.uniform(80, 1560), R.uniform(80, 980), R.uniform(14, 22), R.choice(['#E8434A', '#FF9F43', '#FFC93C']), R.uniform(-80, 80)))
    s.append(P(cute.girl, 360, 430, 1.05, mood='smile', cardigan='#C8A07A', cardigan_sh='#A07E5A', skirt='#5A4A7A', skirt_sh='#45385E'))
    s.append(f'<g transform="translate(560 690)" filter="url(#sh)"><rect x="0" y="0" width="70" height="80" rx="10" fill="#FFF6E8" stroke="{INK}" stroke-width="4"/><path d="M70 18 q24 0 24 22 q0 22 -24 22" stroke="{INK}" stroke-width="5" fill="none"/><path d="M20 -10 q-10 -20 4 -40 M44 -10 q-10 -20 4 -40" stroke="#C8B49A" stroke-width="5" fill="none"/></g>')
    s.append(bubble(140, 240, '나 가을 타나 봐', 54, 'down-right'))
    s.append(tag(860, 700, '쓸쓸하다', '#FFFFFF', 50) + tag(1150, 820, '산책', '#FFF6D1', 50))
    s.append(sparkle(700, 120, 20) + sparkle(120, 760, 18, '#FF9C9C'))
    return svg(d, ''.join(s))

def apology():
    """Park bench at dusk: one character offers an ice cream to a friend who looks away; bubbles 미안해 / 화 풀어; tag 우리 화해하자."""
    d = _bg('apbg', '#FFD6C8', '#C8B6F0')
    s = ['<rect width="1600" height="1000" fill="url(#apbg)"/>', '<path d="M0 760 Q800 720 1600 770 L1600 1000 L0 1000Z" fill="#9BC88A"/>']
    s.append('<circle cx="1360" cy="200" r="90" fill="#FFE6A8" opacity=".9"/>')
    s.append(P(cute.boy, 420, 410, 1.05, mood='talk', vest='#2446F0', vest_sh='#1632C4'))
    s.append(f'<g transform="scale(-1 1) translate(-2100 0)">{P(cute.girl, 900, 410, 1.05, mood="smile", cardigan="#FFFFFF", cardigan_sh="#E0DCE8")}</g>')
    s.append(f'<g filter="url(#sh)"><rect x="320" y="740" width="960" height="34" rx="10" fill="#B47A48" stroke="{INK}" stroke-width="5"/><rect x="380" y="774" width="26" height="120" fill="#5C3A22"/><rect x="1190" y="774" width="26" height="120" fill="#5C3A22"/></g>')
    s.append(f'<g transform="translate(740 520) rotate(18)" filter="url(#sh)"><path d="M0 40 L30 140 L60 40Z" fill="#E8B070" stroke="{INK}" stroke-width="4"/><circle cx="30" cy="30" r="34" fill="#FFB0C8" stroke="{INK}" stroke-width="4"/></g>')
    s.append(bubble(150, 220, '미안해', 60, 'down-right') + bubble(240, 380, '화 풀어', 50, 'down-right', '#FFF6D1'))
    s.append(tag(980, 230, '우리 화해하자', '#FFFFFF', 48))
    s.append(_heart(1060, 420, 30) + _heart(1120, 360, 20, '#FF9C9C'))
    s.append(sparkle(700, 100, 22) + sparkle(1520, 600, 18))
    return svg(d, ''.join(s))

def phone_call():
    """A character on the phone at home with sound waves; delivery box at the door; bubble 여보세요?; tags 잘 안 들려요 · 들어가세요."""
    d = _bg('pcbg', '#E4F2FD', '#D0E4F6')
    s = ['<rect width="1600" height="1000" fill="url(#pcbg)"/>', '<rect y="800" width="1600" height="200" fill="#C89A74"/>']
    s.append(f'<g filter="url(#sh)"><rect x="1180" y="160" width="300" height="640" rx="10" fill="#B47A48" stroke="{INK}" stroke-width="6"/></g><circle cx="1230" cy="500" r="14" fill="#FFD84A" stroke="{INK}" stroke-width="4"/>')
    s.append(f'<g transform="translate(1260 690)" filter="url(#sh)"><rect x="0" y="0" width="190" height="120" rx="6" fill="#D8A86E" stroke="{INK}" stroke-width="5"/><rect x="80" y="0" width="30" height="120" fill="#F2E6D0"/></g>')
    s.append(P(cute.boy, 420, 380, 1.15, mood='talk', vest='#12A57A', vest_sh='#0B7F5D'))
    s.append(f'<g transform="translate(650 450) rotate(18)" filter="url(#sh)"><rect x="0" y="0" width="64" height="120" rx="14" fill="#2B2F55" stroke="{INK}" stroke-width="5"/><rect x="8" y="12" width="48" height="90" rx="6" fill="#9BD0FF"/></g>')
    for r in (60, 100, 140):
        s.append(f'<path d="M{760+r*.2} {440-r*.6} A{r} {r} 0 0 1 {760+r*.2} {440+r*.6}" stroke="#2446F0" stroke-width="8" fill="none" stroke-linecap="round" opacity=".7"/>')
    s.append(bubble(120, 170, '여보세요?', 66, 'down-right'))
    s.append(tag(900, 300, '잘 안 들려요', '#FFFFFF', 46) + tag(900, 430, '들어가세요', '#FFD84A', 46))
    s.append(sparkle(1100, 90, 22) + sparkle(80, 600, 18, '#FF9C9C'))
    return svg(d, ''.join(s))

def mbti():
    """Two friends at a café table with type cards; bubble 너 T야?; tags 공감 · 극I · 대문자 E."""
    d = _bg('mbbg', '#EFEAFF', '#FFE9E8')
    s = ['<rect width="1600" height="1000" fill="url(#mbbg)"/>', '<rect y="800" width="1600" height="200" fill="#C8A0D8"/>']
    s.append(P(cute.girl, 260, 400, 1.05, mood='talk', cardigan='#FFD84A', cardigan_sh='#D9B21E'))
    s.append(P(cute.boy, 1000, 400, 1.05, mood='smile', vest='#4A4A5A', vest_sh='#33333F', glasses=True))
    s.append(f'<g filter="url(#sh)"><rect x="300" y="760" width="1040" height="40" rx="12" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/></g>')
    for i, (lt, c) in enumerate([('E', '#F2555A'), ('N', '#7C5CFF'), ('F', '#12A57A'), ('P', '#FF9F43'), ('I', '#2446F0'), ('S', '#FFD84A'), ('T', '#1E8DE0'), ('J', '#F2555A')]):
        x = 560 + i * 62; r = (-10, 6, -4, 8, -6, 10, -8, 4)[i]
        s.append(f'<g transform="translate({x} 680) rotate({r})" filter="url(#sh)"><rect x="0" y="0" width="54" height="74" rx="8" fill="{c}" stroke="{INK}" stroke-width="4"/><text x="27" y="52" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="900" font-size="38" fill="#FFFFFF">{lt}</text></g>')
    s.append(bubble(140, 200, '너 T야?', 70, 'down-right'))
    s.append(tag(980, 210, '공감', '#FFFFFF', 54) + tag(1220, 330, '극I', '#E4F2FD', 54) + tag(700, 120, '대문자 E', '#FFF6D1', 48))
    s.append(_heart(900, 340, 26) + sparkle(1520, 120, 22) + sparkle(80, 620, 18, '#FF9C9C'))
    return svg(d, ''.join(s))

def address():
    """Campus hallway: name tags 씨 · 님 · 선배 · 언니 float around; a younger character calls out 언니! to an older one."""
    d = _bg('adbg', '#FFF4E0', '#E4F2FD')
    s = ['<rect width="1600" height="1000" fill="url(#adbg)"/>', '<rect y="790" width="1600" height="210" fill="#D8C4A8"/>']
    for x in range(60, 1600, 260):
        s.append(f'<g filter="url(#sh)"><rect x="{x}" y="120" width="180" height="300" rx="10" fill="#BFE3FF" stroke="#8A9AA8" stroke-width="8"/></g><path d="M{x+90} 120 V420" stroke="#8A9AA8" stroke-width="6"/>')
    s.append(P(cute.girl, 300, 400, 1.05, mood='talk', cardigan='#FFB0C8', cardigan_sh='#E890A8'))
    s.append(P(cute.girl, 960, 400, 1.05, mood='happy', hair='#2C2220', hair_hi='#6A544C', cardigan='#2446F0', cardigan_sh='#1632C4', skirt='#4A4A5A', skirt_sh='#33333F'))
    s.append(f'<g transform="translate(1200 640)" filter="url(#sh)"><rect x="0" y="0" width="130" height="90" rx="8" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/><rect x="0" y="0" width="130" height="26" rx="8" fill="#F2555A"/></g>')
    s.append(bubble(180, 220, '언니!', 70, 'down-right'))
    s.append(tag(760, 160, '민지 씨', '#FFFFFF', 50) + tag(1150, 260, '선생님', '#FFF6D1', 50) + tag(700, 330, '선배', '#E3F7F0', 50) + tag(1280, 470, '님', '#EFEAFF', 56))
    s.append(sparkle(660, 560, 22) + sparkle(1540, 120, 18, '#FF9C9C'))
    return svg(d, ''.join(s))

SCENES_1023 = {'topik-ii-reading-strategy': topik_reading, 'past-tense-asseoyo-eosseoyo': past_tense, 'hobby-words-in-korean': hobby,
               'plain-aspirated-tense-consonants': consonants, 'gaeul-tada-autumn-blues': autumn_blues, 'k-drama-apology-making-up-lines': apology,
               'korean-phone-call-phrases': phone_call, 'mbti-talk-korean-slang': mbti, 'korean-forms-of-address': address}
SCENES.update(SCENES_1023)


# ================= 2026-10-24 batch =================
import re as _re

def _at(x, y, s, inner):
    """Draw `inner` in a character's 300x420 box coordinates (same mapping as P())."""
    return f'<g transform="translate({x} {y}) scale({s})">{inner}</g>'

def PR(fn, x, y, s=1.0, side=1, hand='wave', **kw):
    """Like P(), but one arm is raised (side=1: viewer's right, -1: left); hand = 'wave' | 'thumb' | 'point'."""
    g = fn(0, 0, 1, **kw)
    sleeve = kw.get('cardigan', '#FFF1CF') if fn is cute.girl else kw.get('shirt', '#FFFFFF')
    X = (lambda v: v) if side == 1 else (lambda v: 300 - v)
    arm = (f'<path d="M{X(190)} 232 Q{X(238)} 222 {X(258)} 166 L{X(282)} 172 Q{X(266)} 246 {X(206)} 258Z" fill="{sleeve}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>'
           f'<circle cx="{X(272)}" cy="152" r="13" fill="{cute.SKIN}" stroke="{INK}" stroke-width="4"/>')
    if hand == 'thumb':   # fist with the thumb up, a little away from the ear
        hx = X(286)
        arm = arm.replace(f'<circle cx="{X(272)}" cy="152" r="13"', f'<rect x="{hx-16}" y="140" width="32" height="30" rx="11"')
        arm += (f'<rect x="{hx-6*side-6}" y="114" width="13" height="32" rx="6.5" fill="{cute.SKIN}" stroke="{INK}" stroke-width="4"/>'
                f'<path d="M{hx-8} 152 h16 M{hx-8} 160 h16" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    elif hand == 'wave':
        arm += f'<path d="M{X(292)} 118 q{12*side} 14 {4*side} 34 M{X(306)} 104 q{20*side} 24 {8*side} 54" stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round"/>'
    g = _re.sub(rf'<path d="M{150+44*side} 230 [^"]*"[^>]*/>', arm, g, count=1)
    g = _re.sub(rf'<circle cx="{150+66*side}" cy="312" r="12.5"[^>]*/>', '', g, count=1)
    return f'<svg x="{x}" y="{y}" width="{300*s:.0f}" height="{420*s:.0f}" viewBox="0 0 300 420" overflow="visible">{g}</svg>'

def _tw(text, size):
    return 56 + size * 1.02 * len(text)

def _cloud(cx, cy, r, c='#FFFFFF'):
    return (f'<g filter="url(#sh)"><path d="M{cx-r*1.4} {cy+r*.5} Q{cx-r*1.7} {cy-r*.2} {cx-r} {cy-r*.3} Q{cx-r*.8} {cy-r*1.1} {cx} {cy-r} Q{cx+r*.8} {cy-r*1.2} {cx+r} {cy-r*.3} '
            f'Q{cx+r*1.7} {cy-r*.2} {cx+r*1.4} {cy+r*.5}Z" fill="{c}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/></g>')

def topik_listening():
    """Exam room: a student in big headphones at a desk with an OMR card and marker; wall speaker with sound waves; tags 듣기 · 한 번 · 두 번."""
    d = _bg('tlbg', '#EAF1FF', '#D3DEF7')
    s = ['<rect width="1600" height="1000" fill="url(#tlbg)"/>', '<rect y="800" width="1600" height="200" fill="#C9A47A"/><rect y="800" width="1600" height="10" fill="#A9875E"/>']
    # wall speaker + waves
    s.append(f'<rect x="150" y="50" width="50" height="24" fill="#8A90C0" stroke="{INK}" stroke-width="4"/><g filter="url(#sh)"><rect x="90" y="70" width="170" height="220" rx="24" fill="#3A3F66" stroke="{INK}" stroke-width="6"/></g>'
             f'<circle cx="175" cy="135" r="36" fill="#22264A" stroke="#8A90C0" stroke-width="5"/><circle cx="175" cy="135" r="13" fill="#8A90C0"/>'
             f'<circle cx="175" cy="228" r="42" fill="#22264A" stroke="#8A90C0" stroke-width="5"/><circle cx="175" cy="228" r="16" fill="#8A90C0"/>')
    for r in (50, 90, 130):
        s.append(f'<path d="M{285+r*.25:.0f} {180-r*.7:.0f} A{r} {r} 0 0 1 {285+r*.25:.0f} {180+r*.7:.0f}" stroke="#2446F0" stroke-width="9" fill="none" stroke-linecap="round" opacity=".75"/>')
    s.append(tag(400, 110, '듣기', '#FFD84A', 70))
    # board + clock
    s.append(f'<g filter="url(#sh)"><rect x="920" y="60" width="600" height="270" rx="16" fill="#2F5A48" stroke="#8A5A34" stroke-width="14"/></g>'
             f'<text x="1220" y="170" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="800" font-size="64" fill="#FFFFFF">TOPIK II</text>'
             f'<text x="1220" y="265" text-anchor="middle" {F} font-size="54" fill="#CFE8DA">1번 ~ 50번</text>')
    s.append(_clock(760, 160, 72))
    # student with headphones
    s.append(P(cute.boy, 575, 290, 1.2, mood='smile', vest='#7C5CFF', vest_sh='#5B3FD6'))
    band = 'M40 160 C30 -30 270 -30 260 160'
    s.append(_at(575, 290, 1.2, f'<path d="{band}" stroke="{INK}" stroke-width="28" fill="none" stroke-linecap="round"/><path d="{band}" stroke="#F2555A" stroke-width="16" fill="none" stroke-linecap="round"/>'
             + ''.join(f'<rect x="{x}" y="106" width="56" height="100" rx="26" fill="#F2555A" stroke="{INK}" stroke-width="5"/><rect x="{x+10}" y="120" width="36" height="72" rx="16" fill="#C93E44"/>' for x in (12, 232))))
    s.append(''.join(f'<text x="{x}" y="{y}" {F} font-size="{fs}" fill="#2446F0" opacity=".8">♪</text>' for x, y, fs in [(420, 330, 60), (500, 280, 46)]))
    # desk + papers
    s.append(f'<g filter="url(#sh)"><rect x="360" y="700" width="980" height="44" rx="12" fill="#D8A86E" stroke="{INK}" stroke-width="6"/><rect x="380" y="744" width="940" height="170" fill="#C08A55" stroke="{INK}" stroke-width="6"/><rect x="420" y="780" width="860" height="10" rx="5" fill="#A87444"/></g>')
    s.append(f'<g transform="translate(420 620) rotate(-6)" filter="url(#sh)"><rect width="190" height="96" rx="8" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/><rect x="14" y="14" width="54" height="68" rx="4" fill="#E8ECFF" stroke="{INK}" stroke-width="3"/>'
             + ''.join(f'<rect x="82" y="{20+k*20}" width="{90-k*14}" height="8" rx="4" fill="#C8CDE4"/>' for k in range(3)) + '</g>')
    s.append(f'<g transform="translate(880 600) rotate(4)" filter="url(#sh)"><rect width="260" height="110" rx="6" fill="#FFF6D1" stroke="{INK}" stroke-width="4"/><rect width="260" height="22" rx="6" fill="#F2555A"/>'
             + ''.join(f'<circle cx="{26+c*30}" cy="{42+r*22}" r="8" fill="{"#141838" if (r*3+c)%4==1 else "none"}" stroke="#F2555A" stroke-width="2"/>' for r in range(3) for c in range(8)) + '</g>')
    s.append(f'<g transform="translate(1170 690) rotate(-28)" filter="url(#sh)"><rect x="0" y="-11" width="170" height="22" rx="8" fill="#141838" stroke="{INK}" stroke-width="4"/><rect x="30" y="-11" width="40" height="22" fill="#FFFFFF" stroke="{INK}" stroke-width="3"/><path d="M170 -8 l24 8 l-24 8Z" fill="#141838" stroke="{INK}" stroke-width="3"/></g>')
    # plant
    s.append(f'<g filter="url(#sh)"><path d="M1400 700 h120 l-14 100 h-92Z" fill="#E8B070" stroke="{INK}" stroke-width="5"/></g>'
             + _leaf(1430, 640, 46, '#12A57A', -25) + _leaf(1490, 630, 50, '#3CBF8C', 20) + _leaf(1460, 590, 44, '#0B7F5D', 0))
    s.append(tag(110, 430, '한 번', '#FFFFFF', 56) + tag(150, 570, '두 번', '#E3F7F0', 56))
    s.append(sparkle(1010, 450, 22) + sparkle(1540, 420, 18, '#FF9C9C') + sparkle(60, 360, 18, '#7C5CFF'))
    return svg(d, ''.join(s))

def future_plans():
    """Cosy bedroom: a girl points at the wall calendar with the weekend circled and holds a cinema ticket; backpack; bubbles 주말에 뭐 할 거예요? / 갈 거예요!; tags 주말 · 영화."""
    d = _bg('fpbg', '#FFEFE6', '#FFDCCF')
    s = ['<rect width="1600" height="1000" fill="url(#fpbg)"/>', '<rect y="820" width="1600" height="180" fill="#D9B48A"/><rect y="820" width="1600" height="10" fill="#B88E62"/>']
    # window with curtains
    s.append(f'<g filter="url(#sh)"><rect x="50" y="60" width="180" height="220" rx="14" fill="#BFE3FF" stroke="#8A5A34" stroke-width="10"/></g><path d="M140 60 V280 M50 170 H230" stroke="#8A5A34" stroke-width="7"/>'
             f'<circle cx="190" cy="110" r="22" fill="#FFF3C4"/><path d="M40 50 Q70 170 40 300 L20 300 L20 50Z M240 50 Q210 170 240 300 L260 300 L260 50Z" fill="#FF9C9C" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>')
    # wall calendar, Monday first, October 2026
    s.append(f'<g filter="url(#sh)"><rect x="1120" y="60" width="380" height="380" rx="16" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/><rect x="1120" y="60" width="380" height="74" rx="16" fill="#F2555A" stroke="{INK}" stroke-width="6"/></g>'
             f'<rect x="1123" y="110" width="374" height="22" fill="#F2555A"/><text x="1310" y="116" text-anchor="middle" {F} font-size="48" fill="#FFFFFF">10월</text>'
             f'<circle cx="1200" cy="58" r="9" fill="{INK}"/><circle cx="1420" cy="58" r="9" fill="{INK}"/>')
    for c, w in enumerate('월화수목금토일'):
        s.append(f'<text x="{1162+c*50}" y="172" text-anchor="middle" {F} font-size="24" fill="{"#F2555A" if c>4 else "#8A90A8"}">{w}</text>')
    for n in range(1, 32):
        k = n + 2; r, c = divmod(k, 7)
        s.append(f'<text x="{1162+c*50}" y="{214+r*48}" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="700" font-size="24" fill="{"#F2555A" if c>4 else INK}">{n}</text>')
    s.append('<ellipse cx="1437" cy="350" rx="50" ry="28" fill="none" stroke="#F2555A" stroke-width="6" transform="rotate(-6 1437 350)"/>')
    # bed
    s.append(f'<g filter="url(#sh)"><rect x="1150" y="620" width="40" height="230" rx="10" fill="#B47A48" stroke="{INK}" stroke-width="5"/><rect x="1170" y="700" width="430" height="130" rx="18" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>'
             f'<path d="M1300 700 H1600 V830 H1290 Q1270 760 1300 700Z" fill="#7C5CFF" stroke="{INK}" stroke-width="6"/><rect x="1196" y="660" width="110" height="56" rx="24" fill="#FFF6D1" stroke="{INK}" stroke-width="5"/></g>')
    # backpack
    s.append(f'<g filter="url(#sh)"><path d="M590 720 Q590 660 650 660 Q710 660 710 720 V840 H590Z" fill="#12A57A" stroke="{INK}" stroke-width="5"/><path d="M620 668 Q650 620 680 668" stroke="{INK}" stroke-width="6" fill="none"/>'
             f'<rect x="608" y="760" width="84" height="60" rx="14" fill="#3CBF8C" stroke="{INK}" stroke-width="4"/><path d="M608 780 H692" stroke="{INK}" stroke-width="3"/></g>')
    s.append(P(cute.boy, 230, 410, 1.05, mood='talk', vest='#FF9F43', vest_sh='#D97B22'))
    s.append(PR(cute.girl, 760, 410, 1.05, side=1, hand='point', mood='happy', cardigan='#FFFFFF', cardigan_sh='#E0DCE8', skirt='#2446F0', skirt_sh='#1632C4'))
    s.append(f'<path d="M1085 520 Q1180 500 1250 455" stroke="#F2555A" stroke-width="6" fill="none" stroke-dasharray="14 10" stroke-linecap="round"/><path d="M1228 448 l24 6 l-10 22" stroke="#F2555A" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    # cinema ticket in the other hand
    s.append(f'<g transform="translate(790 690) rotate(-14)" filter="url(#sh)"><path d="M0 0 H150 V24 a12 12 0 0 0 0 24 V74 H0 V48 a12 12 0 0 0 0 -24Z" fill="#FFD84A" stroke="{INK}" stroke-width="4"/>'
             f'<path d="M110 6 V68" stroke="{INK}" stroke-width="3" stroke-dasharray="6 6"/><rect x="22" y="24" width="70" height="10" rx="5" fill="#F2555A"/><rect x="22" y="42" width="50" height="10" rx="5" fill="#F2A03A"/></g>')
    s.append(bubble(240, 250, '주말에 뭐 할 거예요?', 46, 'down-left') + bubble(640, 110, '갈 거예요!', 50, 'down-right', '#FFF6D1'))
    s.append(tag(1300, 470, '주말', '#FFE9E8', 50) + tag(560, 560, '영화', '#FFD84A', 50))
    s.append(sparkle(560, 60, 20) + sparkle(1060, 380, 18, '#FF9C9C') + sparkle(80, 600, 20, '#7C5CFF'))
    return svg(d, ''.join(s))

def family():
    """Living room: grandma, mum and a little sibling on the sofa; family-tree frame on the wall, photo frame; tags 가족 · 할머니 · 동생."""
    d = _bg('fmbg', '#FFF4E0', '#F7E2C4')
    s = ['<rect width="1600" height="1000" fill="url(#fmbg)"/>', '<rect y="800" width="1600" height="200" fill="#D9B48A"/><rect y="800" width="1600" height="10" fill="#B88E62"/>',
         '<ellipse cx="700" cy="900" rx="560" ry="60" fill="#F2A0A0" opacity=".55"/>']
    # family-tree frame
    s.append(f'<g filter="url(#sh)"><rect x="1080" y="50" width="430" height="360" rx="12" fill="#B47A48" stroke="{INK}" stroke-width="6"/><rect x="1104" y="74" width="382" height="312" rx="6" fill="#FFFBF0"/></g>'
             f'<path d="M1295 384 V300" stroke="#8A5A34" stroke-width="24"/><circle cx="1295" cy="205" r="118" fill="#CDEBB8"/>'
             f'<path d="M1295 130 V180 M1215 180 H1375 M1215 180 V230 M1375 180 V230 M1375 230 V270 M1325 270 H1425 M1325 270 V300 M1425 270 V300" stroke="{INK}" stroke-width="4" fill="none"/>')
    for x, y, c in [(1295, 120, '#C9C4C0'), (1215, 236, '#7A4A30'), (1375, 236, '#2C2220'), (1325, 310, '#5A3328'), (1425, 310, '#2C2220')]:
        s.append(f'<circle cx="{x}" cy="{y}" r="28" fill="#FFE9DA" stroke="{INK}" stroke-width="4"/><path d="M{x-28} {y-4} Q{x} {y-44} {x+28} {y-4} Q{x} {y-20} {x-28} {y-4}Z" fill="{c}" stroke="{INK}" stroke-width="3"/>'
                 f'<circle cx="{x-9}" cy="{y+4}" r="3" fill="{INK}"/><circle cx="{x+9}" cy="{y+4}" r="3" fill="{INK}"/><path d="M{x-6} {y+14} q6 6 12 0" stroke="{INK}" stroke-width="3" fill="none"/>')
    # window + lamp
    s.append(f'<g filter="url(#sh)"><rect x="300" y="60" width="240" height="200" rx="14" fill="#BFE3FF" stroke="#8A5A34" stroke-width="10"/></g><path d="M420 60 V260 M300 160 H540" stroke="#8A5A34" stroke-width="7"/>')
    # sofa
    s.append(f'<g filter="url(#sh)"><rect x="140" y="520" width="1060" height="220" rx="50" fill="#5B8DEF" stroke="{INK}" stroke-width="6"/><rect x="100" y="560" width="100" height="240" rx="44" fill="#3D6CCB" stroke="{INK}" stroke-width="6"/><rect x="1140" y="560" width="100" height="240" rx="44" fill="#3D6CCB" stroke="{INK}" stroke-width="6"/></g>'
             f'<rect x="200" y="740" width="940" height="60" rx="16" fill="#4A7BE0" stroke="{INK}" stroke-width="6"/>')
    # grandma (grey hair, glasses), mum, little sibling
    s.append(P(cute.girl, 200, 446, 1.0, mood='happy', hair='#C9C4C0', hair_hi='#EDEAE6', cardigan='#9B7BD8', cardigan_sh='#7A5CB8', skirt='#5A4A7A', skirt_sh='#45385E', ribbon='#F2555A'))
    s.append(_at(200, 446, 1.0, f'<g fill="none" stroke="{INK}" stroke-width="4"><circle cx="110" cy="150" r="26" fill="#FFFFFF" fill-opacity=".2"/><circle cx="190" cy="150" r="26" fill="#FFFFFF" fill-opacity=".2"/><path d="M136 146 q14 -8 28 0"/></g>'))
    s.append(P(cute.girl, 560, 432, 1.04, mood='talk', hair='#7A4A30', hair_hi='#B07A58', cardigan='#F2777C', cardigan_sh='#D45A60', skirt='#2E3A5C', skirt_sh='#1E2840', ribbon='#FFD84A'))
    s.append(P(cute.boy, 920, 548, 0.76, mood='happy', vest='#FFD84A', vest_sh='#D9B21E'))
    # side table + photo frame
    s.append(f'<g filter="url(#sh)"><rect x="1290" y="690" width="230" height="26" rx="8" fill="#B47A48" stroke="{INK}" stroke-width="5"/><rect x="1310" y="716" width="22" height="100" fill="#8A5A34"/><rect x="1478" y="716" width="22" height="100" fill="#8A5A34"/></g>'
             f'<g transform="translate(1330 520) rotate(-4)" filter="url(#sh)"><rect width="150" height="170" rx="10" fill="#F2A03A" stroke="{INK}" stroke-width="5"/><rect x="14" y="14" width="122" height="142" rx="4" fill="#E4F2FD"/>'
             f'<path d="M14 156 V120 Q75 96 136 120 V156Z" fill="#9BD08A"/><circle cx="50" cy="96" r="16" fill="#FFE9DA" stroke="{INK}" stroke-width="3"/><circle cx="96" cy="90" r="18" fill="#FFE9DA" stroke="{INK}" stroke-width="3"/>'
             f'<path d="M34 92 q16 -26 32 0 M78 84 q18 -28 36 0" fill="#5A3328" stroke="{INK}" stroke-width="2"/></g>')
    s.append(tag(600, 120, '가족', '#FFD84A', 72) + tag(50, 330, '할머니', '#EFEAFF', 50) + tag(1110, 440, '동생', '#E3F7F0', 50))
    s.append(_heart(840, 160, 26) + _heart(890, 110, 18, '#FF9C9C') + sparkle(1560, 470, 18) + sparkle(290, 300, 18, '#FF9C9C'))
    return svg(d, ''.join(s))

def compound_vowels():
    """Classroom blackboard ㅗ+ㅏ=ㅘ and ㅐ / ㅔ; a cartoon dog (개) and crab (게) side by side; a confused student; tags 개 · 게 · 모음."""
    d = _bg('cvbg', '#E3F7F0', '#CDEDE2')
    s = ['<rect width="1600" height="1000" fill="url(#cvbg)"/>', '<rect y="840" width="1600" height="160" fill="#C9A47A"/><rect y="840" width="1600" height="10" fill="#A9875E"/>']
    s.append(f'<g filter="url(#sh)"><rect x="70" y="50" width="1080" height="460" rx="18" fill="#B47A48" stroke="{INK}" stroke-width="6"/><rect x="96" y="76" width="1028" height="408" rx="8" fill="#2F6B55"/></g>')
    chalk = f'{F} fill="#F4F7EF"'
    s.append(f'<text x="210" y="250" text-anchor="middle" {chalk} font-size="150">ㅗ</text><text x="365" y="235" text-anchor="middle" {chalk} font-size="100">+</text>'
             f'<text x="520" y="250" text-anchor="middle" {chalk} font-size="150">ㅏ</text><text x="675" y="235" text-anchor="middle" {chalk} font-size="100">=</text>'
             f'<text x="850" y="255" text-anchor="middle" {F} font-size="170" fill="#FFD84A">ㅘ</text>')
    s.append(f'<path d="M130 300 H1080" stroke="#F4F7EF" stroke-width="4" stroke-dasharray="14 12" opacity=".5"/>')
    s.append(f'<text x="230" y="450" text-anchor="middle" {F} font-size="130" fill="#FF9C9C">ㅐ</text><text x="380" y="440" text-anchor="middle" {chalk} font-size="100">/</text>'
             f'<text x="530" y="450" text-anchor="middle" {F} font-size="130" fill="#9FD3F7">ㅔ</text>'
             f'<text x="860" y="420" text-anchor="middle" {chalk} font-size="54">비슷한 소리</text><text x="860" y="465" text-anchor="middle" {chalk} font-size="32" opacity=".75">ae ≈ e</text>')
    s.append('<rect x="90" y="500" width="1040" height="20" rx="6" fill="#8A5A34"/><rect x="200" y="490" width="60" height="14" rx="4" fill="#FFFFFF"/><rect x="280" y="492" width="44" height="12" rx="4" fill="#FFD84A"/>')
    # dog
    s.append(f'<g transform="translate(360 776)" filter="url(#sh)"><path d="M100 -20 Q150 -60 140 -100" stroke="{INK}" stroke-width="14" fill="none" stroke-linecap="round"/><path d="M100 -20 Q150 -60 140 -100" stroke="#E8B070" stroke-width="7" fill="none" stroke-linecap="round"/>'
             + ''.join(f'<rect x="{x}" y="40" width="32" height="70" rx="14" fill="#E8B070" stroke="{INK}" stroke-width="5"/>' for x in (-70, -20, 40, 90)) +
             f'<ellipse cx="20" cy="10" rx="120" ry="70" fill="#E8B070" stroke="{INK}" stroke-width="5"/>'
             + f'<ellipse cx="60" cy="0" rx="34" ry="26" fill="#FFF1DA"/><circle cx="-90" cy="-60" r="68" fill="#E8B070" stroke="{INK}" stroke-width="5"/>'
             f'<path d="M-150 -100 Q-190 -40 -160 0 Q-140 -30 -130 -80Z M-30 -100 Q10 -40 -20 0 Q-40 -30 -50 -80Z" fill="#8A5A34" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
             f'<circle cx="-112" cy="-66" r="9" fill="{INK}"/><circle cx="-68" cy="-66" r="9" fill="{INK}"/><circle cx="-115" cy="-69" r="3" fill="#fff"/><circle cx="-71" cy="-69" r="3" fill="#fff"/>'
             f'<ellipse cx="-90" cy="-40" rx="13" ry="9" fill="{INK}"/><path d="M-90 -32 v10 M-104 -20 q14 12 28 0" stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M-96 -18 q6 16 12 0Z" fill="#F2555A"/>'
             f'<path d="M-150 -10 q60 20 120 0" stroke="#F2555A" stroke-width="10" fill="none" stroke-linecap="round"/><circle cx="-90" cy="2" r="9" fill="#FFD84A" stroke="{INK}" stroke-width="3"/></g>')
    # crab
    s.append(f'<g transform="translate(860 790)" filter="url(#sh)">'
             + ''.join(f'<path d="M{sx*60} 20 l{sx*60} 40 l{sx*14} 30 M{sx*40} 34 l{sx*50} 46 l{sx*6} 26" stroke="{INK}" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M{sx*60} 20 l{sx*60} 40 l{sx*14} 30 M{sx*40} 34 l{sx*50} 46 l{sx*6} 26" stroke="#F2555A" stroke-width="4" fill="none" stroke-linecap="round"/>' for sx in (-1, 1)) +
             ''.join(f'<path d="M{sx*80} -10 Q{sx*130} -40 {sx*130} -90" stroke="{INK}" stroke-width="16" fill="none" stroke-linecap="round"/><path d="M{sx*80} -10 Q{sx*130} -40 {sx*130} -90" stroke="#F2555A" stroke-width="8" fill="none" stroke-linecap="round"/>'
                     f'<path d="M{sx*130} -90 m{-sx*32} 0 a32 36 0 1 1 {sx*64} 0 l{-sx*24} -6 l{-sx*10} 26 Z" fill="#F2555A" stroke="{INK}" stroke-width="5" stroke-linejoin="round" transform="rotate({sx*-10} {sx*130} -90)"/>' for sx in (-1, 1)) +
             f'<ellipse cx="0" cy="0" rx="110" ry="66" fill="#F2555A" stroke="{INK}" stroke-width="5"/><ellipse cx="-30" cy="-26" rx="30" ry="12" fill="#FF9C9C" opacity=".8"/>'
             f'<path d="M-30 -60 V-90 M30 -60 V-90" stroke="{INK}" stroke-width="6"/><circle cx="-30" cy="-98" r="16" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/><circle cx="30" cy="-98" r="16" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/>'
             f'<circle cx="-27" cy="-96" r="7" fill="{INK}"/><circle cx="33" cy="-96" r="7" fill="{INK}"/><path d="M-20 14 q20 16 40 0" stroke="{INK}" stroke-width="5" fill="none" stroke-linecap="round"/></g>')
    # confused student
    s.append(P(cute.boy, 1220, 400, 1.05, mood='smile', vest='#2446F0', vest_sh='#1632C4', glasses=True))
    s.append(f'<text x="1470" y="400" {F} font-size="110" fill="#F2555A">?</text><text x="1210" y="380" {F} font-size="76" fill="#2446F0">?</text>'
             f'<path d="M1512 450 q-14 22 0 32 q14 -10 0 -32Z" fill="#9FD3F7" stroke="{INK}" stroke-width="3"/>')
    s.append(tag(212, 530, '개', '#FFF6D1', 60) + tag(802, 540, '게', '#FFE9E8', 60) + tag(1250, 110, '모음', '#FFD84A', 64))
    s.append(sparkle(1200, 270, 22) + sparkle(1540, 600, 18, '#FF9C9C') + sparkle(640, 640, 18, '#7C5CFF'))
    return svg(d, ''.join(s))

def nunchi():
    """Office corner: a worker peeks over a monitor at a colleague with a little storm cloud overhead; clock, coffee, sweat drop; tags 눈치 · 눈치 보여 · 눈치껏."""
    d = _bg('ncbg', '#EEF2F7', '#DCE4EE')
    s = ['<rect width="1600" height="1000" fill="url(#ncbg)"/>', '<rect y="820" width="1600" height="180" fill="#B8BCC8"/><rect y="820" width="1600" height="10" fill="#9AA0B0"/>']
    # window with blinds
    s.append(f'<g filter="url(#sh)"><rect x="70" y="60" width="380" height="270" rx="10" fill="#BFE3FF" stroke="{INK}" stroke-width="6"/></g>'
             + ''.join(f'<rect x="76" y="{70+i*26}" width="368" height="14" fill="#FFFFFF" opacity=".85"/>' for i in range(10)))
    s.append(_clock(760, 160, 78))
    # notice board
    s.append(f'<g transform="translate(0 -32)"><g filter="url(#sh)"><rect x="1220" y="60" width="300" height="200" rx="10" fill="#D8A86E" stroke="{INK}" stroke-width="6"/></g>'
             + ''.join(f'<g transform="translate({x} {y}) rotate({r})"><rect width="70" height="64" fill="{c}" stroke="{INK}" stroke-width="3"/><circle cx="35" cy="8" r="6" fill="#F2555A"/></g>' for x, y, r, c in [(1250, 90, -6, '#FFF6D1'), (1340, 100, 4, '#E3F7F0'), (1430, 86, -3, '#FFE9E8'), (1300, 170, 5, '#E4F2FD')]) + '</g>')
    # peeking worker behind a monitor
    s.append(P(cute.girl, 250, 430, 1.0, mood='smile', cardigan='#FFFFFF', cardigan_sh='#E0DCE8', skirt='#2E3A5C', skirt_sh='#1E2840'))
    s.append(f'<g filter="url(#sh)"><rect x="240" y="598" width="330" height="200" rx="16" fill="#2B2F55" stroke="{INK}" stroke-width="6"/><rect x="380" y="798" width="50" height="20" fill="#2B2F55"/></g>'
             f'<rect x="256" y="612" width="298" height="164" rx="8" fill="#9BD0FF"/><rect x="276" y="634" width="150" height="14" rx="7" fill="#FFFFFF"/><rect x="276" y="660" width="220" height="14" rx="7" fill="#FFFFFF" opacity=".7"/><circle cx="318" cy="598" r="13" fill="#FFE9DA" stroke="{INK}" stroke-width="4"/><circle cx="492" cy="598" r="13" fill="#FFE9DA" stroke="{INK}" stroke-width="4"/>')
    s.append(f'<path d="M522 488 q-16 24 0 36 q16 -12 0 -36Z" fill="#9FD3F7" stroke="{INK}" stroke-width="3"/>')
    s.append(f'<path d="M560 580 Q800 500 1060 540" stroke="#7C5CFF" stroke-width="5" fill="none" stroke-dasharray="4 14" stroke-linecap="round"/>')
    # desks
    s.append(f'<g filter="url(#sh)"><rect x="60" y="800" width="720" height="36" rx="10" fill="#D8A86E" stroke="{INK}" stroke-width="5"/><rect x="80" y="836" width="680" height="110" fill="#C08A55" stroke="{INK}" stroke-width="5"/></g>')
    s.append(f'<g transform="translate(620 730)"><rect width="70" height="80" rx="10" fill="#F2555A" stroke="{INK}" stroke-width="4"/><path d="M70 18 q26 0 26 22 q0 22 -26 22" stroke="{INK}" stroke-width="5" fill="none"/><path d="M22 -10 q-10 -20 4 -40 M46 -10 q-10 -20 4 -40" stroke="#B8BCC8" stroke-width="5" fill="none"/></g>')
    # colleague with a storm cloud
    s.append(P(cute.boy, 1060, 400, 1.05, mood='smile', shirt='#FFFFFF', vest='#4A4A5A', vest_sh='#33333F'))
    s.append(f'<g filter="url(#sh)"><rect x="960" y="690" width="600" height="36" rx="10" fill="#D8A86E" stroke="{INK}" stroke-width="5"/><rect x="980" y="726" width="560" height="220" fill="#C08A55" stroke="{INK}" stroke-width="5"/></g><g filter="url(#sh)"><rect x="1345" y="580" width="190" height="110" rx="10" fill="#C8CDE4" stroke="{INK}" stroke-width="5"/></g><circle cx="1440" cy="635" r="12" fill="#FFFFFF"/><g transform="translate(1020 640)" filter="url(#sh)"><rect width="110" height="50" rx="6" fill="#FFF6D1" stroke="{INK}" stroke-width="4"/><rect y="-14" width="110" height="18" rx="6" fill="#7FB8F0" stroke="{INK}" stroke-width="4"/></g>')
    s.append(_cloud(1217, 290, 52, '#9AA0B8') + f'<path d="M1210 320 l-18 34 h20 l-14 32 l36 -44 h-20 l14 -22Z" fill="#FFD84A" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>')
    s.append(tag(70, 400, '눈치', '#FFD84A', 72) + tag(600, 300, '눈치 보여', '#FFFFFF', 50) + tag(660, 430, '눈치껏', '#EFEAFF', 50))
    s.append(sparkle(560, 70, 20) + sparkle(1560, 430, 18, '#FF9C9C'))
    return svg(d, ''.join(s))

def goodbye():
    """Night bus stop under a streetlight with falling leaves; two friends wave, one holds a phone; bubbles 잘 가 · 잘 있어 · 연락해."""
    R = random.Random(24)
    d = _bg('gbbg', '#2A2F66', '#6A5AA8') + '<radialGradient id="gblamp" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFF3C4" stop-opacity=".85"/><stop offset="1" stop-color="#FFF3C4" stop-opacity="0"/></radialGradient>'
    s = ['<rect width="1600" height="1000" fill="url(#gbbg)"/>']
    for _ in range(30):
        s.append(f'<circle cx="{R.uniform(0,1600):.0f}" cy="{R.uniform(0,300):.0f}" r="{R.uniform(2,4):.0f}" fill="#FFFFFF" opacity=".7"/>')
    s.append('<circle cx="760" cy="110" r="56" fill="#FFF3C4"/><circle cx="785" cy="95" r="50" fill="#2C3168"/>')
    for i in range(9):
        x = i * 180; h = R.uniform(160, 300)
        s.append(f'<rect x="{x}" y="{840-h:.0f}" width="160" height="{h:.0f}" fill="#3A3F7E"/>' + ''.join(f'<rect x="{x+22+c*46}" y="{860-h+r*50:.0f}" width="22" height="26" fill="#FFE59A" opacity="{R.choice([.2,.6,.9])}"/>' for c in range(3) for r in range(int(h//60))))
    s.append('<rect y="840" width="1600" height="160" fill="#4A4470"/><rect y="840" width="1600" height="16" fill="#8A84B0"/>')
    # streetlight
    s.append(f'<circle cx="150" cy="200" r="240" fill="url(#gblamp)"/><rect x="140" y="200" width="20" height="640" fill="#2B2F55" stroke="{INK}" stroke-width="4"/><path d="M100 190 h100 l-20 30 h-60Z" fill="#FFE59A" stroke="{INK}" stroke-width="5"/>')
    # bus shelter
    s.append(f'<g filter="url(#sh)"><rect x="1200" y="350" width="370" height="30" rx="8" fill="#2446F0" stroke="{INK}" stroke-width="5"/><rect x="1220" y="380" width="14" height="460" fill="#2B2F55"/><rect x="1536" y="380" width="14" height="460" fill="#2B2F55"/></g>'
             f'<rect x="1234" y="380" width="302" height="300" fill="#BFE3FF" opacity=".35" stroke="#BFE3FF" stroke-width="3"/><rect x="1270" y="420" width="120" height="160" rx="6" fill="#FFD84A" opacity=".85"/>'
             f'<g filter="url(#sh)"><rect x="1250" y="720" width="270" height="22" rx="8" fill="#B47A48" stroke="{INK}" stroke-width="4"/></g>'
             f'<g filter="url(#sh)"><rect x="1420" y="400" width="96" height="70" rx="12" fill="#12A57A" stroke="{INK}" stroke-width="4"/><rect x="1436" y="414" width="64" height="34" rx="8" fill="#FFFFFF"/><circle cx="1448" cy="456" r="6" fill="#FFFFFF"/><circle cx="1488" cy="456" r="6" fill="#FFFFFF"/></g>')
    for _ in range(18):
        s.append(_leaf(R.uniform(40, 1560), R.uniform(60, 980), R.uniform(12, 20), R.choice(['#E8434A', '#FF9F43', '#FFC93C']), R.uniform(-80, 80)))
    s.append(PR(cute.girl, 430, 420, 1.05, side=1, mood='talk', cardigan='#FFD84A', cardigan_sh='#D9B21E', skirt='#7C5CFF', skirt_sh='#5B3FD6', ribbon='#F2555A'))
    s.append(f'<g transform="translate(500 700) rotate(-12)" filter="url(#sh)"><rect width="56" height="100" rx="12" fill="#2B2F55" stroke="{INK}" stroke-width="4"/><rect x="7" y="12" width="42" height="72" rx="6" fill="#9BD0FF"/><rect x="13" y="22" width="28" height="10" rx="5" fill="#FFD84A"/></g>')
    s.append(PR(cute.boy, 900, 420, 1.05, side=-1, mood='smile', vest='#F2555A', vest_sh='#C93E44'))
    s.append(f'<g transform="translate(1110 690)" filter="url(#sh)"><rect width="80" height="100" rx="18" fill="#12A57A" stroke="{INK}" stroke-width="4"/><path d="M20 4 q20 -30 40 0" stroke="{INK}" stroke-width="5" fill="none"/></g>')
    s.append(bubble(330, 200, '잘 가', 60, 'down-right') + bubble(90, 370, '연락해', 52, 'down-right', '#FFF6D1') + bubble(930, 200, '잘 있어', 60, 'down-left'))
    s.append(_heart(820, 470, 22, '#FF9C9C') + sparkle(1100, 90, 22) + sparkle(1560, 220, 18, '#FF9C9C'))
    return svg(d, ''.join(s))

def compliments():
    """Café table: one friend shows a drawing, the other gives a thumbs-up; sparkles; bubbles 대단해요! / 과찬이세요; tag 멋있어요."""
    d = _bg('cpbg', '#FFF1E6', '#F6DCC4')
    s = ['<rect width="1600" height="1000" fill="url(#cpbg)"/>', '<rect y="820" width="1600" height="180" fill="#B47A48"/>']
    # shelf with cups, framed art, lamps
    s.append(f'<g filter="url(#sh)"><rect x="80" y="130" width="300" height="20" rx="6" fill="#8A5A34" stroke="{INK}" stroke-width="4"/></g>'
             f'<path d="M110 130 h50 l-6 -50 h-38Z" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/><path d="M190 130 h46 v-60 h-46Z" fill="#7FB28A" stroke="{INK}" stroke-width="4"/><circle cx="300" cy="96" r="34" fill="#5E9C72" stroke="{INK}" stroke-width="4"/><path d="M280 130 h40 l-4 -24 h-32Z" fill="#B47A48" stroke="{INK}" stroke-width="4"/>')
    s.append(f'<g filter="url(#sh)"><rect x="1430" y="70" width="130" height="160" rx="8" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/></g><rect x="1446" y="86" width="98" height="128" fill="#FFD6C8"/><circle cx="1495" cy="130" r="22" fill="#F2A03A"/><path d="M1446 214 L1480 160 L1510 190 L1544 150 V214Z" fill="#12A57A"/>')
    for x in (640, 960):
        s.append(f'<path d="M{x} 0 V110" stroke="{INK}" stroke-width="4"/><path d="M{x-56} 170 Q{x} 80 {x+56} 170Z" fill="#F2A03A" stroke="{INK}" stroke-width="5"/><ellipse cx="{x}" cy="178" rx="24" ry="10" fill="#FFE98A"/>')
    s.append(P(cute.girl, 300, 400, 1.05, mood='happy', hair='#2B1E1A', hair_hi='#5A4038', cardigan='#E3F7F0', cardigan_sh='#A9DCC9', skirt='#F2555A', skirt_sh='#C93E44'))
    # sketchbook with a drawing
    s.append(f'<g transform="translate(570 570) rotate(6)" filter="url(#sh)"><rect width="250" height="180" rx="10" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>'
             + ''.join(f'<circle cx="{24+i*28}" cy="0" r="8" fill="none" stroke="{INK}" stroke-width="4"/>' for i in range(8)) +
             f'<path d="M20 162 Q70 96 120 142 Q170 86 230 162Z" fill="#9BD08A" stroke="{INK}" stroke-width="3"/><circle cx="190" cy="60" r="26" fill="#FFD84A" stroke="{INK}" stroke-width="3"/>'
             f'<path d="M70 120 l0 -40 M70 80 m-16 0 a16 16 0 1 0 32 0 a16 16 0 1 0 -32 0" stroke="{INK}" stroke-width="3" fill="#FF9C9C"/></g>')
    s.append(PR(cute.boy, 990, 400, 1.05, side=-1, hand='thumb', mood='talk', vest='#2446F0', vest_sh='#1632C4'))
    # table and cups
    s.append(f'<g filter="url(#sh)"><rect x="220" y="770" width="1160" height="40" rx="12" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/><path d="M232 810 H1368 L1350 930 H250Z" fill="#F2A0A0" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/><path d="M250 900 H1350" stroke="#FFFFFF" stroke-width="8" stroke-dasharray="20 14" opacity=".8"/></g>')
    for x in (280, 1320):
        s.append(f'<path d="M{x-36} 700 h72 l-8 70 h-56Z" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/><path d="M{x+36} 716 q22 2 18 22 q-4 16 -22 12" fill="none" stroke="{INK}" stroke-width="4"/><path d="M{x-10} 690 q-8 -16 4 -30 M{x+12} 690 q-8 -16 4 -30" stroke="#C8B49A" stroke-width="4" fill="none"/>')
    s.append(f'<g transform="translate(900 740)"><ellipse cx="0" cy="30" rx="70" ry="14" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/><path d="M-40 26 V-10 L40 -24 V26Z" fill="#FFE6C2" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/><path d="M-40 -10 L40 -24" stroke="#F2555A" stroke-width="10"/><circle cx="10" cy="-30" r="10" fill="#F2555A" stroke="{INK}" stroke-width="3"/></g>')
    s.append(bubble(100, 220, '과찬이세요', 48, 'down-right', '#FFF6D1') + bubble(1060, 220, '대단해요!', 54, 'down-left'))
    s.append(tag(650, 360, '멋있어요', '#FFD84A', 48))
    s.append(sparkle(630, 500, 18) + sparkle(860, 540, 22, '#FF9C9C') + sparkle(870, 690, 16) + sparkle(980, 500, 14, '#7C5CFF') + sparkle(1520, 460, 20))
    return svg(d, ''.join(s))

def office_slang():
    """Office at 6 p.m.: a worker in a coat dashes past a clock at 6:00 toward the door; laptop closing, FRI calendar; tags 칼퇴 · 불금 · 퇴근각."""
    d = _bg('osbg', '#FFE8D0', '#F6CFAE') + _bg('ossky', '#FF9F6A', '#FFD08A')
    s = ['<rect width="1600" height="1000" fill="url(#osbg)"/>', '<rect y="830" width="1600" height="170" fill="#B9A48A"/><rect y="830" width="1600" height="10" fill="#9A8668"/>']
    # sunset window
    s.append(f'<g filter="url(#sh)"><rect x="60" y="60" width="400" height="320" rx="10" fill="url(#ossky)" stroke="{INK}" stroke-width="6"/></g>'
             f'<circle cx="260" cy="300" r="60" fill="#FFF3C4"/>' + ''.join(f'<rect x="{66+i*56}" y="{380-h}" width="50" height="{h-6}" fill="#7A5A8A"/>' for i, h in enumerate([90, 140, 70, 120, 160, 100, 80])) +
             f'<path d="M260 60 V380 M60 220 H460" stroke="{INK}" stroke-width="6"/>')
    # FRI calendar page
    s.append(f'<g transform="rotate(-4 600 190)" filter="url(#sh)"><rect x="510" y="90" width="180" height="200" rx="10" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/><rect x="510" y="90" width="180" height="60" rx="10" fill="#F2555A" stroke="{INK}" stroke-width="5"/>'
             f'<rect x="513" y="130" width="174" height="18" fill="#F2555A"/><text x="600" y="136" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="800" font-size="42" fill="#FFFFFF">FRI</text>'
             f'<text x="600" y="255" text-anchor="middle" {F} font-size="96" fill="{INK}">금</text></g>')
    # clock at 6:00
    s.append(f'<g filter="url(#sh)"><circle cx="880" cy="170" r="92" fill="#FFFFFF" stroke="{INK}" stroke-width="7"/></g>'
             + ''.join(f'<rect x="877" y="88" width="6" height="16" fill="{INK}" transform="rotate({a} 880 170)"/>' for a in range(0, 360, 30)) +
             f'<path d="M880 170 V98" stroke="{INK}" stroke-width="7" stroke-linecap="round"/><path d="M880 170 V222" stroke="#F2555A" stroke-width="10" stroke-linecap="round"/><circle cx="880" cy="170" r="10" fill="{INK}"/>')
    # door, slightly open with light
    s.append(f'<g filter="url(#sh)"><rect x="1270" y="250" width="270" height="580" fill="#8A5A34" stroke="{INK}" stroke-width="6"/></g><rect x="1290" y="270" width="230" height="560" fill="#FFF3C4"/>'
             f'<path d="M1290 270 L1440 300 V810 L1290 830Z" fill="#B47A48" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/><circle cx="1415" cy="560" r="12" fill="#FFD84A" stroke="{INK}" stroke-width="4"/>')
    # desk with closing laptop
    s.append(f'<g filter="url(#sh)"><rect x="70" y="690" width="560" height="34" rx="10" fill="#D8A86E" stroke="{INK}" stroke-width="5"/><rect x="100" y="724" width="26" height="110" fill="#8A5A34"/><rect x="574" y="724" width="26" height="110" fill="#8A5A34"/></g>'
             f'<path d="M250 690 H500 L496 676 H254Z" fill="#C8CDE4" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/><g transform="translate(256 676) rotate(-24)"><rect x="0" y="-14" width="250" height="14" rx="5" fill="#9AA0B8" stroke="{INK}" stroke-width="4"/></g>'
             f'<path d="M500 560 q30 18 26 56 M532 540 q40 26 32 80" stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round"/>'
             f'<g transform="translate(140 640)"><rect width="60" height="50" rx="8" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/><path d="M60 12 q18 0 18 14 q0 14 -18 14" stroke="{INK}" stroke-width="4" fill="none"/></g>')
    # worker in a coat, leaning forward, speed lines
    coat = f'<path d="M94 296 L206 296 L222 362 L78 362Z" fill="#C8A070" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/><path d="M150 300 V360" stroke="#A88050" stroke-width="4"/><rect x="92" y="290" width="116" height="14" rx="5" fill="#8A6040" stroke="{INK}" stroke-width="3"/>'
    s.append(''.join(f'<path d="M{x} {y} h{w}" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round" opacity=".9"/>' for x, y, w in [(700, 560, 90), (670, 620, 130), (710, 680, 80), (680, 740, 110)]))
    s.append(f'<g transform="rotate(10 1010 830)">{P(cute.boy, 840, 360, 1.15, mood="happy", shirt="#C8A070", vest="#C8A070", vest_sh="#A88050", legs="#2E3A5C")}{_at(840, 360, 1.15, coat)}'
             f'<g transform="translate(1100 690) rotate(-10)"><rect width="90" height="70" rx="10" fill="#4A2E2A" stroke="{INK}" stroke-width="4"/><path d="M20 0 q25 -30 50 0" stroke="{INK}" stroke-width="5" fill="none"/></g></g>')
    s.append(''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" stroke="{INK}" stroke-width="3" opacity=".9"/>' for x, y, r in [(880, 828, 18), (850, 812, 12), (826, 830, 9)]))
    s.append(tag(1010, 80, '칼퇴', '#FFD84A', 64) + tag(470, 380, '불금', '#FFE9E8', 58) + tag(1290, 120, '퇴근각', '#FFFFFF', 52))
    s.append(sparkle(1210, 260, 20) + sparkle(720, 440, 18, '#FF9C9C') + sparkle(1560, 900, 16))
    return svg(d, ''.join(s))

def polite_requests():
    """By a window: a girl next to an open window; a five-step staircase rising from 닫아 줘 to 닫아 주실 수 있으세요?."""
    R = random.Random(9)
    d = _bg('prbg', '#E8ECFF', '#D8DEFA')
    s = ['<rect width="1600" height="1000" fill="url(#prbg)"/>', '<rect y="880" width="1600" height="120" fill="#C9A47A"/><rect y="880" width="1600" height="10" fill="#A9875E"/>']
    # open window with blowing curtain and wind
    s.append(f'<g filter="url(#sh)"><rect x="60" y="60" width="340" height="380" rx="12" fill="#BFE3FF" stroke="#8A5A34" stroke-width="12"/></g>'
             f'<path d="M66 300 Q160 270 230 300 T394 290 V434 H66Z" fill="#9BD08A"/><circle cx="320" cy="130" r="30" fill="#FFF3C4"/>'
             f'<path d="M230 66 L300 96 V412 L230 434Z" fill="#E4F2FD" stroke="#8A5A34" stroke-width="8" stroke-linejoin="round"/>'
             f'<path d="M50 50 Q120 140 80 250 Q140 330 120 460 L40 460 L40 50Z" fill="#FF9C9C" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>')
    s.append(''.join(f'<path d="M{x} {y} q40 -20 80 0 t80 0" stroke="#FFFFFF" stroke-width="7" fill="none" stroke-linecap="round" opacity=".9"/>' for x, y in [(330, 160), (360, 230), (320, 300)]))
    s.append(_leaf(560, 150, 16, '#12A57A', 40) + _leaf(640, 230, 14, '#3CBF8C', -30))
    s.append(P(cute.girl, 110, 460, 1.0, mood='talk', cardigan='#FFD84A', cardigan_sh='#D9B21E', skirt='#2446F0', skirt_sh='#1632C4'))
    # staircase
    cols = ['#FFF6D1', '#FFE2B8', '#FFD0C8', '#F2C8EC', '#DCCBFF']
    words = ['닫아 줘', '닫아 줄래?', '닫아 주세요', '닫아 주시겠어요?', '닫아 주실 수 있으세요?']
    x0, w, size = 460, 220, 44
    for i in range(5):
        top = 760 - i * 120; x = x0 + i * w
        s.append(f'<g filter="url(#sh)"><rect x="{x}" y="{top}" width="{w}" height="{880-top}" fill="{cols[i]}" stroke="{INK}" stroke-width="5"/></g>'
                 f'<rect x="{x}" y="{top}" width="{w}" height="18" fill="#FFFFFF" opacity=".6"/><text x="{x+w/2}" y="{top+90}" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="800" font-size="56" fill="{INK}" opacity=".25">{i+1}</text>')
    for i in range(5):
        top = 760 - i * 120; right = x0 + (i + 1) * w - 10
        s.append(tag(right - _tw(words[i], size), top - 92, words[i], '#FFFFFF' if i % 2 == 0 else '#FFF6D1', size))
    s.append(sparkle(1530, 120, 24) + sparkle(800, 160, 20, '#FF9C9C') + sparkle(1040, 90, 16, '#7C5CFF'))
    return svg(d, ''.join(s))

SCENES_1024 = {'topik-ii-listening-strategy': topik_listening, 'eul-geoyeyo-future-plans': future_plans, 'family-words-in-korean': family,
               'compound-vowels-hangul': compound_vowels, 'nunchi-meaning': nunchi, 'k-drama-goodbye-lines': goodbye,
               'korean-compliments': compliments, 'korean-office-slang': office_slang, 'polite-requests-korean': polite_requests}
SCENES.update(SCENES_1024)
