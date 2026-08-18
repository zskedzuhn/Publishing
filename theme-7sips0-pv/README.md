# 7sips0-pv.myshopify.com — theme pull

Full pull of the live ("Zendrop") theme from the Shopify store `7sips0-pv.myshopify.com`,
equivalent to running:

```
shopify theme pull --store 7sips0-pv.myshopify.com
```

This is a separate, unrelated store from the one covered by `theme/` and `marketing/`
elsewhere in this repo (musicsplitsheets.com) — kept in its own directory to avoid mixing
the two.

Pulled via the Shopify Admin API's `OnlineStoreTheme.files` GraphQL field rather than the
Shopify CLI directly: the CLI's browser-based device-authorization flow (`POST
https://accounts.shopify.com/oauth/device_authorization`) returned an HTTP 403 from
Shopify's own server in this sandboxed environment, unrelated to any local proxy
configuration. The already-authorized Shopify MCP connector for this store was used
instead to fetch the same file contents.

## WAGBOUND rebuild (August 2026)

This store was rebuilt as a single-product brand, **WAGBOUND**, around the
**Wagbound GoBottle™** (3-in-1 dog travel bottle: water bowl, food compartment, waste-bag
holder). Changes made directly on the live store via the Shopify Admin API:

- All 10 unrelated dropshipping products (toys, grooming tools, pet accessories, etc.)
  permanently deleted.
- Wagbound GoBottle™ (`wagbound-gobottle`): vendor/type/tags set to Wagbound branding,
  fake "was $53.91 / $43.58" compare-at pricing cleared from all 8 variants (500ml marked
  Recommended, real price $34.99 with no invented discount), image alt text corrected.
- Wagbound GoBottle™ 2-Pack (`wagbound-gobottle-2-pack`): published (was an unpurchasable
  draft with 0 inventory), $54.99, inventory stocked.

Theme changes (`templates/index.json`, `templates/product.json`,
`config/settings_data.json` in this directory) were pushed to a new **unpublished**
duplicate theme, `WAGBOUND — Go Further Together (publish me)`, because the Shopify MCP
connector blocks file writes and publishing on the live/MAIN theme. The homepage was
rebuilt around "Go Further. Together." (problem → three functions → lifestyle use cases →
product demo → CTA), the product page and cart drawer had fake urgency/rating/testimonial
blocks removed (`HOT PRODUCT | LOW STOCK` badge, fake "(126 Reviews)" and "4.5 out of 5
stars" claims, an invented "ORDER NOW AND RECEIVE IN 4 DAYS" shipping estimate, a fake
three-quote testimonial carousel, an empty placeholder comparison table, and a fake
"Cart reserved for 4 minutes" countdown), and the color scheme was changed to cream
(`#F5F1E8`) / charcoal (`#2B2B28`) / muted forest green (`#4A5D45`). The "Free Worldwide
Shipping" announcement was kept as-is since the store has a real, active Free Shipping
delivery method configured — everything else fabricated or unverifiable was removed
rather than reworded.

**Manual step required:** go to **Online Store → Themes → WAGBOUND — Go Further Together
(publish me) → Publish** to make this live (Shopify's API does not allow publishing
themes). Preview first at
`https://7sips0-pv.myshopify.com/?preview_theme_id=148121944138`.
