---
tags: enhancement
title: "Migrate `steiner_tree()` and `metric_closure()` to rustworkx-core"
html_url: "https://github.com/Qiskit/rustworkx/issues/769"
user: mtreinish
repo: Qiskit/rustworkx
---

<!-- ⚠️ If you do not respect this template, your issue will be closed -->
<!-- ⚠️ Make sure to browse the opened and closed issues to confirm this idea does not exist. -->

### What is the expected enhancement?


The `metric_closure()` and `steiner_tree()` functions available at: https://github.com/Qiskit/rustworkx/blob/main/src/steiner_tree.rs should be straightforward to port to rustworkx-core and rework as generic for any petgraph graph and then update the python functions to call the inner rustworkx-core function. This will then expose this functionality to any rust users that might want this functionality.