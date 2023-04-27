---
tags: Documentation,Good-first-issue,topic-animation
title: "Animation docs should include a simple \"save as gif with pillow\" example"
html_url: "https://github.com/matplotlib/matplotlib/issues/22374"
user: anntzer
repo: matplotlib/matplotlib
---

### Documentation Link

_No response_

### Problem

pillow is the only animation writer that does not require additional dependencies (we already depend on pillow in any case) but it is not the default writer.  I think the main animation formation it can save to is gif.

There should be a simple "save as gif with pillow example" with its own entry in https://matplotlib.org/devdocs/gallery/index#animation (although some of the examples have a few lines on saving as mp4 with ffmpeg, 1. it is not even clear from the index which are these examples, and 2. ffmpeg may or may not be present on the user's machine).

### Suggested improvement

_No response_

### Matplotlib Version

3.6.0.dev1512