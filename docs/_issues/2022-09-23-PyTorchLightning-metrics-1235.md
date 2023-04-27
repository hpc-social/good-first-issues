---
tags: enhancement
title: "Add weights for the pearson, spearman, and r2_score"
html_url: "https://github.com/Lightning-AI/torchmetrics/issues/1235"
user: DomInvivo
repo: PyTorchLightning/metrics
---

## 🚀 Feature

We can provide a weight Tensor to the regression coefficients, such as pearson, spearman, and r2_score

### Motivation

It should be relatively simple to add weights to these computations. And it can be useful in many contexts, including masking by providing 0-weights, or adding more weights to the relevant sample/target pairs.

### Pitch

Adding `weights` parameter in `pearson`, `spearman`, and `r2_score`. The parameter `weights` should be either `None`, 1D ,or 2D.

### Alternatives

None

### Additional context

See [weighted pearsonr](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient#Weighted_correlation_coefficient). For the spearmanr, it should be identical, since spearman is the correlation of the rank.

For the r2_score, there exist some implementations for example in [sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html), but it would be better to provide either a 1D or 2D matrix, and it would be broadcasted to the same shape as preds / target. instead of forcing `sample_weight` to be 1D.
