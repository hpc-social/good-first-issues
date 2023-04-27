---
tags: nice-to-have,stale,utils
title: "Unify `get_residue_contact_pairs()` from buildgraph.py by `get_IRCs()` from irc.py"
html_url: "https://github.com/DeepRank/deeprank-core/issues/394"
user: DaniBodor
repo: DeepRank/deeprank-core
---

The buildgraph function (exclusively used in some unit tests) already existed before I worked on irc feature. Later I discovered that I largely recreated that function.

The one used created for irc features is more elegantly/concisely written, so it would be nice to replace the buildgraph function with what is needed from the irc one and then call the function both for the tests and irc features