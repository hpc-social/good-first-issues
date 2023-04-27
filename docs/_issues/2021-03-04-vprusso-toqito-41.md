---
tags: feature-request
title: "Feature: Max-relative entropy for quantum states"
html_url: "https://github.com/vprusso/toqito/issues/41"
user: vprusso
repo: vprusso/toqito
---

Implement a function that calculates the max-relative entropy for quantum states. 

The functionality for this should be created in `state_props/max_relative_entropy.py` with corresponding unit tests found in `tests/test_state_props/test_max_relative_entropy.py`. Be sure to also update the docs in `/docs/states.rst` under "Properties of Quantum States" with `toqito.state_props.max_relative_entropy.py`.

For a definition of max-relative entropy for quantum states, consult:
https://arxiv.org/abs/1905.11629

See related tasks:
Min-relative entropy (quantum states): #40 
