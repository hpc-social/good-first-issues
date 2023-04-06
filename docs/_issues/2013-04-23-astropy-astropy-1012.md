---
tags: ,Effort-low,Feature-Request,Package-novice,coordinates
title: "Add option to project `separation` onto an ellipse"
html_url: "https://github.com/astropy/astropy/issues/1012"
user: eteq
repo: astropy/astropy
---

Right now separation only gives the angle between two points.  Another common "separation" in astronomy is the distance _projected_ along a particular axis (e.g. the major axis of a galaxy).  This would be particularly useful because of the rather sordid history of various people confusing which way a PA goes ("degrees east of north" I think is the most common convention).

Also useful (at least in galaxy contexts) might be an "elliptical" distance  (where the separation along the major and minor axes is weighted by the ellipticity).

This should probably await until some of the significant coordinate internal changes are done, so I'm not targeting a particular milestone.
