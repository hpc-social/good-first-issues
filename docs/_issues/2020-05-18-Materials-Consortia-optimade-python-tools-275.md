---
tags: adapters,priority/medium,tests
title: "Check \"truth\" of CIF exporter"
html_url: "https://github.com/Materials-Consortia/optimade-python-tools/issues/275"
user: CasperWA
repo: Materials-Consortia/optimade-python-tools
---

Can someone clarify whether that structure is "correct", as displayed by recent VESTA versions?

If it isn't, maybe we should consider converting to fractionals in the cif exporter (until fractional is added to optimade)? We would have to be careful to deal with e.g. indeterminate lattice vectors and so on, but if the point is to make a file usable by viewers, then its probably worth the effort.

_Originally posted by @ml-evs in https://github.com/Materials-Consortia/optimade-python-tools/issues/271#issuecomment-630187598_

_Answer by @CasperWA in the same issue_:

I guess we could retrieve a CIF file from somewhere, e.g., COD, run it through our functions, export it, and see how they match up?