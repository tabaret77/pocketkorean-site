# pocketkorean.com

The website for Pocket Korean, hosted on Cloudflare Pages.

## Site structure

| Section | URL | Content |
|---|---|---|
| Home | `/{lang}/` | Dictionary search, word of the day, latest articles, quiz |
| Korea Today | `/{lang}/korea-today/` | K-drama & film, K-pop, culture, trends |
| Life & Travel | `/{lang}/life-travel/` | Living, places, food, transport, festivals, survival Korean |
| Learn | `/{lang}/learn/` | TOPIK guide, grammar lessons, words by topic, hangul (+ TOPIK word lists, grammar pages) |
| Words & Talk | `/{lang}/words/` | Word of the day, drama lines, phrases, slang, polite vs casual |
| Dictionary | `/{lang}/dictionary/` | Search in your language or Korean (app data) |
| Your name in Korean | `/{lang}/name/` | Name maker (coming) |
| Level test | `/{lang}/level-test/` | Level test → goal → daily plan (coming) |

## Writing an article

**Pages CMS (web editor):** https://app.pagescms.org → `pocketkorean-site` → **Articles** → **Add an entry**.
Pick the language, section and category, add a short description, optional cover photo (with photo credit),
an optional "phrase from this story", then the text. Save → live in 1–2 minutes. Tick **Draft** to save without publishing.

Free photos with credits are in `media/library/` (see `media/library/CREDITS.md`). Photos of people may only be used in articles, not in ads.

## Cloudflare Pages settings

- Build command: `pip install -r tools/requirements.txt && python3 tools/blog.py` (runs `tools/articles.py`)
- Build output directory: `/`

## Folders

- `content/articles/` – articles (Markdown)
- `media/uploads/` – images uploaded in the CMS; `media/library/` – free photo library
- `tools/` – layout, strings, article builder
- Everything else (`/en/`, `/data/` …) is generated from the app data by the generator. Ask for changes rather than editing those pages by hand.
