---
tags: c-methods,help-wanted,s-keep-open,t-feature-request
title: "More categorical and numeric split types for decision trees"
html_url: "https://github.com/mlpack/mlpack/issues/884"
user: rcurtin
repo: mlpack/mlpack
---

Right now, the decision tree implementation in `src/mlpack/methods/decision_tree/` has only the `AllCategoricalSplit` for categorical splits and the `BestBinaryNumericSplit` for numeric splits.  Ideally, we would like to expand this to handle some other types of splits.

This is a very open-ended issue: we should survey the literature, find decent split ideas to add, and then implement and test them.

The primary split I am thinking about as I write this ticket is something faster than `BestBinaryNumericSplit` based on sampling: instead of searching every possibly binary numeric split exhaustively, merely sampling a few could be sufficient.

Another interesting idea is "Extremely Randomized Trees": http://orbi.ulg.be/bitstream/2268/9357/1/geurts-mlj-advance.pdf

In that idea, you don't use the data to determine the split, you merely choose the split randomly.  (That tends to be best in ensemble settings, and we don't have a random forest right now, but that will change soon-ish.)