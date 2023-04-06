---
tags: ,Difficulty-Medium,Good-first-issue,New-feature,topic-rcparams,topic-ticks-axis-labels
title: "[ENH]: Add default kwargs values if figure.suptitle(t, **kwargs) to rcParams and inherit from there."
html_url: "https://github.com/matplotlib/matplotlib/issues/24090"
user: FKSWB
repo: matplotlib/matplotlib
---

### Problem

Problem summary
===========

I cannot change the default location of a ``figure.suptitle()`` through the ``rcParams`` as I can with the title location of the axis title.

Origin/background
===========

I am tweaking the default settings of Matplotlib to create plots that in appearance match the corporate styling. Most changes have been made by re-setting the default values of certain ``rcParams``.

One of the requirements is the left-alignment of titles of graphs. For the axis title I can set ``rcParams['axes.titlelocation']`` to ``'left'``, as itdefaults to ``center``. I would like to do something similar to the figure's suptitle.

Currently, setting the figure's suptitle only takes defaults ``rcParams['figure.titlesize']`` and ``rcParams['figure.titleweight']``. The other parameters for location and alignment of the suptitle are defaulted in the method's argument definition. My desire is to add these to ``rcParams`` as well, and refer hereto as default.

### Proposed solution

E.g. expand the ``rcParams`` with:

```
{
    'figure.titleloc_x': 0.5,
    'figure.titleloc_y': 0.98,
    'figure.titleha': 'center',
    'figure.titleva': 'center'
}
```

And then use these defaults in ``figure.suptitle()``, very similar to how ``rcParams['figure.titlesize']`` and ``rcParams['figure.titleweight']`` are already used as default values.