---
tags: ,Docs,Effort-low,Hacktoberfest,Package-novice,coordinates
title: "Doc for objects that inherit from BaseCoordinateFrame is messy"
html_url: "https://github.com/astropy/astropy/issues/7458"
user: dstansby
repo: astropy/astropy
---

e.g. see this page: http://docs.sunpy.org/en/stable/api/sunpy.coordinates.frames.HeliographicStonyhurst.html#sunpy.coordinates.frames.HeliographicStonyhurst and scroll down to "Attributes summary"

Because `BaseCoordinateFrame` has a few class attributes, these get automatically documented (without any docstrings) when documenting an inheriting class. It would be nice to make these disappear somehow - maybe converting them to properties, and making the class attributes hidden by putting an underscore before their names?