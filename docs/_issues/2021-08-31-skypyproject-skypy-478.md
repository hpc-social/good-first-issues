---
tags: ,enhancement,low-priority,module-galaxies
title: "ENH: Rename noise keyword argument in redshifts_from_comoving_density function"
html_url: "https://github.com/skypyproject/skypy/issues/478"
user: rrjbca
repo: skypyproject/skypy
---

It was noted in the review for our JOSS paper that the keyword argument `noise` for the function `redshifts_from_comoving_density` has a misleading name. See the review comment [here](https://github.com/openjournals/joss-reviews/issues/3056#issuecomment-877270540). They suggested renaming to `fixed_N`. My own suggestion would be `shot_noise` (or perhaps `poisson`). Since this would require a breaking API change, this should only be made as part of a future major release (if at all).