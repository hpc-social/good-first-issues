---
tags: enhancement
title: "Add new layout methods"
html_url: "https://github.com/Qiskit/rustworkx/issues/438"
user: mtreinish
repo: Qiskit/rustworkx
---

<!-- ⚠️ If you do not respect this template, your issue will be closed -->
<!-- ⚠️ Make sure to browse the opened and closed issues to confirm this idea does not exist. -->

### What is the expected enhancement?

Right now retworkx has several layout methods available: https://qiskit.org/documentation/retworkx/api.html#layout-functions
but there are some other common examples (like a planar layout and kamada kawai) missing. We should expand the available layout functions so that they can be leveraged with the drawers. We can look at what networkx offers for this functionality to get some good examples: https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout