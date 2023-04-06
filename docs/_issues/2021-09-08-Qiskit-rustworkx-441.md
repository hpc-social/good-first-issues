---
tags: ,enhancement
title: "Add more centrality measures"
html_url: "https://github.com/Qiskit/rustworkx/issues/441"
user: georgios-ts
repo: Qiskit/rustworkx
---

<!-- ⚠️ If you do not respect this template, your issue will be closed -->
<!-- ⚠️ Make sure to browse the opened and closed issues to confirm this idea does not exist. -->

### What is the expected enhancement?
Recently a new function that calculates the `betweenness_centrality` was added (https://qiskit.org/documentation/retworkx/api.html#centrality). We can add similar measures like 
- `edge_betweenness_centrality` https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.edge_betweenness_centrality.html#networkx.algorithms.centrality.edge_betweenness_centrality, or 
- `closeness_centrality` https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.closeness_centrality.html#networkx.algorithms.centrality.closeness_centrality
