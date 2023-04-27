---
tags: help-wanted
title: "ipython Sphinx directive executes code when excluded by only, ifconfig"
html_url: "https://github.com/ipython/ipython/issues/9339"
user: cgranade
repo: ipython/ipython
---

The `ipython` directive for Sphinx provided by `IPython.sphinxext.ipython_directive` executes its code block at the parsing stage. As a result, even if an `ipython` directive is surrounded by an `only` or `ifconfig` directive with a false-y condition, the code block is still executed. I have posted a [minimum working example](https://gist.github.com/cgranade/3cc6b87c8efef89d54b5) for this issue that includes a Sphinx configuration file and a reStructuredText file to reproduce the problem.
