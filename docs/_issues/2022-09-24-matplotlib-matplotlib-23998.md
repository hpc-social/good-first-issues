---
tags: Good-first-issue,topic-collections-and-mappables,topic-legend
title: "Labels for PatchCollection do not show"
html_url: "https://github.com/matplotlib/matplotlib/issues/23998"
user: Robotatron
repo: matplotlib/matplotlib
---

### Bug summary

1. Labels / legend is not displayed
2. Autoscale does nothing, I have to manually set the limits

![image](https://user-images.githubusercontent.com/95919873/192120011-d112d17d-9ac8-4d03-9b6f-6142e7e43b1a.png)


### Code for reproduction

```python
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon

fig, axs = plt.subplots()
p1, p2 = Polygon([[0,0],[100,100],[200,0]], label="p1"), Polygon([[400,0],[500,100],[600,0]], label="p2")
p = PatchCollection([p1,p2], label="asd")
axs.add_collection(p, autolim=True)
axs.set_xlim(right=600)
axs.set_ylim(top=100)
axs.legend()
```


### Actual outcome

No labels/legend are shown - ![image](https://user-images.githubusercontent.com/95919873/192120011-d112d17d-9ac8-4d03-9b6f-6142e7e43b1a.png)

### Expected outcome

Legend is shown

### Additional information

_No response_

### Operating system

_No response_

### Matplotlib Version

3.5.2

### Matplotlib Backend

_No response_

### Python version

_No response_

### Jupyter version

_No response_

### Installation

_No response_