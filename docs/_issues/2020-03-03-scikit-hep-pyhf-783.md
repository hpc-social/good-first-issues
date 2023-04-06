---
tags: ,feat/enhancement
title: "show total number of parameters (not only parsets) in pyhf inspect"
html_url: "https://github.com/scikit-hep/pyhf/issues/783"
user: lukasheinrich
repo: scikit-hep/pyhf
---

# Description

to comopare w/ ROOT workspaces it's useful to compare the parameter sets. Right now we print the overall number of parameter*sets* but it would be good to

* have tthe total number of parmeters (`m.config.npars`)
* and for each par set line the size of the slice (`s.stop-s.start`)


