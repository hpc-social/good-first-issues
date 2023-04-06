---
tags: ,Good-first-issue,enhancement
title: "when ~ncores=1, Parmap should not fork"
html_url: "https://github.com/rdicosmo/parmap/issues/77"
user: UnixJunkie
repo: rdicosmo/parmap
---

We don't want Parmap to be invoked in vain.
Also, this would ease writing tests for Parmap.
List.map is equivalent to Parmap.map ~ncores:1 and there is almost no overhead.
