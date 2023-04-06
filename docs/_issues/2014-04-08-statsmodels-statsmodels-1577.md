---
tags: ,comp-discrete,type-enh
title: "classification performance measures"
html_url: "https://github.com/statsmodels/statsmodels/issues/1577"
user: jseabold
repo: statsmodels/statsmodels
---

Add classification performance statistics

```
def precision(pred_table):
    """
    Precision given pred_table. Binary classification only. Assumes group 0
    is the True.

    Analagous to (absence of) Type I errors. Probability that a randomly
    selected document is classified correctly. I.e., no false negatives.
    """
    tp, fp, fn, tn = map(float, pred_table.flatten())
    return tp / (tp + fp)


def recall(pred_table):
    """
    Precision given pred_table. Binary classification only. Assumes group 0
    is the True.

    Analagous to (absence of) Type II errors. Out of all the ones that are
    true, how many did you predict as true. I.e., no false positives.
    """
    tp, fp, fn, tn = map(float, pred_table.flatten())
    try:
        return tp / (tp + fn)
    except ZeroDivisionError:
        return np.nan


def accuracy(pred_table):
    """
    Precision given pred_table. Binary classification only. Assumes group 0
    is the True.
    """
    tp, fp, fn, tn = map(float, pred_table.flatten())
    return (tp + tn) / (tp + tn + fp + fn)


def fscore_measure(pred_table, b=1):
    """
    For b, 1 = equal importance. 2 = recall is twice important. .5 recall is
    half as important, etc.
    """
    r = recall(pred_table)
    p = precision(pred_table)
    try:
        return (1 + b**2) * r*p/(b**2 * p + r)
    except ZeroDivisionError:
        return np.nan
```

Also missing ROC curve.
