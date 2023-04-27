---
tags: enhancement,help-wanted
title: "Least squares fit to speed up sampler"
html_url: "https://github.com/sblunt/orbitize/issues/57"
user: sblunt
repo: sblunt/orbitize
---

This might be something @logan-pearce is interested in working on. In particular, I think we should implement the following:
- use a scipy optimization routine to estimate the minimum chi square for a given dataset, then use that to calculate a modified chi square for each tested orbit.
- adaptively modify priors as regions of parameter space are ruled out.