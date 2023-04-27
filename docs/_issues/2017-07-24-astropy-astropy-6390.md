---
tags: Docs,Effort-low,Feature-Request,Hacktoberfest,Package-novice,units
title: "multiple functions from scipy.special do not work with quantities"
html_url: "https://github.com/astropy/astropy/issues/6390"
user: namurphy
repo: astropy/astropy
---

I just tried to use SciPy's error function, and Astropy politely requested that I raise this issue here:
```Python
>>> from astropy import units
>>> from scipy.special import erf, erfc
>>> r1 = 5*u.m
>>> r2 = 6*u.m
>>> erf(r1/r2)
TypeError: Unknown ufunc erf.  Please raise issue on https://github.com/astropy/astropy
>>> erfc(r1/r2)
TypeError: Unknown ufunc erfc.  Please raise issue on https://github.com/astropy/astropy
>>> erf(r1.value/r2.value)  # workaround
0.76140717068356445
```
In scipy.special, ufuncs that I would prioritize include:
- [ ] [Error function, etc](https://docs.scipy.org/doc/scipy/reference/special.html#error-function-and-fresnel-integrals)
- [ ] [Bessel functions](https://docs.scipy.org/doc/scipy/reference/special.html#bessel-functions)
- [ ] [Gamma and related functions](https://docs.scipy.org/doc/scipy/reference/special.html#gamma-and-related-functions)
- [ ] [Legendre functions](https://docs.scipy.org/doc/scipy/reference/special.html#legendre-functions)
- [ ] `zeta` and `zetac` - Riemann zeta functions

Thanks!