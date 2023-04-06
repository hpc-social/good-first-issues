---
tags: ,Area---Documentation-📒,Enhancement-✨
title: "deduplication of louvain and leiden doc"
html_url: "https://github.com/scverse/scanpy/issues/570"
user: fbnrst
repo: scverse/scanpy
---

`louvain` and `leiden` have a lot of redundant documentation. After having learned in #557, I could file a PR to deduplicate this. Would it be valid to shuffle the arguments in such a way that the shared documentation is grouped together? Otherwise, one would have to introduce many short strings and puzzle them together.