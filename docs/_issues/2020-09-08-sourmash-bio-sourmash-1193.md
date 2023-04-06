---
tags: 
title: "fix LCA_Database __repr__ so that `None` is not displayed"
html_url: "https://github.com/sourmash-bio/sourmash/issues/1193"
user: ctb
repo: sourmash-bio/sourmash
---

reported by @bluegenes -- right now the `__repr__` relies on `self.filename`, which is sometimes set to `None`.

The fix is to check if `self.filename` is None, and if so, just display `LCA_Database()`. See file `sourmash/lca/lca_db.py`.