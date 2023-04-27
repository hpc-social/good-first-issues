---
tags: API-argument-checking,Difficulty-Medium,Good-first-issue,topic-legend
title: "No error message in matplotlib.axes.Axes.legend() if there are more labels than handles"
html_url: "https://github.com/matplotlib/matplotlib/issues/24050"
user: haferburg
repo: matplotlib/matplotlib
---

I had a bug in my code where I called `plot()` six times, stored the handles in a list, then called `legend()` with six handles, but seven labels for the legend.

It would have been very helpful if matplotlib raised an exception in this case.

`matplotlib.__version__` is 3.6.0, Python 3.9.6.