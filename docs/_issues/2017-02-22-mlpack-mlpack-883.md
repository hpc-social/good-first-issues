---
tags: ,c-methods,help-wanted,s-keep-open,t-feature-request
title: "MDL penalty for decision tree splits"
html_url: "https://github.com/mlpack/mlpack/issues/883"
user: rcurtin
repo: mlpack/mlpack
---

There's a new decision tree implementation in `src/mlpack/methods/decision_tree/`.  This implementation is pretty similar to J48 from Weka or C4.5 (but not exactly the same).  The basic structure of finding a split is:

  1. Calculate gain for all possible splits.
  2. Pick split with the best gain.

In this implementation, the splits themselves are determined by the `NumericSplitType` and `CategoricalSplitType` template parameters, and the gain function is the `FitnessFunction` template parameter.

In order to reduce overfitting, often a penalty parameter is applied to the gain.  In C4.5, the penalty that's used is called the 'minimum descriptor length' (MDL) penalty, and the penalized gain is calculated as

```
penalized gain = gain - log2(number of children / sum of weights)
```

where a binary split has `number of children = 2`, and the `sum of weights` refers to the sum of the instance weights over all points (see #882), and if instance weights are not being used, then the sum of weights is just equal to the number of points in the set that's being split.

A PR to fix this should have an implementation of this MDL penalty that can be turned on or off by the user (probably through template parameters but not necessarily), and tests to ensure that the MDL penalty calculation works.