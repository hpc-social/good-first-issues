---
tags: enhancement,viz
title: "Add more viz plot types"
html_url: "https://github.com/parmoo/parmoo/issues/35"
user: HyrumDickinson
repo: parmoo/parmoo
---

Plots types we should add include:
 - heatmap
 - 3D scatterplot
 - radviz (designed for visualizing MOOP results)
 - petal diagram
 - star coordinates plot

Plot types should be based on Plotly. Graph generating code should be written in viz/graph.py. Wrappers can be easily added in viz/plot.py. We may need some tweaking in viz/utilities.py. Ideally, addition of this feature won't require any changes to viz/dashboard.py (dashboard should be graph-agnostic).