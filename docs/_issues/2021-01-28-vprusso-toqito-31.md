---
tags: ,feature-request
title: "Feature: Complementary channel"
html_url: "https://github.com/vprusso/toqito/issues/31"
user: vprusso
repo: vprusso/toqito
---

Given a map (quantum channel) compute the complementary map. 

As an example, this functionality is present in the QETLAB package. While the implementation there is in MATLAB, the spirit of the implementation should be quite similar to the implementation for `toqito`:
http://www.qetlab.com/ComplementaryMap

Write the functionality for this task in `toqito/channel_ops/complimentary_channel.py` and ensure proper unit tests for this feature are written in `tests/test_channel_ops/test_complimentary_channel.py`. Also ensure that the automated docs are updated by placing the line `toqito.channel_ops.complimentary_channel` in `docs/channels.rst` under `Operations on Quantum Channels`. 