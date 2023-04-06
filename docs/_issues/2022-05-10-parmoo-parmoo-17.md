---
tags: ,enhancement
title: "Reduce Duplicate Code in Unit Tests"
html_url: "https://github.com/parmoo/parmoo/issues/17"
user: thchang
repo: parmoo/parmoo
---

Due to rapid development and interface changes, the unit tests contain significant duplicate code.

This could be reduced by
 1) Using built-in utilities from ``parmoo.util`` instead of checking things by hand
 2) Using built-in functions from the objectives/simulations/constraints libraries
 3) Making better usage of ParMOO's new methods, which may not have existed in previous development cycles
 4) Adding testing utilities that are used over and over again (either by creating ``setup.py`` files in the test directories, or by adding to ``parmoo.util``)