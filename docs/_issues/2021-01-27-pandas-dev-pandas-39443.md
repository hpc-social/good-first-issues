---
tags: ,Needs-Tests
title: "BUG: Concatenating categorical datetime columns raises a ValueError since v1.2"
html_url: "https://github.com/pandas-dev/pandas/issues/39443"
user: aiudirog
repo: pandas-dev/pandas
---

- [X] I have checked that this issue has not already been reported.

- [X] I have confirmed this bug exists on the latest version of pandas.

- [X] (optional) I have confirmed this bug exists on the master branch of pandas.

---

#### Code Sample, a copy-pastable example

```python
import pandas as pd
from datetime import datetime

pd.concat([
    pd.DataFrame({'x': pd.Series(datetime(2021, 1, 1), index=[0], dtype='category')}),
    pd.DataFrame({'x': pd.Series(datetime(2021, 1, 2), index=[1], dtype='category')}),
])
```

#### Problem description

Since v1.2, concatenating two or more dataframes with at least one categorical datetime column with different categories raises this error:

<details>
    <summary>Traceback</summary>

```python-traceback
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-1-36ad6bb4648d> in <module>
      2 from datetime import datetime
      3 
----> 4 pd.concat([
      5     pd.DataFrame({'x': pd.Series(datetime(2021, 1, 1), index=[0], dtype='category')}),
      6     pd.DataFrame({'x': pd.Series(datetime(2021, 1, 2), index=[1], dtype='category')}),

venv/lib/python3.9/site-packages/pandas/core/reshape/concat.py in concat(objs, axis, join, ignore_index, keys, levels, names, verify_integrity, sort, copy)
    296     )
    297 
--> 298     return op.get_result()
    299 
    300 

venv/lib/python3.9/site-packages/pandas/core/reshape/concat.py in get_result(self)
    518                 mgrs_indexers.append((obj._mgr, indexers))
    519 
--> 520             new_data = concatenate_block_managers(
    521                 mgrs_indexers, self.new_axes, concat_axis=self.bm_axis, copy=self.copy
    522             )

venv/lib/python3.9/site-packages/pandas/core/internals/concat.py in concatenate_block_managers(mgrs_indexers, axes, concat_axis, copy)
     78                     values = values.reshape(1, len(values))
     79 
---> 80             b = make_block(values, placement=placement, ndim=blk.ndim)
     81         else:
     82             b = make_block(

venv/lib/python3.9/site-packages/pandas/core/internals/blocks.py in make_block(values, placement, klass, ndim, dtype)
   2730         values = DatetimeArray._simple_new(values, dtype=dtype)
   2731 
-> 2732     return klass(values, ndim=ndim, placement=placement)
   2733 
   2734 

venv/lib/python3.9/site-packages/pandas/core/internals/blocks.py in __init__(self, values, placement, ndim)
    135         """
    136         # TODO(EA2D): ndim will be unnecessary with 2D EAs
--> 137         self.ndim = self._check_ndim(values, ndim)
    138         self.mgr_locs = placement
    139         self.values = self._maybe_coerce_values(values)

venv/lib/python3.9/site-packages/pandas/core/internals/blocks.py in _check_ndim(self, values, ndim)
    184 
    185         if self._validate_ndim and values.ndim != ndim:
--> 186             raise ValueError(
    187                 "Wrong number of dimensions. "
    188                 f"values.ndim != ndim [{values.ndim} != {ndim}]"

ValueError: Wrong number of dimensions. values.ndim != ndim [1 != 2]
```
</details>

I have confirmed that:
- it happens on `v1.2.0`, `v1.2.1`, and `v1.3.0.dev0+553.gd0cfa0303` on both Windows 10 and Linux
- it doesn't happen before `v1.2` or if the categories are the same

#### Expected Output

A single, properly concatenated dataframe:

```
           x
0 2021-01-01
1 2021-01-02
```

#### Output of ``pd.show_versions()``

<details>

```
INSTALLED VERSIONS
------------------
commit           : 9d598a5e1eee26df95b3910e3f2934890d062caa
python           : 3.9.1.final.0
python-bits      : 64
OS               : Linux
OS-release       : 5.10.10-zen1-1-zen
Version          : #1 ZEN SMP PREEMPT Sat, 23 Jan 2021 23:59:50 +0000
machine          : x86_64
processor        : 
byteorder        : little
LC_ALL           : None
LANG             : en_US.UTF-8
LOCALE           : en_US.UTF-8

pandas           : 1.2.1
numpy            : 1.19.5
pytz             : 2020.5
dateutil         : 2.8.1
pip              : 20.3.1
setuptools       : 52.0.0
Cython           : 0.29.21
pytest           : 6.2.1
hypothesis       : None
sphinx           : 3.4.3
blosc            : None
feather          : None
xlsxwriter       : None
lxml.etree       : 4.6.2
html5lib         : 1.1
pymysql          : None
psycopg2         : None
jinja2           : 2.11.2
IPython          : 7.19.0
pandas_datareader: None
bs4              : 4.9.3
bottleneck       : None
fsspec           : 0.8.5
fastparquet      : None
gcsfs            : None
matplotlib       : 3.3.3
numexpr          : None
odfpy            : None
openpyxl         : None
pandas_gbq       : None
pyarrow          : None
pyxlsb           : None
s3fs             : None
scipy            : 1.6.0
sqlalchemy       : 1.3.22
tables           : None
tabulate         : None
xarray           : None
xlrd             : None
xlwt             : None
numba            : None
```

</details>
