---
tags: enhancement
title: "Sum and difference bodies"
html_url: "https://github.com/glotzerlab/coxeter/issues/23"
user: b-butler
repo: glotzerlab/coxeter
---

## Description
Taking the sum or difference body of two shapes in 2D or 3D would not be difficult to implement and would be a nice feature. This could use duck typing to work with 2D or 3D vectors as well. I would recommend overwriting the `__add__` and `__sub__`  methods of `Poly` classes for this.

### Tasks
- [ ] Create functions to calculate the sum and difference body and wrap results in the correct object
- [ ] Use these functions to allow `shape1 + shape2` and `shape1 - shape2`
- [ ] Document these function
- [ ] write unit tests for these functions