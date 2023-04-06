---
tags: ,bug
title: "Rectangle domain creator / Affine coordinate map should output error instead of FPE for invalid input"
html_url: "https://github.com/sxs-collaboration/spectre/issues/2934"
user: nilsvu
repo: sxs-collaboration/spectre
---

# Bug reports:

### Expected behavior:

These options should output a useful error message:

```yaml
DomainCreator:
  Rectangle:
    # This is invalid, since the length is zero along the x-axis
    LowerBound: [-0.5, -1.]
    UpperBound: [-0.5, 1.]
    InitialRefinement: [1, 1]
    InitialGridPoints: [4, 4]
```

### Current behavior:

A floating point exception :(
