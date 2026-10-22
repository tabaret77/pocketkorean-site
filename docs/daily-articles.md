# Daily articles: how a day's batch is made

Used by the daily scheduled run. The owner reviews each batch on a preview link and publishes it by merging.

## The batch

Every day, one new English article for each of the 19 categories in `.pages.yml` (19 articles), each also translated into the other 11 site languages (228 files):

- korea-today (news from the last 24–72 hours): k-drama, k-pop, culture, trends
- life-travel: living, places, food, transport, festivals, survival-korean
- learn: topik-guide, grammar-lessons, topic-words, hangul
- words: word-of-the-day, drama-lines, phrases, slang, polite-casual

Use the season and upcoming Korean dates (exams, holidays, anniversaries, festivals).

Before choosing, list `content/articles/*.md` (English files) and do not repeat a story, a grammar point or a theme that is already there. A follow-up on an existing story is fine only with genuinely new facts (e.g. new ratings).

## Facts

- Research with web search. Every number, date, name and title must come from a source you opened. Prefer Soompi, Korea JoongAng Daily, The Korea Herald, Korea Times, Yonhap, Sports Kyunghyang (English), Nielsen Korea figures as reported, official agency/broadcaster pages.
- Write it in your own words; never copy sentences. No invented quotes. Say "as of <month year>" for anything that can change (streaming availability, prices, rules).
- End news pieces with a `Sources:` line of markdown links (see existing articles).
- No gossip about private lives, no rumours, no politics-as-opinion, nothing about crimes or deaths beyond neutral facts – skip such stories.

## Format (copy the house style of existing articles)

File name `content/articles/YYYY-MM-DD-<slug>.md`, date = the publish day (today, Europe/Berlin). Front matter:

```
---
title: "…"
lang: en
section: korea-today | life-travel | learn | words
category: (must belong to the section, see .pages.yml)
date: YYYY-MM-DD
description: "One or two sentences for the card and search results."
cover: /media/library/<group>/<file>.jpg   # optional, see Photos
cover_credit: "Author / License (Wikimedia Commons)"   # required with a cover
official_url: https://…   # stories about a drama/show/film/release: its official page (see Photos)
official_label: "tvN – 100 Days of Deception"
phrase: 시청률
phrase_meaning: TV ratings
draft: false
---
```

Body, 450–800 words: a plain, friendly opening paragraph with the facts → 2–3 `##` sections → for news, a "Why it matters for learners" style section → `## Korean from this story` table (Korean | Romanization | Meaning, 6–10 rows) → one useful sentence pattern in bold with romanization and meaning → Sources.

- Korean words in the text: bold, with romanization in parentheses; link the first mention of a dictionary word as `[병원](/en/dictionary/?q=병원)` (use the dictionary form, e.g. 괜찮다).
- Romanization: Revised Romanization, and check pronunciation changes (e.g. 시청률 sicheongnyul).
- Sentence case, no ALL CAPS, no emoji.

## Covers

News (korea-today) pieces: an original scene illustration that captures the mood of the story (the drama's setting and era, the place behind a trend, a stage for a K-pop story) – people only from behind or as silhouettes, never a real person's face, no logos, and never traced from a press photo. Add a scene function to `tools/scenes2.py` (see `operating`, `atrium`, `maple`; layered flat shapes, gradients, the `paint` and `blur` filters), register it in `SCENES` in `tools/illus.py`, render with `python3 tools/illus.py <scene>` (writes `media/photos/<scene>.png`; keep the left-bottom area calm for the title), then add `PHOTO['<slug>'] = (MEDIA + 'photos/<scene>.png', '<Korean key phrase>', '<short Korean line>', C['coral'], 'center')` in `tools/covers.py`. No `cover_credit`. `tools/covers.py` also writes a text-free `<slug>-t.jpg`; set it as `thumb: /media/covers/<slug>-t.jpg` (list cards use it so the title text is never cropped).

Learning and life pieces: an original illustration – add a `COVERS['<slug>']` entry to `tools/covers.py` following the existing ones (manuscript-grid background in the section's light colour, hangul in manuscript cells, simple flat objects that show the topic, Korean text only, no logos, no real people), no `cover_credit`.

When you replace an existing cover, save it under a new file name (e.g. `<slug>-v2.jpg`): images are cached for a week, so a changed file with the same name would keep showing the old picture.

Render with `npm i --prefix /tmp/pkfonts @fontsource/nanum-myeongjo@5 && python3 tools/covers.py <slug>`, open the JPG to check it, set `cover: /media/covers/<slug>.jpg`, and commit the JPG, its `.w480/.w800/.w1600.webp` size variants (made automatically; run `python3 tools/imgvariants.py` after adding any other image) and the scene PNG with the articles.

## Photos

A photo may be used instead when it clearly shows the topic (a place, a dish, the subway). Use only photos from `media/library/` (all free-licence Wikimedia Commons, with credits in `media/library/credits.json` – use its `attribution` field as `cover_credit`). Pick one that fits the topic (a place, food, a general K-pop concert photo for a K-pop story is fine; never imply a photo shows a specific person if it doesn't). If nothing fits, leave `cover` out – the card shows the Korean phrase instead. Never hotlink, download, screenshot or re-photograph press/agency photos, posters, drama stills, video frames or album art.

Instead, for a story about a specific drama, show, film or release, set `official_url` to its official page where readers can see the poster and trailer: the broadcaster's programme page (tvN/SBS/KBS/MBC/JTBC/ENA…), the Netflix/Disney+/TVING title page, or the agency/label's official page or YouTube channel. Open the URL to confirm it is the right, working, official page; if you can't find one, leave the field out. The article page shows it as an "Official page" box.

## Translations

For each English file `YYYY-MM-DD-slug.md` write `YYYY-MM-DD-slug.<code>.md` for codes: es, vi, th, id, zh-hk, zh-tw, ja, zh-cn, pt, ru, mn.

- `title`, `description`, `phrase_meaning` translated, always in double quotes; `lang: <code>`; add `slug: <slug>`; other fields (including `official_url`, `official_label`, cover fields) unchanged.
- Hangul, romanization and pronunciation brackets stay exactly as written. Explanations are translated naturally for a native reader learning Korean; adapt English-specific comparisons when a natural local one exists.
- Internal links `/en/…` become `/<code>/…` (codes are the URL prefixes above); query strings unchanged.
- Use the established local title of a drama/group when one exists. Never add or drop information; never shorten.
- zh-hk: Traditional Chinese with Hong Kong usage; zh-tw: Traditional Chinese with Taiwan usage; zh-cn: Simplified; pt: Brazilian; es: neutral Latin American; ja: です・ます調; mn: Cyrillic.

## Checks before pushing

```
python3 -c "import sys,glob;sys.path.insert(0,'tools');import articles;[print('FAIL',f) for f in glob.glob('content/articles/YYYY-MM-DD-*.md') if not articles.read(f)]"
pip install -r tools/requirements.txt -q && python3 tools/blog.py
```

The first must print nothing; the build must finish without errors. Then confirm there are 228 new files. Commit only the new files in `content/articles/`.
