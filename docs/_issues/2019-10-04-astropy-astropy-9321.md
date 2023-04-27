---
tags: Docs,Effort-low,Hacktoberfest,Package-novice,coordinates
title: "Automate generation of the `SkyCoord` tab-completion documentation"
html_url: "https://github.com/astropy/astropy/issues/9321"
user: eteq
repo: astropy/astropy
---

The documentation for `SkyCoord` has a section listing the attributes on a `SkyCoord` (http://docs.astropy.org/en/stable/coordinates/skycoord.html#attributes, which is in `docs/coordinates/skycoord.rst`).  This could/should be auto-generated instead of the current state of it having to be manually updated.

It looks to me like the tab-completion list is the same as you get from the following:
```
>>> from astropy.coordinates import SkyCoord
>>> sc = SkyCoord(1*u.deg, 2*u.deg)
>>> ["sc."+attrname for attrname in dir(sc) if not attrname.startswith('_')]
```
so in principle, it's just a matter of injecting that list into the documentation.  Would be nice to do this so that it's not necessary to manually keep that list up to date (or more likely: forget to do so...).

cc @adrn (who recently pointed out this table isn't up-to-date)