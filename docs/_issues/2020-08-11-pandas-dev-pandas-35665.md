---
tags: ,Needs-Tests,Regression,Timedelta
title: "BUG: iterrows encounters OverflowError with str and datetime64[ns] columns"
html_url: "https://github.com/pandas-dev/pandas/issues/35665"
user: allentsouhuang
repo: pandas-dev/pandas
---

- [x] I have checked that this issue has not already been reported.

- [x] I have confirmed this bug exists on the latest version of pandas.

- [ ] (optional) I have confirmed this bug exists on the master branch of pandas.

---

**Note**: Please read [this guide](https://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports) detailing how to provide the necessary information for us to reproduce your bug.

#### Code Sample, a copy-pastable example

```python
import pandas as pd
foo = pd.DataFrame({'some_string': ['612092d7-071f-467e832d-dd53e0f2b590-0006'], 'time': [pd.NaT]})
for _, row in foo.iterrows():
    pass

```

#### Problem description

The error `OverflowError: Python int too large to convert to C long`. I would expect the snippet to iterate just fine without any issue.

#### Expected Output

The snippet is not expected to show any output.

#### Output of ``pd.show_versions()``

```
INSTALLED VERSIONS
------------------
commit           : d9fff2792bf16178d4e450fe7384244e50635733
python           : 3.8.5.final.0
python-bits      : 64
OS               : Darwin
OS-release       : 19.5.0
Version          : Darwin Kernel Version 19.5.0: Tue May 26 20:41:44 PDT 2020; root:xnu-6153.121.2~2/RELEASE_X86_64
machine          : x86_64
processor        : i386
byteorder        : little
LC_ALL           : None
LANG             : en_US.UTF-8
LOCALE           : en_US.UTF-8

pandas           : 1.1.0
numpy            : 1.19.1
pytz             : 2020.1
dateutil         : 2.8.1
pip              : 20.2
setuptools       : 49.2.0.post20200712
Cython           : 0.29.21
pytest           : 6.0.1
hypothesis       : None
sphinx           : None
blosc            : None
feather          : None
xlsxwriter       : None
lxml.etree       : None
html5lib         : None
pymysql          : None
psycopg2         : None
jinja2           : 2.11.2
IPython          : 7.17.0
pandas_datareader: None
bs4              : None
bottleneck       : None
fsspec           : None
fastparquet      : None
gcsfs            : None
matplotlib       : 3.3.0
numexpr          : None
odfpy            : None
openpyxl         : None
pandas_gbq       : None
pyarrow          : None
pytables         : None
pyxlsb           : None
s3fs             : None
scipy            : 1.5.2
sqlalchemy       : None
tables           : None
tabulate         : None
xarray           : None
xlrd             : None
xlwt             : None
numba            : None
```


<details>

```
---------------------------------------------------------------------------
OverflowError                             Traceback (most recent call last)
<ipython-input-7-d71373909082> in <module>
      1 foo = pd.DataFrame({'some_string': ['612092d7-071f-467e832d-dd53e0f2b590-0006'], 'time': [pd.NaT]})
----> 2 for _, row in foo.iterrows():
      3     pass

~/env/miniconda3/envs/data/lib/python3.8/site-packages/pandas/core/frame.py in iterrows(self)
   1011         klass = self._constructor_sliced
   1012         for k, v in zip(self.index, self.values):
-> 1013             s = klass(v, index=columns, name=k)
   1014             yield k, s
   1015 

~/env/miniconda3/envs/data/lib/python3.8/site-packages/pandas/core/series.py in __init__(self, data, index, dtype, name, copy, fastpath)
    325                     data = data.copy()
    326             else:
--> 327                 data = sanitize_array(data, index, dtype, copy, raise_cast_failure=True)
    328 
    329                 data = SingleBlockManager.from_array(data, index)

~/env/miniconda3/envs/data/lib/python3.8/site-packages/pandas/core/construction.py in sanitize_array(data, index, dtype, copy, raise_cast_failure)
    425         else:
    426             # we will try to copy be-definition here
--> 427             subarr = _try_cast(data, dtype, copy, raise_cast_failure)
    428 
    429     elif isinstance(data, ABCExtensionArray):

~/env/miniconda3/envs/data/lib/python3.8/site-packages/pandas/core/construction.py in _try_cast(arr, dtype, copy, raise_cast_failure)
    551             subarr = arr
    552         else:
--> 553             subarr = maybe_cast_to_datetime(arr, dtype)
    554 
    555         # Take care in creating object arrays (but iterators are not

~/env/miniconda3/envs/data/lib/python3.8/site-packages/pandas/core/dtypes/cast.py in maybe_cast_to_datetime(value, dtype, errors)
   1430             )
   1431         ):
-> 1432             value = maybe_infer_to_datetimelike(value)
   1433 
   1434     return value

~/env/miniconda3/envs/data/lib/python3.8/site-packages/pandas/core/dtypes/cast.py in maybe_infer_to_datetimelike(value, convert_dates)
   1290             # try timedelta first to avoid spurious datetime conversions
   1291             # e.g. '00:00:01' is a timedelta but technically is also a datetime
-> 1292             value = try_timedelta(v)
   1293             if lib.infer_dtype(value, skipna=False) in ["mixed"]:
   1294                 # cannot skip missing values, as NaT implies that the string

~/env/miniconda3/envs/data/lib/python3.8/site-packages/pandas/core/dtypes/cast.py in try_timedelta(v)
   1266 
   1267         try:
-> 1268             td_values = to_timedelta(v)
   1269         except ValueError:
   1270             return v.reshape(shape)

~/env/miniconda3/envs/data/lib/python3.8/site-packages/pandas/core/tools/timedeltas.py in to_timedelta(arg, unit, errors)
    110         arg = arg.item()
    111     elif is_list_like(arg) and getattr(arg, "ndim", 1) == 1:
--> 112         return _convert_listlike(arg, unit=unit, errors=errors)
    113     elif getattr(arg, "ndim", 1) > 1:
    114         raise TypeError(

~/env/miniconda3/envs/data/lib/python3.8/site-packages/pandas/core/tools/timedeltas.py in _convert_listlike(arg, unit, errors, name)
    149 
    150     try:
--> 151         value = sequence_to_td64ns(arg, unit=unit, errors=errors, copy=False)[0]
    152     except ValueError:
    153         if errors == "ignore":

~/env/miniconda3/envs/data/lib/python3.8/site-packages/pandas/core/arrays/timedeltas.py in sequence_to_td64ns(data, copy, unit, errors)
    926     if is_object_dtype(data.dtype) or is_string_dtype(data.dtype):
    927         # no need to make a copy, need to convert if string-dtyped
--> 928         data = objects_to_td64ns(data, unit=unit, errors=errors)
    929         copy = False
    930 

~/env/miniconda3/envs/data/lib/python3.8/site-packages/pandas/core/arrays/timedeltas.py in objects_to_td64ns(data, unit, errors)
   1036     values = np.array(data, dtype=np.object_, copy=False)
   1037 
-> 1038     result = array_to_timedelta64(values, unit=unit, errors=errors)
   1039     return result.view("timedelta64[ns]")
   1040 

pandas/_libs/tslibs/timedeltas.pyx in pandas._libs.tslibs.timedeltas.array_to_timedelta64()

pandas/_libs/tslibs/timedeltas.pyx in pandas._libs.tslibs.timedeltas.parse_timedelta_string()

pandas/_libs/tslibs/timedeltas.pyx in pandas._libs.tslibs.timedeltas.timedelta_from_spec()

pandas/_libs/tslibs/conversion.pyx in pandas._libs.tslibs.conversion.cast_from_unit()

OverflowError: Python int too large to convert to C long
```

</details>
