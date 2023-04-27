---
tags: easy,enhancement
title: "add missing_only=True to all imputers to use in combination with variables=None"
html_url: "https://github.com/feature-engine/feature_engine/issues/388"
user: solegalli
repo: feature-engine/feature_engine
---

Add missing_only functionality to all imputers to use in combination with variables=None

When variables is None, the imputers select all numerical, or categorical or all variables by default. With the missing_only, it would select only those from each subgroup that show missing data during fit.
