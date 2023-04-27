---
tags: easy
title: "Add units to BlackBodySimpleSource"
html_url: "https://github.com/tardis-sn/tardis/issues/1653"
user: smithis7
repo: tardis-sn/tardis
---

We would like to make the `BlackBodySimpleSource.create_packets()` method (in `tardis/montecarlo/packet_source.py`) unit-sensitive. That is, we would like to take in quantities with units and return quantities with units.

**Additional context**
A potential thing to think about here is how this method is used in the code, and having that be unit-sensitive as well. Remembering that this class can be replaced by a user's own packet source, do we want to require that the user's function includes units? That may be something for @wkerzendorf to answer.