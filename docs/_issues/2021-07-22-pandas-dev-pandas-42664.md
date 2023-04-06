---
tags: ,Docs,IO-Parquet,Strings
title: "BUG: `DataFrame.to_parquet` doesn't round-trip pyarrow StringDtype"
html_url: "https://github.com/pandas-dev/pandas/issues/42664"
user: TomAugspurger
repo: pandas-dev/pandas
---

- [x] I have checked that this issue has not already been reported.

- [x] I have confirmed this bug exists on the latest version of pandas.

- [ ] (optional) I have confirmed this bug exists on the master branch of pandas.

---


#### Code Sample, a copy-pastable example

```python
import pandas as pd
a = pd.DataFrame({"A": pd.array(['a', 'b'], dtype=pd.StringDtype("pyarrow"))})
a.to_parquet("test.parquet")
b = pd.read_parquet("test.parquet")
pd.testing.assert_frame_equal(a, b)

---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
/tmp/ipykernel_493/3001616580.py in <module>
      3 a.to_parquet("test.parquet")
      4 b = pd.read_parquet("test.parquet")
----> 5 pd.testing.assert_frame_equal(a, b)

    [... skipping hidden 3 frame]

/srv/conda/envs/notebook/lib/python3.8/site-packages/pandas/_testing/asserters.py in raise_assert_detail(obj, message, left, right, diff, index_values)
    663         msg += f"\n[diff]: {diff}"
    664 
--> 665     raise AssertionError(msg)
    666 
    667 

AssertionError: Attributes of DataFrame.iloc[:, 0] (column name="A") are different

Attribute "dtype" are different
[left]:  string[pyarrow]
[right]: string[python]
```


#### Problem description

read_parquet currently loads all string dtype as `string[python]`. We'd ideally match what was written.

#### Expected Output

A DataFrame with `string[pyarrow]` rather than `string[python]`

#### Output of ``pd.show_versions()``

<details>

```
INSTALLED VERSIONS
------------------
commit           : f00ed8f47020034e752baf0250483053340971b0
python           : 3.8.10.final.0
python-bits      : 64
OS               : Linux
OS-release       : 5.4.0-1040-azure
Version          : #42~18.04.1-Ubuntu SMP Mon Feb 8 19:05:32 UTC 2021
machine          : x86_64
processor        : x86_64
byteorder        : little
LC_ALL           : C.UTF-8
LANG             : C.UTF-8
LOCALE           : en_US.UTF-8

pandas           : 1.3.0
numpy            : 1.21.0
pytz             : 2021.1
dateutil         : 2.7.5
pip              : 20.3.4
setuptools       : 49.6.0.post20210108
Cython           : None
pytest           : None
hypothesis       : None
sphinx           : None
blosc            : 1.10.2
feather          : None
xlsxwriter       : None
lxml.etree       : None
html5lib         : None
pymysql          : None
psycopg2         : 2.9.1 (dt dec pq3 ext lo64)
jinja2           : 3.0.1
IPython          : 7.25.0
pandas_datareader: None
bs4              : 4.9.3
bottleneck       : 1.3.2
fsspec           : 2021.06.1
fastparquet      : None
gcsfs            : 2021.06.1
matplotlib       : 3.4.2
numexpr          : None
odfpy            : None
openpyxl         : None
pandas_gbq       : None
pyarrow          : 4.0.0
pyxlsb           : None
s3fs             : 2021.06.1
scipy            : 1.7.0
sqlalchemy       : 1.4.20
tables           : None
tabulate         : 0.8.9
xarray           : 0.18.2
xlrd             : None
xlwt             : None
numba            : 0.53.1
```​

</details>
