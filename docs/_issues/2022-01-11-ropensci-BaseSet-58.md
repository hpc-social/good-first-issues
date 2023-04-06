---
tags: 
title: "sets %in% sets"
html_url: "https://github.com/ropensci/BaseSet/issues/58"
user: llrs
repo: ropensci/BaseSet
---

There are several cases of `sets %in% sets` on the length.R file.
Not sure if it is a bug, probably it is really `isTRUE(all(sets %in% sets))` so it wouldn't matter, but if it is so it can be safely removed. 
https://github.com/ropensci/BaseSet/blob/4b376bb9ef2071b7e3985b2b4aee0354c84e0a8e/R/length.R#L186