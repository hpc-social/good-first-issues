---
tags: feat/enhancement
title: "xml2json recursively search for the root data file"
html_url: "https://github.com/scikit-hep/pyhf/issues/696"
user: kratsg
repo: scikit-hep/pyhf
---

# Description

When running xml2json, it's often configured that the input file prefix is `results/<analysis name>/<filename>.root` which is not necessarily something I make initially when I copy over the files. In these cases, I'd want `xml2json` to just search the directory I'm running in for the root file (i.e. using its basename).