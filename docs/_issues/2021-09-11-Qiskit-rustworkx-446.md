---
tags: enhancement
title: "Add `is_semiconnected` function."
html_url: "https://github.com/Qiskit/rustworkx/issues/446"
user: georgios-ts
repo: Qiskit/rustworkx
---

<!-- ⚠️ If you do not respect this template, your issue will be closed -->
<!-- ⚠️ Make sure to browse the opened and closed issues to confirm this idea does not exist. -->

### What is the expected enhancement?
A graph is semiconnected if, and only if, for any pair of nodes, either one is reachable from the other, or they are mutually reachable. 

For reference, see https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.components.is_semiconnected.html#networkx.algorithms.components.is_semiconnected

For the implementation, we can consider adapting `petgraph::condesation` function https://docs.rs/petgraph/0.6.0/petgraph/algo/fn.condensation.html. We can't use it directly since it only works with `petgraph::Graph` but we have a `petgraph::StableGraph` as our underlying graph data structure.


