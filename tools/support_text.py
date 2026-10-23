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
    faq=[('평생 이용권은 어떤 건가요?', '한 번만 결제하면 모든 레벨과 기능을 계속 쓸 수 있어요. 구독이 아니라서 매달 결제되거나 해지할 필요가 없어요.'),
         ('새 폰이나 앱을 다시 설치했을 때 평생 이용권은?', '구매할 때 쓴 Apple ID로 App Store에 로그인한 뒤 앱에서 평생 이용권 구매를 다시 눌러 주세요. Apple이 이미 구매한 항목이라고 알려 주고, 추가 결제 없이 다시 열려요.'),
         ('환불받고 싶어요.', '환불은 저희가 아니라 Apple이 처리해요. <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>에서 요청해 주세요.'),
         ('소리가 안 나요.', '볼륨, 블루투스 이어폰 연결, 인터넷 연결을 확인해 주세요. 그래도 안 되면 앱을 완전히 닫았다가 다시 열어 주세요.'),
         ('폰을 바꿨더니 학습 기록이 없어졌어요.', '학습 기록은 기기에만 저장되고 서버에 따로 보관하지 않아요. 그래서 다른 기기로 옮길 수 없어요.'),
         ('웹에서는 어디까지 무료인가요?', 'A1 단어와 주제별 단어는 웹 앱에서 무료로 써 볼 수 있어요. 그 이상은 앱에서 평생 이용권으로 열려요.')]),
'en': dict(t='Support', lead=f'Help for the Pocket German app and website. Questions or problems? Write to {MAIL} — we usually answer within 1–2 days.',
    faqh='Frequently asked questions', ch='Contact', cp=f'E-mail: {MAIL}<br>Please tell us your device (e.g. iPhone 15, iOS 26), the app version and what happened.',
    faq=[('What is the lifetime unlock?', 'You pay once and keep all levels and features. It is not a subscription, so there is nothing to renew or cancel.'),
         ('I have a new phone or reinstalled the app.', 'Sign in to the App Store with the Apple ID you used to buy, then tap the lifetime purchase in the app again. Apple will tell you that you already own it and unlock it again at no charge.'),
         ('How do I get a refund?', 'Refunds are handled by Apple, not by us. Request one at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.'),
         ('There is no sound.', 'Check the volume, Bluetooth headphones and your internet connection. If it still fails, close the app completely and open it again.'),
         ('I changed phones and my progress is gone.', 'Your progress is saved only on your device — we keep no accounts or server copies, so it cannot be moved between devices.'),
         ('What is free on the web?', 'A1 words and the topic word lists are free to try in the web app. Everything else unlocks with the lifetime purchase in the app.')]),
'ja': dict(t='サポート', lead=f'ポケットドイツ語のアプリとウェブサイトのヘルプです。ご質問や不具合は {MAIL} までメールでお問い合わせください。通常1〜2日以内に返信します。',
    faqh='よくある質問', ch='お問い合わせ', cp=f'メール：{MAIL}<br>お使いの端末（例：iPhone 15、iOS 26）、アプリのバージョン、起きたことを書いていただくとスムーズです。',
    faq=[('買い切り（永久ライセンス）とは？', '一度お支払いいただくと、すべてのレベルと機能をずっと使えます。サブスクリプションではないので、更新や解約は不要です。'),
         ('機種変更・再インストールしたら？', '購入時と同じ Apple ID で App Store にサインインし、アプリで買い切りの購入をもう一度タップしてください。購入済みと表示され、追加料金なしで再び利用できます。'),
         ('返金してほしい。', '返金は Apple が対応します。<a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a> からリクエストしてください。'),
         ('音が出ません。', '音量、Bluetooth イヤホン、インターネット接続を確認してください。それでも出ない場合はアプリを完全に終了してから開き直してください。'),
         ('機種変更したら学習記録が消えた。', '学習記録は端末にのみ保存され、サーバーには保管していません。そのため別の端末には移せません。'),
         ('ウェブではどこまで無料？', 'A1 の単語とテーマ別単語はウェブアプリで無料で試せます。それ以外はアプリの買い切り購入で利用できます。')]),
}

def pg(g, h='h1'):
    s = PG[g]; h2 = 'h3' if h == 'h2' else 'h2'
    return (f'<{h}>{s["t"]}</{h}><p class="lead">{s["lead"]}</p><{h2}>{s["faqh"]}</{h2}>{_faq(s["faq"])}'
            f'<{h2}>{s["ch"]}</{h2}><p>{s["cp"]}</p>')
