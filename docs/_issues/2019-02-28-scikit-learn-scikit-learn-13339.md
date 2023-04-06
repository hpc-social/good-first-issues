---
tags: ,modulemultioutput
title: "Bad error messages in ClassifierChain on multioutput multiclass"
html_url: "https://github.com/scikit-learn/scikit-learn/issues/13339"
user: amueller
repo: scikit-learn/scikit-learn
---

trying to run classifier chain on a multiclass problem with a reshaped y (which is interpreted as multioutput multiclass) doesn't work (see #9245), which is fine. But the error messages are really bad making it hard to understand what's going on.

We should detect that we're trying to do multioutput multiclass instead of multilabel and give an informative error.