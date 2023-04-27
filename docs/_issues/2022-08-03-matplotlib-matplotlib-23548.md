---
tags: Difficulty-Medium,Good-first-issue
title: "Create fully pinned requirements file for bug-fix branches"
html_url: "https://github.com/matplotlib/matplotlib/issues/23548"
user: tacaswell
repo: matplotlib/matplotlib
---

I spent some time yesterday and today trying to get tests to run on old versions of Matplotlib which....was harder than I wished it would be.  We may want to have one very pinned requirements file (possible managed by one of the auto-bump services 😞 or tools) that we rename to `fully-pinned-v3.6.x.txt` on branching.  We can then use that (exclusively) for tests on the backport branch which should hopefully reduce the amount of dep-only backports we have to do (and provide a useful reference for anyone who wants to get old versions testing again).

_Originally posted by @tacaswell in https://github.com/matplotlib/matplotlib/issues/22574#issuecomment-1059892443_