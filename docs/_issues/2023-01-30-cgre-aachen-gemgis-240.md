---
tags: documentation,enhancement
title: "[DOC] Add Notebook to illustrate exporting shapefiles from GemPy geological maps and section lines"
html_url: "https://github.com/cgre-aachen/gemgis/issues/240"
user: KetMic
repo: cgre-aachen/gemgis
---

**Is your feature request related to a problem? Please describe.**
Add notebook to illustrate exporting GemPy section lines and geological maps to shapefiles.

**Describe the solution you'd like**
Upload a notebook showing how to export 

1) GemPy section lines as shapefile:

`from shapely.geometry import LineString`
`gdf_sections = geo_model.grid.sections.df.copy(deep=True)`  
`gdf_sections.reset_index()` 
`linestrings = [LineString((gdf_sections.iloc[i]['start'],gdf_sections.iloc[i]['stop'] )) for i in range(len(gdf_sections))]`
`gdf_sections_new = gpd.GeoDataFrame(geometry=linestrings, data= gdf_sections.reset_index()[['index']], crs='EPSG:32632')`      
`gdf_sections_new.to_file(file_path + 'test_sections.shp') `

2) GemPy geological map polygons as shapefile:

`gdf = gg.postprocessing.extract_lithologies(geo_model, geo_model.grid.regular_grid.extent[:4], crs='EPSG:32632')`
`gdf.to_file(file_path + 'test.shp')`

