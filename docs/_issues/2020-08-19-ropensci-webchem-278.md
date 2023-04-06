---
tags: bug,consistent-api
title: "column types not consistent in etox_targets()"
html_url: "https://github.com/ropensci/webchem/issues/278"
user: Aariq
repo: ropensci/webchem
---

`etox_targets()` returns a list of data.frames (and URLs for microattribution).  It is not easy to bind the data.frames together because at least the `Duration` column is sometimes character and sometimes integer.

```r
> library(webchem)
> library(purrr)
> library(dplyr)
> etox_data <-etox_tests(c(8668, 8494))
Querying https://webetox.uba.de/webETOX/public/basics/stoff.do?id=8668
Querying https://webetox.uba.de/webETOX/public/basics/stoff.do?id=8494
Warning message:
In FUN(X[[i]], ...) : NAs introduced by coercion
> map(etox_data, ~pluck(.x, "res")) %>% bind_rows()
Error: Can't combine `..1$Duration` <character> and `..2$Duration` <integer>.
```

P.S., this would be a breaking change, but wouldn't it be better for the output to just be a single tidy dataframe with the URLs as an additional column or stored as an attribute?