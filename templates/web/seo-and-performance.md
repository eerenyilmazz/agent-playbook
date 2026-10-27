---
scope: task
template: web
owner: Eren
status: draft
---
# SEO and Performance

Performance targets: see templates/software/performance-budget.md.

## SEO basics
- Unique `<title>` and meta description per page.
- One `h1` per page matching its main topic.
- Clean, stable URLs. Changing a URL requires a 301 redirect.
- `canonical` tag on pages with duplicates (filters, parameters).
- `sitemap.xml` and `robots.txt` present and correct.
- Structured data (JSON-LD) where relevant: organization, product, article, breadcrumb.
- Open Graph and Twitter card tags for shareable pages.
- Content that must be indexed is server-rendered or pre-rendered.
- `lang` attribute set; `hreflang` for multi-language sites.

## Performance for SEO
- Images: modern formats (WebP/AVIF), explicit width/height, lazy-load below the fold.
- Fonts: limit families and weights; use `font-display: swap`.
- Third-party scripts loaded async/defer and reviewed before adding.

## Rules
- Run Lighthouse on key pages before release; investigate any drop.
- Staging must be `noindex`; production must not be.
