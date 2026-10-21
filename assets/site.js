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

  /* ---- audio: plays a slice of an app audio pack (HTTP range request) ---- */
  var ctx = null, cur = null;
  function play(a, which, btn) {  // a = [pack, wordOff, wordLen, exOff, exLen]
    if (!a) return;
    var off = which === 'ex' ? a[3] : a[1], len = which === 'ex' ? a[4] : a[2];
    if (off < 0 || !len) return;
    if (btn) btn.disabled = true;
    fetch(AUDIO + a[0], { headers: { Range: 'bytes=' + off + '-' + (off + len - 1) } })
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
  var SPK = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M11 5 6 9H3v6h3l5 4z" fill="currentColor"/><path d="M15.5 8.5a5 5 0 0 1 0 7M18.5 5.5a9 9 0 0 1 0 13"/></svg>';

  var getJSON = (function () { var c = {}; return function (u) { return c[u] || (c[u] = fetch(u).then(function (r) { return r.json(); })); }; })();
  var dayIndex = function (n) { var d = new Date(); return Math.floor((Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()) / 864e5)) % n; };

  /* ---- word of the day ---- */
  var wod = $('#wod');
  if (wod) getJSON(wod.getAttribute('data-src')).then(function (list) {
    var w = list[dayIndex(list.length)], f = function (k) { return wod.querySelector('[data-f="' + k + '"]'); };
    var tip = f('t'); var tb = tip.querySelector('b'); var lab = tb ? tb.outerHTML : '';
    f('de').textContent = w.de; f('rom').textContent = w.rom + ' · ' + w.pos; f('m').textContent = w.m;
    f('ex').textContent = w.ex; f('x').textContent = w.x; tip.innerHTML = lab + ' ' + esc(w.t || w.e);
    f('lv').textContent = 'TOPIK ' + w.lv.slice(1); f('lv').className = 'tag t' + w.lv.slice(1);
    f('link').href = '/' + U + '/dictionary/?q=' + encodeURIComponent(w.de);
    var b = wod.querySelector('[data-play]'); b.onclick = function () { play(w.a, 'w', b); };
  });

  /* ---- mini quiz ---- */
  var qz = $('#quiz');
  if (qz) getJSON(qz.getAttribute('data-src')).then(function (list) {
    var n = dayIndex(list.length) + 1;
    function ask() {
      var pick = [], seen = {};
      while (pick.length < 4) { var w = list[(n * 7 + pick.length * 131 + Math.floor(Math.random() * list.length)) % list.length]; if (!seen[w.id] && w.m) { seen[w.id] = 1; pick.push(w); } }
      var ans = pick[0]; pick.sort(function () { return Math.random() - .5; });
      qz.querySelector('.q').textContent = qz.getAttribute('data-q').replace('{m}', ans.m.split(/[;,]/)[0]);
      var box = qz.querySelector('.opts'), fb = qz.querySelector('.fb'); fb.textContent = '';
      box.innerHTML = pick.map(function (w) { return '<button lang="ko" data-id="' + w.id + '">' + esc(w.de) + '</button>'; }).join('');
      box.onclick = function (e) {
        var b = e.target.closest('button'); if (!b || box.dataset.done) return; box.dataset.done = 1;
        var ok = b.getAttribute('data-id') === ans.id;
        [].forEach.call(box.children, function (x) { if (x.getAttribute('data-id') === ans.id) x.classList.add('ok'); else if (x === b) x.classList.add('no'); });
        fb.innerHTML = esc(ok ? qz.getAttribute('data-ok') : qz.getAttribute('data-no').replace('{w}', ans.de)) +
          ' <button class="btn sm dark" style="margin-left:8px" type="button">' + esc(qz.getAttribute('data-next')) + '</button>';
        play(ans.a, 'w');
        fb.querySelector('button').onclick = function () { n++; delete box.dataset.done; ask(); };
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
        '<h2 lang="ko">' + esc(w.de) + '</h2><p class="muted" style="margin:6px 0 0">' + esc(w.rom) + (w.pr ? ' · <span lang="ko">[' + esc(w.pr) + ']</span>' : '') + '</p></div>' +
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
      getJSON('/data/' + U + '/T' + lv + '.json').then(function (det) {
        var w = det[id], el = dict.querySelector('.cardslot'); el.innerHTML = card(w);
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

  /* ---- placeholders for features that open later ---- */
  [['#newsform', null], ['#nform', '#nmsg']].forEach(function (p) {
    var f = $(p[0]); if (!f) return;
    f.addEventListener('submit', function (e) { e.preventDefault(); var m = f.getAttribute('data-msg'); if (p[1]) $(p[1]).textContent = m; else { f.innerHTML = '<p style="margin:0;font-weight:700">' + esc(m) + '</p>'; } });
  });
  document.querySelectorAll('.tabs [role=tab]').forEach(function (t, i, all) { t.onclick = function () { all.forEach(function (x) { x.setAttribute('aria-selected', x === t ? 'true' : 'false'); }); }; });
})();
