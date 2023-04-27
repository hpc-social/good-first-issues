---
tags: IFC,evaluation,example-files,quality_of_life
title: "Slow calculation time for IfcSine and IfcCosine"
html_url: "https://github.com/tumcms/Open-Infra-Platform/issues/560"
user: Elvira2227
repo: tumcms/Open-Infra-Platform
---

**Describe the bug**
Calculation of `IfcSine` and `IfcCosine` takes a long time.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to `CurveConverter.h`
2. Scroll down to the line 2693 for `IfcSine` or to the line 2748 for `IfcCosine`
3. Set an additional breakpoint if necessary
4. Wait for the end of the calculation

**CMake configuration**
If applicable, list any special configurations you have selected in CMake.
- EARLYBINDING_WITH_IFC4X3_RC4: selected

**Additional context**
On my machine it took approximately 9 minutes.
