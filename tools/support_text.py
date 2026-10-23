"""Support / FAQ text. pk(): Pocket Korean (/support/, English). pg(g): Pocket German (ko/en/ja: /german/ home section + /german/support/)."""
MAIL = '<a href="mailto:hello@pocketkorean.com">hello@pocketkorean.com</a>'

def _faq(items):
    return ''.join(f'<details class="faq"><summary>{q}</summary><p>{a}</p></details>' for q, a in items)

PK_FAQ = [
    ('How do I restore my Premium purchase on a new phone?',
     'Sign in to the App Store (or Google Play) with the same account you used to buy, open Pocket Korean, go to Premium and tap <b>Restore purchases</b>.'),
    ('How do I cancel my subscription?',
     'Subscriptions are managed by Apple or Google. On iPhone: Settings → your name → Subscriptions → Pocket Korean. On Android: Google Play → Profile → Payments &amp; subscriptions → Subscriptions. Cancel at least 24 hours before the renewal date.'),
    ('How do I get a refund?',
     'Refunds are handled by the store, not by us. On iPhone, request one at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>; on Android, use Google Play\'s refund request.'),
    ('There is no sound.',
     'Check the volume, Bluetooth headphones and your internet connection. If you use offline audio, download it again in the app settings.'),
    ('I changed phones and my progress is gone.',
     'Your progress is saved only on your device — we do not keep accounts or copies on a server. It cannot be moved between devices.'),
]

def pk():
    return (f'<h1>Support</h1><p class="lead">Help for the Pocket Korean app and website. Questions or problems? Write to {MAIL} — we usually answer within 1–2 days.</p>'
            f'<h2>Frequently asked questions</h2>{_faq(PK_FAQ)}'
            f'<h2>Contact</h2><p>E-mail: {MAIL}<br>Please tell us your device (e.g. iPhone 15, iOS 26), the app version and what happened.</p>'
            f'<p><a href="/privacy/">Privacy policy</a></p>')

PG = {
'ko': dict(t='고객 지원', lead=f'포켓독일어 앱과 웹사이트 도움말이에요. 궁금한 점이나 문제가 있으면 {MAIL}로 메일 주세요. 보통 1~2일 안에 답장해요.',
    faqh='자주 묻는 질문', ch='문의하기', cp=f'이메일: {MAIL}<br>사용 중인 기기(예: iPhone 15, iOS 26), 앱 버전, 어떤 문제가 있었는지 적어 주시면 빨리 도와드릴 수 있어요.',
    faq=[('새 폰에서 구매한 프리미엄을 다시 쓰려면?', '구매할 때 쓴 Apple ID로 App Store에 로그인한 뒤, 포켓독일어 앱의 프리미엄 화면에서 <b>구매 복원</b>을 눌러 주세요.'),
         ('구독은 어떻게 해지하나요?', '구독은 Apple이 관리해요. iPhone 설정 → 내 이름 → 구독 → 포켓독일어에서 해지할 수 있어요. 갱신일 24시간 전까지 해지해야 다음 결제가 되지 않아요.'),
         ('환불받고 싶어요.', '환불은 저희가 아니라 Apple이 처리해요. <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>에서 요청해 주세요.'),
         ('소리가 안 나요.', '볼륨, 블루투스 이어폰 연결, 인터넷 연결을 확인해 주세요. 그래도 안 되면 앱을 완전히 닫았다가 다시 열어 주세요.'),
         ('폰을 바꿨더니 학습 기록이 없어졌어요.', '학습 기록은 기기에만 저장되고 서버에 따로 보관하지 않아요. 그래서 다른 기기로 옮길 수 없어요.'),
         ('웹에서는 어디까지 무료인가요?', 'A1 단어와 주제별 단어는 웹 앱에서 무료로 써 볼 수 있어요. 그 이상은 앱에서 프리미엄으로 열려요.')]),
'en': dict(t='Support', lead=f'Help for the Pocket German app and website. Questions or problems? Write to {MAIL} — we usually answer within 1–2 days.',
    faqh='Frequently asked questions', ch='Contact', cp=f'E-mail: {MAIL}<br>Please tell us your device (e.g. iPhone 15, iOS 26), the app version and what happened.',
    faq=[('How do I restore my Premium purchase on a new phone?', 'Sign in to the App Store with the Apple ID you used to buy, open Pocket German, go to Premium and tap <b>Restore purchases</b>.'),
         ('How do I cancel my subscription?', 'Subscriptions are managed by Apple: Settings → your name → Subscriptions → Pocket German. Cancel at least 24 hours before the renewal date.'),
         ('How do I get a refund?', 'Refunds are handled by Apple, not by us. Request one at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.'),
         ('There is no sound.', 'Check the volume, Bluetooth headphones and your internet connection. If it still fails, close the app completely and open it again.'),
         ('I changed phones and my progress is gone.', 'Your progress is saved only on your device — we keep no accounts or server copies, so it cannot be moved between devices.'),
         ('What is free on the web?', 'A1 words and the topic word lists are free to try in the web app. Everything else unlocks with Premium in the app.')]),
'ja': dict(t='サポート', lead=f'ポケットドイツ語のアプリとウェブサイトのヘルプです。ご質問や不具合は {MAIL} までメールでお問い合わせください。通常1〜2日以内に返信します。',
    faqh='よくある質問', ch='お問い合わせ', cp=f'メール：{MAIL}<br>お使いの端末（例：iPhone 15、iOS 26）、アプリのバージョン、起きたことを書いていただくとスムーズです。',
    faq=[('新しいスマホでプレミアムを使うには？', '購入時と同じ Apple ID で App Store にサインインし、ポケットドイツ語のプレミアム画面で<b>購入を復元</b>をタップしてください。'),
         ('サブスクリプションの解約方法は？', 'サブスクリプションは Apple が管理しています。iPhone の設定 → ユーザー名 → サブスクリプション → ポケットドイツ語から解約できます。更新日の24時間前までに解約してください。'),
         ('返金してほしい。', '返金は Apple が対応します。<a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a> からリクエストしてください。'),
         ('音が出ません。', '音量、Bluetooth イヤホン、インターネット接続を確認してください。それでも出ない場合はアプリを完全に終了してから開き直してください。'),
         ('機種変更したら学習記録が消えた。', '学習記録は端末にのみ保存され、サーバーには保管していません。そのため別の端末には移せません。'),
         ('ウェブではどこまで無料？', 'A1 の単語とテーマ別単語はウェブアプリで無料で試せます。それ以外はアプリのプレミアムで利用できます。')]),
}

def pg(g, h='h1'):
    s = PG[g]; h2 = 'h3' if h == 'h2' else 'h2'
    return (f'<{h}>{s["t"]}</{h}><p class="lead">{s["lead"]}</p><{h2}>{s["faqh"]}</{h2}>{_faq(s["faq"])}'
            f'<{h2}>{s["ch"]}</{h2}><p>{s["cp"]}</p>')
