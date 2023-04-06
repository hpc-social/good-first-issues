---
title: "use `world` instead of `usa` for default basemap"
html_url: "https://github.com/ropensci/rinat/issues/52"
user: stragu
repo: ropensci/rinat
---

The current default value for the `map` argument is `usa` in function `inat_map()`, which is a very US-centric choice and creates rubbish maps in many cases when the data is not located in or close to the US.

We should use the `world` basemap, also provided by the maps package, and mention the other basemap available by default (`france`, `italy`, `nz` and `usa`).

This is a breaking change as it would produce different maps in existing scripts using the default argument value (but would not produce an error or warning).