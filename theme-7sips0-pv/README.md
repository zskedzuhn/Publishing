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
