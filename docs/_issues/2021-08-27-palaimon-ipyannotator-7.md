---
tags: 
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

> In computational geometry, an alpha shape, or α-shape, is a family of piecewise linear simple curves in the Euclidean plane associated with the shape of a finite set of points. They were first defined by Edelsbrunner, Kirkpatrick & Seidel (1983). The alpha-shape associated with a set of points is a generalization of the concept of the convex hull, i.e. every convex hull is an alpha-shape but not every alpha shape is a convex hull. 
source: https://en.wikipedia.org/wiki/Alpha_shape

Alpha-Concave Hull [0] is one such algorithm that could be interested for us.

Suggested steps.

- literature review to find simple algorithm to associate shape with set of points. 
- poc implementation of algorithm in `01d_polygon_canvas.ipynb`
- create minimal sequence diagram https://plantuml.com/sequence-diagram to specify expected user iteration for creating and deleting points
- refactor current polygon annotation widget to support the new algorithm


[0] [Alpha-Concave  Hull,  a Generalization  of Convex  Hull](https://arxiv.org/pdf/1309.7829.pdf)


Note: This is an internal issue till the polygon annotation widget https://github.com/palaimon/ipyannotator/issues/5 is released.
