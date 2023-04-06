---
tags: ,enhancement
title: "ENH: Improve error message for attempting to write multiple geometry columns using `to_file`"
html_url: "https://github.com/geopandas/geopandas/issues/2566"
user: m-richards
repo: geopandas/geopandas
---

xref #2565

```python
In [16]: gdf = gpd.GeoDataFrame({"a":[1,2]}, geometry=[Point(1,1), Point(1,2)])

In [17]: gdf['geom2'] = gdf.geometry

In [18]: gdf.to_file("tmp.gpkg")
-----------------------------------
File ...\venv\lib\site-packages\geopandas\io\file.py:596, in infer_schema.<locals>.convert_type(column, in_type)
    594     out_type = types[str(in_type)]
    595 else:
--> 596     out_type = type(np.zeros(1, in_type).item()).__name__
    597 if out_type == "long":
    598     out_type = "int"

TypeError: Cannot interpret '<geopandas.array.GeometryDtype object at 0x0000025FA88908E0>' as a data type

```

