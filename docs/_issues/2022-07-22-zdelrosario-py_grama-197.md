---
tags: ,invalid
title: "ValueErrors that should be TypeErrors"
html_url: "https://github.com/zdelrosario/py_grama/issues/197"
user: mstites
repo: zdelrosario/py_grama
---

While working on Issue #188 / PR #195 I noticed that across the code base there are a number of places that use ValueErrors that should be TypeErrors. For example, in grama/comp_building.py line 59 & 60 read:
```
elif out is None:
        raise ValueError("`out` must be list or int")
```
This is an error for an invalid type (give out argument is None) but it throws a ValueError. This doesn't match Python naming conventions. This happens many places across the code base and this should be updated for user readability and matching the syntax of other packages. I went ahead and updated the eval functions, but the rest of the code base still needs to be updated.

This should be a simple fix of just updating the error type, and updating the associated unittests.