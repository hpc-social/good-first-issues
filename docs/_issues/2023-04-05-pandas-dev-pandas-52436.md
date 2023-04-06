---
tags: ,Docs,Regression,Reshaping
title: "BUG: DataFrame.pivot(index=None) raises KeyError"
html_url: "https://github.com/pandas-dev/pandas/issues/52436"
user: douglas-raillard-arm
repo: pandas-dev/pandas
---

### Pandas version checks

- [X] I have checked that this issue has not already been reported.

- [X] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas.

- [ ] I have confirmed this bug exists on the [main branch](https://pandas.pydata.org/docs/dev/getting_started/install.html#installing-the-development-version-of-pandas) of pandas.


### Reproducible Example

```python
import pandas as pd

df = pd.DataFrame(dict(a=[0,1,1,0], b=[42,43,44,45]), index=[10,20,30,40])
pivoted = df.pivot(index=None, columns='a', values='b')
print(pivoted)
```

### Issue Description

DataFrame.pivot() documentation states:

```
index: str or object or a list of str, optional

    Column to use to make new frame’s index. If None, uses existing index.
```
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html

In pandas 1.5, index=None provides the expected result. In pandas 2.0.0, it raises a KeyError exception.

### Expected Behavior

index=None should use the existing index as per documentation, or documentation should be modified and 2.0.0 breaking changes list updated to add that new behavior. 

### Installed Versions

<details>
INSTALLED VERSIONS
------------------
commit           : 478d340667831908b5b4bf09a2787a11a14560c9
python           : 3.8.10.final.0
python-bits      : 64
OS               : Linux
OS-release       : 5.15.0-60-generic
Version          : #66~20.04.1-Ubuntu SMP Wed Jan 25 09:41:30 UTC 2023
machine          : x86_64
processor        : x86_64
byteorder        : little
LC_ALL           : None
LANG             : en_US.UTF-8
LOCALE           : en_US.UTF-8

pandas           : 2.0.0
numpy            : 1.24.2
pytz             : 2023.3
dateutil         : 2.8.2
setuptools       : 67.6.1
pip              : 23.0.1
Cython           : None
pytest           : 7.2.2
hypothesis       : None
sphinx           : 6.1.3
blosc            : None
feather          : None
xlsxwriter       : None
lxml.etree       : 4.9.2
html5lib         : None
pymysql          : None
psycopg2         : None
jinja2           : 3.1.2
IPython          : 8.12.0
pandas_datareader: None
bs4              : 4.12.0
bottleneck       : None
brotli           : None
fastparquet      : None
fsspec           : None
gcsfs            : None
matplotlib       : 3.7.1
numba            : None
numexpr          : None
odfpy            : None
openpyxl         : None
pandas_gbq       : None
pyarrow          : 11.0.0
pyreadstat       : None
pyxlsb           : None
s3fs             : None
scipy            : 1.10.1
snappy           : None
sqlalchemy       : None
tables           : None
tabulate         : None
xarray           : None
xlrd             : None
zstandard        : None
tzdata           : 2023.3
qtpy             : None
pyqt5            : None

</details>
