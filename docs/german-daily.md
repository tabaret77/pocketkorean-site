# Pocket German — daily "Life in Germany" posts

Every day two posts go up in the **독일 이야기 / Life in Germany / ドイツ暮らし** section of pocketkorean.com/german/, each in every site language: Korean, English, Japanese, plus every language that has a file in `tools/german_langs/` (now: Turkish `tr`). Below, "all languages" means this list.

1. **Daily news briefing** — the most important German news of the day plus the weather, short and practical.
2. **Life & culture** — one free-topic post about living in Germany or German culture.

Repository: `tabaret77/pocketkorean-site` (this repo). Work on `main`, commit and push when done; the site deploys from `main`.

## Files
For the date `YYYY-MM-DD` (Europe/Berlin):

| What | Path |
|---|---|
| News, one file per language | `content/german/ko/YYYY-MM-DD-news.md`, `content/german/en/…`, `content/german/ja/…`, `content/german/tr/…` |
| Culture post (same slug in all languages) | `content/german/{ko,en,ja,tr}/YYYY-MM-DD-<slug>.md` — slug in English, lowercase, hyphens |
| Images | `german/media/life/YYYY-MM-DD/` (JPG, ≤ 250 KB each) |

Front matter (between `---` lines, one `key: value` per line):
```
---
title: …
date: YYYY-MM-DD
category: news        # or: life
summary: one or two sentences for the card
cover: /german/media/life/YYYY-MM-DD/news-ko-cover.jpg
---
```
The body is Markdown (tables, `## headings`, `![alt](/german/media/life/…jpg)`, links). Raw HTML is allowed for `<figure>` with `<figcaption>`.

## Images — always generated, never downloaded
The workspace cannot download photos, so every picture is made with `tools/german_cards.py` (Chromium renders HTML; fonts: Noto Sans CJK, Noto Color Emoji). Make each image **in every language** (text inside the picture is in that language).

- `news_cover(lang, date, hook, items, out, hook_red=…)` — cover of the briefing (pastel: hook on an index card, other items as pastel chips).
- `weather_card(lang, title, days, cities, rows, tip, out)` — pastel weather strip (rows: per city a list of (emoji, max, min)). All images are pastel — no dark/navy backgrounds.
- `news_card(…)` — **not used**: news items have no card images.
- `life_cover(lang, title, out, kicker=…, emoji=…, emojis=[…])` and `life_card(lang, heading, points=[(emoji, title, line), …], out)` — culture post pictures.
- `render(html, w, h, out)` — anything else: a weather strip (cities × days with emoji icons and temperatures), a small map-like diagram, a timeline, a chart (or draw a chart with matplotlib and save as JPG). Keep text short and numbers big.

Run from the repository root, e.g. `python3 -c "import sys; sys.path.insert(0,'tools'); from german_cards import *; …"`.

## 1. News briefing
**Every day must bring different news.** Before choosing, read the news posts of the last 7 days (`content/german/ko/*-news.md`, newest first) and list the stories they covered. Do not repeat a story. A follow-up is allowed only when something genuinely new happened (a decision, a date, a result) — then say in one line what changed since the earlier post and link to it. Pick **7 items, one from each area**, in this order: 정치 Politics · 경제 Economy · 사회 Society (incl. transport, education, health, Berlin/local) · 문화 Culture · 예술 Arts (exhibitions, theatre, music, film festivals, books) · 연예 Entertainment (German film/TV/music/celebrity news — no private life or rumours) · 스포츠 Sports (Bundesliga, national teams, big events). If an area truly has nothing worth reporting today, take a second item from another area, but never fewer than 6 items and never two from the same area while another area is empty. Start each heading with the area as a label, e.g. `## 1. [정치] …` / `## 1. [Politics] …` / `## 1. 【政治】…`.

**Research** (WebSearch/WebFetch; prefer tagesschau.de, zdfheute.de, spiegel.de, rbb24.de, dw.com, kicker.de / sportschau.de for sports, monopol-magazin.de / deutschlandfunkkultur.de for arts, DWD/wetter.com for weather): pick the items (see the area list above) from today/yesterday that matter to people living in Germany — new rules taking effect, strikes and transport (Deutsche Bahn, BVG/S-Bahn), prices/energy/fuel, holidays and shop closures, big political decisions, Berlin news, and one lighter item if there is one. Check every date and number against a second source. Never invent facts; if something is unclear, leave it out.

**Weather**: tomorrow + the next two days for Berlin, Hamburg, Munich, Cologne, Frankfurt (max/min °C and conditions), and one line of practical advice (umbrella, ice, heat). Show it as a table (a weather strip image is optional).

**Structure** (each language written for its reader, not translated word for word):
- Title — ko: `오늘의 독일 뉴스 (M/D 요일)｜<hook> + <item> + <item> + <item>` (full-width `｜`, ` + ` between items, hook first, most practical/surprising). en: `Germany today (Thu 22 Oct): <hook>, <item>, <item>`. ja: `今日のドイツニュース（10/22 木）｜<hook>＋<item>＋<item>`. tr: `Bugün Almanya (22 Ekim Per): <hook>, <item>, <item>` (same shape as en: the part after the colon, comma-separated, becomes the card's headline list). Section labels in tr: `## 1. [Siyaset] …` (Siyaset · Ekonomi · Toplum · Kültür · Sanat · Magazin · Spor); weather `## Hava durumu`, words `## Günün haberlerinden Almanca`; source line `Kaynak:`.
- 2–3 friendly lines of intro (the cover from the front matter is shown above the post automatically — don't put it in the body again).
- One `## n. headline` section per item, **bullet points only — no card image, no prose paragraphs**: 3–5 bullets, each `- **short key point** — one line of detail`. The first bullet carries the key fact (date, number, who); include one bullet on what it means for the reader (what to do, who is affected). Add a small table only when facts are genuinely listable. End each item with a source line: `<p class="src">Source: <a href="…">tagesschau.de</a></p>` (ko: 출처, ja: 出典).
- `## 날씨 / Weather / 天気` with the weather image and table.
- `## 오늘의 독일어 / German from today's news / 今日のニュースのドイツ語`: a table of 4–6 German words from the news (word with article · meaning · example from the news topic).
- A one-line sign-off.

Write the news in your own words (no copied sentences; at most one short quote per post). Korean voice: 해요체, friendly and practical, like a Korean living in Berlin. English: plain and friendly. Japanese: です・ます調. Turkish: warm, plain and polite (siz), written for Turks living in or moving to Germany.

## 2. Life & culture post
- Pick a fresh topic: list `content/german/ko/` first and don't repeat a topic or angle used before. Good areas: everyday rules and habits (Pfand, Sunday rest, Mülltrennung, Lüften), seasons and festivals coming up soon (match the calendar!), food and bakeries, regional differences, bureaucracy tips, language quirks, history behind a custom, city life in Berlin.
- 900–1,400 characters of body text in ko (similar length in en/ja), 4–6 `##` sections, warm and concrete, with small personal-feeling scenes but no invented personal claims presented as fact.
- At least: a `life_cover`, one or two `life_card` images (or other rendered pictures), one table (e.g. compare, checklist, do's and don'ts), and a **"오늘의 독일어 / Today's German words / 今日のドイツ語"** table with 4–6 words from the topic (article, meaning).
- Facts must be correct and durable: no prices or statistics you cannot verify; say "often/usually/depends on the state" where rules vary.

## Build, check, publish
1. `git pull --ff-only`
2. Write the Markdown files (2 posts × all languages) and the images. Images with text are made per language like the others (pass the language code to the card functions; for `tr` use the English layout with Turkish text).
3. `python3 tools/german.py` (builds /german/, including the Life in Germany grid and the post pages).
4. Check: the pages exist under `german/life/…` and `german/<lang>/life/…` for every language, images load (paths start with `/german/media/life/`), front matter has all fields, no Markdown left unrendered. Open one page per language in Chromium (Playwright) and look at a screenshot.
5. `git add -A && git commit -m "Pocket German: daily news + <topic> (YYYY-MM-DD)" && git push origin main`

## Notes from the first edition
- Some news sites refuse connections from the workspace (tagesschau.de, spiegel.de, rbb24.de, dw.com, n-tv.de, deutschlandfunk.de). zdfheute.de, t-online.de, lto.de, wetter.com and wetter.net work. Try others (rbb24 via search results, berlin.de, bz-berlin.de, tagesspiegel.de) when they load.
- `docs/german-daily-example-images.py` is the script that made the 22 Oct images — copy and adapt it.
- Present older decisions (e.g. a price change announced weeks ago) as background, not as today's news.

- Images are cached for a long time. If you ever change an image that is already published, save it under a **new file name** (e.g. add `-2`) and update the references — never overwrite a published file.
