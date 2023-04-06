---
tags: 
title: "Deprecate GeoSeries.almost_equals (deprecated in shapely)"
html_url: "https://github.com/geopandas/geopandas/issues/2538"
user: jorisvandenbossche
repo: geopandas/geopandas
---

The `almost_equals` method in Shapely is deprecated (and will be removed in a future version): https://github.com/shapely/shapely/blob/6c896a7fb0348f46630e4045e1fdc3e54212dc42/shapely/geometry/base.py#L666-L669

So we should probably follow suite in geopandas as well and deprecate our almost_equals method in favor of its alias `equals_exact`