---
tags: Bug,Effort-low,Package-novice,stats
title: "poisson_conf_interval 'kraft-burrows-nousek' fails unexpectedly"
html_url: "https://github.com/astropy/astropy/issues/13334"
user: hamogu
repo: astropy/astropy
---

<!-- This comments are hidden when you submit the issue,
so you do not need to remove them! -->

<!-- Please be sure to check out our contributing guidelines,
https://github.com/astropy/astropy/blob/main/CONTRIBUTING.md .
Please be sure to check out our code of conduct,
https://github.com/astropy/astropy/blob/main/CODE_OF_CONDUCT.md . -->

<!-- Please have a search on our GitHub repository to see if a similar
issue has already been posted.
If a similar issue is closed, have a quick look to see if you are satisfied
by the resolution.
If not please go ahead and open an issue! -->

<!-- Please check that the development version still produces the same bug.
You can install development version with
pip install git+https://github.com/astropy/astropy
command. -->

### Description
<!-- Provide a general description of the bug. -->

### Expected behavior
<!-- What did you expect to happen. -->
poisson_conf_interval 'kraft-burrows-nousek'  calculated values or fails with an obvious error message.

### Actual behavior
<!-- What actually happened. -->
<!-- Was the output confusing or poorly described? -->
The error message comes form deep within `scipy.optimize` and it's not clear for a user how to react. It's particularly confusing here because, at least on my platform, the function could work if not for a hardcoded upper value of an interval. The problem is in line 1160 `S_max = brentq(func, N - B, 100)` (see pasted error output below). In the function, the upper end of the interval that `brentq` searches is hardcoded to 100. That's because (looking at the code comments and also speaking from memory as the person who originally implemented this) much larger value lead to numerical overflow error - scipy simple can't be used. However, for the numbers in my example, the calculation works when changing the hardcoded `100` to `200`.

### Notes for tackling this
So, this looks very simple - just increase the hardcoded `100`. However, we want to be a bit careful not to increase it too much because nobody is helped by running into overflow's instead. So, one might instead have to decrease that "Don't use scipy with N > 100" rule to a smaller number  - finding the balance here might require some experimentation and new numbers in the test.

### Steps to Reproduce
<!-- Ideally a code example could be provided so we can run it ourselves. -->
<!-- If you are pasting code, use triple backticks (```) around
your code snippet. -->
<!-- If necessary, sanitize your screen output to be pasted so you do not
reveal secrets like tokens and passwords. -->

With scipy installed:

```python
from astropy.stats import poisson_conf_interval
poisson_conf_interval(n=int(98), background=3.8, confidence_level=0.95,
                                             interval='kraft-burrows-nousek')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Input In [48], in <cell line: 1>()
----> 1 poisson_conf_interval(n=int(98), background=3.8, confidence_level=0.95,
      2                                              interval='kraft-burrows-nousek')

File /nfs/melkor/d1/guenther/soft/mambaforge/envs/ciao-4.14/lib/python3.9/site-packages/astropy/stats/funcs.py:764, in poisson_conf_interval(n, interval, sigma, background, confidence_level)
    762     if np.any(background < 0):
    763         raise ValueError('Background must be >= 0.')
--> 764     conf_interval = np.vectorize(_kraft_burrows_nousek,
    765                                  cache=True)(n, background, confidence_level)
    766     conf_interval = np.vstack(conf_interval)
    767 else:

File /nfs/melkor/d1/guenther/soft/mambaforge/envs/ciao-4.14/lib/python3.9/site-packages/numpy/lib/function_base.py:2304, in vectorize.__call__(self, *args, **kwargs)
   2301     vargs = [args[_i] for _i in inds]
   2302     vargs.extend([kwargs[_n] for _n in names])
-> 2304 return self._vectorize_call(func=func, args=vargs)

File /nfs/melkor/d1/guenther/soft/mambaforge/envs/ciao-4.14/lib/python3.9/site-packages/numpy/lib/function_base.py:2382, in vectorize._vectorize_call(self, func, args)
   2380     res = func()
   2381 else:
-> 2382     ufunc, otypes = self._get_ufunc_and_otypes(func=func, args=args)
   2384     # Convert args to object arrays first
   2385     inputs = [asanyarray(a, dtype=object) for a in args]

File /nfs/melkor/d1/guenther/soft/mambaforge/envs/ciao-4.14/lib/python3.9/site-packages/numpy/lib/function_base.py:2342, in vectorize._get_ufunc_and_otypes(self, func, args)
   2338     raise ValueError('cannot call `vectorize` on size 0 inputs '
   2339                      'unless `otypes` is set')
   2341 inputs = [arg.flat[0] for arg in args]
-> 2342 outputs = func(*inputs)
   2344 # Performance note: profiling indicates that -- for simple
   2345 # functions at least -- this wrapping can almost double the
   2346 # execution time.
   2347 # Hence we make it optional.
   2348 if self.cache:

File /nfs/melkor/d1/guenther/soft/mambaforge/envs/ciao-4.14/lib/python3.9/site-packages/astropy/stats/funcs.py:1290, in _kraft_burrows_nousek(N, B, CL)
   1288 if HAS_SCIPY and N <= 100:
   1289     try:
-> 1290         return _scipy_kraft_burrows_nousek(N, B, CL)
   1291     except OverflowError:
   1292         if not HAS_MPMATH:

File /nfs/melkor/d1/guenther/soft/mambaforge/envs/ciao-4.14/lib/python3.9/site-packages/astropy/stats/funcs.py:1160, in _scipy_kraft_burrows_nousek(N, B, CL)
   1157     out = eqn9_left(s_min, s, N, B)
   1158     return out[0] - CL
-> 1160 S_max = brentq(func, N - B, 100)
   1161 S_min = find_s_min(S_max, N, B)
   1162 return S_min, S_max

File /nfs/melkor/d1/guenther/soft/mambaforge/envs/ciao-4.14/lib/python3.9/site-packages/scipy/optimize/_zeros_py.py:783, in brentq(f, a, b, args, xtol, rtol, maxiter, full_output, disp)
    781 if rtol < _rtol:
    782     raise ValueError("rtol too small (%g < %g)" % (rtol, _rtol))
--> 783 r = _zeros._brentq(f, a, b, xtol, rtol, maxiter, args, full_output, disp)
    784 return results_c(full_output, r)

ValueError: f(a) and f(b) must have different signs
```

### System Details
Linux-3.10.0-1062.12.1.el7.x86_64-x86_64-with-glibc2.17
Python 3.9.7 (default, Sep 16 2021, 13:09:58) 
[GCC 7.5.0]
Numpy 1.21.2
pyerfa 2.0.0
astropy 5.1
Scipy 1.7.1

<!-- Even if you do not think this is necessary, it is useful information for the maintainers.
Please run the following snippet and paste the output below:
import platform; print(platform.platform())
import sys; print("Python", sys.version)
import numpy; print("Numpy", numpy.__version__)
import erfa; print("pyerfa", erfa.__version__)
import astropy; print("astropy", astropy.__version__)
import scipy; print("Scipy", scipy.__version__)
import matplotlib; print("Matplotlib", matplotlib.__version__)
-->
