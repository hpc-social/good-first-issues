---
tags: Difficulty-Medium,Good-first-issue,topic-mpl_toolkit
title: "[Bug]: `CbarAxesBase.toggle_label` doesn't seem to work properly"
html_url: "https://github.com/matplotlib/matplotlib/issues/23595"
user: oscargus
repo: matplotlib/matplotlib
---

### Bug summary

It appears as if `CbarAxesBase.toggle_label` and therefore, maybe, `SimpleAxisArtist.toggle` and possibly something else does not work as expected.

Probably related to the colorbar rewrite?

### Code for reproduction

https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_grid.html

### Actual outcome

The two middle figures have visible tick labels for the color bar.

### Expected outcome

No visible tick labels.

### Additional information

There seems to be some sort of mismatch between the `_axisnum` property and the location of the labels. It seems to work if the labels are located at the same side as the colorbar, i.e., right and bottom.

### Operating system

Arch

### Matplotlib Version

3.5.2 and `main`

### Matplotlib Backend

_No response_

### Python version

_No response_

### Jupyter version

_No response_

### Installation

git checkout