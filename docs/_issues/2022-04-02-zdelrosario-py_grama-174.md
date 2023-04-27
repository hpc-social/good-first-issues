---
tags: enhancement
title: "Consistent treatment of `nan` in summary functions"
html_url: "https://github.com/zdelrosario/py_grama/issues/174"
user: zdelrosario
repo: zdelrosario/py_grama
---

Right now `gr.mean()` will silently drop `nan`'s, while `gr.corr()` will not. Make the default behavior to throw an error on `nan`, with an argument to drop `nan`'s; make this syntax consistent across all summary functions.