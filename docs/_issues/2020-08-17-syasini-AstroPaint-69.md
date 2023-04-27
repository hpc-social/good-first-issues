---
tags: help-wanted
title: "cut mask (experiment footprint) based on input keyword"
html_url: "https://github.com/syasini/AstroPaint/issues/69"
user: syasini
repo: syasini/AstroPaint
---

Currently, the `canvas.cut_mask()` method takes in the healpix map of an experiment footprint. It would be nice to allow the user to apply such cuts using experiment footprints. For example

```python 
canvas.cut_mask("CMB-S4", inplace=True) 
canvas.cut_mask("DESI", inplace=True) 
```

would limit the catalog to the common footprint between S4 and DESI. 

TODO: Add masks from [cmb x galaxy web app](https://cmb-x-galaxy-overlaps.herokuapp.com/) to the data directory.

