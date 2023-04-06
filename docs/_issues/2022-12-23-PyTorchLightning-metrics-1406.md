---
tags: ,enhancement,help-wanted
title: "Add `.plot()` to all modular metrics"
html_url: "https://github.com/Lightning-AI/torchmetrics/issues/1406"
user: SkafteNicki
repo: PyTorchLightning/metrics
---

## 🚀 Feature

We are in the process of adding native plotting to torchmetrics such that our users can easily create simple plots of metrics, which is especially useful for metrics such as confusion matrix and pr-curves but even single-scalar metrics such as accuracy it can be beneficial to quickly create a plot of computed values.

The first proof of concept PR has just been merged: https://github.com/Lightning-AI/metrics/pull/1328

We are inviting anyone interested in contributing to torchmetrics to help add this feature to all remaining metrics. The tasks are fairly simple and an example of how to implement the `plot` metric can be seen here: https://github.com/Lightning-AI/metrics/blob/d8caeeb28efc0afb86ae68cf66b06412749a4e46/src/torchmetrics/classification/accuracy.py#L110-L156

We would like the work divided into PRs tackling each domain, however if any are interested in only contributing to a few metrics within a particular domain that is also more than welcome.

- [x] Aggregation ->#1485 @SkafteNicki 
- [x] Audio ->#1434 @shhs29
- [x] Classification -> #1624 #1638 @srishti-git1110
- [x] Image ->#1480 @venomouscyanide
- [x] Nominal -> #1581 @SkafteNicki
- [x] Multimodal -> https://github.com/Lightning-AI/metrics/pull/1639 @SkafteNicki 
- [x] Detection -> #1585 @SkafteNicki
- [x] Regression -> #1609 #1621 @srishti-git1110
- [x] Retrieval -> #1610 #1623 @ufukhurriyetoglu
- [x] Text -> #1631 @ufukhurriyetoglu
- [x] Wrappers -> https://github.com/Lightning-AI/metrics/pull/1639 @SkafteNicki 
