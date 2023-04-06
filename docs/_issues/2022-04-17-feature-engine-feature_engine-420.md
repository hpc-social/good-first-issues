---
tags: ,enhancement
title: "expand non_fitted_error_checks for methods get_feature_names_out and inverse transform"
html_url: "https://github.com/feature-engine/feature_engine/issues/420"
user: solegalli
repo: feature-engine/feature_engine
---

Methods transform, inverse_transform, get_feature_names_out and other specific methods (see DropMissingData) should run only after the transformer was fit.

At the moment, we test that this is the case only for the transform method. We should expand this to test all methods.

