---
tags: enhancement
title: "Add equivalent of cycle_basis that returns an edge list"
html_url: "https://github.com/Qiskit/rustworkx/issues/551"
user: IvanIsCoding
repo: Qiskit/rustworkx
---

<!-- ⚠️ If you do not respect this template, your issue will be closed -->
<!-- ⚠️ Make sure to browse the opened and closed issues to confirm this idea does not exist. -->

### What is the expected enhancement?

Create an equivalent of the `retworkx.cycle_basis` method but returning edges instead of nodes.

https://github.com/Qiskit/retworkx/blob/5b90ee7821398625b16aec2e4d782dd2ec26daf2/src/connectivity/mod.rs#L67-L135

The original paper (http://www.cs.kent.edu/~dragan/GraphAn/CycleBasis/p514-paton.pdf) which we implement returns a set of nodes instead a set of edges. #505 pointed out that returning a set of edges is more useful in many cases. The expected enhancement is to have a method for each such that users can get a cycle basis both with nodes and with edges.
