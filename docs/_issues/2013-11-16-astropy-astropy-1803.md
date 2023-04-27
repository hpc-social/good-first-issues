---
tags: Effort-low,Feature-Request,Package-novice,time
title: "improve interpolation in IERS data"
html_url: "https://github.com/astropy/astropy/issues/1803"
user: mhvk
repo: astropy/astropy
---

Currently, UT1-UTC is interpolated linearly in the IERS data, ignoring the effects of tides (which are not included in the tables)..While this is fine for almost all purposes, the recommended procedure is to use a Lagrangian interpolation scheme and include the tides [1]. This is a reminder to implement this in IERS, following the ideas in the fortran code mentioned in [1], after checking what should be done for jumps in UT1-UTC due to leap seconds.

[1] http://maia.usno.navy.mil/iers-gaz13
