---
tags: ,Good-first-issue,typeStyle
title: "Remove whitespaces before scope resolution operators"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/3069"
user: jhlegarreta
repo: InsightSoftwareConsortium/ITK
---

### Description

A few places are found across ITK having a whitespace before the scope resolution operator separating a class name and a method.

### Expected coding style

No whitespace should exist before the scope resolution operator separating the class name and the method, i.e.
```
ChainCodePath2D::Evaluate
LBFGSBOptimizerv4::PrintSelf
SingleValuedNonLinearVnlOptimizerv4::PrintSelf
```

### Actual coding style

Currently, whitespaces are found in a few places, e.g.
```
ChainCodePath2D ::Evaluate
LBFGSBOptimizerv4 ::PrintSelf
SingleValuedNonLinearVnlOptimizerv4 ::PrintSelf
```

### Versions

`master`.

### Additional Information

The above lists are not exhaustive. `Review` classes should also be inspected.

Related to #2096.