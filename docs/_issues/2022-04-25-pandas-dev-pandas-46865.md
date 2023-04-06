---
tags: ,Code-Style
title: "STYLE replace flake8-rst with something maintained"
html_url: "https://github.com/pandas-dev/pandas/issues/46865"
user: MarcoGorelli
repo: pandas-dev/pandas
---

Currently, we use flake8-rst for running flake8 in code snippets in rst files:

https://github.com/pandas-dev/pandas/blob/2e56a838cf5ed3058df16c11e5ebae862520bab7/.pre-commit-config.yaml#L95-L102

However, flake8-rst isn't maintained, and is currently run in its own environment with a different flake8 version because of incompatibilities with flake8 v4

Task here is:
- search around to see if there's a maintained tool which does the same thing (runs flake8 on code snippets in rst files)
- try using that instead, fixup any new errors which may result from running it via `pre-commit` on all files
- make a PR