---
tags: Good-first-issue,topic-rcparams
title: "[Bug]: rcParams['legend.loc'] can't use float-tuple like kwarg legend(loc...)"
html_url: "https://github.com/matplotlib/matplotlib/issues/22338"
user: cphlewis
repo: matplotlib/matplotlib
---

### Bug summary

We can now use a (x,y) argument for `plt.legend(loc=(x,y))`,
but using the tuple as a value for rcParams['legend.loc'] fails. 



### Code for reproduction

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
xs, ys = [1,2,3], [2,3,1]

fig, ax = plt.subplots(3)

ax[0].scatter(xs, ys, label='loc-tuple-arg')
ax[0].legend(loc=(1.1, .5)) # works

ax[1].scatter(xs, ys, label='loc-rcparam-tuple')
mpl.rcParams['legend.loc'] = (0.9, .7)
ax[1].legend() # fails w/o documentation

ax[2].scatter(xs, ys, label='loc-rcparam-str(tuple)')
mpl.rcParams['legend.loc'] = '(.8, .3)'
ax[2].legend() # fails with documentation
```


### Actual outcome

Setting rcParams['legend.loc'] to a tuple fails with 

> AttributeError: 'tuple' object has no attribute 'lower'

setting rcParams['legend.loc'] to the string representation of a tuple fails with a list of supported values. 

### Expected outcome

Ideally  rcParams['legend.loc']  would apply a tuple the same way the kwarg does. 

Second best would be a bit more documentation; 1) reporting the list of supported strings for any un-interpretable value, and 2) mentioning in the default matplotlibrc  that only a set of strings are supported. 

### Additional information

I believe the  `loc` kwarg originally only took string values, but that seems to have been at least a major version ago. 

### Operating system

Ubuntu

### Matplotlib Version

3.3.4

### Matplotlib Backend

TkAgg

### Python version

Python 3.9.7

### Jupyter version

_No response_

### Installation

pip