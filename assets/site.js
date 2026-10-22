/* pocketkorean.com — small site scripts (no framework) */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var esc = function (s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var U = document.body.getAttribute('data-u') || 'en';
  var AUDIO = 'https://app.pocketkorean.com/audio/';

  /* ---- mega menu ---- */
  var hdr = $('#top'), mb = $('#menubtn');
  if (hdr && mb) {
    var set = function (o) { hdr.classList.toggle('open', o); mb.setAttribute('aria-expanded', o ? 'true' : 'false'); };
    mb.addEventListener('click', function (e) { e.stopPropagation(); set(!hdr.classList.contains('open')); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') set(false); });
    document.addEventListener('click', function (e) { if (hdr.classList.contains('open') && !e.target.closest('#mega')) set(false); });
  }

  /* ---- desktop dropdowns: Escape closes, a click on a link closes ---- */
  var nm = $('nav.main');
  if (nm) {
    var hush = function () { nm.classList.add('hush'); if (document.activeElement && nm.contains(document.activeElement)) document.activeElement.blur(); };
    nm.addEventListener('mouseleave', function () { nm.classList.remove('hush'); });
    [].forEach.call(nm.querySelectorAll('.ni'), function (n) { n.addEventListener('mouseenter', function () { nm.classList.remove('hush'); }); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') hush(); });
  }

  /* ---- audio: plays a slice of an app audio pack (HTTP range request) ---- */
  var ctx = null, cur = null;
  function play(a, which, btn) {  // a = [pack, wordOff, wordLen, exOff, exLen]
    if (!a) return;
    var off = which === 'ex' ? a[3] : a[1], len = which === 'ex' ? a[4] : a[2];
    if (off < 0 || !len) return;
    if (btn) btn.disabled = true;
    fetch((a[0].charAt(0) === '/' ? a[0] : AUDIO + a[0]), { headers: { Range: 'bytes=' + off + '-' + (off + len - 1) } })
      .then(function (r) { if (!r.ok) throw 0; return r.arrayBuffer(); })
      .then(function (buf) {
        if (cur) { try { cur.pause(); } catch (e) {} }
        var url = URL.createObjectURL(new Blob([buf], { type: 'audio/mpeg' }));
        cur = new Audio(url); cur.onended = function () { URL.revokeObjectURL(url); };
        return cur.play();
      })
      .catch(function () {})
      .then(function () { if (btn) btn.disabled = false; });
  }
  var fnv = function (s) { var h = 2166136261; for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; } return h % 256; };
  var wslug = function (de) { return de.replace(/\//g, '-'); };
  var wurl = function (de) { return '/' + U + '/word/' + encodeURIComponent(wslug(de)) + '/'; };
  /* word pages: play buttons carry their audio slice */
  /* ---- listen buttons in articles: native recording (data-pa) or Google TTS via /api/tts (data-t) ---- */
  function speakFallback(t) {
    if (!('speechSynthesis' in window)) return;
    var u = new SpeechSynthesisUtterance(t); u.lang = 'ko-KR'; u.rate = 0.9;
    window.speechSynthesis.cancel(); window.speechSynthesis.speak(u);
  }
  function sayTTS(t, el) {
    if (cur) { try { cur.pause(); } catch (e) {} }
    var done = false, a = new Audio('/api/tts?t=' + encodeURIComponent(t));
    var fail = function () { if (done) return; done = true; el.classList.remove('playing'); speakFallback(t); };
    el.classList.add('playing');
    a.onended = function () { done = true; el.classList.remove('playing'); };
    a.onerror = fail;
    cur = a;
    var p = a.play(); if (p && p.catch) p.catch(fail);
  }
  document.querySelectorAll('[data-t]:not([data-pa])').forEach(function (el) {
    var go = function (e) { e.preventDefault(); sayTTS(el.getAttribute('data-t'), el); };
    el.addEventListener('click', go);
    if (el.tagName !== 'BUTTON') el.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') go(e); });
  });
  document.querySelectorAll('span.say[data-pa]').forEach(function (el) {
    el.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); el.click(); } });
  });
  document.querySelectorAll('[data-pa]').forEach(function (b) { b.addEventListener('click', function () { try { play(JSON.parse(b.getAttribute('data-pa')), b.getAttribute('data-which'), b); } catch (e) {} }); });
  var SPK = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M11 5 6 9H3v6h3l5 4z" fill="currentColor"/><path d="M15.5 8.5a5 5 0 0 1 0 7M18.5 5.5a9 9 0 0 1 0 13"/></svg>';

  var getJSON = (function () { var c = {}; return function (u) { return c[u] || (c[u] = fetch(u).then(function (r) { return r.json(); })); }; })();
  var dayIndex = function (n) { var d = new Date(); return Math.floor((Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()) / 864e5)) % n; };

  /* ---- word of the day ---- */
  var wod = $('#wod');
  if (wod) getJSON(wod.getAttribute('data-src')).then(function (list) {
    var w = list[dayIndex(list.length)], f = function (k) { return wod.querySelector('[data-f="' + k + '"]'); };
    var tip = f('t'); var tb = tip.querySelector('b'); var lab = tb ? tb.outerHTML : '';
    f('de').innerHTML = Array.from(w.de).map(function (ch) { return '<span>' + esc(ch) + '</span>'; }).join(''); f('de').setAttribute('aria-label', w.de); f('rom').textContent = w.rom; f('pos').textContent = w.pos; f('m').textContent = w.m;
    f('ex').textContent = w.ex; f('x').textContent = w.x; tip.innerHTML = lab + ' ' + esc(w.t || w.e);
    f('lv').textContent = 'TOPIK ' + w.lv.slice(1); f('lv').className = 'tag t' + w.lv.slice(1);
    f('link').href = '/' + U + '/dictionary/?q=' + encodeURIComponent(w.de);
    var b = wod.querySelector('[data-play]'); b.onclick = function () { play(w.a, 'w', b); };
  });

  /* ---- mini quiz ---- */
  var qz = $('#quiz');
  if (qz) getJSON(qz.getAttribute('data-src')).then(function (list) {
    var n = dayIndex(list.length) + 1, score = 0, tries = 0;
    var CHK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="m5 12 5 5 9-10"/></svg>';
    var XX = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>';
    function ask() {
      var pick = [], seen = {};
      while (pick.length < 4) { var w = list[(n * 7 + pick.length * 131 + Math.floor(Math.random() * list.length)) % list.length]; if (!seen[w.id] && w.m) { seen[w.id] = 1; pick.push(w); } }
      var ans = pick[0]; pick.sort(function () { return Math.random() - .5; });
      var m = ans.m.split(/[;,]/)[0].trim(), qt = qz.getAttribute('data-q').split('{m}');
      qz.querySelector('.q').innerHTML = esc(qt[0]) + '<mark>' + esc(m) + '</mark>' + esc(qt[1] || '');
      var box = qz.querySelector('.opts'), fb = qz.querySelector('.fb'); fb.innerHTML = ''; qz.classList.remove('done');
      box.innerHTML = pick.map(function (w, i) {
        return '<button type="button" data-id="' + w.id + '"><span class="k">' + 'ABCD'[i] + '</span><span class="w"><b lang="ko">' + esc(w.de) + '</b><small>' + esc(w.rom) + ' · ' + esc(w.m.split(/[;,]/)[0]) + '</small></span><span class="ic"></span></button>';
      }).join('');
      box.onclick = function (e) {
        var b = e.target.closest('button'); if (!b || qz.classList.contains('done')) return; qz.classList.add('done');
        var ok = b.getAttribute('data-id') === ans.id; tries++; if (ok) score++;
        qz.querySelector('.qz-ok').textContent = score; qz.querySelector('.qz-n').textContent = tries;
        [].forEach.call(box.children, function (x) {
          if (x.getAttribute('data-id') === ans.id) { x.classList.add('ok'); x.querySelector('.ic').innerHTML = CHK; }
          else if (x === b) { x.classList.add('no'); x.querySelector('.ic').innerHTML = XX; }
        });
        fb.innerHTML = '<p class="' + (ok ? 'good' : 'bad') + '">' + esc(ok ? qz.getAttribute('data-ok') : qz.getAttribute('data-no').replace('{w}', ans.de)) + '</p>' +
          '<button class="qz-next" type="button">' + esc(qz.getAttribute('data-next')) + ' <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></button>';
        play(ans.a, 'w');
        fb.querySelector('button').onclick = function () { n++; ask(); };
      };
    }
    ask();
  });

  /* ---- dictionary ---- */
  var dict = $('#dict');
  if (dict) {
    var D = function (k) { return dict.getAttribute('data-' + k) || ''; };
    var stat = $('#dstat'), form = $('#dform'), inp = $('#dq'), idx = null;
    var norm = function (s) { return String(s || '').toLowerCase().normalize('NFKD').replace(/[̀-ͯ]/g, '').trim(); };
    function card(w) {
      var parts = (w.parts || []).filter(function (p) { return p[0]; }).map(function (p) { return '<span><b lang="ko">' + esc(p[0]) + '</b>' + (p[1] ? ' ' + esc(p[1]) : '') + '</span>'; }).join('<em aria-hidden="true">+</em>');
      var rel = (w.rel || []).map(function (r) { return '<button type="button" data-q="' + esc(r[0]) + '"><b lang="ko">' + esc(r[0]) + '</b> <span class="muted">' + esc(r[1]) + '</span></button>'; }).join('');
      return '<article class="card"><div class="hd"><div><p style="margin:0 0 6px;display:flex;gap:8px;align-items:center"><span class="tag t' + w.lv.slice(1) + '">TOPIK ' + w.lv.slice(1) + '</span><span class="muted">' + esc(w.pos) + '</span></p>' +
        '<h2 lang="ko"><a href="' + wurl(w.de) + '" style="color:inherit;text-decoration:none">' + esc(w.de) + '</a></h2><p class="muted" style="margin:6px 0 0">' + esc(w.rom) + (w.pr ? ' <span lang="ko">[' + esc(w.pr) + ']</span>' : '') + '</p></div>' +
        (w.a ? '<button class="play" data-w aria-label="' + esc(D('l-listen')) + '">' + SPK + '</button>' : '') + '</div><div class="bd">' +
        '<div>' + (w.forms ? '<p class="muted" lang="ko" style="margin:0 0 2px">' + esc(w.forms) + '</p>' : '') + '<p class="mean">' + esc(w.m) + '</p></div>' +
        (w.ex ? '<div><p style="margin:0 0 8px;display:flex;align-items:center;gap:10px"><span class="hl">' + esc(D('l-ex')) + '</span>' + (w.a && w.a[3] >= 0 ? '<button class="play sm" data-e aria-label="' + esc(D('l-listen')) + '">' + SPK + '</button>' : '') + '</p><p lang="ko" style="margin:0;font-size:21px;font-weight:700">' + esc(w.ex) + '</p><p class="muted" style="margin:2px 0 0;font-size:17px">' + esc(w.x) + '</p></div>' : '') +
        (parts || w.e ? '<div><p style="margin:0 0 10px"><span class="hl">' + esc(D('l-parts')) + '</span></p>' + (parts ? '<div class="parts">' + parts + '</div>' : '') + (w.e ? '<p style="margin:10px 0 0">' + esc(w.e) + '</p>' : '') + '</div>' : '') +
        (w.t ? '<div><p style="margin:0 0 6px"><span class="hl">' + esc(D('l-tip')) + '</span></p><p style="margin:0">' + esc(w.t) + '</p></div>' : '') +
        (rel ? '<div><p style="margin:0 0 10px"><span class="hl">' + esc(D('l-rel')) + '</span></p><div class="rel">' + rel + '</div></div>' : '') +
        '</div></article>';
    }
    function show(id) {
      var lv = idx.byId[id][4];
      var sl = wslug(idx.byId[id][1]);
      getJSON('/data/' + U + '/w/' + ('0' + fnv(sl).toString(16)).slice(-2) + '.json').then(function (b) {
        var w = (b[sl] || []).filter(function (x) { return x.id === id; })[0]; if (!w) return;
        var el = dict.querySelector('.cardslot'); el.innerHTML = card(w);
        var bw = el.querySelector('[data-w]'), be = el.querySelector('[data-e]');
        if (bw) bw.onclick = function () { play(w.a, 'w', bw); };
        if (be) be.onclick = function () { play(w.a, 'ex', be); };
        el.querySelectorAll('.rel button').forEach(function (b) { b.onclick = function () { inp.value = b.getAttribute('data-q'); run(true); }; });
        dict.querySelectorAll('.dlist button').forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-id') === id); });
      });
    }
    function search(q) {
      var nq = norm(q), hangul = /[가-힣ㄱ-ㆎ]/.test(q), res = [];
      if (!nq) return res;
      idx.list.forEach(function (r) {
        var s = 0;
        if (hangul) { if (r[1] === q) s = 100; else if (r[1].indexOf(q) === 0) s = 60; else if (r[1].indexOf(q) >= 0) s = 30; }
        else {
          var m = r.nm; if (!m) return;
          var parts = m.split(/[;,/()]+/).map(function (x) { return x.replace(/^(to|a|an|the)\s+/, '').trim(); });
          if (parts.indexOf(nq) >= 0) s = 90; else if (m.indexOf(nq) === 0) s = 60;
          else if ((' ' + m + ' ').indexOf(' ' + nq) >= 0) s = 40; else if (m.indexOf(nq) >= 0) s = 20;
          if (!s && norm(r[2]).replace(/[^a-z]/g, '') === nq.replace(/[^a-z]/g, '')) s = 80;
        }
        if (s) res.push([s - (+r[4]) * 2, r]);
      });
      res.sort(function (a, b) { return b[0] - a[0]; });
      return res.slice(0, 30).map(function (x) { return x[1]; });
    }
    function run(push) {
      var q = inp.value.trim(); if (!q) return;
      if (push) history.replaceState(null, '', '?q=' + encodeURIComponent(q));
      var go = function () {
        var r = search(q);
        if (!r.length) { stat.textContent = D('none'); dict.innerHTML = '<div class="empty">' + esc(D('none')) + '</div>'; return; }
        stat.textContent = D('found').replace('{n}', r.length);
        dict.innerHTML = '<div class="cardslot"></div>' + (r.length > 1 ? '<div class="dlist">' + r.map(function (x) {
          return '<button type="button" data-id="' + x[0] + '"><span><b lang="ko">' + esc(x[1]) + '</b> <span class="muted">— ' + esc(x[3]) + '</span></span><span class="tag t' + x[4] + '">' + x[4] + '</span></button>';
        }).join('') + '</div>' : '');
        dict.querySelectorAll('.dlist button').forEach(function (b) { b.onclick = function () { show(b.getAttribute('data-id')); window.scrollTo({ top: dict.offsetTop - 90, behavior: 'smooth' }); }; });
        show(r[0][0]);
      };
      if (idx) go();
      else { stat.textContent = D('loading'); getJSON('/data/' + U + '/dict.json').then(function (list) { idx = { list: list, byId: {} }; list.forEach(function (r) { r.nm = norm(r[3]); idx.byId[r[0]] = r; }); go(); }); }
    }
    form.addEventListener('submit', function (e) { e.preventDefault(); run(true); });
    var q0 = new URLSearchParams(location.search).get('q'); if (q0) { inp.value = q0; run(false); }
  }

  /* ---- i18n helper (strings embedded in the page) ---- */
  var I = {}; try { I = JSON.parse(($('#i18n') || {}).textContent || '{}'); } catch (e) {}
  var t = function (k, v) { var s = I[k] || k; if (v) Object.keys(v).forEach(function (x) { s = s.split('{' + x + '}').join(v[x]); }); return s; };

  /* ---- hangul helpers ---- */
  var CHO = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ', JUNG = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ',
      JONG = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'];
  var RC = { 'ㄱ': 'g', 'ㄲ': 'kk', 'ㄴ': 'n', 'ㄷ': 'd', 'ㄸ': 'tt', 'ㄹ': 'r', 'ㅁ': 'm', 'ㅂ': 'b', 'ㅃ': 'pp', 'ㅅ': 's', 'ㅆ': 'ss', 'ㅇ': '', 'ㅈ': 'j', 'ㅉ': 'jj', 'ㅊ': 'ch', 'ㅋ': 'k', 'ㅌ': 't', 'ㅍ': 'p', 'ㅎ': 'h' };
  var RV = { 'ㅏ': 'a', 'ㅐ': 'ae', 'ㅑ': 'ya', 'ㅒ': 'yae', 'ㅓ': 'eo', 'ㅔ': 'e', 'ㅕ': 'yeo', 'ㅖ': 'ye', 'ㅗ': 'o', 'ㅘ': 'wa', 'ㅙ': 'wae', 'ㅚ': 'oe', 'ㅛ': 'yo', 'ㅜ': 'u', 'ㅝ': 'wo', 'ㅞ': 'we', 'ㅟ': 'wi', 'ㅠ': 'yu', 'ㅡ': 'eu', 'ㅢ': 'ui', 'ㅣ': 'i' };
  var RF = { '': '', 'ㄱ': 'k', 'ㄴ': 'n', 'ㄷ': 't', 'ㄹ': 'l', 'ㅁ': 'm', 'ㅂ': 'p', 'ㅅ': 't', 'ㅇ': 'ng', 'ㅈ': 't', 'ㅊ': 't', 'ㅋ': 'k', 'ㅌ': 't', 'ㅍ': 'p', 'ㅎ': 't', 'ㄲ': 'k', 'ㅆ': 't' };
  function dec(ch) { var o = ch.charCodeAt(0) - 0xac00; if (o < 0 || o > 11171) return null; return [CHO[Math.floor(o / 588)], JUNG[Math.floor((o % 588) / 28)], JONG[o % 28]]; }
  function com(c, v, f) { return String.fromCharCode(0xac00 + CHO.indexOf(c) * 588 + JUNG.indexOf(v) * 28 + JONG.indexOf(f || '')); }
  function romSyl(ch) { var d = dec(ch); return d ? (RC[d[0]] + RV[d[1]] + (RF[d[2]] || '')) : ch; }
  function sayKo(text) {
    try { var u = new SpeechSynthesisUtterance(text); u.lang = 'ko-KR'; u.rate = .85; var v = speechSynthesis.getVoices().filter(function (x) { return /^ko/i.test(x.lang); })[0]; if (v) u.voice = v; speechSynthesis.cancel(); speechSynthesis.speak(u); } catch (e) {}
  }

  /* ---- approximate transliteration for names not in the list ---- */
  function translit(name) {
    var s = name.toLowerCase().normalize('NFKD').replace(/[̀-ͯ]/g, '').replace(/[^a-z]/g, '');
    if (!s) return '';
    s = s.replace(/e$/, function () { return s.length > 3 ? '' : 'e'; }).replace(/^chr/, 'kr').replace(/ch(?=[lrnm])/g, 'k').replace(/(er|or|ar)$/, function (m) { return m === 'ar' ? 'a' : 'O'; }).replace(/er(?=[^aeiou])/g, 'O');
    var R = [['sch', 'S'], ['tch', 'C'], ['sh', 'S'], ['ch', 'C'], ['th', 's'], ['ph', 'f'], ['ck', 'k'], ['qu', 'kw'], ['ng', 'N'], ['ee', 'i'], ['ea', 'i'], ['oo', 'u'], ['ou', 'au'], ['ai', 'ei'], ['ay', 'ei'], ['ey', 'ei'], ['ie', 'i'], ['x', 'ks'], ['j', 'J'], ['wh', 'w'], ['gh', 'g']];
    R.forEach(function (r) { s = s.split(r[0]).join(r[1]); });
    s = s.replace(/c(?=[eiy])/g, 's').replace(/c/g, 'k').replace(/y(?=[aeiou])/g, 'Y').replace(/y/g, 'i').replace(/w(?=[aeiou])/g, 'W').replace(/w/g, 'u');
    var V = { a: 'ㅏ', e: 'ㅔ', i: 'ㅣ', o: 'ㅗ', u: 'ㅜ', O: 'ㅓ' }, YV = { a: 'ㅑ', e: 'ㅖ', i: 'ㅣ', o: 'ㅛ', u: 'ㅠ', O: 'ㅕ' }, WV = { a: 'ㅘ', e: 'ㅞ', i: 'ㅟ', o: 'ㅝ', u: 'ㅜ', O: 'ㅝ' };
    var C = { b: 'ㅂ', d: 'ㄷ', f: 'ㅍ', g: 'ㄱ', h: 'ㅎ', J: 'ㅈ', k: 'ㅋ', l: 'ㄹ', m: 'ㅁ', n: 'ㄴ', p: 'ㅍ', r: 'ㄹ', s: 'ㅅ', t: 'ㅌ', v: 'ㅂ', z: 'ㅈ', S: 'ㅅ', C: 'ㅊ', N: 'ㅇ' };
    var FIN = { n: 'ㄴ', m: 'ㅁ', N: 'ㅇ', l: 'ㄹ', k: 'ㄱ', p: 'ㅂ', t: 'ㅅ' };
    var out = [], i = 0;
    while (i < s.length) {
      var ch = s[i], nx = s[i + 1];
      if (V[ch]) { out.push([ 'ㅇ', V[ch], '' ]); i++; continue; }
      if (ch === 'Y' || ch === 'W') { var vv = nx && V[nx] ? (ch === 'Y' ? YV : WV)[nx] : 'ㅣ'; out.push(['ㅇ', vv, '']); i += nx && V[nx] ? 2 : 1; continue; }
      var c = C[ch] || 'ㅇ';
      if (nx && V[nx]) { var v = V[nx]; if (ch === 'S') v = { a: 'ㅑ', e: 'ㅖ', i: 'ㅣ', o: 'ㅛ', u: 'ㅠ' }[nx]; if (ch === 'h' && out.length && !out[out.length - 1][2] && false) {} out.push([c, v, '']); i += 2; continue; }
      if (nx && (nx === 'Y' || nx === 'W') && s[i + 2] && V[s[i + 2]]) { out.push([c, (nx === 'Y' ? YV : WV)[s[i + 2]], '']); i += 3; continue; }
      // consonant without a following vowel: batchim or extra ㅡ
      var last = out[out.length - 1];
      if (ch === 'r' && last && !last[2]) { i++; continue; }  // r after a vowel is mostly silent (English-style)
      if (ch === 'h') { i++; continue; }
      if (last && !last[2] && FIN[ch] && !(nx && C[nx] && ch === 't')) { last[2] = FIN[ch]; if (ch === 'l' && nx && V[s[i + 1]]) {} i++; continue; }
      if (ch === 'l') { if (last && !last[2]) last[2] = 'ㄹ'; out.push(['ㄹ', 'ㅡ', '']); i++; continue; }
      out.push([c, ch === 'S' || ch === 'C' || ch === 'J' ? 'ㅣ' : 'ㅡ', '']); i++;
    }
    return out.map(function (x) { return com(x[0], x[1], x[2]); }).join('');
  }

  /* ---- name maker ---- */
  var nres = $('#nres');
  if (nres) {
    var nform = $('#nform'), nin = $('#nm'), nlang = $('#nl'), nmsg = $('#nmsg'), mode = 'w', G = '', VB = '';
    var NAMES = null, getNames = function () { return NAMES ? Promise.resolve(NAMES) : getJSON('/data/names.json').then(function (d) { NAMES = d; return d; }); };
    var dictIdx = null, getDict = function () { return dictIdx ? Promise.resolve(dictIdx) : getJSON('/data/' + U + '/dict.json').then(function (l) { dictIdx = {}; l.forEach(function (r) { if (!dictIdx[r[1]]) dictIdx[r[1]] = r[3]; }); return dictIdx; }); };
    var normN = function (s) { return String(s || '').toLowerCase().normalize('NFKD').replace(/[̀-ͯ]/g, '').replace(/[^a-z]/g, ''); };
    document.querySelectorAll('.tabs [data-mode]').forEach(function (b) { b.addEventListener('click', function () { mode = b.getAttribute('data-mode'); $('#kopts').hidden = mode !== 'k'; if (nin.value.trim()) go(); }); });
    document.querySelectorAll('#kopts [data-g],#kopts [data-v]').forEach(function (b) {
      b.addEventListener('click', function () {
        var k = b.hasAttribute('data-g') ? 'data-g' : 'data-v';
        document.querySelectorAll('#kopts [' + k + ']').forEach(function (x) { x.classList.toggle('on', x === b); });
        if (k === 'data-g') G = b.getAttribute('data-g'); else VB = b.getAttribute('data-v');
        if (nin.value.trim()) go();
      });
    });
    function find(d, name, lang) {
      var n = normN(name), hits = d.names.filter(function (x) { return normN(x.n) === n; });
      if (!hits.length) return null;
      return hits.filter(function (x) { return (x.from || []).indexOf(lang) >= 0; })[0] || hits[0];
    }
    function alikeScan(d, ko, own) {
      var res = (own || []).slice(), seen = {};
      res.forEach(function (a) { seen[a.ko] = 1; });
      d.alike.forEach(function (a) { if (!seen[a.ko] && ko.indexOf(a.ko) >= 0) { res.push(a); seen[a.ko] = 1; } });
      return res;
    }
    function suggest(d, ko) {
      var f = dec(ko[0]), cho = f ? f[0] : 'ㅇ';
      var pool = d.korean.filter(function (k) { var x = dec(k.ko[0]); return x && x[0] === cho && (!G || k.g === G || k.g === 'u') && (!VB || (k.vibe || []).indexOf(VB) >= 0); });
      if (pool.length < 3) pool = pool.concat(d.korean.filter(function (k) { var x = dec(k.ko[0]); return x && x[0] === cho && pool.indexOf(k) < 0; }));
      if (pool.length < 3) pool = pool.concat(d.korean.filter(function (k) { return (!G || k.g === G || k.g === 'u') && pool.indexOf(k) < 0; }));
      var seed = 0; for (var i = 0; i < ko.length; i++) seed += ko.charCodeAt(i);
      return pool.slice(seed % Math.max(1, pool.length - 2)).concat(pool).slice(0, 3);
    }
    function nameCard(ko, sub) {
      var c = document.createElement('canvas'); c.width = 1080; c.height = 1350; var x = c.getContext('2d');
      x.fillStyle = '#2D4BFF'; x.fillRect(0, 0, 1080, 1350);
      x.fillStyle = '#FFD43B'; x.font = '800 44px "Bricolage Grotesque", sans-serif'; x.fillText(t('name_card_k'), 90, 150);
      x.fillStyle = '#fff'; var fs = Math.min(260, Math.floor(900 / Math.max(1, ko.length)));
      x.font = '900 ' + fs + 'px "Noto Sans KR", sans-serif'; x.fillText(ko, 80, 760);
      x.fillStyle = '#DCE2FF'; x.font = '500 52px "Bricolage Grotesque", sans-serif'; x.fillText(sub, 90, 860);
      x.font = '600 40px "Bricolage Grotesque", sans-serif'; x.fillText('pocketkorean.com/name', 90, 1250);
      return c;
    }
    function render(name, e, approx, d) {
      var ko = e ? e.ko : translit(name), sy = ko.split('');
      if (!ko) { nmsg.textContent = t('name_enter'); return; }
      var rom = e && e.rom ? e.rom : sy.map(romSyl).join('-');
      var needEu = sy.some(function (c, i) { var x = dec(c); return x && (x[1] === 'ㅡ' || (x[1] === 'ㅣ' && i === sy.length - 1)) && !x[2]; });
      var al = alikeScan(d, ko, e && e.alike);
      var lv = al.some(function (a) { return a.lv === 'caution'; }) ? 'caution' : al.some(function (a) { return a.lv === 'mild'; }) ? 'mild' : 'ok';
      var lvc = { ok: ['#E8FBF2', '#0B6B43'], mild: ['#FFF8E1', '#8A5E00'], caution: ['#FFE6E6', '#B42323'] }[lv];
      var last = dec(ko[ko.length - 1]), cop = last && last[2] ? '이에요' : '예요';
      var syl = sy.map(function (c) {
        var x = dec(c); if (!x) return '';
        var j = x[0] + ' + ' + x[1] + (x[2] ? ' + ' + x[2] : '');
        return '<div style="border:1.5px solid var(--line);border-radius:18px;padding:16px;text-align:center"><p lang="ko" style="margin:0;font-size:48px;font-weight:900;line-height:1.1">' + esc(c) + '</p>' +
          '<p lang="ko" style="margin:6px 0 0;font-size:18px;color:var(--blue);font-weight:700">' + esc(j) + '</p><p class="muted" style="margin:2px 0 0;font-size:14px">' +
          esc(romSyl(c)) + (x[0] === 'ㅇ' ? ' · ' + esc(t('name_silent')) : '') + '</p></div>';
      }).join('');
      var tags = (e && e.tags || []).map(function (g) { return '<span class="chip" style="background:var(--blue-l);border-color:transparent;color:var(--blue-t)">' + esc(t('tag_' + g)) + '</span>'; }).join('');
      var alts = (e && e.alt || []).map(function (a) { return '<span class="chip"><b lang="ko">' + esc(a) + '</b></span>'; }).join('');
      var sug = suggest(d, ko).map(function (k) {
        return '<div class="box" style="padding:16px 18px"><p style="margin:0;display:flex;align-items:baseline;gap:10px;flex-wrap:wrap"><b lang="ko" style="font-size:30px">' + esc(k.ko) + '</b><span class="muted">' + esc(k.rom) + '</span>' +
          (k.hj ? '<span lang="zh-Hant" style="margin-left:auto;font-size:18px" class="muted">' + esc(k.hj) + '</span>' : '') + '</p><p style="margin:4px 0 0;font-size:15px">' + esc(k.mean) + '</p></div>';
      }).join('');
      var head = mode === 'k' ? '' : '';
      nres.innerHTML =
        '<article class="card" style="margin-bottom:24px"><div class="hd" style="background:var(--blue);color:#fff;border:0;align-items:center">' +
        '<div><p style="margin:0 0 4px;color:#DCE2FF">' + esc(t('name_result_t', { name: name })) + '</p><h2 lang="ko" style="color:#fff;font-size:clamp(56px,9vw,84px)">' + esc(ko) + '</h2>' +
        '<p style="margin:10px 0 0;color:#DCE2FF;font-size:18px">' + esc(rom) + ' · ' + esc(t('name_syll', { n: sy.length })) + '</p></div>' +
        '<div style="display:flex;flex-direction:column;gap:10px"><button class="btn yellow" id="nsay">' + SPK + ' ' + esc(t('name_hear')) + '</button>' +
        '<button class="btn ghost" id="ndl" style="background:transparent;color:#fff;border-color:#fff">' + esc(t('name_download')) + '</button><button class="btn ghost" id="ncp" style="background:transparent;color:#fff;border-color:#fff">' + esc(t('name_copy')) + '</button></div></div>' +
        '<div class="bd">' + (approx ? '<p class="box yellow" style="margin:0">' + esc(t('name_approx')) + '</p>' : '') +
        '<div><p style="margin:0 0 12px"><span class="hl">' + esc(I.name_sec1 || '') + '</span></p><div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px">' + syl + '</div>' +
        (needEu ? '<p class="muted" style="margin:10px 0 0">' + esc(t('name_why_eu')) + '</p>' : '') + '</div>' +
        (alts ? '<div><p style="margin:0 0 10px"><span class="hl">' + esc(t('name_alt')) + '</span></p><div class="chips" style="margin:0"><span class="chip on"><b lang="ko">' + esc(ko) + '</b>&nbsp;' + esc(t('name_std')) + '</span>' + alts + '</div></div>' : '') +
        (tags ? '<div><p style="margin:0 0 10px"><span class="hl">' + esc(I.name_sec3 || '') + '</span></p><div class="chips" style="margin:0">' + tags + '</div></div>' : '') +
        '<div style="border-radius:20px;background:' + lvc[0] + ';padding:18px 20px"><p style="margin:0 0 8px;font-weight:800;color:' + lvc[1] + '">' + esc(I.name_sec4 || '') + ': ' + esc(t('name_lv_' + lv)) + '</p>' +
        '<p style="margin:0 0 6px">' + esc(t('name_' + lv)) + '</p><ul id="nal" style="margin:0;padding-left:18px">' + al.map(function (a) { return '<li><b lang="ko">' + esc(a.ko) + '</b> — <span data-ko="' + esc(a.ko) + '">' + esc(a.en) + '</span></li>'; }).join('') + '</ul></div>' +
        '<div><p style="margin:0 0 6px"><span class="hl">' + esc(I.name_intro || '') + '</span></p><p lang="ko" style="margin:0;font-size:24px;font-weight:700">제 이름은 ' + esc(ko) + cop + '.</p>' +
        '<p class="muted" style="margin:2px 0 6px">' + esc(t('name_my', { name: name })) + '</p><p class="muted" style="margin:0;font-size:15px">' + esc(t('name_intro_rule')) + '</p></div>' +
        '</div></article>' +
        '<h2 style="font-size:26px">' + esc(t('name_suggest_h')) + '</h2>' + (mode === 'k' ? '' : '<p class="muted">' + esc(t('name_k_p')) + '</p>') +
        '<div class="grid" style="margin-top:12px">' + sug + '</div>';
      $('#nsay').onclick = function () { sayKo(ko); };
      $('#ndl').onclick = function () { var c = nameCard(ko, name + ' · ' + rom); var a = document.createElement('a'); a.download = 'my-korean-name-' + normN(name) + '.png'; a.href = c.toDataURL('image/png'); a.click(); };
      $('#ncp').onclick = function () {
        var u = nres.getAttribute('data-n') ? location.origin + location.pathname : location.origin + location.pathname + '?n=' + encodeURIComponent(name);
        if (navigator.share && matchMedia('(max-width: 900px)').matches) { navigator.share({ title: name + ' = ' + ko, text: name + ' → ' + ko + ' (' + rom + ')', url: u }).catch(function () {}); return; }
        (navigator.clipboard ? navigator.clipboard.writeText(u) : Promise.reject()).then(function () { nmsg.textContent = t('name_copied'); }).catch(function () { nmsg.textContent = u; });
      };
      if (al.length) getDict().then(function (dx) { document.querySelectorAll('#nal [data-ko]').forEach(function (s) { var m = dx[s.getAttribute('data-ko')]; if (m) s.textContent = m; }); });
      if (mode === 'k') nres.insertBefore(nres.querySelector('h2'), nres.firstChild), nres.insertBefore(nres.querySelector('.grid'), nres.children[1]);
    }
    function go() {
      var name = nin.value.trim(); if (!name) { nmsg.textContent = t('name_enter'); return; }
      nmsg.textContent = ''; if (!nres.getAttribute('data-n')) history.replaceState(null, '', '?n=' + encodeURIComponent(name));
      getNames().then(function (d) { var e = find(d, name, nlang.value); render(name.charAt(0).toUpperCase() + name.slice(1), e, !e, d); });
    }
    nform.addEventListener('submit', function (e) { e.preventDefault(); go(); });
    var n0 = new URLSearchParams(location.search).get('n') || nres.getAttribute('data-n'); if (n0) { nin.value = n0; go(); }
  }

  /* ---- level test ---- */
  var lt = $('#lt');
  if (lt) {
    var steps = document.querySelectorAll('#ltsteps .step');
    var stepOn = function (k) { steps.forEach(function (s, i) { s.classList.toggle('on', i === k); }); };
    var LV = null, counts = {}, cum = {};
    var load = function () { return LV ? Promise.resolve() : getJSON('/data/' + U + '/dict.json').then(function (l) { LV = { 1: [], 2: [], 3: [], 4: [], 5: [], 6: [] }; l.forEach(function (r) { if (r[3]) LV[r[4]].push(r); }); var c = 0; for (var k = 1; k <= 6; k++) { counts[k] = LV[k].length; c += LV[k].length; cum[k] = c; } cum[0] = 0; }); };
    var rnd = function (a) { return a[Math.floor(Math.random() * a.length)]; };
    var gl = function (m) { return String(m).split(/[;,]/)[0].trim(); };
    var level = 1, inLevel = 0, okInLevel = 0, passed = 0, qn = 0, MAXQ = 18, PER = 3;
    function finish() { goal(passed); }
    function ask() {
      if (qn >= MAXQ || level > 6) return finish();
      qn++; var pool = LV[level], ans = rnd(pool), opts = [ans], seen = {}; seen[gl(ans[3])] = 1;
      while (opts.length < 4) { var o = rnd(pool); if (!seen[gl(o[3])]) { seen[gl(o[3])] = 1; opts.push(o); } }
      opts.sort(function () { return Math.random() - .5; });
      lt.innerHTML = '<div class="box" style="max-width:640px;margin:0 auto;padding:28px"><div style="display:flex;justify-content:space-between;font-size:14px" class="muted"><span>' + esc(t('lt_prog', { n: qn, t: MAXQ })) + '</span><span>TOPIK ' + level + '</span></div>' +
        '<div role="progressbar" aria-valuenow="' + qn + '" aria-valuemin="0" aria-valuemax="' + MAXQ + '" style="height:8px;border-radius:999px;background:var(--blue-l);overflow:hidden;margin:8px 0 22px"><div style="width:' + Math.round(qn / MAXQ * 100) + '%;height:100%;background:var(--blue)"></div></div>' +
        '<p class="muted" style="margin:0 0 6px">' + esc(t('lt_q')) + '</p><p lang="ko" style="margin:0 0 20px;font-size:48px;font-weight:900;line-height:1.15">' + esc(ans[1]) + '</p>' +
        '<div style="display:flex;flex-direction:column;gap:10px">' + opts.map(function (o) { return '<button class="btn ghost" style="justify-content:flex-start;min-height:54px" data-id="' + o[0] + '">' + esc(gl(o[3])) + '</button>'; }).join('') +
        '<button class="btn ghost" style="justify-content:flex-start;min-height:54px;color:var(--muted)" data-id="">' + esc(t('lt_idk')) + '</button></div></div>';
      lt.querySelectorAll('button[data-id]').forEach(function (b) {
        b.onclick = function () {
          var ok = b.getAttribute('data-id') === ans[0]; inLevel++; if (ok) okInLevel++;
          if (inLevel >= PER) { if (okInLevel >= 2) { passed = level; level++; inLevel = 0; okInLevel = 0; } else return finish(); }
          ask();
        };
      });
    }
    function goal(p) {
      stepOn(1);
      var known = p ? cum[p] : 0, tgt = Math.min(6, Math.max(p + 1, 3)), mon = 6, why = 'topik';
      var lvLabel = function (n) { return n ? 'TOPIK ' + n : t('lt_beginner'); };
      var draw = function () {
        var target = Math.max(1, tgt), need = cum[target] - known, days = mon * 30, per = need > 0 ? Math.ceil(need / days) : 0, mins = Math.max(10, Math.round((per * 0.8 + 5) / 5) * 5);
        var dur = { 3: t('lt_m3'), 6: t('lt_m6'), 12: t('lt_y1'), 24: t('lt_y2') }[mon];
        var chip = function (attr, val, cur, label) { return '<button type="button" class="chip' + (String(val) === String(cur) ? ' on' : '') + '" data-' + attr + '="' + val + '">' + esc(label) + '</button>'; };
        lt.innerHTML = '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px">' +
          '<div class="box" style="padding:28px"><span class="kicker">' + esc(t('lt_result')) + '</span><p style="margin:0;font-size:40px;font-weight:800;line-height:1.1">' + esc(lvLabel(p)) + '</p>' +
          '<p class="muted" style="margin:6px 0 22px">' + esc(t('lt_known', { n: known.toLocaleString() })) + '</p>' +
          '<p style="font-weight:800;margin:0 0 8px">' + esc(t('lt_goal_q')) + '</p><div class="chips" style="margin:0 0 18px">' +
          ['topik', 'drama', 'travel', 'live'].map(function (g) { return chip('why', g, why, t('goal_' + g)); }).join('') + '</div>' +
          '<p style="font-weight:800;margin:0 0 8px">' + esc(t('lt_target')) + '</p><div class="chips" style="margin:0 0 18px">' +
          [1, 2, 3, 4, 5, 6].filter(function (n) { return n > p || n === 6; }).map(function (n) { return chip('tgt', n, tgt, 'TOPIK ' + n); }).join('') + '</div>' +
          '<p style="font-weight:800;margin:0 0 8px">' + esc(t('lt_when')) + '</p><div class="chips" style="margin:0">' +
          [[3, 'lt_m3'], [6, 'lt_m6'], [12, 'lt_y1'], [24, 'lt_y2']].map(function (m) { return chip('mon', m[0], mon, t(m[1])); }).join('') + '</div></div>' +
          '<div class="step on" style="padding:28px"><span class="kicker">' + esc(I.lt_s3 || '') + '</span>' +
          (need > 0 ? '<p style="margin:0 0 4px;color:#DCE2FF">' + esc(t('lt_plan', { lv: target, t: dur })) + '</p><div style="background:#fff;color:var(--ink);border-radius:22px;padding:22px;margin:8px 0 16px">' +
            '<p style="margin:0;font-size:56px;font-weight:800;line-height:1;color:var(--blue)">' + per + ' <span style="font-size:22px;color:var(--ink)">' + esc(t('lt_perday')) + '</span></p><p class="muted" style="margin:10px 0 0">' + esc(t('lt_minutes', { n: mins })) + '</p></div>' +
            '<ul style="margin:0 0 22px;padding-left:20px"><li>' + esc(t('lt_r1', { n: per })) + '</li><li>' + esc(t('lt_r2')) + '</li><li>' + esc(t('lt_r3')) + '</li></ul>'
            : '<p style="font-size:20px">' + esc(t('lt_there')) + '</p>') +
          '<a class="btn yellow" href="' + lt.getAttribute('data-app') + '">' + esc(t('lt_start_plan')) + '</a> <button class="btn ghost" id="ltre" style="margin-top:10px">' + esc(t('lt_again')) + '</button></div></div>';
        stepOn(2);
        lt.querySelectorAll('[data-why]').forEach(function (b) { b.onclick = function () { why = b.getAttribute('data-why'); draw(); }; });
        lt.querySelectorAll('[data-tgt]').forEach(function (b) { b.onclick = function () { tgt = +b.getAttribute('data-tgt'); draw(); }; });
        lt.querySelectorAll('[data-mon]').forEach(function (b) { b.onclick = function () { mon = +b.getAttribute('data-mon'); draw(); }; });
        $('#ltre').onclick = function () { level = 1; inLevel = 0; okInLevel = 0; passed = 0; qn = 0; stepOn(0); ask(); };
      };
      draw();
    }
    $('#ltgo').onclick = function () { load().then(ask); };
    $('#ltskip').onclick = function () { load().then(function () { goal(0); }); };
  }

  /* ---- placeholders for features that open later ---- */
  [['#newsform', null]].forEach(function (p) {
    var f = $(p[0]); if (!f) return;
    f.addEventListener('submit', function (e) { e.preventDefault(); var m = f.getAttribute('data-msg'); if (p[1]) $(p[1]).textContent = m; else { f.innerHTML = '<p style="margin:0;font-weight:700">' + esc(m) + '</p>'; } });
  });
  document.querySelectorAll('.tabs [role=tab]').forEach(function (tb, i, all) { tb.addEventListener('click', function () { all.forEach(function (x) { x.setAttribute('aria-selected', x === tb ? 'true' : 'false'); }); }); });
  /* keep the main menu on one line: if it would wrap, make every item a little smaller, step by step */
  (function () {
    var n = $('nav.main'); if (!n) return;
    var rows = function () { var t = {}; for (var i = 0; i < n.children.length; i++) t[n.children[i].offsetTop] = 1; return Object.keys(t).length; };
    var fit = function () { if (!n.offsetParent) return; n.classList.remove('t1', 't2', 't3'); ['t1', 't2', 't3'].forEach(function (c) { if (rows() > 1) n.classList.add(c); }); };
    fit(); if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
    var tm; window.addEventListener('resize', function () { clearTimeout(tm); tm = setTimeout(fit, 120); });
  })();
})();
