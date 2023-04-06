---
tags: ,enhancement,help-wanted
title: "Random seed should be encoded as a random generator object in SimulatedUniverse"
html_url: "https://github.com/dsavransky/EXOSIMS/issues/219"
user: dsavransky
repo: dsavransky/EXOSIMS
---

Any random draws after the setting of a seed in SU will cause the subsequent draws to diverge.  This can be addressed by instantiating a random number generator and adding it to specs to be passed to all sub-initializations with random draws.
