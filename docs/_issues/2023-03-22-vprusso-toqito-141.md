---
tags: feature-request,help-wanted,unitaryhack
title: "Feature: Fidelity of separability"
html_url: "https://github.com/vprusso/toqito/issues/141"
user: vprusso
repo: vprusso/toqito
---

The fidelity of separability (also known as the maximum separable fidelity [1, 2]) is an entanglement measure that can be approximated via semidefinite programs outlined in [3]. Ancillary files provided with [3] (here) implement SDPs that approximate the fidelity of separability.  

This task would entail:

1. Adding and generalizing the channel and density matrix SDPs from here and placing them into `state_metrics/fidelity_of_separability.py`. 
2. Adding corresponding unit tests in `tests/test_state_metrics/test_fidelity_of_separability.py`
3. Updating docs in `docs/states.rst` under "Distance Metrics for Quantum States"

[1][Two-message quantum interactive proofs and the quantum separability problem](https://arxiv.org/abs/1211.6120)
[2] [Quantum interactive proofs and the complexity of separability testing](https://arxiv.org/abs/1308.5788)
[3] [Quantum Steering Algorithm for Estimating Fidelity of Separability](https://arxiv.org/abs/2303.07911)