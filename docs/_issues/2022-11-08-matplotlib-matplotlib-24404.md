---
tags: API-consistency,Difficulty-Medium,Good-first-issue
title: "[Bug]: Cannot use empty markers in scatter"
html_url: "https://github.com/matplotlib/matplotlib/issues/24404"
user: Atcold
repo: matplotlib/matplotlib
---

### Bug summary

I'd like to have a scatter plot with empty `'o'` markers (just the edge).
This seems impossible.

### Code for reproduction

```python
from matplotlib.pylab import *
x = arange(0, 10)
scatter(x, x, c=x, facecolors='none')
```


### Actual outcome

![image](https://user-images.githubusercontent.com/2119355/200681966-8173ca7e-5aa9-4e27-8ebe-83306de4bb73.png)


### Expected outcome

Empty markers.

### Matplotlib Version

3.5.1