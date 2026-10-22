// Server-side pages for pocketkorean.com: /{lang}/word/{slug}/ and /{lang}/name/{slug}/.
// Data comes from small static files (/data/{u}/w/xx.json, /data/{u}/nm/x.json); the page shell from /tpl/{u}/*.html.
const LANGS = new Set(['en', 'es', 'vi', 'th', 'id', 'zh-hk', 'zh-tw', 'ja', 'zh-cn', 'pt', 'ru', 'mn']);
const HL = { 'zh-hk': 'zh-HK', 'zh-tw': 'zh-TW', 'zh-cn': 'zh-CN', pt: 'pt-BR' };
const BASE = 'https://pocketkorean.com';
const esc = (s) => String(s == null ? '' : s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const fnv = (s) => { let h = 2166136261; for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; } return h % 256; };
const wslug = (de) => de.replace(/\//g, '-');
const wurl = (u, de) => `/${u}/word/${encodeURIComponent(wslug(de))}/`;
const SPK = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M11 5 6 9H3v6h3l5 4z" fill="currentColor"/><path d="M15.5 8.5a5 5 0 0 1 0 7M18.5 5.5a9 9 0 0 1 0 13"/></svg>';

async function asset(ctx, path) {
  // Pages answers /x.html with a 308 to /x; follow such redirects inside the asset store
  let u = new URL(path, ctx.request.url);
  for (let i = 0; i < 3; i++) {
    const r = await ctx.env.ASSETS.fetch(new Request(u.toString(), { redirect: 'manual' }));
    if (r.ok) return r;
    const loc = r.status >= 300 && r.status < 400 && r.headers.get('location');
    if (!loc) return null;
    u = new URL(loc, u);
  }
  return null;
}
const short = (m) => String(m || '').split(/[;]/)[0].trim();

function card(u, w, L, first) {
  const lvn = w.lv.slice(1), H = first ? 'h1' : 'h2';
  const a = w.a ? esc(JSON.stringify(w.a)) : '';
  const parts = (w.parts || []).filter((p) => p[0]).map((p) => `<span><b lang="ko">${esc(p[0])}</b>${p[1] ? ' ' + esc(p[1]) : ''}</span>`).join('<em aria-hidden="true">+</em>');
  const rel = (w.rel || []).map((r) => `<a href="${wurl(u, r[0])}"><b lang="ko">${esc(r[0])}</b> <span class="muted">${esc(r[1])}</span></a>`).join('');
  return `<article class="card" style="margin-bottom:24px"><div class="hd"><div><p style="margin:0 0 6px;display:flex;gap:8px;align-items:center"><a class="tag t${lvn}" href="/${u}/topik/${lvn}/">TOPIK ${lvn}</a><span class="muted">${esc(w.pos)}</span></p>` +
    `<${H} lang="ko" style="margin:0;font-family:var(--my);font-size:clamp(44px,6vw,64px);font-weight:800;letter-spacing:-.02em">${esc(w.de)}</${H}><p class="muted" style="margin:6px 0 0">${esc(w.rom)}${w.pr ? ' <span lang="ko">[' + esc(w.pr) + ']</span>' : ''}</p></div>` +
    (a ? `<button class="play" data-pa="${a}" data-which="w" aria-label="${esc(L.listen)}">${SPK}</button>` : '') + '</div><div class="bd">' +
    `<div>${w.forms ? `<p class="muted" lang="ko" style="margin:0 0 2px">${esc(w.forms)}</p>` : ''}<p class="mean">${esc(w.m)}</p></div>` +
    (w.ex ? `<div><p style="margin:0 0 8px;display:flex;align-items:center;gap:10px"><span class="hl">${esc(L.ex)}</span>${a && w.a[3] >= 0 ? `<button class="play sm" data-pa="${a}" data-which="ex" aria-label="${esc(L.listen)}">${SPK}</button>` : ''}</p><p lang="ko" style="margin:0;font-size:21px;font-weight:700">${esc(w.ex)}</p><p class="muted" style="margin:2px 0 0;font-size:17px">${esc(w.x)}</p></div>` : '') +
    (parts || w.e ? `<div><p style="margin:0 0 10px"><span class="hl">${esc(L.parts)}</span></p>${parts ? '<div class="parts">' + parts + '</div>' : ''}${w.e ? `<p style="margin:10px 0 0">${esc(w.e)}</p>` : ''}</div>` : '') +
    (w.t ? `<div><p style="margin:0 0 6px"><span class="hl">${esc(L.tip)}</span></p><p style="margin:0">${esc(w.t)}</p></div>` : '') +
    (rel ? `<div><p style="margin:0 0 10px"><span class="hl">${esc(L.rel)}</span></p><div class="rel">${rel}</div></div>` : '') + '</div></article>';
}

function fill(tpl, map) {
  let s = tpl;
  for (const k of Object.keys(map)) s = s.split(k).join(map[k]);
  return s;
}

async function cached(ctx, build) {
  const url = new URL(ctx.request.url);
  const cache = caches.default, key = new Request(url.toString(), { method: 'GET' });
  const hit = await cache.match(key);
  if (hit) return hit;
  const res = await build(url);
  if (res.status === 200) ctx.waitUntil(cache.put(key, res.clone()));
  return res;
}
const html = (s) => new Response(s, { headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'public, max-age=3600, s-maxage=86400' } });

export async function wordPage(ctx) {
  const u = ctx.params.lang, seg = ctx.params.path || [];
  if (!LANGS.has(u) || !seg.length || !seg[0]) return ctx.next();
  const url = new URL(ctx.request.url);
  if (!url.pathname.endsWith('/')) return Response.redirect(url.origin + url.pathname + '/' + url.search, 301);
  return cached(ctx, () => wordInner(ctx, u, seg, url));
}

async function wordInner(ctx, u, seg, url) {
  {
    let slug = seg[0]; try { slug = decodeURIComponent(slug); } catch (e) {}
    const b = await asset(ctx, `/data/${u}/w/${fnv(slug).toString(16).padStart(2, '0')}.json`);
    const list = b ? (await b.json())[slug] : null;
    if (!list) return Response.redirect(`${url.origin}/${u}/dictionary/?q=${encodeURIComponent(slug)}`, 302);
    const t = await asset(ctx, `/tpl/${u}/word`); if (!t) return Response.redirect(`${url.origin}/${u}/dictionary/?q=${encodeURIComponent(slug)}`, 302);
    const tpl = await t.text();
    const L = JSON.parse((tpl.match(/<script type="application\/json" id="wl">([\s\S]*?)<\/script>/) || [, '{}'])[1]);
    const w = list[0], lvn = w.lv.slice(1);
    const title = `${w.de} ${L.meaning}: ${short(w.m)} (${w.rom}) | Pocket Korean`;
    const desc = `${w.de} (${w.rom}): ${list.map((x) => short(x.m)).join(' / ')}.${w.ex ? ' ' + w.ex + ' – ' + w.x : ''}`.slice(0, 300);
    const main = list.map((x, i) => card(u, x, L, i === 0)).join('');
    const nb = (w.nb || []).length ? `<div class="box"><b>${esc(L.more.replace('{n}', lvn))}</b><p class="nlinks" style="margin:10px 0 0">${w.nb.map((d) => `<a href="${wurl(u, d)}" lang="ko">${esc(d)}</a>`).join('')}</p><a class="more" href="/${u}/topik/${lvn}/">TOPIK ${lvn}</a></div>` : '';
    const ld = '<script type="application/ld+json">' + JSON.stringify({ '@context': 'https://schema.org', '@type': 'DefinedTerm', name: w.de, alternateName: w.rom, description: list.map((x) => x.m).join(' / '), inLanguage: 'ko', url: BASE + wurl(u, w.de),
      inDefinedTermSet: { '@type': 'DefinedTermSet', name: 'Pocket Korean dictionary', url: `${BASE}/${u}/dictionary/` } }).replace(/</g, '\\u003c') + '</script>';
    return html(fill(tpl, { __TITLE__: esc(title), __DESC__: esc(desc), __SLUG__: encodeURIComponent(slug), __MAIN__: main, __NB__: nb, __LD__: ld,
      __CRUMB__: `<a href="/${u}/topik/${lvn}/">TOPIK ${lvn}</a>` }));
  }
}

export async function namePage(ctx) {
  const u = ctx.params.lang, seg = ctx.params.path || [];
  if (!LANGS.has(u) || !seg.length || !seg[0]) return ctx.next();
  const url = new URL(ctx.request.url);
  const slug = String(seg[0]).toLowerCase().normalize('NFKD').replace(/[̀-ͯ]/g, '').replace(/[^a-z]/g, '');
  if (!slug) return Response.redirect(`${url.origin}/${u}/name/`, 302);
  if (slug !== seg[0] || !url.pathname.endsWith('/')) return Response.redirect(`${url.origin}/${u}/name/${slug}/`, 301);
  return cached(ctx, async () => {
    const b = await asset(ctx, `/data/${u}/nm/${slug[0]}.json`);
    const all = b ? await b.json() : {};
    const e = all[slug];
    if (!e) return Response.redirect(`${url.origin}/${u}/name/?n=${encodeURIComponent(seg[0])}`, 302);
    const t = await asset(ctx, `/tpl/${u}/name`); if (!t) return Response.redirect(`${url.origin}/${u}/name/`, 302);
    const keys = Object.keys(all).sort(), i = keys.indexOf(slug);
    const near = keys.slice(Math.max(0, i - 8), i).concat(keys.slice(i + 1, i + 9));
    const more = `<div class="box"><b>${esc(MORE[u] || MORE.en)}</b><p class="nlinks" style="margin:10px 0 0">${near.map((k) => `<a href="/${u}/name/${k}/">${esc(all[k].n)} <span lang="ko">${esc(all[k].ko)}</span></a>`).join('')}</p></div>`;
    return html(fill(await t.text(), { __TITLE__: esc(e.t + ' | Pocket Korean'), __DESC__: esc(e.d), __SLUG__: slug, __H1__: esc(e.t), __NAME__: esc(e.n), __RES__: e.h, __MORE__: more }));
  });
}
const MORE = { en: 'More names', es: 'Más nombres', vi: 'Tên khác', th: 'ชื่ออื่น ๆ', id: 'Nama lainnya', 'zh-hk': '更多名字', 'zh-tw': '更多名字', ja: 'ほかの名前', 'zh-cn': '更多名字', pt: 'Mais nomes', ru: 'Другие имена', mn: 'Бусад нэрс' };

// /api/tts?t=… — Google Cloud TTS for Korean text that appears in articles (listed in /data/tts.json).
// The API key lives only in the Cloudflare secret GOOGLE_TTS_KEY. Audio is cached at the edge for a year.
let ALLOW = null, ALLOW_AT = 0;
async function ttsAllowed(ctx, t) {
  if (!ALLOW || Date.now() - ALLOW_AT > 600000) {
    const r = await asset(ctx, '/data/tts.json');
    ALLOW = new Set(r ? await r.json() : []); ALLOW_AT = Date.now();
  }
  const h = await crypto.subtle.digest('SHA-1', new TextEncoder().encode(t));
  const hex = [...new Uint8Array(h)].map((b) => b.toString(16).padStart(2, '0')).join('').slice(0, 16);
  return ALLOW.has(hex);
}
export async function ttsAudio(ctx) {
  const url = new URL(ctx.request.url);
  const t = (url.searchParams.get('t') || '').trim();
  const err = (s, m) => new Response(m, { status: s, headers: { 'content-type': 'text/plain', 'cache-control': 'no-store' } });
  if (!t || t.length > 180) return err(400, 'bad text');
  const cache = caches.default, key = new Request(`${url.origin}/api/tts?t=${encodeURIComponent(t)}&v=1`, { method: 'GET' });
  const hit = await cache.match(key);
  if (hit) return hit;
  if (!(await ttsAllowed(ctx, t))) return err(404, 'unknown text');
  const k = ctx.env.GOOGLE_TTS_KEY;
  if (!k) return err(503, 'tts not configured');
  const g = await fetch(`https://texttospeech.googleapis.com/v1/text:synthesize?key=${encodeURIComponent(k)}`, {
    method: 'POST', headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ input: { text: t }, voice: { languageCode: 'ko-KR', name: 'ko-KR-Neural2-A' }, audioConfig: { audioEncoding: 'MP3', speakingRate: 0.9 } }),
  });
  if (!g.ok) return err(502, 'tts failed');
  const b64 = (await g.json()).audioContent || '';
  const bin = Uint8Array.from(atob(b64), (c) => c.charCodeAt(0));
  const res = new Response(bin, { headers: { 'content-type': 'audio/mpeg', 'cache-control': 'public, max-age=31536000, immutable' } });
  ctx.waitUntil(cache.put(key, res.clone()));
  return res;
}
