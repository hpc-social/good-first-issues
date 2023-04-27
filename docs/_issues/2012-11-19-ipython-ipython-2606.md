---
tags: bug
title: "Fallback to pydoc if site._Helper is not defined"
html_url: "https://github.com/ipython/ipython/issues/2606"
user: eudoxos
repo: ipython/ipython
---

ipython uses site._Helper as `help()` function. In some cases (specifically, when running in frozen pyInstaller setup), `site.py` is not have the same implementation as the one shipped with cpython. Since `site._Helper` is an internal function (leading underscore), there should be a fallback in case of `ImporrError` implementing `site._Helper` locally (http://hg.python.org/cpython/file/cf606c403f14/Lib/site.py#l445)
