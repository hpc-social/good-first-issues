---
tags: ,enhancement
title: "Performance of _get_relevance()"
html_url: "https://github.com/DeepRank/deeprank/issues/205"
user: NicoRenaud
repo: DeepRank/deeprank
---

The function `_get_relevance` of `NeuralNet` (that is called at each epoch) is really slow and takes up to a few hours on cartesius when training on 001-003 of BM5. In comparison the training during the epoch takes about 2 hours .This is due to the fact that for each molecule we open the hdf5, read the irmsd and close the hdf5. We could instead preload the irmsd during the data preprocessing when we create the indexing of the molecule. 

In general I think we should pre-load all the class metrics we need when pre processing the data set before the first epoch