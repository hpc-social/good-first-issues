---
tags: ,easy,enhancement
title: "`WoEEncoder` should return a list with all the variables that have 0 in the denominator of the WoE"
html_url: "https://github.com/feature-engine/feature_engine/issues/430"
user: solegalli
repo: feature-engine/feature_engine
---

At the moment, the transformer fails when it encounters one variable with 0 in the denominator of the WoE formula. We would like it to assess and raise an error with all the variables that show this behaviour.