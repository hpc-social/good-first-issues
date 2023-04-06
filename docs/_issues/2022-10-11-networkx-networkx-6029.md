---
tags: Good-First-Issue,Maintenance
title: "Improve test coverage for algorithms in maxflow.py"
html_url: "https://github.com/networkx/networkx/issues/6029"
user: MridulS
repo: networkx/networkx
---

<!-- If you have a general question about NetworkX, please use the discussions tab to create a new discussion -->

<!--- Provide a general summary of the issue in the Title above -->

Currently we don't have full coverage for algorithms in maxflow.py. Code blocks which are highlighted with red at codcov https://app.codecov.io/gh/networkx/networkx/blob/main/networkx/algorithms/flow/maxflow.py don't have corresponding tests. The tests should be added in https://github.com/networkx/networkx/blob/main/networkx/algorithms/flow/tests/test_maxflow.py

### Current Behavior

<!--- Tell us what happens instead of the expected behavior -->

We don't test all the paths the code can take us.

### Expected Behavior

<!--- Tell us what should happen -->

We should be testing everything so there aren't any surprises.

### Steps to Reproduce

<!--- Provide a minimal example that reproduces the bug -->

Visit https://app.codecov.io/gh/networkx/networkx/blob/main/networkx/algorithms/flow/maxflow.py
