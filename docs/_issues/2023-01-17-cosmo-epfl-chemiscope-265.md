---
tags: component-jupyter,component-structure
title: "Allow more than one structure viewer in structure-only mode"
html_url: "https://github.com/lab-cosmo/chemiscope/issues/265"
user: Luthaf
repo: cosmo-epfl/chemiscope
---

We currently only allow 1 structure viewer in the grid when using structure-only vizualisation (`mode="structure"` in jupyter), but some users would like to be able to compare multiple structure.

I could see a point of having more than one viewer, but if we have more than one viewer it would be nice to give more space to the grid to ensure everything is legible, so fixing this issue will involve some CSS work.