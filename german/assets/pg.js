/* Pocket German section: today's words + sentence of the day (by date, same rule as the app), dictionary search, audio */
(function () {
  "use strict";
  var B = document.body, G = B.dataset.g || "ko", BASE = B.dataset.base || "/german/";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var cache = {};
  function getJSON(u) { return cache[u] || (cache[u] = fetch(u).then(function (r) { if (!r.ok) throw new Error(u); return r.json(); })); }
  function shard(id) { var h = 0x811c9dc5; for (var i = 0; i < id.length; i++) { h ^= id.charCodeAt(i); h = Math.imul(h, 0x01000193) >>> 0; } return ("0" + (h & 255).toString(16)).slice(-2); }
  function wordHTML(de) { var m = /^(der|die|das)\s/.exec(de); return m ? '<b class="a-' + m[1] + '">' + m[1] + "</b> " + esc(de.slice(m[1].length + 1)) : esc(de); }
  function lvTag(lv) { return '<span class="lv l' + String(lv || "A").charAt(0) + '">' + esc(lv) + "</span>"; }
  var SPK = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M11 5 6 9H3v6h3l5 4z" fill="currentColor"/><path d="M15.5 8.5a5 5 0 0 1 0 7M18.5 5.5a9 9 0 0 1 0 13"/></svg>';

  /* ---------- audio: the web app's sprites (A1, topic words, sentences of the day) ---------- */
  var AUD = null, ctx = null, playing = null;
  function audIdx() { return AUD ? Promise.resolve(AUD) : getJSON("/german/web/audio/idx2.json").then(function (j) { AUD = j; return j; }); }
  /* idx2 stores BYTE ranges in the MP3 files (like the app): fetch the file once, cut the range, decode just that slice */
  var files = {};
  function play(key, part, btn) {
    audIdx().then(function (a) {
      var e = a.m[key]; if (!e) return;
      var s = part === 1 && e.length > 3 ? e[3] : e[1], n = part === 1 && e.length > 3 ? e[4] : e[2];
      if (s == null || s < 0 || !n) return;
      ctx = ctx || new (window.AudioContext || window.webkitAudioContext)();
      if (ctx.state === "suspended") ctx.resume();
      var f = a.p[e[0]];
      (files[f] || (files[f] = fetch("/german/web/audio/" + f).then(function (r) { return r.arrayBuffer(); }))).then(function (ab) {
        var cut = ab.slice(s, s + n);
        return new Promise(function (ok, no) { ctx.decodeAudioData(cut, ok, no); });
      }).then(function (buf) {
        if (playing) try { playing.stop(); } catch (x) {}
        var src = ctx.createBufferSource(); src.buffer = buf; src.connect(ctx.destination); src.start(0); playing = src;
        if (btn) { btn.classList.add("on"); src.onended = function () { btn.classList.remove("on"); }; }
      }).catch(function () {});
    });
  }
  /* German text in posts: pre-generated pack slice (data-tp="file,offset,length") or /api/tts?l=de */
  function playBuf(p, btn) {
    p.then(function (buf) {
      if (playing) try { playing.stop(); } catch (x) {}
      var src = ctx.createBufferSource(); src.buffer = buf; src.connect(ctx.destination); src.start(0); playing = src;
      if (btn) { btn.classList.add("on"); src.onended = function () { btn.classList.remove("on"); }; }
    }).catch(function () { if (btn) btn.classList.remove("on"); });
  }
  function sayDe(btn) {
    ctx = ctx || new (window.AudioContext || window.webkitAudioContext)();
    if (ctx.state === "suspended") ctx.resume();
    var dec = function (ab) { return new Promise(function (ok, no) { ctx.decodeAudioData(ab, ok, no); }); }, tp = btn.dataset.tp;
    if (tp) {
      var a = tp.split(","), f = "/german/media/tts/" + a[0], s = +a[1], n = +a[2];
      playBuf((files[f] || (files[f] = fetch(f).then(function (r) { return r.arrayBuffer(); }))).then(function (ab) { return dec(ab.slice(s, s + n)); }), btn);
    } else {
      playBuf(fetch("/api/tts?l=de&t=" + encodeURIComponent(btn.dataset.tts)).then(function (r) { if (!r.ok) throw 0; return r.arrayBuffer(); }).then(dec), btn);
    }
  }
  document.addEventListener("click", function (ev) {
    var d = ev.target.closest("[data-tts]"); if (d) { ev.preventDefault(); sayDe(d); return; }
    var b = ev.target.closest("[data-say]"); if (!b) return;
    ev.preventDefault(); play(b.dataset.say, +(b.dataset.part || 0), b);
  });

  /* ---------- today (same rule as the app: (day of year + year*7) % n) ---------- */
  function dayIndex(d, n) { var doy = Math.floor((d - new Date(d.getFullYear(), 0, 0)) / 864e5); return (doy + d.getFullYear() * 7) % n; }
  function iso(d) { return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2); }
  function fdate(d) {
    if (G === "en") return ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][d.getMonth()] + " " + d.getDate() + ", " + d.getFullYear();
    return G === "ja" ? d.getFullYear() + "年" + (d.getMonth() + 1) + "月" + d.getDate() + "日" : d.getFullYear() + "년 " + (d.getMonth() + 1) + "월 " + d.getDate() + "일";
  }
  function picFor(id) { return getJSON("/german/data/pic/" + shard(id) + ".json").then(function (j) { return j[id] || ""; }).catch(function () { return ""; }); }
  function initToday() {
    var blocks = document.querySelectorAll("[data-today]"); if (!blocks.length) return;
    var now = new Date(), key = iso(now);
    if (blocks[0].dataset.today === key) return;           // the page was built today
    /* today page: swap in today's word post (posts live at words/<topic>/) */
    var tp = document.querySelector("[data-order]"), post = document.querySelector(".ppost");
    if (tp && post) {
      var order = tp.dataset.order.split(","), k2 = order[dayIndex(now, order.length)];
      if (k2 && k2 !== tp.dataset.post) fetch(BASE + "words/" + k2 + "/").then(function (r) { return r.ok ? r.text() : ""; }).then(function (h) {
        if (!h) return; var np = new DOMParser().parseFromString(h, "text/html").querySelector(".ppost"); if (!np) return;
        var when = post.querySelector(".pkick time"); post.replaceWith(np); tp.dataset.post = k2;
        var kick = np.querySelector(".pkick"); if (kick && !kick.querySelector("time")) { var t = document.createElement("time"); t.textContent = fdate(now); kick.appendChild(t); }
      }).catch(function () {});
    }
    getJSON("/german/data/" + G + "/today.json").then(function (T) {
      var t = T.t[dayIndex(now, T.t.length)], n = dayIndex(now, T.d.length), x = T.d[n];
      blocks.forEach(function (bl) {
        bl.dataset.today = key;
        bl.querySelectorAll(".tdate").forEach(function (el) { el.textContent = fdate(now); el.setAttribute("datetime", key); });
        var head = '<div class="topic"><span class="emo" aria-hidden="true">' + esc(t.e) + "</span><b>" + esc(t.n) + "</b></div>";
        var tw = bl.querySelector(".twb");
        if (tw && tw.classList.contains("full")) {
          tw.innerHTML = head + '<ol class="wcards">' + t.w.map(function (w) {
            return '<li class="wcard"><span class="pic" data-pic="' + w[0] + '"></span><div class="wb"><p class="wde" lang="de">' + wordHTML(w[1]) + '</p><p class="wm">' + esc(w[2]) + "</p>" + lvTag(w[3]) + "</div></li>";
          }).join("") + "</ol>";
          tw.querySelectorAll("[data-pic]").forEach(function (el) { picFor(el.dataset.pic).then(function (p) { if (p) el.innerHTML = '<svg viewBox="0 0 100 100" aria-hidden="true">' + p + "</svg>"; }); });
        } else if (tw) {
          tw.innerHTML = head + '<ol class="wlist">' + t.w.map(function (w) {
            return '<li><a href="' + BASE + "dictionary/?q=" + encodeURIComponent(w[1]) + '"><span class="wde" lang="de">' + wordHTML(w[1]) + '</span><span class="wm">' + esc(w[2]) + "</span>" + lvTag(w[3]) + "</a></li>";
          }).join("") + "</ol>";
        }
        var ts = bl.querySelector(".tsb");
        if (ts) {
          var k = "N" + ("00" + n).slice(-3), lab = (document.querySelector(".spat small") || {}).textContent || "";
          ts.innerHTML = '<p class="sde" lang="de">' + esc(x[0]) + '<button class="say" data-say="' + k + '" aria-label="listen">' + SPK + "</button></p>" +
            '<p class="str">' + esc(x[1]) + '</p><div class="spat"><small>' + esc(lab) + '</small><p lang="de">' + esc(x[2]) + "</p></div>" +
            '<p class="snote">' + esc(x[3]) + '</p><p class="stag">' + lvTag(x[5]) + " " + esc(x[4]) + "</p>";
        }
      });
    }).catch(function () {});
  }

  /* ---------- dictionary ---------- */
  function norm(s) { return String(s).toLowerCase().replace(/ß/g, "ss").normalize("NFD").replace(/[̀-ͯ]/g, ""); }
  function head(de) { return norm(de).replace(/^(der|die|das)\s+/, "").replace(/^sich\s+/, ""); }
  function initDict() {
    var box = $("#dict"); if (!box) return;
    var L = JSON.parse(box.dataset.l), input = $("#pgq", box), res = $("#dres"), card = $("#dcard"), cnt = $(".dcount", box), IDX = null, timer = null;
    function load() { return IDX ? Promise.resolve(IDX) : (cnt.textContent = L.loading, getJSON("/german/data/" + G + "/idx.json").then(function (j) {
      IDX = j.map(function (r) { return { id: r[0], de: r[1], m: r[2], lv: r[3], h: head(r[1]), n: norm(r[1]), nm: norm(r[2]) }; }); return IDX; })); }
    function mark(text, q) {
      var t = String(text), i = norm(t).indexOf(q);
      return i < 0 || !q ? esc(t) : esc(t.slice(0, i)) + "<mark>" + esc(t.slice(i, i + q.length)) + "</mark>" + esc(t.slice(i + q.length));
    }
    function search(qs, openFirst) {
      var q = norm(qs.trim()).replace(/^(der|die|das)\s+/, "");
      if (!q) { res.innerHTML = ""; cnt.textContent = L.dict_hint; return; }
      load().then(function (I) {
        var out = [];
        I.forEach(function (w) {
          var s = w.h === q ? 0 : w.h.indexOf(q) === 0 ? 1 : w.nm === q || w.nm.split(/[,、，;·]\s*/).indexOf(q) >= 0 ? 2 : w.n.indexOf(q) >= 0 ? 3 : w.nm.indexOf(q) >= 0 ? 4 : -1;
          if (s >= 0) out.push([s, w.h.length, w]);
        });
        out.sort(function (a, b) { return a[0] - b[0] || a[1] - b[1]; });
        cnt.textContent = out.length ? L.n_found.replace("{n}", out.length.toLocaleString()) : L.none.replace("{q}", qs);
        res.innerHTML = out.slice(0, 80).map(function (r) {
          var w = r[2];
          return '<li><button type="button" data-id="' + w.id + '"><span class="wde" lang="de">' + mark(w.de, q) + '</span><span class="wm">' + mark(w.m, q) + "</span>" + lvTag(w.lv) + "</button></li>";
        }).join("");
        if (openFirst && out.length) open(out[0][2].id, true);
      });
    }
    function open(id, quiet) {
      res.querySelectorAll("[aria-current]").forEach(function (b) { b.removeAttribute("aria-current"); });
      var btn = res.querySelector('[data-id="' + id + '"]'); if (btn) btn.setAttribute("aria-current", "true");
      Promise.all([getJSON("/german/data/" + G + "/w/" + shard(id) + ".json"), picFor(id), audIdx().catch(function () { return { m: {} }; })]).then(function (r) {
        var w = r[0][id]; if (!w) return;
        var has = !!(r[2].m && r[2].m[id]);
        var say = has ? '<button class="say" data-say="' + id + '" aria-label="' + esc(L.listen) + '">' + SPK + "</button>" : "";
        var sec = function (k, v) { return v ? '<div class="dsec"><h4>' + esc(L[k]) + "</h4>" + v + "</div>" : ""; };
        card.innerHTML = '<article class="tcard"><div class="dhead"><div class="dw"><div class="dmeta">' + lvTag(w.lv) + "<span>" + esc(L.lv[w.lv] || "") + "</span><span>" + esc(w.pos || "") + "</span></div>" +
          '<h2 class="dword" lang="de">' + wordHTML(w.de) + "</h2></div>" + (r[1] ? '<span class="dpic"><svg viewBox="0 0 100 100" aria-hidden="true">' + r[1] + "</svg></span>" : "") + say + "</div>" +
          (w.forms ? '<p class="dforms" lang="de">' + esc(w.forms) + "</p>" : "") + '<p class="dmean">' + esc(w.ko) + "</p>" +
          sec("ex", w.ex ? '<p class="dex" lang="de">' + esc(w.ex) + (has ? ' <button class="say" style="width:30px;height:30px;vertical-align:middle" data-say="' + id + '" data-part="1" aria-label="' + esc(L.listen) + '">' + SPK + "</button>" : "") + '</p><p class="dexk">' + esc(w.exk || "") + "</p>" : "") +
          sec("ety", w.ety ? "<p>" + esc(w.ety) + "</p>" : "") +
          sec("rel", w.rel && w.rel.length ? '<div class="drel">' + w.rel.map(function (x) { return '<button type="button" data-q="' + esc(x.de) + '" lang="de">' + esc(x.de) + "<i>" + esc(x.ko) + "</i></button>"; }).join("") + "</div>" : "") +
          sec("tip", w.tip ? "<p>" + esc(w.tip) + "</p>" : "") +
          (has ? "" : '<p class="dnote">' + esc(L.in_app) + "</p>") + "</article>";
        card.hidden = false;
        var u = new URL(location.href); u.searchParams.set("w", id); if (input.value) u.searchParams.set("q", input.value); history.replaceState(null, "", u);
        if (!quiet && window.matchMedia("(max-width:860px)").matches) card.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    }
    input.addEventListener("input", function () { clearTimeout(timer); timer = setTimeout(function () { search(input.value); }, 120); });
    box.querySelector("form").addEventListener("submit", function (e) { e.preventDefault(); search(input.value, true); });
    res.addEventListener("click", function (e) { var b = e.target.closest("[data-id]"); if (b) open(b.dataset.id); });
    card.addEventListener("click", function (e) { var b = e.target.closest("[data-q]"); if (b) { input.value = b.dataset.q; search(b.dataset.q, true); window.scrollTo({ top: box.offsetTop - 80, behavior: "smooth" }); } });
    var p = new URLSearchParams(location.search);
    if (p.get("q")) { input.value = p.get("q"); search(p.get("q"), !p.get("w")); }
    if (p.get("w")) open(p.get("w"), true);
    if (!p.get("q")) input.addEventListener("focus", function () { load(); }, { once: true });
  }

  initToday(); initDict();
})();
