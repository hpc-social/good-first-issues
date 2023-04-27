---
tags: enhancement
title: "Test on grids with Gauss points"
html_url: "https://github.com/sxs-collaboration/spectre/issues/769"
user: nilsvu
repo: sxs-collaboration/spectre
---

# Feature request:

We need to extend many tests to non-LGL grids to make sure they generalize as expected, in particular to Gauss points. Some will certainly fail because they implicitly assume that the zero-index and max-index points represent the element boundaries (e.g. `Unit.Numerical.LinearOperators.MeanValueOnBoundary`), which is not the case for Gauss quadrature. Others should generalize fine, e.g. `Unit.Numerical.LinearOperators.DefiniteIntegral`.

This is not super high priority since we use non-LGL grids only rarely, but we should be aware of this.

I add the _bug_ label because some functions don't work as advertised.

### Component:

- [x] Code
- [ ] Documentation
- [ ] Build system
- [ ] Continuous integration

### Detailed discussion:
