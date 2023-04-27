---
tags: IS2HW_2022
title: "add page size checks for sync/async request mode"
html_url: "https://github.com/icesat2py/icepyx/issues/243"
user: JessicaS11
repo: icesat2py/icepyx
---

There's still a reference to using a smaller page size in `examples/examples/ICESat-2_DAAC_DataAccess_Example.ipynb` because it refers to synchronous requests. Note that this notebook indicates that synchronous requests are done by default, but I think this must be outdated. It looks like the request mode is `async` by default (https://github.com/icesat2py/icepyx/blob/development/icepyx/core/APIformatting.py#L446).

Given that the page size limit is only 100 when the request mode is synchronous, maybe we need another check somewhere that decreases the page size when a user overrides that default and uses synchronous mode?

_Originally posted by @trey-stafford in https://github.com/icesat2py/icepyx/issues/239#issuecomment-963612931_