---
tags: ,Difficulty-Medium,Good-first-issue
title: "[Bug]: axes vlines() / hlines() incorrectly use data coordinate as min when blended transform is applied"
html_url: "https://github.com/matplotlib/matplotlib/issues/23171"
user: orionlee
repo: matplotlib/matplotlib
---

### Bug summary

For `Axes.vlines()`, when I want to use axes coordinate for `ymin` / `ymax`, as suggested in [blended transformation](https://matplotlib.org/3.5.0/tutorials/advanced/transforms_tutorial.html#blended-transformations), `ymin` is incorrectly treated as data coordinate.

`Axes.hlines()` has a similar problem with `xmin`.

### Code for reproduction

```python
# Sample derived from
# https://matplotlib.org/3.5.0/gallery/lines_bars_and_markers/vline_hline_demo.html#sphx-glr-gallery-lines-bars-and-markers-vline-hline-demo-py
    
import matplotlib.pyplot as plt
import numpy as np

import matplotlib 
print('matplotlib', matplotlib.__version__)


t = np.arange(5.0, 10.0, 0.1)
s = np.exp(-t) + np.sin(2 * np.pi * t) + 10

vax = plt.figure(figsize=(12, 6)).gca()
vax.plot(t, s, '^')

# By using ``transform=vax.get_xaxis_transform()`` the y coordinates are scaled
# such that 0 maps to the bottom of the axes and 1 to the top.

vax.vlines([6, 7], ymin=0, ymax=0.15, transform=vax.get_xaxis_transform(), colors='r')
# if I use axvline() instead, it correctly treats ymin as axes coordinate.
# vax.axvline(6, ymin=0, ymax=0.15, c='r')
# vax.axvline(7, ymin=0, ymax=0.15, c='r')

vax.set_xlabel('time (s)')
vax.set_title('Vertical lines demo');
```


### Actual outcome

One can see that while `ymax` is applied correctly (about 15% of the y-axis), `ymin` is applied incorrectly. `ymin` is treated as data coordinate, incorrectly stretching the y-axis.

![image](https://user-images.githubusercontent.com/250644/171294142-451a27fe-2e01-498e-84cb-9acc99aa3232.png)


### Expected outcome

The expected outcome can be obtained using multiple `axvline()` instead of `vlines()`:
```python
vax.axvline(6, ymin=0, ymax=0.15, c='r')
vax.axvline(7, ymin=0, ymax=0.15, c='r')
```

![image](https://user-images.githubusercontent.com/250644/171294186-a4570463-54e6-4a26-ab59-36245567c096.png)


### Additional information

I've encountered the problem in earlier versions. I cannot recall it ever works correctly.

`Axes.hlines()`  has a similar problem with `xmin`.

One can add the following to the example codes above to test it:

```python
# axes.hlines() has similar problem.
vax.hlines([9, 9,5], xmin=0, xmax=0.2, transform=vax.get_yaxis_transform(), colors='green')
# uses multiple axhline() call would work correctly
# vax.axhline(9, xmin=0, xmax=0.2, c='green')
# vax.axhline(9.5, xmin=0, xmax=0.2, c='green')
```


### Operating system

Windows

### Matplotlib Version

3.5.2

### Matplotlib Backend

module://matplotlib_inline.backend_inline

### Python version

Python 3.9.10

### Jupyter version

6.4.11

### Installation

conda