---
tags: bug
title: "Wrong `eigenvector_centrality` test case in `rustworkx-core`"
html_url: "https://github.com/Qiskit/rustworkx/issues/798"
user: IvanIsCoding
repo: Qiskit/rustworkx
---

<!-- ⚠️ If you do not respect this template, your issue will be closed -->
<!-- ⚠️ Make sure to browse the opened and closed issues -->

### Information

- **rustworkx version**: master
- **Python version**: 3.10
- **Rust version**: 1.61
- **Operating system**: Linux

### What is the current behavior?

The `assert_almost_equal!` method in rustworkx-core's test suite for `eigenvector_centrality`  is implemented incorrectly. It always returns true and never panics. This let a bad test case slip through. (see https://github.com/Qiskit/rustworkx/blob/main/rustworkx-core/src/centrality.rs#L433)

### What is the expected behavior?

Implement the correct `assert_almost_equal!` like in #797. After, fix the test case.

### Steps to reproduce the problem

Replace any values in the `expected_values` array and the test case still passes. Implement the correct `assert_almost_equal` and the test case fails.
