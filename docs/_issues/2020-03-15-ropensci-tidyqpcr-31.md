---
tags: enhancement,help-wanted
title: "Support for Taqman / hydrolysis / multi-colour probes"
html_url: "https://github.com/ropensci/tidyqpcr/issues/31"
user: ewallace
repo: ropensci/tidyqpcr
---

Current edition of tidyqpcr works for SYBR safe experiments, i.e. 1 probe in 1 colour per well. The other major approach to qPCR is hydrolysis probes (TaqMan), which has multiple probes measured in different wavelengths per well. tidyqpcr should cope with this fine, but the plate plans & `display_plate` will need adapting. We may need a new function to read multicolour data.

Help wanted! Good first issue for someone with Taqman data, especially from a Roche Lightcycler.