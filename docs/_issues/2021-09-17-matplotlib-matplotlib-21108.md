---
tags: ,API-consistency,Difficulty-Easy,Good-first-issue,topic-hatch,topic-rcparams
title: "[Bug]: Hatch linewidths cannot be modified in an  rcParam context"
html_url: "https://github.com/matplotlib/matplotlib/issues/21108"
user: mwaskom
repo: matplotlib/matplotlib
---

### Bug summary

The only way (that I am aware of) to control the linewidth of hatches is through an rc parameter. But temporarily modifying the parameter with `plt.rc_context` has not effect.

### Code for reproduction

```python
import matplotlib.pyplot as plt

plt.figure().subplots().bar([0, 1], [1, 2], hatch=["/", "."], fc="r")

with plt.rc_context({"hatch.linewidth": 5}):
    plt.figure().subplots().bar([0, 1], [1, 2], hatch=["/", "."], fc="g")

plt.rc("hatch", linewidth=5)
plt.figure().subplots().bar([0, 1], [1, 2], hatch=["/", "."], fc="b")
```


### Actual outcome

![image](https://user-images.githubusercontent.com/315810/133707131-74c9d47c-917b-44f8-9fb2-953145bcf63b.png)

![image](https://user-images.githubusercontent.com/315810/133707137-2745159b-4595-419e-bb83-23098c29a46b.png)

![image](https://user-images.githubusercontent.com/315810/133707143-6f2cee3b-0a35-45ad-9db4-58d3d2593be7.png)

### Expected outcome

That second image (the green bars) should have thick hatches.

FWIW I think hatches ought to have an actual API, but given that they don't, this limitation makes them *really* hard to work with.

### Operating system

macos

### Matplotlib Version

3.4.3

### Matplotlib Backend

inline