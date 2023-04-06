---
tags: ,bug,docs,follow-up
title: "Revise decorators to allow for docstring rendering"
html_url: "https://github.com/scikit-hep/pyhf/issues/673"
user: matthewfeickert
repo: scikit-hep/pyhf
---

# Description

All functions that are currently wrapped by decorators (such as [`pyhf.set_backend`](https://scikit-hep.org/pyhf/_generated/pyhf.set_backend.html#pyhf.set_backend)) are unable to produce proper docstrings that can be rendered by Sphinx. As outlined in this [post by Hynek Schlawack](https://hynek.me/articles/decorators/) a solution would to be to use something like [`wrapt`](https://github.com/GrahamDumpleton/wrapt) to avoid this.

This should be investigated to make sure the API is properly documented on the website.