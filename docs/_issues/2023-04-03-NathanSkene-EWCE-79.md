---
tags: ,help-wanted
title: "Consider removing <4 gene limit"
html_url: "https://github.com/NathanSkene/EWCE/issues/79"
user: bschilder
repo: NathanSkene/EWCE
---

Currently `EWCE::bootstrap_enrichment_test` doesn't let you run tests where the number of hit genes is <4. @NathanSkene has noted this cutoff is arbitrary and could be removed. But we should first consider the potential statistical ramifications of small gene lists within the `EWCE` framework.

@bschilder 
> what are the dangers of reducing the number of genes? from a stats standpoint

@Al-Murphy 
> The way I understand it, the bootstrapping works well since you are looking for the specificity averaged over a gene list. For example, consider you are just looking at the specificity of one gene. This changes the question, you are now basically asking if that gene has a higher specificity than the average specificity across all genes (due the random sampling of the background gene list). So 49% of genes tested would then be specific. I think when the number of genes you test is large the chance of seeing a FP drops. Does that make sense? It's hard to articulate
>I just think you shouldn't run EWCE for it as the probability of getting an enrichment in a cell type is much higher. I think this is a bit of an issue with EWCE in general since people can just reduce the size of their gene lists to get significant results. Like a form of p-value hacking. Ideally, I guess you would add some penalisation weight for smaller gene lists to avoid the issue but that would require some testing or theoretical statistical background calculations (where you keep the probability of finding enrichment equal regardless of gene list length)

We should
1. Test the effect of hit gene list size on `EWCE` p-values.
2. Test the effect of hit gene list size on Fisher's exact test p-values.
3. Compare the distributions of p-values in both cases.
4. Perhaps look at some of the benchmarking results that Shuhan performed, or use her framework for testing these potential biases @ss8518


