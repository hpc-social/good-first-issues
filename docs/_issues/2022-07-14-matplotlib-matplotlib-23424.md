---
tags: Good-first-issue
title: "[Bug]: Axes.indicate_inset[_zoom](linewidth=...) doesn't affect connectors"
html_url: "https://github.com/matplotlib/matplotlib/issues/23424"
user: QuLogic
repo: matplotlib/matplotlib
---

### Bug summary

When using `Axes.indicate_inset`/`Axes.indicate_inset_zoom`, it may be necessary to increase the size of edges in order to be visible. It is possible to change edge colour with `edgecolor=...` which affects both the frame and the connectors. However, using `linewidth=...` only affects the frame.

### Code for reproduction

```python
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2)
for ax in axs:
    ax.plot([1, 2, 3])

axs[1].set_xlim(0.5, 1.5)
axs[0].indicate_inset_zoom(axs[1], linewidth=5)

plt.show()
```


### Actual outcome

![Figure_1](https://user-images.githubusercontent.com/302469/178911771-21e2f05b-4b23-4678-8f83-9369f40ca83b.png)

### Expected outcome

![Figure_1](https://user-images.githubusercontent.com/302469/178912221-a0571a94-350b-452f-b960-bedc2365cd52.png)

### Additional information

_No response_

### Operating system

_No response_

### Matplotlib Version

37ccdca5028725b3b9d689b42947b6284a73d690

### Matplotlib Backend

_No response_

### Python version

_No response_

### Jupyter version

_No response_

### Installation

git checkout