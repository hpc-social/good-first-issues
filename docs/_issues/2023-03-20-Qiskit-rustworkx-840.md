---
tags: ,enhancement
title: "Add reverse direction serialization"
html_url: "https://github.com/Qiskit/rustworkx/issues/840"
user: mtreinish
repo: Qiskit/rustworkx
---

<!-- ⚠️ If you do not respect this template, your issue will be closed -->
<!-- ⚠️ Make sure to browse the opened and closed issues to confirm this idea does not exist. -->

### What is the expected enhancement?

Right now rustworkx has a json node link serializer (https://qiskit.org/documentation/rustworkx/apiref/rustworkx.node_link_json.html#rustworkx.node_link_json) and a graphml deserializer (https://qiskit.org/documentation/rustworkx/apiref/rustworkx.read_graphml.html#rustworkx.read_graphml) but no  reverse path functions. We should add a node link json deserializer (to read node link json into a graph object) and a graphml serializer (to generate a graphml payload from a graph object) so that you can round-trip a graph over a serialization format.