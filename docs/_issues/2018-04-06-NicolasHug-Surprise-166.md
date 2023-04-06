---
tags: ,enhancement
title: "measures param for grid search and cross_validate should support callables"
html_url: "https://github.com/NicolasHug/Surprise/issues/166"
user: NicolasHug
repo: NicolasHug/Surprise
---

For now only strings are accepted as the `measures` parameter in `GridSearchCV`, `RandomizedSearchCV`, and `cross_validate`. It's thus impossible to use those with measures that take specific parameters as input (e.g. #156 ), or to use custom measures.

We should then accept callables in addition to strings.

Each callable should only take the `predictions` parameter. In order to handle measures with mulptile parameters, we could implement a `make_measure` helper (much like sklearn make_scorer) which would simply perform some partial application on the parameters, and set a `greater_is_better` parameter (this would clean a bit the current code).

Any other option is welcome