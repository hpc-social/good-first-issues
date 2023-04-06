---
tags: ,enhancement,help-wanted
title: "rewrite git history to remove jupyter notebook outputs"
html_url: "https://github.com/undark-lab/swyft/issues/59"
user: bkmi
repo: undark-lab/swyft
---

Our repo is needlessly large because of the excessive saves of notebooks from previous git commits. This can be undone. We should do so.

A method can be found here:
https://mg.readthedocs.io/git-jupyter.html#cleaning-a-whole-repository

@cweniger are you fine with this? If you want to save the output of the current notebooks we can keep them in the next version release.

In general, we should avoid changing the notebook outputs if possible. One option would be to clear them automatically with pre-commit.