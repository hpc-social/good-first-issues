---
tags: ,documentation
title: "Fix documentation build"
html_url: "https://github.com/DeltaRCM/pyDeltaRCM/issues/267"
user: elbeejay
repo: DeltaRCM/pyDeltaRCM
---

Documentation build is failing (https://github.com/DeltaRCM/pyDeltaRCM/actions/runs/4298769386/jobs/7493268323).

Looks like this is due to a link that is perceived as "broken": https://github.com/DeltaRCM/pyDeltaRCM/actions/runs/4298769386/jobs/7493268323#step:6:255

This is the link: https://doi.org/10.1086/626637 which appears to redirect to https://www.journals.uchicago.edu/doi/10.1086/626637

Suggestion is to just do a bit of investigation and testing locally, but simplest solution may be to edit the `conf.py` file and have it "ignore" that URL: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-linkcheck_ignore