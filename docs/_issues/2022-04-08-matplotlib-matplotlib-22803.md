---
tags: ,Difficulty-Medium,Good-first-issue
title: "[Bug]: Large file size when using fill_between()"
html_url: "https://github.com/matplotlib/matplotlib/issues/22803"
user: tgrohens
repo: matplotlib/matplotlib
---

### Bug summary

Hi,

I am trying to save a plot to PDF (or SVG) that uses the fill_between function between two time series, and the resulting file is much larger than when plotting each series individually.


### Code for reproduction

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=424242)

t_max = int(1e5)
t = np.arange(1, t_max+1, dtype=int)

data = rng.normal(size=(10, t_max))

# Lightweight figure (266 kb)
plt.figure(dpi=200)

plt.plot(t, np.min(data, axis=0), color='tab:blue', alpha=0.75)
plt.plot(t, np.max(data, axis=0), color='tab:blue', alpha=0.75)

plt.xlim(1, t_max)
plt.savefig(f"plot_minmax_{t_max}.svg")

# Large figure (1.1 Mb)
plt.figure(dpi=200)
plt.fill_between(t, np.min(data, axis=0), np.max(data, axis=0), color='tab:blue', alpha=0.5)
plt.xlim(1, t_max)
plt.savefig(f"plot_fill_{t_max}.svg")
```


### Actual outcome

![plot_minmax_2e+04](https://user-images.githubusercontent.com/302936/162471136-c0eb13ff-f606-4dc7-8e62-d6fc693ec01e.svg)
![plot_fill_2e+04](https://user-images.githubusercontent.com/302936/162471144-7e9f479d-0d2e-4d6d-8359-948417c2c8ac.svg)



### Expected outcome

The file size of the file drawn with `fill_between()` should stay roughly the same as the file drawing the min and the max only.

### Additional information

I have plotted the resulting file sizes for different numbers of data points.
The file size of the file generated with `fill_between()` grows linearly with the number of data points (as could be expected), but not the file size of the file plotting the min and the max directly: maybe there's an optimization in `plot()` that's not being used in `fill_between()` ?
![download](https://user-images.githubusercontent.com/302936/162469458-5b5ec3bc-5f9d-45fb-bf89-b57c850b5c08.png)


### Operating system

macOS

### Matplotlib Version

3.4.3

### Matplotlib Backend

module://matplotlib_inline.backend_inline

### Python version

Python 3.9.7

### Jupyter version

_No response_

### Installation

pip