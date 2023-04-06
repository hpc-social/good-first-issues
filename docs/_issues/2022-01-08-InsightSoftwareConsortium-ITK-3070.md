---
tags: ,Good-first-issue,typeStyle
title: "Optimizer classes should not print non-self member variables"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/3070"
user: jhlegarreta
repo: InsightSoftwareConsortium/ITK
---

### Description

Some optimizer(v4) classes are printing non-self member variables in their `PrintSelf` methods.

### Expected coding style

Classes should only print self member variables in their `PrintSelf` methods. They should rely on their superclass and any other member variable `PrintSelf` method implementations to reveal their state at a given execution point.

### Actual coding style

Classes are printing non-self member variables in their `PrintSelf` methods, e.g. `itk::itkLBFGSBOptimizerv4` prints inherited members, such as `m_CostFunctionConvergenceFactor`:
https://github.com/InsightSoftwareConsortium/ITK/blob/master/Modules/Numerics/Optimizersv4/src/itkLBFGSBOptimizerv4.cxx#L80
defined in its base class:
https://github.com/InsightSoftwareConsortium/ITK/blob/master/Modules/Numerics/Optimizersv4/include/itkLBFGSOptimizerBasev4.h#L163

### Versions

`master`.

### Additional Information

The above is only an example; the same class is printing more inherited variables. It is highly likely that many more cases exist. The optimizers involve metrics and transforms, which should also be examined. This behavior in `v4` versions might be a remnant of the transition from their non- `v4` counterparts.

Noticed in https://github.com/InsightSoftwareConsortium/ITK/pull/3066#issuecomment-1008011986.
