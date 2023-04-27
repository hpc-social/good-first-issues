---
tags: feature-request,unitaryhack
title: "Feature: Is UPB (unextendible product basis)"
html_url: "https://github.com/vprusso/toqito/issues/33"
user: vprusso
repo: vprusso/toqito
---

Given a collection of vectors, determine if the set constitutes an unextendible product basis (UPB). 

According to [arXiv:quant-ph/9808030](https://arxiv.org/abs/quant-ph/9808030):

> An unextendible product basis (UPB) for a multipartite quantum system is an incomplete orthogonal product basis whose complementary subspace contains no product state. 

In spirit, the functionality of being able to determine whether a collection of vectors form a UPB can be derived from the QETLAB package, specifically the function "[IsUPB](http://www.qetlab.com/IsUPB)". 

The functionality for this should be created in `state_props/is_unextendible_product_basis.py` with corresponding unit tests found in `tests/test_state_props/test_is_unextendible_product_basis.py`. Be sure to also update the docs in `/docs/states.rst` under "Properties of Quantum States" with `toqito.state_props.is_unextendible_product_basis.py`. 

Please ensure proper credit is provided to QETLAB as serving as the inspiration for including this function. 