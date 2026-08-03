# musicsplitsheets.com — Conversion Optimization (August 2026)

Theme sections for the Shopify store at [musicsplitsheets.com](https://musicsplitsheets.com).

## What changed and why

The store had 370 sessions over 60 days with **zero add-to-carts** after switching from a
buy-once PDF to a pay-per-sheet online builder. Root causes found in the builder flow:

1. **No link between payment and delivery.** The PDF was generated client-side (jsPDF) from
   `localStorage` on `/pages/download`. Nothing after Shopify checkout returned the customer
   to that page, and checking out on another device (or the Shop app) lost the data entirely.
2. **Free-rider hole.** `/pages/download` never verified payment — anyone who filled the form
   could download without paying.
3. **Trust-killing interstitial.** Before checkout, a full-screen gate warned customers to
   bookmark a link that "only works in the same browser" — maximum anxiety at the moment of payment.

Sales data agreed: 5 orders in March under the original buy-once model, ~zero after the switch.

## Changes in this repo

- `theme/sections/custom-homepage.liquid` — homepage repositioned around the buy-once model
  ("buy once, reuse forever"), one-click checkout cart permalinks, new Catalogue Audit
  cross-sell section (services from $497 were previously not linked anywhere on the homepage),
  updated FAQ + JSON-LD structured data for the new prices ($7 / $12).
- `theme/sections/split-sheet-form.liquid` — `/pages/create` (the retired builder) is now a
  simple sales page with buy buttons; includes a rescue note for past builder customers.
- `sections/split-sheet-download.liquid` — intentionally left as-is so past customers can
  still retrieve documents from their browser.

## Deployment

These files are staged on the unpublished Shopify theme
**"Conversion Update — Aug 2026 (publish me)"** (`gid://shopify/OnlineStoreTheme/189744415002`),
a duplicate of the live theme. The Shopify API does not allow publishing themes, so go to
**Online Store → Themes → Conversion Update — Aug 2026 → Publish** after previewing.

Store-side changes already applied via Admin API (independent of theme publish):

- Music Split Sheet: $3 → **$7**, description rewritten for buy-once positioning
- Music Split Sheet + Letter of Direction: $5 → **$12**, description rewritten
- Mini High Speed Handheld Fan: set to **Draft** (off-brand for a legal-documents store)

**Manual step required:** attach the actual PDF files to both products in the
Digital Downloads app (or equivalent) so buyers receive the files after checkout.
