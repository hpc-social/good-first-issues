---
tags: Apply,Docs,Groupby
title: "BUG: Automatic data alignment fails in the `transform` method of `GroupBy` objects"
html_url: "https://github.com/pandas-dev/pandas/issues/41550"
user: gdudziuk
repo: pandas-dev/pandas
---

- [x] I have checked that this issue has not already been reported. _(... or at least I couldn't find an issue like this)_

- [x] I have confirmed this bug exists on the latest version of pandas. _(which is 1.2.4 at the moment)_

- [ ] (optional) I have confirmed this bug exists on the master branch of pandas.

---
#### Example data and intended output

Let's create some synthetic data to illustrate the issue:
```python
df = pd.DataFrame({
    'household_id' : ['b80', 'b90', 'a70', 'c60', 'a50', 'X13', 'X12', 'X11', 'XYZ'],
    'district' : 5*['Neverland'] + 4*['Narnia'],
    'income' : [1200, 2000, 1000, 900, 1200, 1500, 800, 900, 850],
    })
df = df.set_index('household_id')
```

```
               district  income
household_id                   
b80           Neverland    1200
b90           Neverland    2000
a70           Neverland    1000
c60           Neverland     900
a50           Neverland    1200
X13              Narnia    1500
X12              Narnia     800
X11              Narnia     900
XYZ              Narnia     850
```
Suppose we want to add some money to the poorest households. We have 600$ per district to distribute to households and we decide that this money will be divided equally among all households in a district that have income 1000$ or below. So, our expected result is:
```
               district  income
household_id                   
b80           Neverland    1200
b90           Neverland    2000
a70           Neverland    1300
c60           Neverland    1200
a50           Neverland    1200
X13              Narnia    1500
X12              Narnia    1000
X11              Narnia    1100
XYZ              Narnia    1050
```
#### Code sample and actual output

We will try to achieve the described goal by using `groupby` followed by `transform`:

```python
def add_income_to_poor_households(households):
    money_to_share = 600
    poor_households_ids = households.index[households<=1000]
    paylist = pd.Series(money_to_share/len(poor_households_ids), index=poor_households_ids)
    return households.add(paylist, fill_value=0)

grouped = df.groupby('district')['income']
df['income'] = grouped.transform(add_income_to_poor_households)
```
After executing the above code `df` looks like this:
```
               district  income
household_id                   
b80           Neverland    1200
b90           Neverland    1300
a70           Neverland    1200
c60           Neverland    2000
a50           Neverland    1200
X13              Narnia    1100
X12              Narnia    1000
X11              Narnia    1500
XYZ              Narnia    1050
```
which doesn't match the expected output given above.

#### Problem description

The output obtained with the sample code doesn't match the expected output. It's unclear to me which of the assumptions specified in the documentation of `SeriesGrupBy.transform` are violated by the above code. I think that none, so I figure it's a bug.

To gain some insight into the roots of the problem, note that the series returned by `add_income_to_poor_households` are ordered differently than the original ones. Please execute this on the original `df` (before changing it via using `transform`):
```python
households = df[df['district']=='Neverland']['income']
```
Now `households` looks like this:
```
household_id
b80    1200
b90    2000
a70    1000
c60     900
a50    1200
Name: income, dtype: int64
```
But after calling `add_income_to_poor_households` the order of the index changes:
```python
add_income_to_poor_households(households)
```
```
household_id
a50    1200.0
a70    1300.0
b80    1200.0
b90    2000.0
c60    1200.0
dtype: float64
```
So possibly the `transform` method fails to align the output of the inner function `add_income_to_poor_households` to the original indices of the data frame subject to grouping.

#### Output of ``pd.show_versions()``

<details>

INSTALLED VERSIONS
------------------
commit           : 2cb96529396d93b46abab7bbc73a208e708c642e
python           : 3.8.5.final.0
python-bits      : 64
OS               : Linux
OS-release       : 5.4.0-73-generic
Version          : #82-Ubuntu SMP Wed Apr 14 17:39:42 UTC 2021
machine          : x86_64
processor        : x86_64
byteorder        : little
LC_ALL           : None
LANG             : pl_PL.UTF-8
LOCALE           : pl_PL.UTF-8

pandas           : 1.2.4
numpy            : 1.20.2
pytz             : 2021.1
dateutil         : 2.8.1
pip              : 21.0.1
setuptools       : 54.2.0
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
jinja2           : 2.11.3
IPython          : 7.22.0
pandas_datareader: None
bs4              : None
bottleneck       : None
fsspec           : None
fastparquet      : None
gcsfs            : None
matplotlib       : None
numexpr          : None
odfpy            : None
openpyxl         : 3.0.7
pandas_gbq       : None
pyarrow          : None
pyxlsb           : None
s3fs             : None
scipy            : None
sqlalchemy       : None
tables           : None
tabulate         : None
xarray           : None
xlrd             : 2.0.1
xlwt             : None
numba            : None


</details>
