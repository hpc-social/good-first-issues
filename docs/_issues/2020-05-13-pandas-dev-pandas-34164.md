---
tags: ,Needs-Tests
title: "BUG: grouping with categorical interval columns"
html_url: "https://github.com/pandas-dev/pandas/issues/34164"
user: antipisa
repo: pandas-dev/pandas
---

Versions:
pandas 1.0.3
numpy 1.18.1

There is a bug in the 1.XXX pandas release that does not allow you to group by a categorical interval index column together with another column.

```
import numpy as np
import pandas as pd
pd.set_option("use_inf_as_na",True)
t = pd.DataFrame({"x":np.random.randn(100), 'w':np.random.choice(list("ABC"), 100)})
qq = pd.qcut(t['x'], q=np.linspace(0,1,5))

```

This works and gives the expected result:
`
t.groupby([qq])['x'].agg('mean')
`

`x
(-10.001, -1.0]   -1.431893
(-1.0, 0.0]       -0.423564
(0.0, 1.0]         0.461174
(1.0, 10.0]        1.662297
Name: x, dtype: float64
`



This raises a TypeError:
`
t.groupby([qq,'w'])['x'].agg('mean')
`



```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-43-6d7782f17653> in <module>
----> 1 t.groupby([qq,'w'])['x'].agg('mean')

~/miniconda3/lib/python3.7/site-packages/pandas/core/groupby/generic.py in aggregate(self, func, *args, **kwargs)
    245 
    246         if isinstance(func, str):
--> 247             return getattr(self, func)(*args, **kwargs)
    248 
    249         elif isinstance(func, abc.Iterable):

~/miniconda3/lib/python3.7/site-packages/pandas/core/groupby/groupby.py in mean(self, *args, **kwargs)
   1223         nv.validate_groupby_func("mean", args, kwargs, ["numeric_only"])
   1224         return self._cython_agg_general(
-> 1225             "mean", alt=lambda x, axis: Series(x).mean(**kwargs), **kwargs
   1226         )
   1227 

~/miniconda3/lib/python3.7/site-packages/pandas/core/groupby/groupby.py in _cython_agg_general(self, how, alt, numeric_only, min_count)
    907             raise DataError("No numeric types to aggregate")
    908 
--> 909         return self._wrap_aggregated_output(output)
    910 
    911     def _python_agg_general(self, func, *args, **kwargs):

~/miniconda3/lib/python3.7/site-packages/pandas/core/groupby/generic.py in _wrap_aggregated_output(self, output)
    384             output=output, index=self.grouper.result_index
    385         )
--> 386         return self._reindex_output(result)._convert(datetime=True)
    387 
    388     def _wrap_transformed_output(

~/miniconda3/lib/python3.7/site-packages/pandas/core/groupby/groupby.py in _reindex_output(self, output, fill_value)
   2481         levels_list = [ping.group_index for ping in groupings]
   2482         index, _ = MultiIndex.from_product(
-> 2483             levels_list, names=self.grouper.names
   2484         ).sortlevel()
   2485 

~/miniconda3/lib/python3.7/site-packages/pandas/core/indexes/multi.py in from_product(cls, iterables, sortorder, names)
    551 
    552         codes = cartesian_product(codes)
--> 553         return MultiIndex(levels, codes, sortorder=sortorder, names=names)
    554 
    555     @classmethod

~/miniconda3/lib/python3.7/site-packages/pandas/core/indexes/multi.py in __new__(cls, levels, codes, sortorder, names, dtype, copy, name, verify_integrity, _set_identity)
    278 
    279         if verify_integrity:
--> 280             new_codes = result._verify_integrity()
    281             result._codes = new_codes
    282 

~/miniconda3/lib/python3.7/site-packages/pandas/core/indexes/multi.py in _verify_integrity(self, codes, levels)
    366 
    367         codes = [
--> 368             self._validate_codes(level, code) for level, code in zip(levels, codes)
    369         ]
    370         new_codes = FrozenList(codes)

~/miniconda3/lib/python3.7/site-packages/pandas/core/indexes/multi.py in <listcomp>(.0)
    366 
    367         codes = [
--> 368             self._validate_codes(level, code) for level, code in zip(levels, codes)
    369         ]
    370         new_codes = FrozenList(codes)

~/miniconda3/lib/python3.7/site-packages/pandas/core/indexes/multi.py in _validate_codes(self, level, code)
    302         to a level with missing values (NaN, NaT, None).
    303         """
--> 304         null_mask = isna(level)
    305         if np.any(null_mask):
    306             code = np.where(null_mask[code], -1, code)

~/miniconda3/lib/python3.7/site-packages/pandas/core/dtypes/missing.py in isna(obj)
    124     Name: 1, dtype: bool
    125     """
--> 126     return _isna(obj)
    127 
    128 

~/miniconda3/lib/python3.7/site-packages/pandas/core/dtypes/missing.py in _isna_old(obj)
    181         return False
    182     elif isinstance(obj, (ABCSeries, np.ndarray, ABCIndexClass, ABCExtensionArray)):
--> 183         return _isna_ndarraylike_old(obj)
    184     elif isinstance(obj, ABCGeneric):
    185         return obj._constructor(obj._data.isna(func=_isna_old))

~/miniconda3/lib/python3.7/site-packages/pandas/core/dtypes/missing.py in _isna_ndarraylike_old(obj)
    281         else:
    282             result = np.empty(shape, dtype=bool)
--> 283             vec = libmissing.isnaobj_old(values.ravel())
    284             result[:] = vec.reshape(shape)
    285 

TypeError: Argument 'arr' has incorrect type (expected numpy.ndarray, got Categorical)

```
