---
tags: ,enhancement
title: "have code error out if metallicities exceed tabulated fsps metallcities"
html_url: "https://github.com/dnarayanan/powderday/issues/118"
user: dnarayanan
repo: dnarayanan/powderday
---

only relevant for idealized simulations, quantities (e.g.):

```disk_stars_metals = 11  # in fsps metallicity units```

or alternatively, have user put in metallicity in units of solar, and have the code figure out which tabulated value this corresponds to, to minimize issues like this. 