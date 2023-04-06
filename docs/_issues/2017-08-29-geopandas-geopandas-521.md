---
tags: bug
title: "drop_duplicates functionality"
html_url: "https://github.com/geopandas/geopandas/issues/521"
user: byezy
repo: geopandas/geopandas
---

Currently, applying gdf.drop_duplicates() on a point shapefiles gives:

File "pandas/_libs/hashtable_class_helper.pxi", line 1312, in pandas._libs.hashtable.PyObjectHashTable.get_labels (pandas/_libs/hashtable.c:22034)
TypeError: unhashable type: 'Point'
