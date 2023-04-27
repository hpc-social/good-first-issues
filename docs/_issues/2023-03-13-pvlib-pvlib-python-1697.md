---
tags: easy,help-wanted
title: "`pvlib.irradiance.poa_horizontal_ratio` should be removed"
html_url: "https://github.com/pvlib/pvlib-python/issues/1697"
user: mikofski
repo: pvlib/pvlib-python
---

**Describe the bug**
Currently `pvlib.irradiance.poa_horizontal_ratio` is untested according to codecov

**To Reproduce**
Steps to reproduce the behavior:
1. Go to https://app.codecov.io/gh/pvlib/pvlib-python/blob/main/pvlib/irradiance.py#L259

**Expected behavior**
100% test coverage

**Screenshots**
![image](https://user-images.githubusercontent.com/1385621/224845991-8b9f4068-8572-4d2c-97be-cf2970ece077.png)

**Versions:**
 - ``pvlib.__version__``: 0.9.5-dirty
 - ``pandas.__version__``: ?
 - python: ?

**Additional context**
This causes codecov to fail for any edits to irradiance.py that reduce the number of lines because then code coverage goes down.
