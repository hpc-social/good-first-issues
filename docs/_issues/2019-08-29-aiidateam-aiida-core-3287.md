---
tags: priority/nice-to-have,topic/data-types,topic/materials-science-related,type/feature-request
title: "Define KpointsData via constructor"
html_url: "https://github.com/aiidateam/aiida-core/issues/3287"
user: ltalirz
repo: aiidateam/aiida-core
---

It should be possible to set the properties of a `KpointsData` directly in the constructor. Instead of having to write
```python
kpoints = KpointsData()
kpoints.set_kpoints_mesh([4,4,4])
builder.kpoints = kpoints
```
one should be able to write
```python
builder.kpoints = KpointsData(mesh=[4,4,4])
```