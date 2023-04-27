---
tags: SciPy-Conference,research,tests
title: "Investigate use of testbook for testing Jupyter notebooks"
html_url: "https://github.com/scikit-hep/pyhf/issues/925"
user: matthewfeickert
repo: scikit-hep/pyhf
---

# Description

At SciPy 2020 @rohitsanj gave a (very good) lightning talk on [nteract's `testbook`](https://github.com/nteract/testbook) which is used for unit testing Jupyter Notebooks. Given that Carol Willing mentioned it is designed to be complimentary with [`papermill`](https://github.com/nteract/papermill) it might be worth seeing if it can be used in our testing of the example notebooks in CI.

cc @phinate as [`neos`](https://github.com/pyhf/neos) uses lots of notebooks.