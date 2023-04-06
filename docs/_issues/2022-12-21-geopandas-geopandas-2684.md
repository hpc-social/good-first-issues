---
tags: ,bug
title: "BUG: GeoDataFrame.iterfeatures with na='drop' crashes on non-scalar columns"
html_url: "https://github.com/geopandas/geopandas/issues/2684"
user: himikof
repo: geopandas/geopandas
---

- [x] I have checked that this issue has not already been reported.

- [x] I have confirmed this bug exists on the latest version of geopandas.

- [x] (optional) I have confirmed this bug exists on the main branch of geopandas.

---

#### Code Sample, a copy-pastable example

```python
import geopandas
gdf = geopandas.GeoDataFrame(dict(geometry=geopandas.GeoSeries.from_wkt(['POINT EMPTY']), test=[[1, 2]]))
print(list(gdf.iterfeatures(na='drop')))
```

#### Problem description

The code crashes with 
```
Traceback (most recent call last):
  File "<ipython-input-49-8489f3b42ff4>", line 1, in <module>
    list(gdf.iterfeatures(na='drop'))
  File "/home/nofitserov/.cache/pypoetry/virtualenvs/test-RPhZg3RA-py3.9/lib/python3.9/site-packages/geopandas/geodataframe.py", line 885, in iterfeatures
    properties_items = {
  File "/home/nofitserov/.cache/pypoetry/virtualenvs/test-RPhZg3RA-py3.9/lib/python3.9/site-packages/geopandas/geodataframe.py", line 886, in <dictcomp>
    k: v for k, v in zip(properties_cols, row) if not pd.isnull(v)
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
```
due to auto-magic type confusion in this code:
```python
                if na == "drop":
                    properties_items = {
                        k: v for k, v in zip(properties_cols, row) if not pd.isnull(v)
                    }
```
When `v` is not a pandas scalar with len>1, `pd.isnull` returns a boolean array instead of a single value, breaking the logic completely. I think that explicitly excluding non-scalars from this check should help, as they should never be dropped here?

#### Expected Output
```
[{'id': '0', 'type': 'Feature', 'properties': {'test': [1, 2]}, 'geometry': None}]
```


#### Output of ``geopandas.show_versions()``

<details>

SYSTEM INFO
-----------
python     : 3.9.9 (main, Nov 19 2021, 00:00:00)  [GCC 10.3.1 20210422 (Red Hat 10.3.1-1)]
executable : /home/nofitserov/.cache/pypoetry/virtualenvs/test-RPhZg3RA-py3.9/bin/python
machine    : Linux-5.14.18-100.fc33.x86_64-x86_64-with-glibc2.32

GEOS, GDAL, PROJ INFO
---------------------
GEOS       : 3.11.1
GEOS lib   : None
GDAL       : 3.4.3
GDAL data dir: /home/nofitserov/.cache/pypoetry/virtualenvs/test-RPhZg3RA-py3.9/lib64/python3.9/site-packages/fiona/gdal_data
PROJ       : 9.1.0
PROJ data dir: /home/nofitserov/.cache/pypoetry/virtualenvs/test-RPhZg3RA-py3.9/lib64/python3.9/site-packages/pyproj/proj_dir/share/proj

PYTHON DEPENDENCIES
-------------------
geopandas  : 0.12.2
numpy      : 1.23.5
pandas     : 1.5.2
pyproj     : 3.4.1
shapely    : 2.0.0
fiona      : 1.8.22
geoalchemy2: None
geopy      : None
matplotlib : 3.6.2
mapclassify: 2.4.3
pygeos     : None
pyogrio    : v0.4.2
psycopg2   : None
pyarrow    : 10.0.1
rtree      : None


</details>
