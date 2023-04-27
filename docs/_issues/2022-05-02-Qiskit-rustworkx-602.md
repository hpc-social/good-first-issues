---
tags: enhancement
title: "Move more connected components functions to retworkx-core"
html_url: "https://github.com/Qiskit/rustworkx/issues/602"
user: enavarro51
repo: Qiskit/rustworkx
---

<!-- ⚠️ If you do not respect this template, your issue will be closed -->
<!-- ⚠️ Make sure to browse the opened and closed issues to confirm this idea does not exist. -->

### What is the expected enhancement?

#595 is in the process of moving `connected_components` and `number_connected_components` from `retworkx/src/connectivity/conn_components.rs` to `retworkx-core/src/connectivity/conn_components.rs`.

There are a number of other connected component related functions in `retworkx/src/connectivity/mod.rs`, such as `strongly_connected_components`, `is_connected`, and `node_connected_component`, that could also be moved over to `retworkx-core/src/connectivity`. The function in `mod.rs` would then just call the `retworkx-core` version, similar to what's done with `connected_components`.
