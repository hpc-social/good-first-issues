---
tags: ,enhancement,plotting
title: "ENH: expose `greedy` colouring from mapclassify"
html_url: "https://github.com/geopandas/geopandas/issues/2818"
user: martinfleis
repo: geopandas/geopandas
---

Mapclassify has a function to create labels for topological colouring (xref #1165) called [`greedy`](https://pysal.org/mapclassify/generated/mapclassify.greedy.html#mapclassify.greedy). We could expose it as another option in `plot` and `explore`  under the `scheme` keyword as `scheme="greedy"` and pass the other kwargs through `classification_kwds`. 

Before passing the `scheme` to `mapclassify.classify` we would need to catch that the value is `greedy` and use `mapclassify.greedy` instead.

https://github.com/geopandas/geopandas/blob/e62b74a81428e6ab8ced23d688424a83bdabb686/geopandas/plotting.py#L772-L774