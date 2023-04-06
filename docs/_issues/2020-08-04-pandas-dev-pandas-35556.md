---
tags: ,Docs
title: "DOC: `.str.cat` output in case of `Index` object"
html_url: "https://github.com/pandas-dev/pandas/issues/35556"
user: galipremsagar
repo: pandas-dev/pandas
---

- [x] I have checked that this issue has not already been reported.

- [x] I have confirmed this bug exists on the latest version of pandas.

- [ ] (optional) I have confirmed this bug exists on the master branch of pandas.

---


#### Code Sample, a copy-pastable example

```python
import pandas as pd
import numpy as np
i = pd.Index(["AbC", "de", "FGHI", "j", "kLm"])
other = (
            pd.Series(["f", "g", "h", "i", "j"]),
            np.array(["f", "a", "b", "f", "a"]),
            pd.Series(["f", "g", "h", "i", "j"]),
            np.array(["f", "a", "b", "f", "a"]),
            np.array(["f", "a", "b", "f", "a"]),
            pd.Index(["1", "2", "3", "4", "5"]),
            np.array(["f", "a", "b", "f", "a"]),
            pd.Index(["f", "g", "h", "i", "j"]),
)
print(i.str.cat(other))
x = pd.Series(["f", "g", "h", "i", "j"])
print(i.str.cat(x))

```

0.25.3 output:
```python
Index(['AbCfffff1ff', 'degagaa2ag', 'FGHIhbhbb3bh', 'jififf4fi',
       'kLmjajaa5aj'],
      dtype='object')
Index(['AbCf', 'deg', 'FGHIh', 'ji', 'kLmj'], dtype='object')
```

1.1.0 output:
```python
Index([nan, nan, nan, nan, nan], dtype='object')
Index([nan, nan, nan, nan, nan], dtype='object')
```

#### Problem description

The output of 0.25.3 version seems to be correct as when we change `i` to be a `Series` the incorrect results go away:

```python
import pandas as pd
import numpy as np
i = pd.Series(["AbC", "de", "FGHI", "j", "kLm"])
other = (
            pd.Series(["f", "g", "h", "i", "j"]),
            np.array(["f", "a", "b", "f", "a"]),
            pd.Series(["f", "g", "h", "i", "j"]),
            np.array(["f", "a", "b", "f", "a"]),
            np.array(["f", "a", "b", "f", "a"]),
            pd.Index(["1", "2", "3", "4", "5"]),
            np.array(["f", "a", "b", "f", "a"]),
            pd.Index(["f", "g", "h", "i", "j"]),
)
print(i.str.cat(other))
x = pd.Series(["f", "g", "h", "i", "j"])
print(i.str.cat(x))


0     AbCfffff1ff
1      degagaa2ag
2    FGHIhbhbb3bh
3       jififf4fi
4     kLmjajaa5aj
dtype: object
0     AbCf
1      deg
2    FGHIh
3       ji
4     kLmj
dtype: object
```

#### Expected Output

The output should be similar to `Series` behaviour/ 0.25.3 behaviour.

#### Output of ``pd.show_versions()``

<details>

INSTALLED VERSIONS
------------------
commit           : d9fff2792bf16178d4e450fe7384244e50635733
python           : 3.7.3.final.0
python-bits      : 64
OS               : Darwin
OS-release       : 19.6.0
Version          : Darwin Kernel Version 19.6.0: Sun Jul  5 00:43:10 PDT 2020; root:xnu-6153.141.1~9/RELEASE_X86_64
machine          : x86_64
processor        : i386
byteorder        : little
LC_ALL           : None
LANG             : None
LOCALE           : en_US.UTF-8
pandas           : 1.1.0
numpy            : 1.19.0
pytz             : 2020.1
dateutil         : 2.8.1
pip              : 20.1.1
setuptools       : 49.1.0
Cython           : None
pytest           : None
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
IPython          : None
pandas_datareader: None
bs4              : None
bottleneck       : None
fsspec           : None
fastparquet      : None
gcsfs            : None
matplotlib       : None
numexpr          : None
odfpy            : None
openpyxl         : None
pandas_gbq       : None
pyarrow          : None
pytables         : None
pyxlsb           : None
s3fs             : None
scipy            : None
sqlalchemy       : None
tables           : None
tabulate         : None
xarray           : None
xlrd             : None
xlwt             : None
numba            : None

</details>
