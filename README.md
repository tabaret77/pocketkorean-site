# pocketkorean.com

The website for Pocket Korean, hosted on Cloudflare Pages.

## Writing a blog post

**Easiest: Pages CMS (web editor)**
1. Go to https://app.pagescms.org and sign in with GitHub.
2. Open the `pocketkorean-site` repository → **Blog posts** → **Add an entry**.
3. Fill in title, language, date, a short description and the content. Images can be uploaded into the post or as a cover.
4. Click **Save**. Cloudflare rebuilds the site and the post is live in about 1–2 minutes.
   Tick **Draft** to save without publishing.

**Or directly on GitHub**
Add a Markdown file to `content/blog/`, named `YYYY-MM-DD-short-title.md`, with front matter like the example post in that folder.

## Cloudflare Pages settings

- Build command: `pip install -r tools/requirements.txt && python3 tools/blog.py`
- Build output directory: `/`

`tools/blog.py` turns `content/blog/*.md` into pages under `/{language}/blog/`, adds the latest posts to each language home page and writes `sitemap-blog.xml`.

## Folders

- `content/blog/` – blog posts (Markdown)
- `media/` – images uploaded for blog posts
- `tools/` – blog builder and shared page layout
- Everything else (`/en/`, `/vi/` … word lists, grammar pages) is generated from the app data. Ask for changes rather than editing those pages by hand, because they are regenerated.
