---
tags: ,enhancement,help-wanted
title: "Hashable python objects as node identifiers"
html_url: "https://github.com/Qiskit/rustworkx/issues/496"
user: adriangb
repo: Qiskit/rustworkx
---

### What is the expected enhancement?

I read through some of the existing issues (namely #248) regarding the choice of using indices instead of hashable python objects to identify keys.

Sometimes, it is can be unergonomic to operate with this sort of API, and trying to keep a mapping of python objects to indices on the Python side can be error prone, especially when you get into subgraphs and such.

It would be nice for usability to provide a wrapper around the graph classes that operates on hashable Python objects. It's probably going to be about the same performance to do it on the Python side as the Rust side, but either way as long as it's done in the library itself it's a win for users. 