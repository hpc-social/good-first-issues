---
tags: API,refactor
title: "Add aliases for common accessors"
html_url: "https://github.com/scikit-hep/pyhf/issues/595"
user: kratsg
repo: scikit-hep/pyhf
---

# Description

We should provide some nice aliases to make things easier to use in `pyhf` overall such as:
- `pyhf.tb` to `pyhf.tensorlib`
- `pyhf.np` to `pyhf.tensor.numpy_backend`
- `pyhf.tf` to `pyhf.tensor.tensorflow_backend`
- `pyhf.opt` to `pyhf.optimizer`

and so on. These should all map to the longer name versions.