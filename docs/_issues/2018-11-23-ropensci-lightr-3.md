---
tags: ,Type-enhancement
title: "Allow user to choose parser in get_spec and get_metadata"
html_url: "https://github.com/ropensci/lightr/issues/3"
user: Bisaloo
repo: ropensci/lightr
---

This may be useful, especially for `get_metadata()` to handle `.txt` files because `parse_generic()` returns `NA` for metadata.

```r
get_metadata(where = ".", ext = "txt", parser = parse_jaz)
```