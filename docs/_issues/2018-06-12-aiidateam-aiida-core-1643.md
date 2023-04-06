---
tags: ,priority/nice-to-have,topic/materials-science-related,type/feature-request
title: "Modes for StructureData.get_composition()"
html_url: "https://github.com/aiidateam/aiida-core/issues/1643"
user: zooks97
repo: aiidateam/aiida-core
---

Currently, StructureData.get_composition() returns a dictionary of the composition without reducing with the greatest common divisor.

e.g. BaZrO3 returns `{'Ba': 1, 'Zr': 1, 'O': 3}`
e.g. Ba2Zr2O6 returns `{'Ba': 2, 'Zr': 2, 'O': 6}`

It could be useful to add a `modes` kwarg or similar and add functionality for:

- `direct` as the default
- reducing with the smallest common divisor (`reduced`)
  - e.g. BaZrO3 and Ba2Zr2O6 return `{'Ba': 1, 'Zr': 1, 'O': 3}`
- reducing to fractional composition totaling 1 (`fractional`)
  - e.g. BaZrO3 and Ba2Zr2O6 return`{'Ba': 0.20, 'Zr': 0.20, 'O': 0.60}`