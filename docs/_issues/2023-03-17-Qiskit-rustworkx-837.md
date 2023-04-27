---
title: "Add `PyGraph.substitute_node_with_subgraph()` method"
html_url: "https://github.com/Qiskit/rustworkx/issues/837"
user: mtreinish
repo: Qiskit/rustworkx
---

<!-- ⚠️ If you do not respect this template, your issue will be closed -->
<!-- ⚠️ Make sure to browse the opened and closed issues to confirm this idea does not exist. -->

### What is the expected enhancement?


The directed graph class `PyDiGraph` has a method `substitute_node_with_subgraph()` to replace a node in the graph with an input graph. However, the undirected graph class `PyGraph` doesn't have this method. It would be good if we filled this feature gap and add this method to the `PyGraph` class too.