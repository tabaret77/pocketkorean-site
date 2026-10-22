import sys, os
from datetime import date
sys.path.insert(0, 'tools')
from german_cards import news_cover, news_card, life_cover, life_card, render, page, foot, FLAG, FONT, E

D = date(2026, 10, 22)
OUT = 'german/media/life/2026-10-22'
os.makedirs(OUT, exist_ok=True)
only = sys.argv[1:]  # optional filter of image names

def want(name):
    return not only or any(o in name for o in only)

# ---------------- news ----------------
N = {
 'ko': dict(
  hook='일요일 새벽 3시 → 2시, 시계가 1시간 뒤로 가요', red='1시간 뒤로',
  items=['첫 가을 폭풍, 금요일부터 서부·북부에 강풍', '주정부들 "전기세 모두에게 내려라"', '담배세 법, 실수로 1년 일찍 발효', '지역 열차 축소·요금 인상 경고'],
  cards=[
   dict(headline='이번 일요일, 시계를 1시간 뒤로', keyword='1시간 뒤로', big='3→2', big_unit='시', big_label='10월 25일(일) 새벽', note='하룻밤이 1시간 길어져요. 휴대폰은 자동, 오븐·자동차 시계는 직접!',
        side=[('겨울시간 CET 시작', '한국과 시차 7시간 → 8시간'), ('저녁이 더 빨리 어두워져요', '일몰이 1시간 당겨진 느낌'), ('EU 폐지 논의는 멈춤', '2019년 의회 표결 후 진전 없음')]),
   dict(headline='첫 가을 폭풍, 주말 내내 바람', keyword='가을 폭풍', big='금→월', big_unit='', big_label='서부·북부 강풍 예상 기간', note='독일기상청(DWD): 산간 고지대엔 허리케인급 돌풍도 가능',
        side=[('금요일엔 서부가 가장 강해요', '쾰른·프랑크푸르트 쪽 주의'), ('북부·북동부는 월요일까지', '함부르크·북해 연안 폭풍'), ('저기압 이름은 "루이제"', '영국 기상청은 "오스틴"')]),
   dict(headline='주총리들 "전기세, 모두에게 내려라"', keyword='전기세', big='93', big_unit='€/년', big_label='3인 가구(4,000kWh) 절약 예상', note='Verivox 계산. 2인 가구 65유로, 1인 가구 35유로',
        side=[('지금 2.05센트/kWh', '목표: EU 최저 0.1센트'), ('세수 연 110억€ 더 들어와요', '10/22 세수 추계 발표'), ('재무장관은 신중', '"재원 대책도 함께 내라"')]),
   dict(headline='담배세 법, 실수로 1년 일찍 발효', keyword='실수로', big='8.77', big_unit='€', big_label='2027년 담배 한 갑 예상 가격', note='재무부 추정, 20개비 기준. 지금은 평균 약 8유로',
        side=[('10월 21일 발효돼 버림', '원래 계획은 2027년 1월'), ('계산대 가격은 당분간 그대로', '세관이 기존 가격 용인'), ('2030년엔 11.36유로 예상', '단계적으로 인상')]),
   dict(headline='지역 열차, 줄거나 비싸질 수도', keyword='지역 열차', big='66.80', big_unit='€', big_label='도이칠란트티켓 월 요금 (2027.1.~)', note='지금 63유로. 이건 이미 확정된 인상이에요',
        side=[('선로 사용료 급등', '주정부들 "연방이 메워라"'), ('연방 교통장관은 거절', '추가 재원 없다는 입장'), ('교통장관회의 10/21–22', '바이에른 호엔슈방가우')]),
  ],
  wx_title='날씨 · 금–일', wx_tip='☂️ 우산보다 방수 재킷! 바람이 강해요',
  days=['금 10/23', '토 10/24', '일 10/25'],
  cities=['베를린', '함부르크', '뮌헨', '쾰른', '프랑크푸르트'],
 ),
 'en': dict(
  hook='Sunday 3:00 becomes 2:00 — clocks go back one hour', red='go back one hour',
  items=['First autumn storm: strong wind in the west and north from Friday', 'States: cut electricity tax for everyone', 'Tobacco tax law took effect a year early by mistake', 'Warning: fewer regional trains or higher fares'],
  cards=[
   dict(headline='This Sunday, clocks go back one hour', keyword='go back one hour', big='3→2', big_unit='am', big_label='Sunday 25 October, at night', note='One extra hour of sleep. Phones switch by themselves; ovens and car clocks don’t.',
        side=[('Winter time (CET) starts', 'UK & Ireland change the same night'), ('Darker evenings', 'Sunset feels an hour earlier'), ('EU plan to end it is stuck', 'No progress since the 2019 vote')]),
   dict(headline='First autumn storm, windy all weekend', keyword='autumn storm', big='Fri→Mon', big_unit='', big_label='Stormy spell in the west & north', note='DWD: hurricane-force gusts possible on exposed high ground',
        side=[('Friday: strongest in the west', 'Cologne, Frankfurt area'), ('North & northeast until Monday', 'Hamburg and the North Sea coast'), ('Low named “Luise”', 'UK Met Office: “Austen”')]),
   dict(headline='States: cut the electricity tax for all', keyword='electricity tax', big='€93', big_unit='/yr', big_label='Saving for 3 people (4,000 kWh)', note='Verivox estimate. 2 people: €65, single: €35',
        side=[('Now 2.05 ct/kWh', 'Goal: EU minimum 0.1 ct'), ('Tax revenue +€11bn a year', 'New tax estimate on 22 Oct'), ('Finance minister hesitant', '“Bring a way to pay for it”')]),
   dict(headline='Tobacco tax law in force a year early', keyword='a year early', big='€8.77', big_unit='', big_label='Expected price of a pack in 2027', note='Finance ministry estimate, 20 cigarettes. Today: about €8',
        side=[('In force since 21 October', 'Planned start: January 2027'), ('Shop prices stay for now', 'Customs tolerates old prices'), ('About €11.36 by 2030', 'Rising step by step')]),
   dict(headline='Regional trains: fewer or pricier?', keyword='Regional trains', big='€66.80', big_unit='', big_label='Deutschlandticket per month from Jan 2027', note='Now €63. This rise is already decided.',
        side=[('Track fees jump', 'States want Berlin to pay'), ('Federal minister says no', 'No extra money in his budget'), ('Transport ministers met', '21–22 Oct, Hohenschwangau')]),
  ],
  wx_title='Weather · Fri–Sun', wx_tip='☂️ Rain jacket beats umbrella — it’s windy',
  days=['Fri 23', 'Sat 24', 'Sun 25'],
  cities=['Berlin', 'Hamburg', 'Munich', 'Cologne', 'Frankfurt'],
 ),
 'ja': dict(
  hook='日曜深夜3時→2時、時計を1時間戻します', red='1時間戻します',
  items=['秋の初嵐、金曜から西部・北部で強風', '州首相ら「電気税を全員に引き下げを」', 'たばこ税法、ミスで1年早く施行', '地域列車の減便・値上げを警告'],
  cards=[
   dict(headline='今週日曜、時計を1時間戻す', keyword='1時間戻す', big='3→2', big_unit='時', big_label='10月25日（日）深夜', note='一晩が1時間長くなります。スマホは自動、オーブンや車の時計は手動で。',
        side=[('冬時間（CET）スタート', '日本との時差は7時間→8時間'), ('夕方が早く暗くなります', '日没が1時間早まる感覚'), ('EUの廃止議論は停滞', '2019年の議会採決から進展なし')]),
   dict(headline='秋の初嵐、週末はずっと強風', keyword='秋の初嵐', big='金→月', big_unit='', big_label='西部・北部で荒れる期間', note='ドイツ気象局（DWD）：山の高所ではハリケーン級の突風も',
        side=[('金曜は西部が最も強い', 'ケルン・フランクフルト周辺'), ('北部・北東部は月曜まで', 'ハンブルク・北海沿岸'), ('低気圧の名前は「ルイーゼ」', '英国気象庁は「オースティン」')]),
   dict(headline='州首相ら「電気税を全員に引き下げを」', keyword='電気税', big='93', big_unit='€/年', big_label='3人世帯（4,000kWh）の節約額', note='Verivox試算。2人世帯65ユーロ、単身35ユーロ',
        side=[('現在2.05セント/kWh', '目標：EU最低の0.1セント'), ('税収は年110億€上振れ', '10/22の税収見積もり'), ('財務相は慎重', '「財源案もセットで」')]),
   dict(headline='たばこ税法、ミスで1年早く施行', keyword='ミスで', big='8.77', big_unit='€', big_label='2027年の1箱の予想価格', note='財務省の推計、20本入り。現在は平均約8ユーロ',
        side=[('10月21日に施行されてしまった', '本来は2027年1月から'), ('店頭価格は当面そのまま', '税関が旧価格を容認'), ('2030年には11.36ユーロ', '段階的に値上げ')]),
   dict(headline='地域列車、減便か値上げか', keyword='地域列車', big='66.80', big_unit='€', big_label='ドイチュラントチケット月額・1月〜', note='現在63ユーロ。この値上げはすでに決定済み',
        side=[('線路使用料が急上昇', '州は「連邦が負担を」'), ('連邦交通相は拒否', '追加財源はないとの立場'), ('交通相会議 10/21–22', 'バイエルン州ホーエンシュヴァンガウ')]),
  ],
  wx_title='天気 · 金〜日', wx_tip='☂️ 傘より防水ジャケットを。風が強いです',
  days=['金 10/23', '土 10/24', '日 10/25'],
  cities=['ベルリン', 'ハンブルク', 'ミュンヘン', 'ケルン', 'フランクフルト'],
 ),
}

# (icon, max, min) per city per day — wetter.com forecasts, 22 Oct 2026
WX = [
 [('🌧️', 12, 6), ('🌧️', 12, 8), ('🌧️', 13, 8)],   # Berlin: light rain; light rain + windy x2
 [('🌧️', 11, 6), ('🌧️', 12, 8), ('🌬️', 13, 10)],  # Hamburg: Sun rain + stormy
 [('☁️', 11, 4), ('⛅', 10, 4), ('🌧️', 12, 6)],     # Munich
 [('🌬️', 14, 10), ('🌧️', 14, 9), ('🌬️', 14, 10)], # Cologne: Fri/Sun stormy
 [('🌧️', 14, 8), ('🌦️', 13, 7), ('🌦️', 15, 8)],   # Frankfurt
]

def weather(lang, out):
    t = N[lang]
    head = '<div></div>' + ''.join(f'<div style="color:#B7C2DC;font-size:24px;font-weight:700;text-align:center">{E(d)}</div>' for d in t['days'])
    rows = ''
    for c, days in zip(t['cities'], WX):
        rows += f'<div style="color:#fff;font-size:28px;font-weight:900;display:flex;align-items:center">{E(c)}</div>'
        for ic, hi, lo in days:
            rows += (f'<div style="background:#1C2F57;border-radius:16px;display:flex;align-items:center;justify-content:center;gap:16px;height:74px">'
                     f'<span style="font-size:40px">{ic}</span><span style="font-size:34px;font-weight:900;color:#FFCC00">{hi}°</span>'
                     f'<span style="font-size:26px;color:#B7C2DC">{lo}°</span></div>')
    body = (f'<div style="padding:44px 56px"><div style="display:flex;align-items:center;gap:16px"><span style="background:#DC0000;color:#fff;font-weight:900;font-size:22px;padding:4px 12px;letter-spacing:.06em">WETTER</span>'
            f'<h2 style="color:#fff;font-size:44px;font-weight:900">{E(t["wx_title"])}</h2></div>{FLAG}'
            f'<div style="display:grid;grid-template-columns:240px repeat(3,1fr);gap:12px 16px;margin-top:26px">{head}{rows}</div>'
            f'<p style="margin-top:22px;background:#F5F6FA;color:#0F1E3D;border-radius:16px;padding:14px 22px;font-size:26px;font-weight:900">{E(t["wx_tip"])}</p></div>{foot(lang)}')
    render(page(lang, 1200, 820, body), 1200, 820, out)

for lang, t in N.items():
    f = f'{OUT}/news-{lang}-cover.jpg'
    if want(f): news_cover(lang, D, t['hook'], t['items'], f, hook_red=t['red'])
    for i, c in enumerate(t['cards'], 1):
        f = f'{OUT}/news-{lang}-{i:02d}.jpg'
        if want(f):
            news_card(lang, i, D, c['headline'], f, keyword=c['keyword'], big=c['big'], big_unit=c['big_unit'],
                      big_label=c['big_label'], note=c['note'], side=c['side'])
    f = f'{OUT}/news-{lang}-weather.jpg'
    if want(f): weather(lang, f)

# ---------------- life ----------------
L = {
 'ko': dict(title='10월 31일, 할로윈만 있는 게 아니에요', kicker='독일 이야기 · 종교개혁일과 만성절',
   card_h='10월 말~11월 초, 독일의 세 가지 날',
   points=[('📜', '10/31 종교개혁일', '루터의 95개조. 9개 주 공휴일'), ('🎃', '10/31 할로윈', '"Süßes oder Saures!" 아이들 사탕 받기'), ('🕯️', '11/1 만성절', '남부·서부 5개 주 공휴일, 조용한 날')],
   map_h='어느 주가 쉬나요?', map_a='종교개혁일 (10/31)', map_b='만성절 (11/1)', map_note='베를린은 둘 다 아니에요 — 하지만 브란덴부르크는 31일 휴일!'),
 'en': dict(title='31 October is more than Halloween', kicker='Life in Germany · Reformation Day & All Saints',
   card_h='Three days at the turn of October',
   points=[('📜', '31 Oct: Reformation Day', 'Luther’s 95 theses. Holiday in 9 states'), ('🎃', '31 Oct: Halloween', '“Süßes oder Saures!” — kids collect sweets'), ('🕯️', '1 Nov: All Saints’ Day', 'Holiday in 5 states, a quiet day')],
   map_h='Who has a day off?', map_a='Reformation Day (31 Oct)', map_b='All Saints’ Day (1 Nov)', map_note='Berlin has neither — but Brandenburg is off on the 31st!'),
 'ja': dict(title='10月31日はハロウィンだけじゃない', kicker='ドイツ暮らし · 宗教改革記念日と諸聖人の日',
   card_h='10月末〜11月初め、ドイツの3つの日',
   points=[('📜', '10/31 宗教改革記念日', 'ルターの95か条。9州で祝日'), ('🎃', '10/31 ハロウィン', '「Süßes oder Saures!」子どもがお菓子集め'), ('🕯️', '11/1 諸聖人の日', '南部・西部の5州で祝日、静かな日')],
   map_h='どの州が休み？', map_a='宗教改革記念日（10/31）', map_b='諸聖人の日（11/1）', map_note='ベルリンはどちらも平日 — でもブランデンブルク州は31日が祝日！'),
}
REF = ['Brandenburg', 'Bremen', 'Hamburg', 'Mecklenburg-Vorpommern', 'Niedersachsen', 'Sachsen', 'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen']
ALL = ['Baden-Württemberg', 'Bayern', 'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland']

def states(lang, out):
    t = L[lang]
    def col(title, names, color, emoji):
        chips = ''.join(f'<span style="display:inline-block;background:#fff;border-radius:10px;padding:8px 14px;margin:0 10px 10px 0;font-size:22px;font-weight:700;color:#1B2433;box-shadow:0 6px 14px -10px rgba(27,36,51,.5);border-left:6px solid {color}">{E(n)}</span>' for n in names)
        return (f'<div style="background:rgba(255,255,255,.55);border-radius:20px;padding:24px 26px"><p style="font-size:28px;font-weight:900;color:{color}">{emoji} {E(title)}</p>'
                f'<div style="margin-top:16px">{chips}</div></div>')
    body = (f'<div style="padding:46px 56px"><h2 style="font-size:44px;font-weight:900;color:#1B2433">{E(t["map_h"])}</h2>'
            f'<div style="display:flex;width:120px;height:8px;margin-top:14px"><i style="flex:1;background:#111"></i><i style="flex:1;background:#DC0000"></i><i style="flex:1;background:#FFCC00"></i></div>'
            f'<div style="display:grid;grid-template-columns:1.25fr 1fr;gap:24px;margin-top:30px">{col(t["map_a"], REF, "#D9483B", "📜")}{col(t["map_b"], ALL, "#2F5D9E", "🕯️")}</div>'
            f'<p style="margin-top:22px;font-size:26px;font-weight:900;color:#1B2433">🐻 {E(t["map_note"])}</p></div>{foot(lang, dark=False)}')
    render(page(lang, 1200, 720, body, bg='#F3F5F1'), 1200, 720, out)

for lang, t in L.items():
    f = f'{OUT}/life-{lang}-cover.jpg'
    if want(f): life_cover(lang, t['title'], f, kicker=t['kicker'], emoji='📜', emojis=['🎃', '🕯️', '🍂', '🍬'])
    f = f'{OUT}/life-{lang}-01.jpg'
    if want(f): life_card(lang, t['card_h'], t['points'], f)
    f = f'{OUT}/life-{lang}-02.jpg'
    if want(f): states(lang, f)
print('done')
