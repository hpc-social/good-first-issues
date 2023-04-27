---
title: "More concise error message with feature name, not only feature_idx "
html_url: "https://github.com/catboost/catboost/issues/2044"
user: fingoldo
repo: catboost/catboost
---

Problem:
```
_catboost.pyx in _catboost._set_features_order_data_pd_data_frame()

_catboost.pyx in _catboost.get_cat_factor_bytes_representation()

CatBoostError: Invalid type for cat_feature[non-default value idx=1,feature_idx=336]=2.0 : cat_features must be integer or string, real number values and NaN values should be converted to string.

```
Could you also print a feature name, not only feature_idx (if names are available, of course)? It's not easy to find out what is causing the problem if one uses a complex pipeline with dynamic transformers.

catboost version:
1.0.4
Operating System:
Win
CPU:
+
GPU:
+
