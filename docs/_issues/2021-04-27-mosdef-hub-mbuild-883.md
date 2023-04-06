---
tags: 
title: "Fix boundingbox check for non-orthogonal boxes"
html_url: "https://github.com/mosdef-hub/mbuild/issues/883"
user: jennyfothergill
repo: mosdef-hub/mbuild
---

TODO comments from `mbuild/compound.py`
```
986:        # TODO: Fix this for non-orthogonal boxes
987-        # Make sure the box is bigger than the bounding box
988-        if box is not None:
989-            if (box.lengths < self.boundingbox.lengths).any():
990-                warn(
991-                    "Compound.box.lengths < Compound.boundingbox.lengths. "
992-                    "There may be particles outside of the defined "
993-                    "simulation box."
994-                )
```
related to #872