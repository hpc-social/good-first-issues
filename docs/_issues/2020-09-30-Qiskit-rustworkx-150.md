---
tags: ,enhancement
title: "Expand Generators Module"
html_url: "https://github.com/Qiskit/rustworkx/issues/150"
user: mtreinish
repo: Qiskit/rustworkx
---

<!-- ⚠️ If you do not respect this template, your issue will be closed -->
<!-- ⚠️ Make sure to browse the opened and closed issues to confirm this idea does not exist. -->

### What is the expected enhancement?

In #121 we added a new module for graph generators which will create graphs of with a certain layout easily. #121 only added a few different types of graphs with the intention of adding more in the future. We should add more generators to the graph to offer more options for quickly creating graphs. Networkx has a long list of generators that can be used for inspiration on different types of generators to add:

https://networkx.github.io/documentation/stable/reference/generators.html

Also, specifically for a qiskit use case we should make sure that we have generators to cover ~`qiskit.transpiler.CouplingMap.from_line`, `qiskit.transpiler.CouplingMap.from_ring`, `qiskit.transpiler.CouplingMap.from_grid`, and `qiskit.transpiler.CouplingMap.from_full`~ (this was handled by #191)