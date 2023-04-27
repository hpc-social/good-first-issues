---
tags: feat/enhancement,help-wanted,question,research
title: "Parallelism of calculations in pyhf ala joblib (or similar)"
html_url: "https://github.com/scikit-hep/pyhf/issues/807"
user: kratsg
repo: scikit-hep/pyhf
---

# Description

There are starting to be locations in `pyhf` where one can start parallelizing certain calculations on behalf of the user (rather than the user explicitly parallelizing). For example, one that will come up is with the toy calculation added in #790 where we need to do a for-loop and calculate the test statistic for each toy.

This cannot be batched or vectorized quite simply because a statistical fit is performed for each toy (and num iterations is not necessarily the same for each toy). There may be other good examples in the code-base in the future that we will want the parallelism.

## Is your feature request related to a problem? Please describe.

No.

### Describe the solution you'd like

Perhaps something like `pip install pyhf[toytools]` or `pyhf[toys-joblib]` or `pyhf[toys-dask]`.

### Describe alternatives you've considered

Dunno. I didn't think hard enough yet.

# Relevant Issues and Pull Requests

- PR #790 

# Additional context

Nope.