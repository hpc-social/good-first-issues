---
tags: ,feat/enhancement
title: "Loading json schema via pkgutil"
html_url: "https://github.com/scikit-hep/pyhf/issues/995"
user: alexander-held
repo: scikit-hep/pyhf
---

# Question

This is a small suggestion, feel free to close without comment since the current implementation works perfectly fine as far as I can tell. I came across [this stackoverflow comment](https://stackoverflow.com/questions/6028000/how-to-read-a-static-file-from-inside-a-python-package/58941536#58941536) when investigating how to validate against a json schema (which I need to obtain from my package), and had a look at how `pyhf` does it in parallel. The comment suggests using `pkgutil` instead of `pkg_resources` (which `pyhf` uses) or `importlib.resources`. See also the discussion below the comment, it seems like `pkgutil` might eventually be replaced by something else but seems fine for now.

# Relevant Issues and Pull Requests

none I'm aware of
