---
tags: Clean,IO-HTML
title: "CLN: Use dedup_names in all instances where duplicate column names are renamed"
html_url: "https://github.com/pandas-dev/pandas/issues/50371"
user: datapythonista
repo: pandas-dev/pandas
---

In #50370 the function `dedup_names` has been moved to `pandas.io.common` so it can be reused by any reader dealing with duplicate column names. The function can be expanded in the future to allow custom renaming patterns, so it should be used by any reader, to make sure we keep consistency with the behavior (as well as avoid duplicate code). There is at least one instance identified in #50370 where a different implementation is used to rename the duplicate columns. We should call `dedup_names` instead, and in case other alternative implementations exist, find them and also call `dedup_names`.