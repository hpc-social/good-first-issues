---
tags: ,ScopeSim-Templates,enhancement
title: "METIS calibration pinhole mask"
html_url: "https://github.com/AstarVienna/ScopeSim_Templates/issues/31"
user: astronomyk
repo: AstarVienna/ScopeSim_Templates
---

Code block for adding a pinhole mask to the METIS calibration package for the LMS mode

No particular assignee, no time frame, just whoever wants an easy win one day.

Code used by **TM** - would be better to create a grid of x,y coord then initialise via an astropy Table

```
src = sim.source.source_templates.star(x=0, y=0, flux=0.0001*u.Jy)
nx=5; X = np.linspace(-0.45,0.45,nx)
ny=28; Y = np.linspace(-0.27945,0.27945,ny)
​
for y in Y:
    for x in X :
        src += sim.source.source_templates.star(x=x, y=y, flux=randint(1,12)*u.Jy)
```