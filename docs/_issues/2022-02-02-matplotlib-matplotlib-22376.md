---
tags: Good-first-issue,New-feature
title: "[ENH]: align_titles"
html_url: "https://github.com/matplotlib/matplotlib/issues/22376"
user: anntzer
repo: matplotlib/matplotlib
---

### Problem

There's align_xlabels and align_ylabels to align the x and y labels, but no align_titles; this would be useful e.g. for
```python
from pylab import *
fig, axs = subplots(1, 2, subplot_kw={"xlabel": "x", "ylabel": "y", "title": "t"})
axs[0].imshow(zeros((3, 5)))
axs[1].imshow(zeros((5, 3)))
fig.align_labels()
```
![test](https://user-images.githubusercontent.com/1322974/152163429-d1169ce2-8818-4fb2-9a9b-545780a49a10.png)

### Proposed solution

Add Figure.align_titles.