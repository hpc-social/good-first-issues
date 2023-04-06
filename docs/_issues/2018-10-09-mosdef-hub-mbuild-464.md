---
title: "Wrap coordinates into fractional coordinates"
html_url: "https://github.com/mosdef-hub/mbuild/issues/464"
user: mattwthompson
repo: mosdef-hub/mbuild
---

Some formats write coordinates into fractional coordinates, i.e. positions in each dimension are scaled by `1/L` into a unitless fractional value. I think there should be a function - probably private - that does this wrapping.

An alternative approach to add this functionality would be to allow `mb.Lattice` to optionally populate into fractional coordinates. I am opposed to this, however, because the returned compound would have positions in unitless values, not nm.