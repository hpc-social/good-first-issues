---
tags: ,Docs,Effort-low,Package-novice,modeling
title: "LinearLSQFitter cannot fit compound models"
html_url: "https://github.com/astropy/astropy/issues/6038"
user: jehturner
repo: astropy/astropy
---

**Undo the doc modifications in #6041 before closing this as resolved.**

@nden tells me that "I think in general a compound model should be fitted with a non-linear fitter because at least currently the LinearFitter cannot construct the Vandermonde matrix for compound models". It would be useful to have this working if possible, as I believe non-linear fitters are not guaranteed to converge on the solution without a good starting guess, which may not always be available. Also, the documentation should mention that it currently doesn't work (which I'll fix in the meantime). This is just for the record and in case someone wants to work on it before one of us gets to it.

Running LinearLSQFitter on a couple of compound models currently gives errors like the following:
```python
>>> LinearLSQFitter()(Mapping((0,)) | Chebyshev1D(2), range(0,10), range(0,10))
Traceback (innermost last):
  File "<console>", line 1, in <module>
  File "/home/jturner/anaconda2/envs/peylian/lib/python2.7/site-packages/astropy-2.0.dev18162-py2.7-linux-x86_64.egg/astropy/modeling/fitting.py", line 254, in __call__
    raise ModelLinearityError('Model is not linear in parameters, '
ModelLinearityError: Model is not linear in parameters, linear fit methods should not be used.
```
```python
>>> LinearLSQFitter()(Chebyshev1D(2) | Chebyshev1D(2), range(0,10), range(0,10)) 
Traceback (innermost last):
  File "<console>", line 1, in <module>
  File "/home/jturner/anaconda2/envs/peylian/lib/python2.7/site-packages/astropy-2.0.dev18162-py2.7-linux-x86_64.egg/astropy/modeling/fitting.py", line 279, in __call__
    lhs = model_copy.fit_deriv(x, *model_copy.parameters)
TypeError: 'NoneType' object is not callable
```
