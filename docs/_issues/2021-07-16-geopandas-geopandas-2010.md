---
tags: enhancement
title: "ENH: expose all shapely functions as GeoSeries/GeometryArray methods"
html_url: "https://github.com/geopandas/geopandas/issues/2010"
user: martinfleis
repo: geopandas/geopandas
---

`shapely` now contains some functions which could be exposed as methods on GeoSeries/GeometryArray levels.

Probably incomplete list of candidates (updated Feb 13, 2023):

- [ ] offset_curve
- [ ] concave_hull
- [ ] delaunay_triangles
- [ ] segmentize
- [ ] extract_unique_points
- [ ] build_area
- [ ] node
- [ ] polygonize
- [ ] polygonize_full
- [ ] remove_repeated_points
- [ ] reverse
- [ ] snap
- [ ] voronoi_polygons
- [ ] oriented_envelope
- [ ] minimum_rotated_rectangle
- [ ] transform 
- [ ] count_coordinates 
- [ ] set_coordinates
- [ ] prepare
- [ ] destroy_prepared
- [ ] from_geojson
- [ ] from_ragged_array
- [ ] to_geojson
- [ ] to_ragged_array
- [ ] line_merge
- [ ] shared_paths
- [ ] shortest_line
- [ ] hausdorff_distance
- [ ] frechet_distance
- [ ] minimum_clearance
- [x] minimum_bounding_radius
- [ ] linemerge
- [ ] polygonize
- [ ] polygonize_full
- [ ] triangulate
- [ ] voronoi_diagram
- [ ] split
- [ ] nearest_points
- [ ] validate
- [ ] snap
- [ ] orient
- [ ] substring
- [ ] is_ccw
- [ ] is_geometry
- [ ] is_prepared
- [ ] is_valid_input
- [ ] is_valid_reason
- [ ] contains_xy
- [ ] contains_properly
- [ ] dwithin
- [ ] intersects_xy
- [ ] relate_pattern
- [ ] intersection_all
- [ ] symmetric_difference_all
- [ ] coverage_union
- [ ] coverage_union_all
- [ ] explain_validity 