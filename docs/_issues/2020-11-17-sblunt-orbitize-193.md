---
tags: ,enhancement
title: "chopping chains in results class"
html_url: "https://github.com/sblunt/orbitize/issues/193"
user: semaphoreP
repo: sblunt/orbitize
---

I don't think we currently have the ability to read in posteriors from MCMC that are saved as a HDF5 file, and chop chains in the results class. This can be useful when we identify we have further burn-in that needs to be removed but don't want to rerun the whole MCMC. 

