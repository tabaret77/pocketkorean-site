# Adding a language to Pocket German (pocketkorean.com/german)

Each extra language is one file in `tools/german_langs/<code>.py` (copy `tr.py`) plus the app's files for that language.
A language is built only when its app data is present, so the file can be added before the data.

1. **App files** – from the app's web build (or its published artifact), copy into `/home/claude/pgsrc/`:
   `data_<code>/` (A1–C2.json, daily.json), `help2_<code>/` (screenshots), `index_<code>.html`, and the latest `data/topics.json`
   (topic names must include the new code).
2. **Strings** – `tools/german_langs/<code>.py`: native name, app name and wordmark, menu, page strings (`S`), word-post strings (`PS`),
   months, level names, parts of speech, news/life labels, privacy policy, support FAQ and the web-trial sheet (`trial`, including `back` = "Back to the website").
3. **Build** – `python3 tools/german_app.py` (web trial at /german/web/index_<code>.html), `python3 tools/german.py`,
   then `python3 /home/claude/kr/site/gen.py` and `python3 tools/german.py` again (the Pocket Korean menu lists the language in `tools/layout.py` → `PG_LANGS`).
4. **Content** – add a `"<code>"` block to every `content/german/words/*.json` (see the Turkish brief pattern: same fields as `en`),
   and add the language to the daily posts (`docs/german-daily.md` already says "all languages", and `tools/german_cards.py` needs `FONT/BRAND/TODAY` and a date format).
5. **Check** – screenshots of /german/<code>/, /dictionary/, /today/, /life/, /privacy/, /support/ on desktop and phone; `sitemap-german.xml` lists only pages that exist.
