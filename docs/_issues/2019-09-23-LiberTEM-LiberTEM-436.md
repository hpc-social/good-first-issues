---
tags: ,GUI
title: "Bounds checking for shapes in GUI"
html_url: "https://github.com/LiberTEM/LiberTEM/issues/436"
user: uellue
repo: LiberTEM/LiberTEM
---

How to reproduce:

Open a file and add an analysis that has GUI control elements. Use keyboard controls to adjust the size.

Observed behavior:

1. When reducing an inner radius, the value doesn't reach zero, but starts cycling between an arbitrary x and (stepsize-x).
2. The outer radius can be increased without apparent limit

Expected behavior:

1. The inner radius goes to zero with the last step that is smaller than the step size and remains zero when trying to reduce it further
2. The outer radius is limited by the diagonal of the control.
