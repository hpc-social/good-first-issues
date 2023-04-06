---
tags: ,documentation,help-wanted
title: "use array_like instead of numeric/array-like"
html_url: "https://github.com/pvlib/pvlib-python/issues/765"
user: wholmgren
repo: pvlib/pvlib-python
---

The pvlib parameters/returns type [documentation style](https://pvlib-python.readthedocs.io/en/stable/contributing.html#documentation) is:

* numeric : scalar, np.array, pd.Series. Typically int or float dtype.
* array-like : np.array, pd.Series. Typically int or float dtype.

However, Numpy [defines](https://docs.scipy.org/doc/numpy/glossary.html#term-array-like) *array_like* as "Any sequence that can be interpreted as an ndarray. This includes nested lists, tuples, scalars and existing arrays."

I think we should follow the numpy standard. We lose the implied specification for whether or not a function works with scalar input, but this seems to be a source of confusion anyways. Instead, the docstrings for functions that require array input with length > 1 could explicitly state this.