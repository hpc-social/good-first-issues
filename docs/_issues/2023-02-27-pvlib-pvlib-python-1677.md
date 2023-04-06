---
tags: ,documentation,enhancement,help-wanted
title: "Clarify f_x"
html_url: "https://github.com/pvlib/pvlib-python/issues/1677"
user: cwhanse
repo: pvlib/pvlib-python
---

In some private functions of `pvlib.bifacial.infinite_sheds`, the parameter `f_x` is described as

```
    f_x : numeric
        Fraction of row slant height from the bottom that is shaded from
        direct irradiance.
```

In other public functions, the description is

```
    f_x : numeric
        Fraction of row slant height from the bottom that is shaded. [unitless]
```

For users trying to understand this algorithm, the different definitions can be confusing, because saying just "shaded" could mean shaded from diffuse irradiance by the adjacent row.


**Describe the solution you'd like**
Use the longer description for all instances of `f_x`.
