---
tags: ,enhancement
title: "[feature] implement locally spheroidal surface binding potential "
html_url: "https://github.com/lcpp-org/RustBCA/issues/108"
user: drobnyjt
repo: lcpp-org/RustBCA
---

**Is your feature request related to a problem? Please describe.**
Locally planar and locally isotropic (equivalent to spherical) surface binding potentials are just two limiting cases of a generic spheroidal potential. This would take one extra parameter, k, but all it changes is the calculation of the normal vector. This would be a great feature to have when comparing to MD.

**Proposed solution**
https://doi.org/10.1016/j.nimb.2012.11.022