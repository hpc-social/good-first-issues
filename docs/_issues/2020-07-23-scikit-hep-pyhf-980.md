---
tags: ,feat/enhancement,follow-up
title: "Check for extraneous tensor casts with \"data\" handling"
html_url: "https://github.com/scikit-hep/pyhf/issues/980"
user: kratsg
repo: scikit-hep/pyhf
---

Example is from the optimizer common code where we cast data. Let's try to clean these situations up.

> shouldn't `data` already be a tensor? do we need the cast?

_Originally posted by @lukasheinrich in https://github.com/_render_node/MDIzOlB1bGxSZXF1ZXN0UmV2aWV3VGhyZWFkMjg2NDc2MTIwOnYy/pull_request_review_threads/discussion_

----

Link if render node above isn't working: https://github.com/scikit-hep/pyhf/pull/951#discussion_r459059752

Relevant issues/PRs:
- #951