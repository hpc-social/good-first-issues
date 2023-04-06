---
tags: ,python
title: "Extend Callback Interface"
html_url: "https://github.com/catboost/catboost/issues/1942"
user: ayulockin
repo: catboost/catboost
---

I am working on creating a `WandbCallback` for Weights and Biases. I am glad that CatBoost has a callback system in place but it would be great if we can extend the interface. 

The current callback only supports `after_iteration` that takes `info`. Taking inspiration from XGBoost callback system it would be great if we can have `before iteration` that takes `info`, `before_training`, and `after_training` that takes `model`.

Something similar to this would be awesome: https://github.com/dmlc/xgboost/blob/eee527d2647d22a1f68d804672c78f82da4bcd31/python-package/xgboost/callback.py#L23

Are there any plans to roll it out in the near future?