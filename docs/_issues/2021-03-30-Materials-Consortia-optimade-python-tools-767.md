---
tags: adapters,bug,help-wanted,priority/medium
title: "Possible conversion issues with large unit cells"
html_url: "https://github.com/Materials-Consortia/optimade-python-tools/issues/767"
user: CasperWA
repo: Materials-Consortia/optimade-python-tools
---

In the [Voilà OPTIMADE Client](https://github.com/CasperWA/voila-optimade-client), large unit cells sometimes do not render in the structure viewer, while the lattice vector information seems to definitely be present.
It seems this is not just an issue of the viewer software (nglview), but one of the conversion functions. At least according to @giovannipizzi, who found that the unit cell information was missing for some structures after converting them to CIF.
It might be good to investigate whether this is due to a supporting library failing to handle very large unit cells or there's an error in our local conversion functions.