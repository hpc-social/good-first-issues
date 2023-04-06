---
tags: ,Needs-Tests
title: "BUG: IndexError when boolean indexing on pyarrow array"
html_url: "https://github.com/pandas-dev/pandas/issues/52319"
user: aeryen
repo: pandas-dev/pandas
---

### Pandas version checks

- [X] I have checked that this issue has not already been reported.

- [X] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas.

- [ ] I have confirmed this bug exists on the [main branch](https://pandas.pydata.org/docs/dev/getting_started/install.html#installing-the-development-version-of-pandas) of pandas.


### Reproducible Example

```python
df = pd.DataFrame( [["A", "B", "C"], [True, True, False]] ).T
df.columns=["strings", "ids"]
df["strings"] = df.strings.astype("string[pyarrow]")
df.loc[df.ids, "strings"] = df.loc[df.ids, "strings"]
```


### Issue Description

Using the above example will result in IndexError at this line:
`df.loc[df.ids, "strings"] = df.loc[df.ids, "strings"]`

Below is the Exception.
````
File [~/anaconda3/envs/wtrr/lib/python3.8/site-packages/pandas/core/indexing.py:818], in _LocationIndexer.__setitem__(self, key, value)
    815 self._has_valid_setitem_indexer(key)
    817 iloc = self if self.name == "iloc" else self.obj.iloc
--> 818 iloc._setitem_with_indexer(indexer, value, self.name)

File [~/anaconda3/envs/wtrr/lib/python3.8/site-packages/pandas/core/indexing.py:1795], in _iLocIndexer._setitem_with_indexer(self, indexer, value, name)
   1792 # align and set the values
   1793 if take_split_path:
   1794     # We have to operate column-wise
-> 1795     self._setitem_with_indexer_split_path(indexer, value, name)
   1796 else:
   1797     self._setitem_single_block(indexer, value, name)

File [~/anaconda3/envs/wtrr/lib/python3.8/site-packages/pandas/core/indexing.py:1838], in _iLocIndexer._setitem_with_indexer_split_path(self, indexer, value, name)
   1834     self._setitem_with_indexer_2d_value(indexer, value)
   1836 elif len(ilocs) == 1 and lplane_indexer == len(value) and not is_scalar(pi):
   1837     # We are setting multiple rows in a single column.
-> 1838     self._setitem_single_column(ilocs[0], value, pi)
   1840 elif len(ilocs) == 1 and 0 != lplane_indexer != len(value):
   1841     # We are trying to set N values into M entries of a single
   1842     #  column, which is invalid for N != M
   1843     # Exclude zero-len for e.g. boolean masking that is all-false
   1845     if len(value) == 1 and not is_integer(info_axis):
   1846         # This is a case like df.iloc[:3, [1]] = [0]
   1847         #  where we treat as df.iloc[:3, 1] = 0

File [~/anaconda3/envs/wtrr/lib/python3.8/site-packages/pandas/core/indexing.py:1992], in _iLocIndexer._setitem_single_column(self, loc, value, plane_indexer)
   1988         value = value[pi]
   1989 else:
   1990     # set value into the column (first attempting to operate inplace, then
   1991     #  falling back to casting if necessary)
-> 1992     self.obj._mgr.column_setitem(loc, plane_indexer, value)
   1993     self.obj._clear_item_cache()
   1994     return

File [~/anaconda3/envs/wtrr/lib/python3.8/site-packages/pandas/core/internals/managers.py:1369, in BlockManager.column_setitem(self, loc, idx, value)
   1366     self._clear_reference_block(blkno)
   1368 col_mgr = self.iget(loc)
-> 1369 new_mgr = col_mgr.setitem((idx,), value)
   1370 self.iset(loc, new_mgr._block.values, inplace=True)

File [~/anaconda3/envs/wtrr/lib/python3.8/site-packages/pandas/core/internals/managers.py:388], in BaseBlockManager.setitem(self, indexer, value)
    383 if _using_copy_on_write() and not self._has_no_reference(0):
    384     # if being referenced -> perform Copy-on-Write and clear the reference
    385     # this method is only called if there is a single block -> hardcoded 0
    386     self = self.copy()
--> 388 return self.apply("setitem", indexer=indexer, value=value)

File [~/anaconda3/envs/wtrr/lib/python3.8/site-packages/pandas/core/internals/managers.py:347], in BaseBlockManager.apply(self, f, align_keys, ignore_failures, **kwargs)
    345         applied = b.apply(f, **kwargs)
    346     else:
--> 347         applied = getattr(b, f)(**kwargs)
    348 except (TypeError, NotImplementedError):
    349     if not ignore_failures:

File [~/anaconda3/envs/wtrr/lib/python3.8/site-packages/pandas/core/internals/blocks.py:1415], in EABackedBlock.setitem(self, indexer, value)
   1412 check_setitem_lengths(indexer, value, values)
   1414 try:
-> 1415     values[indexer] = value
   1416 except (ValueError, TypeError) as err:
   1417     _catch_deprecated_value_error(err)

File [~/anaconda3/envs/wtrr/lib/python3.8/site-packages/pandas/core/arrays/arrow/array.py:890], in ArrowExtensionArray.__setitem__(self, key, value)
    869 """Set one or more values inplace.
    870 
    871 Parameters
   (...)
    887 None
    888 """
    889 key = check_array_indexer(self, key)
--> 890 indices = self._indexing_key_to_indices(key)
    891 value = self._maybe_convert_setitem_value(value)
    893 argsort = np.argsort(indices)

File [~/anaconda3/envs/wtrr/lib/python3.8/site-packages/pandas/core/arrays/arrow/array.py:939], in ArrowExtensionArray._indexing_key_to_indices(self, key)
    937 else:
    938     key = np.asarray(key)
--> 939     indices = np.arange(n)[key]
    940 return indices

IndexError: too many indices for array: array is 1-dimensional, but 2 were indexed`
````

### Expected Behavior

The code should complete successfully, with result being similar to 
`df["strings"].loc[df.ids] = df["strings"].loc[df.ids]`


### Installed Versions

<details>

INSTALLED VERSIONS
------------------
commit           : 91111fd99898d9dcaa6bf6bedb662db4108da6e6
python           : 3.8.16.final.0
python-bits      : 64
OS               : Linux
OS-release       : 5.4.235-151.344.amzn2int.x86_64
Version          : #1 SMP Sat Mar 11 23:51:58 UTC 2023
machine          : x86_64
processor        : x86_64
byteorder        : little
LC_ALL           : None
LANG             : en_US.UTF-8
LOCALE           : en_US.UTF-8

pandas           : 1.5.1
numpy            : 1.23.4
pytz             : 2022.7
dateutil         : 2.8.2
setuptools       : 65.6.3
pip              : 23.0.1
Cython           : None
pytest           : None
hypothesis       : None
sphinx           : None
blosc            : None
feather          : None
xlsxwriter       : None
lxml.etree       : 4.9.2
html5lib         : None
pymysql          : 1.0.3
psycopg2         : None
jinja2           : None
IPython          : 8.11.0
pandas_datareader: None
bs4              : 4.12.0
bottleneck       : 1.3.5
brotli           : None
fastparquet      : None
fsspec           : None
gcsfs            : None
matplotlib       : None
numba            : None
numexpr          : 2.8.4
odfpy            : None
openpyxl         : 3.0.10
pandas_gbq       : None
pyarrow          : 10.0.1
pyreadstat       : None
pyxlsb           : None
s3fs             : None
scipy            : None
snappy           : None
sqlalchemy       : None
tables           : None
tabulate         : None
xarray           : None
xlrd             : None
xlwt             : None
zstandard        : None
tzdata           : None

</details>
