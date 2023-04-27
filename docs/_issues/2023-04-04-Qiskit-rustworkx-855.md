---
tags: bug
title: "`PyDiGraph.add_edge()` and `PyGraph.add_edge` panic if an endpoint doesn't exist"
html_url: "https://github.com/Qiskit/rustworkx/issues/855"
user: mtreinish
repo: Qiskit/rustworkx
---

<!-- ⚠️ If you do not respect this template, your issue will be closed -->
<!-- ⚠️ Make sure to browse the opened and closed issues -->

### Information

- **rustworkx version**: 0.12.1
- **Python version**: 3.11
- **Rust version**: 1.68.2
- **Operating system**: Linux

### What is the current behavior?

If you try to add an edge to a graph object with endpoints that aren't present in the graph petgraph panics and that causes an catchable exception to be raised from rustworkx without a user actionable message.
 For example:
 
 ```
 pyo3_runtime.PanicException: StableGraph::add_edge: node index 3 is not a node in the graph
```

### What is the expected behavior?

I think it would be better to raise an `IndexError` or a custom rustworkx exception class. The issue is a `PanicException` isn't something users can catch easily (as it doesn't inherit from `Exception`) and is supposed to be treated as irrecoverable. Also the error message isn't something a python end user will understand. We should do checks that the indices are present in the graph before calling petgraph and return an appropriate error instead.

### Steps to reproduce the problem

```python
g = rx.PyDiGraph()
g.add_edge(2, 3)
```
or

```python
g = rx.PyGraph()
g.add_edge(2, 3)
```
