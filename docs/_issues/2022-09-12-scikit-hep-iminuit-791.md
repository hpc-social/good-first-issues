---
tags: PyHEP-2022-Hackashop,enhancement
title: "Improve error messages when using builtin cost functions"
html_url: "https://github.com/scikit-hep/iminuit/issues/791"
user: HDembinski
repo: scikit-hep/iminuit
---

There are many ways to make mistakes and use the builtin cost functions incorrectly. The user has to provide the model and it is easy to return an array of incorrect size.

```py
from iminuit import cost, Minuit
from numba_stats import norm
import numpy as np

n = [1, 2, 3]
edges = [0.1, 0.2, 0.3, 0.4]

def model(x, n, a, b):
    # oopsi, returned probability per bin instead of scaled cdf
    return n * np.diff(norm.cdf(x, a, b))
    # return n * norm.cdf(x, a, b)  # correct

c = cost.ExtendedBinnedNLL(n, edges, model)
c(1, 2, 3)
```
This produces a very confusing error message:
```
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
/var/folders/tl/pv6mt7z17tz0stm1fjfg01cc0000gn/T/ipykernel_28667/1963231075.py in <module>
     12 
     13 c = cost.ExtendedBinnedNLL(n, edges, model)
---> 14 c(1, 2, 3)

/usr/local/lib/python3.8/site-packages/iminuit/cost.py in __call__(self, *args)
    482         float
    483         """
--> 484         r = self._call(args)
    485         if self.verbose >= 1:
    486             print(args, "->", r)

/usr/local/lib/python3.8/site-packages/iminuit/cost.py in _call(self, args)
   1292         else:
   1293             n = self._masked
-> 1294         return poisson_chi2(n, mu)
   1295 
   1296 

/usr/local/lib/python3.8/site-packages/iminuit/cost.py in poisson_chi2(n, mu)
    345         n, mu = np.atleast_1d(n, mu)  # type:ignore
    346         if mu.dtype in (np.float32, np.float64):  # type:ignore
--> 347             return _poisson_chi2_nb(n, mu)
    348         # fallback to numpy for float128
    349         return _poisson_chi2_np(n, mu)

ValueError: unable to broadcast argument 1 to output array
File "/usr/local/lib/python3.8/site-packages/iminuit/cost.py", line 1, 
```
We need a better error message for this cost function and for others.