---
tags: ,enhancement
title: "dev: Unit tests on `GaussianDistribution` object."
html_url: "https://github.com/JaxGaussianProcesses/GPJax/issues/177"
user: Daniel-Dodd
repo: thomaspinder/GPJax
---

Improve / add unit tests for `GaussianDistribution`.

(1) We need to test shape checking done by the function `check_shapes`.
(2) Remove `distrax ` checking for equality with e.g., likelihood value or the entropy. Write test cases of our own.