---
tags: Difficulty-Medium,GUI-Qt,Good-first-issue,status-confirmed-bug
title: "[Bug]: Mouse Scroll Event is not caputred if ALT key is pressed"
html_url: "https://github.com/matplotlib/matplotlib/issues/25671"
user: ramsluk
repo: matplotlib/matplotlib
---

### Bug summary

I want to use the scroll event in my plot and define different behavior if a certain modifier key is pressed. I used the standard example and found out no scroll event is triggered when pressing the ALT key. Is there a specific reason for this behavior or is it an actual bug?

### Code for reproduction

```python
import numpy as np
import matplotlib.pyplot as plt


class IndexTracker:
    def __init__(self, ax, X):
        self.index = 0
        self.X = X
        self.ax = ax
        self.im = ax.imshow(self.X[:, :, self.index])
        self.update()

    def on_scroll(self, event):
        print(event.button, event.step)
        increment = 1 if event.button == 'up' else -1
        max_index = self.X.shape[-1] - 1
        self.index = np.clip(self.index + increment, 0, max_index)
        self.update()

    def update(self):
        self.im.set_data(self.X[:, :, self.index])
        self.ax.set_title(
            f'Use scroll wheel to navigate\nindex {self.index}')
        self.im.axes.figure.canvas.draw()


x, y, z = np.ogrid[-10:10:100j, -10:10:100j, 1:10:20j]
X = np.sin(x * y * z) / (x * y * z)

fig, ax = plt.subplots()
# create an IndexTracker and make sure it lives during the whole
# lifetime of the figure by assigning it to a variable
tracker = IndexTracker(ax, X)

fig.canvas.mpl_connect('scroll_event', tracker.on_scroll)
plt.show()
```


### Actual outcome

No scroll event at all is captured.

### Expected outcome

Scroll event should be captured.

### Additional information

PyQt recognizes scroll events when pressing ALT

### Operating system

Windows

### Matplotlib Version

3.6.2

### Matplotlib Backend

QtAgg

### Python version

3.9.13

### Jupyter version

_No response_

### Installation

pip