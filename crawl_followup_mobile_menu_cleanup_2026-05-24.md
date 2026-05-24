# DeFiliban Crawl Follow-up: Mobile Menu Cleanup

Date: 2026-05-24

Source crawl:

- `/home/qcweb/defiliban crawl 24-5-2026/internal_all.csv`
- `/home/qcweb/defiliban crawl 24-5-2026/all_inlinks.csv`

## Main Finding

The remaining high-volume `301` and `404` issues are coming from the mobile header / mobile collapse menu, not from article body content.

## Priority Targets

### 1. Remove legacy demo homepage links from the mobile menu

These URLs already redirect correctly, but they still receive thousands of internal links:

- `https://defiliban.io/home-coin/` -> `301` to homepage
  - `6380` inlinks
  - mobile header quick link anchor: `Home`
  - mobile collapse submenu anchor: `Home 1`
- `https://defiliban.io/coin-home-5/` -> `301` to homepage
  - `3190` inlinks
  - mobile collapse submenu anchor: `Home 5`

Observed menu items and paths:

- `menu-item-2515` -> `Home` -> `/home-coin/`
- `menu-item-2517` -> `Home 1` -> `/home-coin/`
- `menu-item-2526` -> `Home 5` -> `/coin-home-5/`

Recommended action:

- remove these menu items from the mobile menu entirely
- do not just keep the `301`; remove the source links

### 2. Remove dead page-id links still present in the mobile submenu

These are still rendering as direct `404` targets:

- `https://defiliban.io/?page_id=2389`
  - `3190` inlinks
  - anchor: `Home 2`
- `https://defiliban.io/?page_id=2413`
  - `3190` inlinks
  - anchor: `Home 4`

Observed menu items and paths:

- `menu-item-2516` -> `Home 2` -> `/?page_id=2389`
- `menu-item-2525` -> `Home 4` -> `/?page_id=2413`

Recommended action:

- remove both menu items from the mobile collapse menu
- if they still exist in WordPress menu management, delete them instead of editing only the URL

### 3. Decide whether `Contact` should stay indexed

Current state:

- `https://defiliban.io/contact/`
- `200`
- `indexable`
- `3215` inlinks
- source appears in the mobile header quick links

Observed menu item:

- `menu-item-2514` -> `Contact`

Recommended action:

- if `Contact` is only a utility page, set it to `noindex,follow`
- keep the link for users if needed, but it should not compete as a search landing page

## Where The Links Are Coming From

The strongest repeated paths are:

- mobile quick-view header links
- mobile collapse navigation submenu under the old home/demo section

These are not isolated links inside article content. They are template-level links repeated across thousands of pages.

## Fast Fix Checklist

1. Open the mobile menu or header menu structure in WordPress / Foxiz menu settings.
2. Find the old demo/home submenu under parent item `menu-item-2496`.
3. Remove:
   - `Home`
   - `Home 1`
   - `Home 2`
   - `Home 4`
   - `Home 5`
4. Review whether `Contact` should remain indexed.
5. Purge cache.
6. Re-crawl only these targets to confirm:
   - `/home-coin/`
   - `/coin-home-5/`
   - `/?page_id=2389`
   - `/?page_id=2413`
   - `/contact/`
