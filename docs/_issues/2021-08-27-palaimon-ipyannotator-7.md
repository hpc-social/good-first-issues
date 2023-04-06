---
title: "Use point set to shape mapping to improve polygon annotation widget"
html_url: "https://github.com/palaimon/ipyannotator/issues/7"
user: ibayer
repo: palaimon/ipyannotator
---

Motivation
----------

The polygon annotation widget `nbs/01d_polygon_canvas.ipynb` https://github.com/palaimon/ipyannotator/issues/5 (not yet included in the public github release) supports only sequential polygon annotation. Adding additional boundary points after creating an initial polygon depends on the creation order of the boundary points which is not very intuitive and also slow to execute.

Defining the polygon by a set of points instead of a list would make adding and removing of points much simpler.

Alpha-Concave Hull
------------------

> In computational geometry, an alpha shape, or 