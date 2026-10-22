"""Cute, cheerful cartoon characters (명랑만화체) for Pocket Korean covers. Original designs.
girl() / boy(): x, y = top-left of a 300x420 box (head + body), s = scale.
mood: 'smile' | 'happy' (closed eyes) | 'talk' (open mouth)."""
import itertools
INK = '#4A2E2A'
SKIN, SKIN_SH, CHEEK = '#FFE9DA', '#F6CDB5', '#FF9C9C'
_n = itertools.count(1)

def _head(cx, cy):
    # chubby cheeks, soft chin
    return (f'<path d="M{cx-98} {cy-6} C{cx-100} {cy-74} {cx-56} {cy-92} {cx} {cy-92} C{cx+56} {cy-92} {cx+100} {cy-74} {cx+98} {cy-6} '
            f'C{cx+96} {cy+56} {cx+56} {cy+86} {cx} {cy+86} C{cx-56} {cy+86} {cx-96} {cy+56} {cx-98} {cy-6}Z" fill="{SKIN}" stroke="{INK}" stroke-width="4.5"/>')

def _eyes(cx, cy, mood, lashes):
    k = next(_n); o = [f'<defs><linearGradient id="ey{k}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2A1814"/><stop offset=".6" stop-color="#5A3424"/><stop offset="1" stop-color="#B07448"/></linearGradient></defs>']
    if mood == 'happy':
        for ex in (cx - 40, cx + 40):
            o.append(f'<path d="M{ex-17} {cy+4} Q{ex} {cy-16} {ex+17} {cy+4}" stroke="{INK}" stroke-width="6" fill="none" stroke-linecap="round"/>')
        return ''.join(o)
    for ex, f in ((cx - 40, -1), (cx + 40, 1)):
        o.append(f'<ellipse cx="{ex}" cy="{cy}" rx="14.5" ry="19" fill="url(#ey{k})"/>')
        o.append(f'<ellipse cx="{ex-5}" cy="{cy-7}" rx="6" ry="7.5" fill="#fff"/><circle cx="{ex+5}" cy="{cy+8}" r="3" fill="#fff" opacity=".95"/>')
        o.append(f'<path d="M{ex-17} {cy-12} Q{ex} {cy-26} {ex+17} {cy-12}" stroke="{INK}" stroke-width="4.5" fill="none" stroke-linecap="round"/>')
        if lashes:
            o.append(f'<path d="M{ex+16*f} {cy-13} l{8*f} -7 M{ex+11*f} {cy-19} l{5*f} -8" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    return ''.join(o)

def _cheeks_mouth(cx, cy, mood):
    o = []
    for x0 in (cx - 64, cx + 64):
        o.append(f'<ellipse cx="{x0}" cy="{cy+28}" rx="17" ry="10" fill="{CHEEK}" opacity=".7"/>'
                 f'<path d="M{x0-8} {cy+31} l5 -7 M{x0} {cy+31} l5 -7 M{x0+8} {cy+31} l5 -7" stroke="#fff" stroke-width="2.2" stroke-linecap="round" opacity=".9"/>')
    if mood == 'talk':
        o.append(f'<path d="M{cx-13} {cy+28} Q{cx} {cy+26} {cx+13} {cy+28} Q{cx+10} {cy+46} {cx} {cy+46} Q{cx-10} {cy+46} {cx-13} {cy+28}Z" fill="#B83E48" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>'
                 f'<path d="M{cx-7} {cy+41} Q{cx} {cy+36} {cx+7} {cy+41} Q{cx} {cy+46} {cx-7} {cy+41}Z" fill="#FF8A8F"/>')
    elif mood == 'happy':
        o.append(f'<path d="M{cx-14} {cy+26} Q{cx} {cy+44} {cx+14} {cy+26}Z" fill="#B83E48" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>')
    else:
        o.append(f'<path d="M{cx-12} {cy+28} Q{cx-6} {cy+36} {cx} {cy+30} Q{cx+6} {cy+36} {cx+12} {cy+28}" stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    return ''.join(o)

def _arms(cx, top, sleeve):
    o = []
    for f in (-1, 1):
        o.append(f'<path d="M{cx+44*f} {top+16} Q{cx+76*f} {top+40} {cx+74*f} {top+86} L{cx+56*f} {top+90} Q{cx+56*f} {top+56} {cx+38*f} {top+40}Z" fill="{sleeve}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>')
        o.append(f'<circle cx="{cx+66*f}" cy="{top+98}" r="12.5" fill="{SKIN}" stroke="{INK}" stroke-width="4"/>')
    return ''.join(o)

def girl(x=0, y=0, s=1.0, mood='smile', hair='#5A3328', hair_hi='#9A664E', cardigan='#FFF1CF', cardigan_sh='#EBCF91', skirt='#F2777C', skirt_sh='#D45A60', ribbon='#FFD84A', shoes='#7A3E3A'):
    cx, cy, top = 150, 132, 214
    k = next(_n)
    g = [f'<g transform="translate({x} {y}) scale({s})">',
         f'<defs><linearGradient id="hr{k}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{hair_hi}"/><stop offset=".35" stop-color="{hair}"/></linearGradient></defs>',
         f'<ellipse cx="150" cy="414" rx="70" ry="8" fill="#141838" opacity=".12"/>',
         # back hair with soft outward curls
         f'<path d="M50 120 C40 30 110 14 150 14 C192 14 262 30 250 120 C254 170 262 214 272 246 C276 262 258 272 246 262 C252 250 244 238 232 236 L222 204 L78 204 L68 236 C56 238 48 250 54 262 C42 272 24 262 28 246 C38 214 46 170 50 120Z" fill="url(#hr{k})" stroke="{INK}" stroke-width="4.5" stroke-linejoin="round"/>',
         # legs, socks, shoes
         f'<path d="M126 340 L126 392 M174 340 L174 392" stroke="{SKIN}" stroke-width="20" stroke-linecap="round"/>',
         f'<path d="M116 340 V392 M136 340 V392 M164 340 V392 M184 340 V392" stroke="{INK}" stroke-width="3.5"/>',
         f'<rect x="115" y="374" width="22" height="20" fill="#FFFFFF" stroke="{INK}" stroke-width="3.5"/><rect x="163" y="374" width="22" height="20" fill="#FFFFFF" stroke="{INK}" stroke-width="3.5"/>',
         f'<path d="M106 402 Q106 388 126 388 Q144 388 144 404 Z M156 404 Q156 388 174 388 Q194 388 194 402 Z" fill="{shoes}" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>',
         f'<rect x="102" y="400" width="44" height="9" rx="4.5" fill="{shoes}" stroke="{INK}" stroke-width="3.5"/><rect x="154" y="400" width="44" height="9" rx="4.5" fill="{shoes}" stroke="{INK}" stroke-width="3.5"/>',
         # pleated skirt
         f'<path d="M96 300 L204 300 L226 350 Q150 364 74 350Z" fill="{skirt}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>',
         f'<path d="M122 304 L112 354 M150 304 V358 M178 304 L188 354" stroke="{skirt_sh}" stroke-width="3.5"/>',
         # cardigan body, blouse collar, buttons
         f'<path d="M104 {top+6} Q150 {top-8} 196 {top+6} L206 306 Q150 316 94 306Z" fill="{cardigan}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>',
         f'<path d="M150 {top} V310" stroke="{cardigan_sh}" stroke-width="4"/>',
         ''.join(f'<circle cx="150" cy="{top+i}" r="4.5" fill="{ribbon}" stroke="{INK}" stroke-width="2.5"/>' for i in (40, 62, 84)),
         f'<path d="M118 {top+2} Q134 {top+28} 150 {top+12} Q166 {top+28} 182 {top+2} Q166 {top+8} 150 {top+4} Q134 {top+8} 118 {top+2}Z" fill="#FFFFFF" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>',
         _arms(cx, top, cardigan),
         _head(cx, cy),
         _eyes(cx, cy + 16, mood, True),
         f'<path d="M98 120 Q110 110 124 116 M176 116 Q190 110 202 120" stroke="{hair}" stroke-width="4" fill="none" stroke-linecap="round"/>',
         _cheeks_mouth(cx, cy + 16, mood),
         # side-swept rounded bangs
         f'<path d="M50 132 C44 52 96 30 150 30 C206 30 258 52 250 132 C242 104 230 86 214 76 C214 98 204 112 188 120 C192 100 186 84 176 76 C164 104 140 116 112 118 C124 104 128 92 126 82 C102 96 76 108 50 132Z" fill="url(#hr{k})" stroke="{INK}" stroke-width="4.5" stroke-linejoin="round"/>',
         f'<path d="M50 132 C52 170 60 196 74 214 C62 210 54 196 50 180Z M250 132 C248 170 240 196 226 214 C238 210 246 196 250 180Z" fill="{hair}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>',
         f'<path d="M92 50 Q120 38 146 38 M164 38 Q186 40 206 48" stroke="#FFFFFF" stroke-width="6" fill="none" stroke-linecap="round" opacity=".45"/>',
         # ribbon
         f'<g transform="translate(220 66) rotate(18)"><path d="M0 0 L-24 -14 L-24 14Z M0 0 L24 -14 L24 14Z" fill="{ribbon}" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/><circle r="7" fill="{ribbon}" stroke="{INK}" stroke-width="3.5"/></g>',
         '</g>']
    return ''.join(g)

def boy(x=0, y=0, s=1.0, mood='smile', hair='#2C2220', hair_hi='#6A544C', shirt='#FFFFFF', vest='#5B8DEF', vest_sh='#3D6CCB', legs='#2E3A5C', shoes='#FFFFFF', glasses=False):
    cx, cy, top = 150, 134, 214
    k = next(_n)
    g = [f'<g transform="translate({x} {y}) scale({s})">',
         f'<defs><linearGradient id="hb{k}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{hair_hi}"/><stop offset=".4" stop-color="{hair}"/></linearGradient></defs>',
         f'<ellipse cx="150" cy="414" rx="70" ry="8" fill="#141838" opacity=".12"/>',
         # trousers and sneakers
         f'<path d="M100 300 L200 300 L194 394 L156 394 L150 330 L144 394 L106 394Z" fill="{legs}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>',
         f'<path d="M100 404 Q100 386 126 386 Q148 386 150 404Z M150 404 Q152 386 174 386 Q200 386 200 404Z" fill="{shoes}" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>',
         f'<rect x="96" y="400" width="56" height="10" rx="5" fill="{shoes}" stroke="{INK}" stroke-width="3.5"/><rect x="148" y="400" width="56" height="10" rx="5" fill="{shoes}" stroke="{INK}" stroke-width="3.5"/>',
         f'<path d="M112 394 l20 0 M168 394 l20 0" stroke="#F2555A" stroke-width="4" stroke-linecap="round"/>',
         # shirt + knit vest
         f'<path d="M100 {top+6} Q150 {top-8} 200 {top+6} L208 306 Q150 316 92 306Z" fill="{shirt}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>',
         f'<path d="M110 {top+14} L150 {top+60} L190 {top+14} L200 306 Q150 316 100 306Z" fill="{vest}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>',
         ''.join(f'<path d="M{x0} {top+70} V300" stroke="{vest_sh}" stroke-width="3" opacity=".7"/>' for x0 in (120, 136, 164, 180)),
         f'<path d="M124 {top+2} L150 {top+22} L176 {top+2} L166 {top-2} L150 {top+10} L134 {top-2}Z" fill="#FFFFFF" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>',
         _arms(cx, top, shirt),
         _head(cx, cy),
         f'<ellipse cx="52" cy="{cy+16}" rx="14" ry="18" fill="{SKIN}" stroke="{INK}" stroke-width="4"/><ellipse cx="248" cy="{cy+16}" rx="14" ry="18" fill="{SKIN}" stroke="{INK}" stroke-width="4"/>',
         _eyes(cx, cy + 18, mood, False),
         f'<path d="M96 122 Q112 114 128 118 M172 118 Q188 114 204 122" stroke="{hair}" stroke-width="6" fill="none" stroke-linecap="round"/>',
         _cheeks_mouth(cx, cy + 18, mood),
         # fluffy hair: rounded tufts, curtain bangs
         f'<path d="M50 140 C30 120 40 92 56 84 C52 56 80 36 104 40 C116 22 146 20 160 30 C180 18 214 26 222 48 C246 50 264 74 256 98 C270 110 266 132 250 142 C246 116 232 96 214 88 C212 106 200 118 184 122 C188 104 180 92 168 86 C160 102 154 110 150 114 C146 104 140 94 130 88 C122 104 110 116 94 120 C96 104 92 94 84 90 C68 104 56 120 50 140Z" fill="url(#hb{k})" stroke="{INK}" stroke-width="4.5" stroke-linejoin="round"/>',
         f'<path d="M150 26 C152 10 168 4 182 8 C172 14 168 22 168 32" fill="{hair}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>',
         f'<path d="M94 54 Q118 42 140 42" stroke="#FFFFFF" stroke-width="6" fill="none" stroke-linecap="round" opacity=".35"/>',
         (f'<g fill="none" stroke="{INK}" stroke-width="4"><circle cx="{cx-40}" cy="{cy+18}" r="25" fill="#FFFFFF" fill-opacity=".15"/><circle cx="{cx+40}" cy="{cy+18}" r="25" fill="#FFFFFF" fill-opacity=".15"/><path d="M{cx-15} {cy+14} q15 -8 30 0"/></g>' if glasses else ''),
         '</g>']
    return ''.join(g)
