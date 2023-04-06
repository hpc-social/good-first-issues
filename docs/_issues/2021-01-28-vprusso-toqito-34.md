---
tags: ,enhancement
title: "Enhancement: Maximum confidence state distinguishability"
html_url: "https://github.com/vprusso/toqito/issues/34"
user: vprusso
repo: vprusso/toqito
---

Presently the `state_distinguishability` function in `state_distinguishability.py` includes minimum-error and unambiguous quantum state distinguishability using the argument `dist_method = "min-error"` and `dist_method="unambiguous"`, respectively. 

This task should enhance the `state_distinguishability` function to include the ability to compute the maximum confidence discrimination. Refer to Section 2.5 of [arXiv:1707.02571](https://arxiv.org/pdf/1707.02571.pdf), specifically the SDP below equation (31) in this section. 

The formulation of the SDP should look familiar to the other distinguishability methods and should serve as an example for how to include this feature. 

 

