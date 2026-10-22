# Pocket German — daily "Life in Germany" posts

Every day two posts go up in the **독일 이야기 / Life in Germany / ドイツ暮らし** section of pocketkorean.com/german/, each in Korean, English and Japanese:

1. **Daily news briefing** — the most important German news of the day plus the weather, short and practical.
2. **Life & culture** — one free-topic post about living in Germany or German culture.

Repository: `tabaret77/pocketkorean-site` (this repo). Work on `main`, commit and push when done; the site deploys from `main`.

## Files
For the date `YYYY-MM-DD` (Europe/Berlin):

| What | Path |
|---|---|
| News, Korean / English / Japanese | `content/german/ko/YYYY-MM-DD-news.md`, `content/german/en/…`, `content/german/ja/…` |
| Culture post (same slug in all 3) | `content/german/{ko,en,ja}/YYYY-MM-DD-<slug>.md` — slug in English, lowercase, hyphens |
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

- `news_cover(lang, date, hook, items, out, hook_red=…)` — cover of the briefing.
- `news_card(lang, n, date, headline, out, keyword=…, big=…, big_unit=…, big_label=…, note=…, side=[(line, sub), …])` — one summary card per news item: one big number or key fact, 2–3 side facts.
- `life_cover(lang, title, out, kicker=…, emoji=…, emojis=[…])` and `life_card(lang, heading, points=[(emoji, title, line), …], out)` — culture post pictures.
- `render(html, w, h, out)` — anything else: a weather strip (cities × days with emoji icons and temperatures), a small map-like diagram, a timeline, a chart (or draw a chart with matplotlib and save as JPG). Keep text short and numbers big.

Run from the repository root, e.g. `python3 -c "import sys; sys.path.insert(0,'tools'); from german_cards import *; …"`.

## 1. News briefing
**Research** (WebSearch/WebFetch; prefer tagesschau.de, zdfheute.de, spiegel.de, rbb24.de, dw.com, DWD/wetter.com for weather): pick **4–6 items** from today/yesterday that matter to people living in Germany — new rules taking effect, strikes and transport (Deutsche Bahn, BVG/S-Bahn), prices/energy/fuel, holidays and shop closures, big political decisions, Berlin news, and one lighter item if there is one. Check every date and number against a second source. Never invent facts; if something is unclear, leave it out.

**Weather**: tomorrow + the next two days for Berlin, Hamburg, Munich, Cologne, Frankfurt (max/min °C and conditions), and one line of practical advice (umbrella, ice, heat). Show it as a table **and** as a weather strip image.

**Structure** (each language written for its reader, not translated word for word):
- Title — ko: `오늘의 독일 뉴스 (M/D 요일)｜<hook> + <item> + <item> + <item>` (full-width `｜`, ` + ` between items, hook first, most practical/surprising). en: `Germany today (Thu 22 Oct): <hook>, <item>, <item>`. ja: `今日のドイツニュース（10/22 木）｜<hook>＋<item>＋<item>`.
- 2–3 friendly lines of intro (the cover from the front matter is shown above the post automatically — don't put it in the body again).
- One `## n. headline` section per item: its summary card image, 2–4 short paragraphs (what happened, who is affected, **what it means for you**), and a small **table** when facts are listable (date / who / what changes / where). End each item with a source line: `<p class="src">Source: <a href="…">tagesschau.de</a></p>` (ko: 출처, ja: 出典).
- `## 날씨 / Weather / 天気` with the weather image and table.
- `## 오늘의 독일어 / German from today's news / 今日のニュースのドイツ語`: a table of 4–6 German words from the news (word with article · meaning · example from the news topic).
- A one-line sign-off.

Write the news in your own words (no copied sentences; at most one short quote per post). Korean voice: 해요체, friendly and practical, like a Korean living in Berlin. English: plain and friendly. Japanese: です・ます調.

## 2. Life & culture post
- Pick a fresh topic: list `content/german/ko/` first and don't repeat a topic or angle used before. Good areas: everyday rules and habits (Pfand, Sunday rest, Mülltrennung, Lüften), seasons and festivals coming up soon (match the calendar!), food and bakeries, regional differences, bureaucracy tips, language quirks, history behind a custom, city life in Berlin.
- 900–1,400 characters of body text in ko (similar length in en/ja), 4–6 `##` sections, warm and concrete, with small personal-feeling scenes but no invented personal claims presented as fact.
- At least: a `life_cover`, one or two `life_card` images (or other rendered pictures), one table (e.g. compare, checklist, do's and don'ts), and a **"오늘의 독일어 / Today's German words / 今日のドイツ語"** table with 4–6 words from the topic (article, meaning).
- Facts must be correct and durable: no prices or statistics you cannot verify; say "often/usually/depends on the state" where rules vary.

## Build, check, publish
1. `git pull --ff-only`
2. Write the 6 Markdown files and the images.
3. `python3 tools/german.py` (builds /german/, including the Life in Germany grid and the post pages).
4. Check: the 6 pages exist under `german/life/…` and `german/{en,ja}/life/…`, images load (paths start with `/german/media/life/`), front matter has all fields, no Markdown left unrendered. Open one page per language in Chromium (Playwright) and look at a screenshot.
5. `git add -A && git commit -m "Pocket German: daily news + <topic> (YYYY-MM-DD)" && git push origin main`

## Notes from the first edition
- Some news sites refuse connections from the workspace (tagesschau.de, spiegel.de, rbb24.de, dw.com, n-tv.de, deutschlandfunk.de). zdfheute.de, t-online.de, lto.de, wetter.com and wetter.net work. Try others (rbb24 via search results, berlin.de, bz-berlin.de, tagesspiegel.de) when they load.
- `docs/german-daily-example-images.py` is the script that made the 22 Oct images — copy and adapt it.
- Present older decisions (e.g. a price change announced weeks ago) as background, not as today's news.
