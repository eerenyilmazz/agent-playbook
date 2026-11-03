---
scope: task
when: Public web pages, landing pages, content sites
owner: Eren
status: draft
---
# SEO and Performance

Speed targets: templates/software/performance-budget.md.

## Per page
- Unique `<title>` (≤ 60 chars) and meta description (≤ 155).
- One `h1`; `lang` set; `canonical` for duplicate/param URLs.
- Open Graph + Twitter card for shareable pages.
- JSON-LD where relevant (Organization, Product, Article, BreadcrumbList, LocalBusiness).

## Site
- Indexable content server-rendered or pre-rendered.
- `sitemap.xml`, `robots.txt`; staging `noindex`, production indexable.
- Stable URLs; changes get 301 redirects. No redirect chains.
- `hreflang` for multi-language.
- Custom 404 returning real 404 status.

## Assets
- Images: WebP/AVIF, `srcset`, explicit width/height, lazy below the fold, priority for LCP image.
- Fonts: ≤ 2 families, subset, `font-display: swap`, preload critical.
- Third-party scripts: async/defer, reviewed before adding, loaded after consent if tracking.

## Verify
Lighthouse on key pages before release; investigate any drop. Search Console connected.
