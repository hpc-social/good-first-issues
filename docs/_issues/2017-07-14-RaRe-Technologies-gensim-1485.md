---
tags: Hacktoberfest,bug,difficulty-medium
title: "proper check for filename before calling subprocess"
html_url: "https://github.com/RaRe-Technologies/gensim/issues/1485"
user: prakhar2b
repo: RaRe-Technologies/gensim
---

Based on discussion [here](https://groups.google.com/forum/#!topic/gensim/nKVWoftW71Q), we should properly check for filename before `process calls` in `utils.check_output()`, and raise more intuitive exception and error message.

cc @jayantj 