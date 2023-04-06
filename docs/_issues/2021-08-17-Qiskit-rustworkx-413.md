---
tags: ,enhancement
title: "Add option to adjacency matrix functions to adjust parallel edge behavior"
html_url: "https://github.com/Qiskit/rustworkx/issues/413"
user: mtreinish
repo: Qiskit/rustworkx
---

<!-- ⚠️ If you do not respect this template, your issue will be closed -->
<!-- ⚠️ Make sure to browse the opened and closed issues to confirm this idea does not exist. -->

### What is the expected enhancement?

Right now the `adjacency_matrix()` function unconditionally sums the weights for parallel edges in the graph. We should make this configurable so that we can do different operations. Off the top of my head, sum(), min(), max(), avg() are all good candidates.

For maximum flexibility we could just make this a python callback function that get's passed both weights and returns the f64 to use (which is what I think networkx does). However that will have much worse performance than using a f64 operation in rust.
