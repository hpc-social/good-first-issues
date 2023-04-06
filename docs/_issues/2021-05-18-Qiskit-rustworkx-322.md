---
tags: ,enhancement
title: "Add random walks to rustworkx"
html_url: "https://github.com/Qiskit/rustworkx/issues/322"
user: nahumsa
repo: Qiskit/rustworkx
---

<!-- ⚠️ If you do not respect this template, your issue will be closed -->
<!-- ⚠️ Make sure to browse the opened and closed issues to confirm this idea does not exist. -->

### What is the expected enhancement?

Add functions that make a [random walk](https://en.wikipedia.org/wiki/Random_walk) on a graph, which could be both a biased or an unbiased random walk. 
This may be important for some network science applications. 

In my opinion, this would be done by two functions:
- `random_walk` for the unbiased random walk;
- `biased_random_walk` for the biased random walk.