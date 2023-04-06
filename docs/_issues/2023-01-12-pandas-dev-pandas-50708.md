---
tags: ,Needs-Tests,Subclassing
title: "BUG: accessing `.dtypes` in a subclass constructor with large frames causes infinite loop"
html_url: "https://github.com/pandas-dev/pandas/issues/50708"
user: ryandvmartin
repo: pandas-dev/pandas
---

### Pandas version checks

- [X] I have checked that this issue has not already been reported.

- [X] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas.

- [ ] I have confirmed this bug exists on the main branch of pandas.


### Reproducible Example

```python
import pandas as pd
import numpy as np

class MyFrame(pd.DataFrame): 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        for col in self.columns:
            if self.dtypes[col] == "O":
                self[col] = pd.to_numeric(self[col], errors='ignore')
    @property
    def _constructor(self): 
        return type(self)

def get_frame(N): 
    return MyFrame(
        data=np.vstack(
            [np.where(np.random.rand(N) > 0.36, np.random.rand(N), np.nan) for _ in range(10)]
        ).T, 
        columns=[f"col{i}" for i in range(10)]
    )

# When N is smallish, no issue
frame = get_frame(5000)
frame.dropna(subset=["col0", "col1"])
print("5000 passed")

# When N is largeish, `dropna` recurses in the `__init__` through `self.dtypes[col]` access
frame = get_frame(5000000)
frame.dropna(subset=["col0", "col1"])
print("5000000 passed")
```

Modifying the class `__init__` to (remove `self.dtypes[col]`): 
```python
class MyFrame(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for col, dt in zip(self.columns, self.dtypes):
            if dt == "O":
                self[col] = pd.to_numeric(self[col], errors='ignore')
    @property
    def _constructor(self):
        return type(self)
```


### Issue Description

I _think_ there has been a regression with access to `.dtypes` property in inherited `DataFrame` constructors, as noted in the MRE.

We noticed this on pandas 1.5.2 when upgrading our production environment , but reproduced with pandas 1.4.4, 1.4.0. The code works as expected going back to 1.3.5. 

As far as what should be done, perhaps more notes about what can/can't/should not be called/done in subclass `__init__` routines when inheriting from `pd.DataFrame`? 



### Expected Behavior

No infinite loop? 

### Installed Versions

<details>

```
In [2]: pd.show_versions()
C:\Users\user\Python\lib\site-packages\_distutils_hack\__init__.py:33: UserWarning: Setuptools is replacing distutils.
  warnings.warn("Setuptools is replacing distutils.")

INSTALLED VERSIONS
------------------
commit           : 8dab54d6573f7186ff0c3b6364d5e4dd635ff3e7
python           : 3.10.8.final.0
python-bits      : 64
OS               : Windows
OS-release       : 10
Version          : 10.0.22621
machine          : AMD64
processor        : AMD64 Family 25 Model 33 Stepping 2, AuthenticAMD
byteorder        : little
LC_ALL           : None
LANG             : None
LOCALE           : English_United States.1252

pandas           : 1.5.2
numpy            : 1.21.6
pytz             : 2022.7
dateutil         : 2.8.2
setuptools       : 65.6.3
pip              : 22.3.1
Cython           : 0.29.33
pytest           : 6.2.5
hypothesis       : 6.62.0
sphinx           : 5.3.0
blosc            : None
feather          : None
xlsxwriter       : None
lxml.etree       : 4.9.2
html5lib         : None
pymysql          : None
psycopg2         : 2.9.3
jinja2           : 3.1.2
IPython          : 8.8.0
pandas_datareader: None
bs4              : 4.11.1
bottleneck       : None
brotli           :
fastparquet      : None
fsspec           : 2022.11.0
gcsfs            : None
matplotlib       : 3.5.3
numba            : 0.56.4
numexpr          : 2.8.3
odfpy            : None
openpyxl         : 3.0.10
pandas_gbq       : None
pyarrow          : 10.0.1
pyreadstat       : None
pyxlsb           : None
s3fs             : None
scipy            : 1.10.0
snappy           : None
sqlalchemy       : 1.4.46
tables           : 3.7.0
tabulate         : None
xarray           : None
xlrd             : 2.0.1
xlwt             : None
zstandard        : 0.19.0
tzdata           : None
```

</details>
