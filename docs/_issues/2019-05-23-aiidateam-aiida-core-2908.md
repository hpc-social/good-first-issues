---
tags: ,topic/documentation
title: "Installation instructions should ensure that the terminal preferred encoding is UTF8"
html_url: "https://github.com/aiidateam/aiida-core/issues/2908"
user: giovannipizzi
repo: aiidateam/aiida-core
---

Otherwise packages (e.g. `click-spinner` would fail), because open() will try to open with the default locale (often ASCII), see [here](https://docs.python.org/3.7/library/functions.html#open).

This can be fixed by setting the locale to UTF-8, e.g. by running:
```bash
export LANG=UTF-8
export LC_ALL=UTF-8
```
(probably only the second one is needed).

Better to put this in the `~/.bashrc` or at least in the `bin/activate` of the venv so that it works in all terminals.