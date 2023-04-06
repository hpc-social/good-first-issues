---
tags: ,docs,feat/enhancement
title: "Test all the Jupyter notebooks in the CI"
html_url: "https://github.com/scikit-hep/pyhf/issues/168"
user: matthewfeickert
repo: scikit-hep/pyhf
---

As [pointed out in PR #167](https://github.com/diana-hep/pyhf/pull/167#issuecomment-388632090) we currently don't test all the Jupyter notebooks even though they all end up in the docs (well, with the exception of the Binder test notebook which the docs don't pick up (do we want them to?)). Instead we only test a few core notebooks:
- `ShapeFactor.ipynb`
- `multichannel-coupled-histo.ipynb`
- `multiBinPois.ipynb`

Ideally if something ends up in the docs it should really be tested first, so we should add testing of all the notebooks to `test_notebooks.py`.
