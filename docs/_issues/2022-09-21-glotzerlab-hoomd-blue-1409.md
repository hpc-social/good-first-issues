---
tags: ,community,enhancement
title: "Document how to change pair interaction parameters"
html_url: "https://github.com/glotzerlab/hoomd-blue/issues/1409"
user: rpcollanton
repo: glotzerlab/hoomd-blue
---

### Description

There are situations where it is desirable to ramp up energy prefactors during a simulation. For example, to gradually "turn on" a pair interaction. 

### Proposed solution

The user API would allow entering objects of hoomd.variant type as values in the parameter dicts for potentials.

### Additional context

This could especially be valuable in relaxation or equilibration routines, such as that used by Kremer and Grest (1990). 