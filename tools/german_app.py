"""Pocket German web trial at /german/web/ (Korean index.html, English index_en.html, Japanese index_ja.html).

Free in the browser: every A1 word and the topic word lists (주제별 단어). Other levels show a lock and open a
'this level is in the app' sheet. The level files for A2–C2 only carry the words the topic lists need,
so nothing else can leak through search or quizzes.

Source: /home/claude/pgsrc (the app's own files). Audio: german_audio.py (run once; writes german/web/audio).
Run: python3 tools/german_app.py
"""
import json, os, re, shutil

SRC = '/home/claude/pgsrc'
OUT = '/home/claude/pocketkorean-site/german/web'
APP_STORE = ''   # fill in after launch: the App Store link turns the 'coming soon' button into a real one
LVS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
FILES = {'ko': ('index.html', 'data'), 'en': ('index_en.html', 'data_en'), 'ja': ('index_ja.html', 'data_ja')}
HOME = {'ko': '/german/', 'en': '/german/en/', 'ja': '/german/ja/'}

T = {
 'ko': dict(name='포켓독일어', badge='웹 체험판',
            intro_h='포켓독일어 웹 체험판', intro_p='A1 단어 845개와 199개 주제의 단어를 무료로 써 볼 수 있어요. A2부터 C2까지 모든 레벨과 미션 기록은 앱에서 열려요.',
            start='체험 시작하기', lock_h='이 레벨은 앱에서 열려요',
            lock_p='A2부터 C2까지 17,780단어 전체, 매일 미션과 복습 기록은 포켓독일어 앱에서 쓸 수 있어요. 웹 체험판에서는 A1 단어와 주제별 단어를 계속 무료로 써 보세요.',
            store='App Store에서 받기', soon='App Store 곧 출시', keep='A1로 계속하기', home='포켓독일어 홈'),
 'en': dict(name='Pocket German', badge='Web version',
            intro_h='Pocket German on the web', intro_p='Try all 845 A1 words and the word lists for 199 topics for free. Every level from A2 to C2 and your mission history open in the app.',
            start='Start', lock_h='This level is in the app',
            lock_p='All 17,780 words from A2 to C2, daily missions and your review history are in the Pocket German app. On the web you can keep using A1 and the topic word lists for free.',
            store='Get it on the App Store', soon='Coming soon to the App Store', keep='Keep going with A1', home='Pocket German home'),
 'ja': dict(name='ポケットドイツ語', badge='ウェブ版',
            intro_h='ポケットドイツ語 ウェブ版', intro_p='A1の845語と199テーマの単語を無料で試せます。A2からC2までのすべてのレベルとミッションの記録はアプリで使えます。',
            start='はじめる', lock_h='このレベルはアプリで使えます',
            lock_p='A2からC2までの17,780語すべて、毎日のミッションと復習の記録はポケットドイツ語アプリで使えます。ウェブ版ではA1とテーマ別単語を引き続き無料で使えます。',
            store='App Storeで入手', soon='App Store 近日公開', keep='A1で続ける', home='ポケットドイツ語ホーム'),
}

TRIAL_CSS = '''<style>
.pglock{position:relative}
.pglock::after{content:"";position:absolute;top:4px;right:4px;width:14px;height:14px;opacity:.75;
 background:no-repeat center/contain url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%235E6878' stroke-width='2.4'%3E%3Crect x='5' y='11' width='14' height='10' rx='2'/%3E%3Cpath d='M8 11V8a4 4 0 0 1 8 0v3'/%3E%3C/svg%3E")}
.pgsheet{position:fixed;inset:0;z-index:400;display:flex;align-items:flex-end;justify-content:center;background:rgba(17,21,28,.55);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);animation:pgIn .18s ease-out}
.pgsheet>div{width:min(100%,520px);background:var(--card,#fff);color:var(--ink,#1B2433);border-radius:24px 24px 0 0;padding:26px 22px calc(22px + env(safe-area-inset-bottom,0px));box-shadow:0 -20px 50px rgba(0,0,0,.25)}
@media (min-width:600px){.pgsheet{align-items:center}.pgsheet>div{border-radius:24px}}
.pgsheet .pgb{display:inline-block;font-size:12.5px;font-weight:700;color:#DD0000;background:rgba(221,0,0,.09);border-radius:999px;padding:2px 10px;margin-bottom:10px}
.pgsheet h2{margin:0 0 8px;font-size:22px;line-height:1.3}
.pgsheet p{margin:0 0 18px;color:var(--muted,#5E6878);font-size:15.5px;line-height:1.6}
.pgsheet .pgbtns{display:grid;gap:8px}
.pgsheet .pgbtns>*{display:flex;align-items:center;justify-content:center;min-height:50px;border-radius:14px;font:inherit;font-weight:700;font-size:16px;text-decoration:none;border:0;cursor:pointer}
.pgsheet .pgstore{background:#151515;color:#fff}.pgsheet .pgstore[aria-disabled]{opacity:.55;cursor:default}
.pgsheet .pgkeep{background:var(--accent,#2D5BD3);color:var(--accent-ink,#fff)}
.pgsheet .pghome{background:transparent;color:var(--muted,#5E6878);min-height:40px!important;font-size:14.5px!important}
@keyframes pgIn{from{opacity:0}to{opacity:1}}
</style>'''

TRIAL_JS = r'''<script>
/* Pocket German web trial: A1 + topic words are free; other levels open a sheet that points to the app */
(function(){
  var FREE=["A1"],T=__T__,STORE=__STORE__,HOME=__HOME__;
  var SEL='[data-lv],[data-lvc],[data-lvsel],[data-qlv],[data-q],[data-pref="mlv"]';
  function val(b){var d=b.dataset;return d.lv||d.lvc||d.lvsel||d.qlv||d.q||(d.pref==="mlv"?d.val:"")||""}
  function locked(b){var v=val(b);if(!v||v==="blog")return false;return v.split(",").some(function(x){return FREE.indexOf(x)<0})}
  function sheet(h,p,first){
    if(document.querySelector(".pgsheet"))return;
    var s=document.createElement("div");s.className="pgsheet";s.setAttribute("role","dialog");s.setAttribute("aria-modal","true");
    var store=STORE?'<a class="pgstore" href="'+STORE+'" rel="noopener">'+T.store+'</a>':'<span class="pgstore" aria-disabled="true">'+T.soon+'</span>';
    s.innerHTML='<div><span class="pgb">'+T.badge+'</span><h2>'+h+'</h2><p>'+p+'</p><div class="pgbtns">'+(first?'<button class="pgkeep" type="button">'+T.start+'</button>'+store:store+'<button class="pgkeep" type="button">'+T.keep+'</button>')+'<a class="pghome" href="'+HOME+'">'+T.home+'</a></div></div>';
    document.body.appendChild(s);
    var close=function(){s.remove()};
    s.addEventListener("click",function(e){if(e.target===s||e.target.closest(".pgkeep"))close()});
    document.addEventListener("keydown",function k(e){if(e.key==="Escape"){close();document.removeEventListener("keydown",k)}});
    var f=s.querySelector(".pgkeep");if(f)f.focus();
  }
  function pay(){sheet(T.lock_h,T.lock_p)}
  document.addEventListener("click",function(e){var b=e.target.closest(SEL);if(b&&locked(b)){e.preventDefault();e.stopImmediatePropagation();pay()}},true);
  function sanitize(){var bad=false;
    try{if(typeof S!=="undefined"&&S&&Array.isArray(S.levels)){var keep=S.levels.filter(function(x){return FREE.indexOf(x)>=0});
      if(keep.length!==S.levels.length){bad=lvMode!=="blog";S.levels=keep.length?keep:["A1"];try{persist()}catch(x){}}}
      if(typeof PREF!=="undefined"&&PREF){if(PREF.mlv&&FREE.indexOf(PREF.mlv)<0)PREF.mlv="A1";
        if(Array.isArray(PREF.qlv)){var q=PREF.qlv.filter(function(x){return FREE.indexOf(x)>=0});PREF.qlv=q.length?q:["A1"]}}}catch(x){}
    if(bad&&armed)setTimeout(pay,300)}
  var armed=false;document.addEventListener("pointerdown",function(){armed=true},{capture:true,once:true});
  if(typeof window.render==="function"){var _r=window.render;window.render=function(){sanitize();return _r.apply(this,arguments)}}
  function lockAll(root){(root||document).querySelectorAll(SEL).forEach(function(b){if(locked(b)){if(!b.classList.contains("pglock")){b.classList.add("pglock");b.setAttribute("aria-description",T.lock_h)}}})}
  new MutationObserver(function(){lockAll()}).observe(document.body,{childList:true,subtree:true});
  sanitize();lockAll();
  /* no intro sheet of our own: the app runs its own first-time onboarding */
})();
</script>'''


def free_ids():
    ids = {w['id'] for w in json.load(open(f'{SRC}/data/A1.json'))}
    for t in json.load(open(f'{SRC}/data/topics.json'))['topics']:
        ids.update(t['ids'])
    return ids


def main():
    if os.path.isdir(OUT):
        for x in os.listdir(OUT):
            if x != 'audio':
                p = f'{OUT}/{x}'; shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    os.makedirs(OUT, exist_ok=True)
    free = free_ids()
    dump = lambda p, o: json.dump(o, open(p, 'w'), ensure_ascii=False, separators=(',', ':'))
    # shared data: topics, Goethe list, pictures only for the free words
    os.makedirs(f'{OUT}/data', exist_ok=True)
    for f in ('topics.json', 'goethe.json'):
        shutil.copy(f'{SRC}/data/{f}', f'{OUT}/data/{f}')
    for f in ('ill', 'ill_B1', 'ill_B2', 'ill_C1', 'ill_C2'):
        j = json.load(open(f'{SRC}/data/{f}.json'))
        m = {k: v for k, v in j['map'].items() if k in free}
        dump(f'{OUT}/data/{f}.json', {'pics': {k: j['pics'][k] for k in set(m.values()) if k in j['pics']}, 'map': m})
    for g, (page, dp) in FILES.items():
        os.makedirs(f'{OUT}/{dp}', exist_ok=True)
        for lv in LVS:
            words = json.load(open(f'{SRC}/{dp}/{lv}.json'))
            dump(f'{OUT}/{dp}/{lv}.json', words if lv == 'A1' else [w for w in words if w['id'] in free])
        shutil.copy(f'{SRC}/{dp}/daily.json', f'{OUT}/{dp}/daily.json')
        hd = 'help2' if g == 'ko' else f'help2_{g}'
        shutil.copytree(f'{SRC}/{hd}', f'{OUT}/{hd}')
        s = open(f'{SRC}/{page}').read()
        s, n = re.subn(r'WEBURL=\{[^}]*\}', 'WEBURL={ko:"/german/web/",en:"/german/web/index_en.html",ja:"/german/web/index_ja.html"}', s)
        assert n == 1, (g, 'WEBURL')
        s, n = re.subn(r'if\(WEB\)\{try\{window\.open\(WEBURL\[L\],"_blank"\)\}catch\(e\)\{\}return\}', 'if(WEB){location.href=WEBURL[L];return}', s)
        assert n == 1, (g, 'lang switch')
        head = (f'<meta name="robots" content="noindex"><link rel="canonical" href="https://pocketkorean.com{HOME[g]}">'
                f'<link rel="icon" href="/german/assets/icon.svg" type="image/svg+xml">')
        s = s.replace('<meta name=viewport', head + '<meta name=viewport', 1)
        s = s.replace('<html>', f'<html lang="{g}">', 1)
        js = TRIAL_JS.replace('__T__', json.dumps(T[g], ensure_ascii=False)).replace('__STORE__', json.dumps(APP_STORE)).replace('__HOME__', json.dumps(HOME[g]))
        i = s.rfind('</body>')
        s = s[:i] + TRIAL_CSS + js + s[i:] if i >= 0 else s + TRIAL_CSS + js
        open(f'{OUT}/{page}', 'w').write(s)
    print('web trial: ok,', len(free), 'free words')


if __name__ == '__main__':
    main()
