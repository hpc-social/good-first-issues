---
tags: enhancement
title: "Add output column headers to .forward files"
html_url: "https://github.com/VirtualPlanetaryLaboratory/vplanet/issues/147"
user: RoryBarnes
repo: VirtualPlanetaryLaboratory/vplanet
---

Gijs Mulders suggested that it would be useful to include commented-out headers in output files. These will be ignored by most python I/O functions, like numpy's genfromtxt of pandas' read_tables, and can make output more human-readable.

It could look like this:

# Time Eccentricity Semi-major Axis
    0.0    0.3                1.0

and so on.