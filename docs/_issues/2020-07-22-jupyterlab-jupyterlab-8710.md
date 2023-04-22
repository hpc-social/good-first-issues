---
tags: enhancement
title: "Add full screen option to JupyterLab"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/8710"
user: jasongrout
repo: jupyterlab/jupyterlab
---

### Problem

I often want to make my JupyterLab interface full screen, without any browser tabs or other window chrome, so I can concentrate on the problem at hand.

Maximizing a chrome browser in macOS almost does what I want, but only if I uncheck "Always show toolbar in Full Screen". I can't figure out a way to do this in Firefox, and I can't figure out a way to do this in Windows either.

### Proposed Solution

Add a command to make the JupyterLab root application DOM element full screen, using the [requestFullScreen](https://developer.mozilla.org/en-US/docs/Web/API/Element/requestFullScreen) api.

Add this as a menu item, perhaps under the View menu next to the Single-Document Mode?

### Additional context

