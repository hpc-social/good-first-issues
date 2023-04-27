---
tags: documentation
title: "conda-forge download statistics"
html_url: "https://github.com/icesat2py/icepyx/issues/301"
user: JessicaS11
repo: icesat2py/icepyx
---

Currently we track (and visualize) GitHub clones and PyPI downloads [here](). It would be great to add conda-forge data to this. Steps required (draft list):
- [ ] build Python script to access/download and visualize data
- [ ] determine the best way to do above (likely via this [anaconda package data library](https://github.com/ContinuumIO/anaconda-package-data))
- [ ] create a GitHub action to run the script regularly and commit the results