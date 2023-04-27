---
tags: feature-request
title: "Feature: Min-relative entropy for quantum channels"
html_url: "https://github.com/vprusso/toqito/issues/42"
user: vprusso
repo: vprusso/toqito
---

Implement a function that calculates the min-relative entropy for quantum channels. 

The functionality for this should be created in `channel_props/min_relative_entropy.py` with corresponding unit tests found in `tests/test_channel_props/test_min_relative_entropy.py`. Be sure to also update the docs in `/docs/channels.rst` under "Properties of Quantum Channels" with `toqito.channel_props.min_relative_entropy.py`.

For a definition of min-relative entropy for quantum channels, consult:
https://arxiv.org/abs/1907.06306

See related tasks:
Min-relative entropy (quantum states): #40 
Max-relative entropy (quantum states): #41 
Max-relative entropy (quantum channels): #43
