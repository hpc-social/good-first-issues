---
tags: enhancement
title: "Improve `dfply` test suite"
html_url: "https://github.com/zdelrosario/py_grama/issues/7"
user: zdelrosario
repo: zdelrosario/py_grama
---

dfply tool tests need work:

- Many of the tests seem redundant; can we reduce to a minimal set?
- Some of the dfply tool files have very low coverage: [`set_ops.py`](https://codecov.io/gh/zdelrosario/py_grama/src/master/grama/dfply/set_ops.py), [`subset.py`](https://codecov.io/gh/zdelrosario/py_grama/src/master/grama/dfply/subset.py), [`window_functions.py`](https://codecov.io/gh/zdelrosario/py_grama/src/master/grama/dfply/window_functions.py)