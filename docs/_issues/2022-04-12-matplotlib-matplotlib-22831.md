---
tags: Documentation,Good-first-issue,topic-animation
title: "[Doc]: Arguments of FFMpegFileWriter not clear."
html_url: "https://github.com/matplotlib/matplotlib/issues/22831"
user: baloe
repo: matplotlib/matplotlib
---

### Documentation Link

https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegFileWriter.html

### Problem

There is no word on what arguments to set via `*args, **kwargs`.

~Also, I am wondering how to control where the temporary frame files are stored. I was unable to find them in my `/tmp` directory~
_okay, that is actually rather clear (`frame_prefix` in `setup`)_

### Suggested improvement

List arguments or refer to class whose initialization arguments are  to be used.