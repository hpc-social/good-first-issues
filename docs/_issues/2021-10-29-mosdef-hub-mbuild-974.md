---
tags: ,enhancement
title: "Opt out of solute centering in solvate"
html_url: "https://github.com/mosdef-hub/mbuild/issues/974"
user: mphoward
repo: mosdef-hub/mbuild
---

**Describe the behavior you would like added to mBuild**

It would be nice to be able to opt out of centering the solute in `mbuild.packing.solvate`. If the solute is large, translating the center of mass may take it outside the box, leading to issues with packmol. 

**Describe the solution you'd like**

Add an option like `center=True` to `mbuild.packing.solvate`. Then, update this template string

https://github.com/mosdef-hub/mbuild/blob/0eca09d0f613afea398003102748e5ec021b5233/mbuild/packing.py#L30-L36

so that it only uses the `center` option & nonzero fixed when `center=True`. Otherwise, only use `fixed 0 0 0 0 0 0`.

**Describe alternatives you've considered**
I've tried workarounds for this, but I couldn't find something that keeps the solute from translating.
