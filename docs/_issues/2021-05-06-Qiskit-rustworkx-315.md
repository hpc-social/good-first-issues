---
tags: ,enhancement
title: "Add Link Analysis functions"
html_url: "https://github.com/Qiskit/rustworkx/issues/315"
user: IvanIsCoding
repo: Qiskit/rustworkx
---

<!-- ⚠️ If you do not respect this template, your issue will be closed -->
<!-- ⚠️ Make sure to browse the opened and closed issues to confirm this idea does not exist. -->

### What is the expected enhancement?

Add functions to calculate [PageRank](https://en.wikipedia.org/wiki/PageRank) and [HITS](https://en.wikipedia.org/wiki/HITS_algorithm) to expand the retworkx's link analysis capabilities.

These algorithms are popular among users of graph libraries, and also appear frequently in benchmarks. The hope by adding those algorithms is to make retworkx appeal to more users and become more popular.

For inspiration, our functions couls have an API that is similar to [networkx's Link Analysis API](https://networkx.org/documentation/stable/reference/algorithms/link_analysis.html?highlight=pagerank#module-networkx.algorithms.link_analysis.pagerank_alg):

* [pagerank](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.link_analysis.pagerank_alg.pagerank.html#networkx.algorithms.link_analysis.pagerank_alg.pagerank)
* [pagerank_numpy](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.link_analysis.pagerank_alg.pagerank_numpy.html#networkx.algorithms.link_analysis.pagerank_alg.pagerank_numpy)
* [hits](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.link_analysis.hits_alg.hits.html#networkx.algorithms.link_analysis.hits_alg.hits)
* [hits_numpy](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.link_analysis.hits_alg.hits_numpy.html#networkx.algorithms.link_analysis.hits_alg.hits_numpy)