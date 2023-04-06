---
tags: ,bug
title: "Add Windows filesystem support"
html_url: "https://github.com/ml-evs/matador/issues/151"
user: ml-evs
repo: ml-evs/matador
---

Several parts of matador that read non-source-code files use hardocded unix-style paths. Instead it should use pathlib so that it works on Windows too.