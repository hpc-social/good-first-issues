---
tags: ,enhancement
title: "Node and Edge Filtering and Selection"
html_url: "https://github.com/Qiskit/rustworkx/issues/800"
user: dhuang-hub
repo: Qiskit/rustworkx
---

<!-- ⚠️ If you do not respect this template, your issue will be closed -->
<!-- ⚠️ Make sure to browse the opened and closed issues to confirm this idea does not exist. -->

### What is the expected enhancement?

It would be great to have the ability to filter a graph's nodes and edges by some abstract criteria conditioned on a node's data payload.

A analogous feature seen in `igraph` would be the methods/functions of `select` and `find`.
```
# G is some arbitrary igraph.Graph

G.vs.select(lambda v: v["weight"] > 4)  # vertex selection
G.vs.find(name="foo")
```
