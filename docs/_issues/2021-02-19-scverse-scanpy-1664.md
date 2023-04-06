---
tags: ,Area---Documentation-📒,Area---Plotting-🌺,Enhancement-✨
title: "Inline example plots in docs"
html_url: "https://github.com/scverse/scanpy/issues/1664"
user: ivirshup
repo: scverse/scanpy
---

Meta-issue for tracking the addition of rendered plots in the examples sections of the API docs (initial functionality implemented in #1632).

We now allow code samples which generate plots in our docs. See the examples sections of [`calculate_qc_metrics`](https://scanpy.readthedocs.io/en/latest/api/scanpy.pp.calculate_qc_metrics.html#scanpy.pp.calculate_qc_metrics) and [`dotplot`](https://scanpy.readthedocs.io/en/latest/api/scanpy.pl.dotplot.html#scanpy.pl.dotplot) for examples of what this looks like. There is a short section in the dev docs with more information on how to make these: [Plots in docstring](https://scanpy.readthedocs.io/en/latest/dev/documentation.html#plots-in-docstrings)

Here is a checklist of the functions which should have rendered examples. This list is not exclusive and can definitely be expanded.

### Functions in `sc.pl`

- [ ] Embedding plots (these may deserve their own prose section)
    - [ ] `sc.pl.embedding`
    - [x] `sc.pl.draw_graph` #1809 @AnnaChristina 
    - [x] `sc.pl.diffmap` #1809 @AnnaChristina
    - [x] `sc.pl.pca` #1813 @lazappi 
    - [x] `sc.pl.tsne` #1809 @AnnaChristina
    - [x] `sc.pl.umap` #1830 @mayarali
    - [ ] `sc.pl.spatial`
    - [x] `sc.pl.embedding_density` @ivirshup 
- [ ] PCA specific
    - [x] `sc.pl.pca_loadings` #1815 @bio-la 
    - [x] `sc.pl.pca_overview` #1812 @MxMstrmn 
    - [ ] `sc.pl.pca_scatter`
    - [ ] `sc.pl.pca_variance_ratio`
- [ ] PAGA
    - [x] `sc.pl.paga` #1811 @le-ander 
    - [ ] `sc.pl.paga_adjacency`
    - [ ] `sc.pl.paga_compare`
    - [ ] `sc.pl.paga_path`
- [ ] DPT pseudotime
    - [ ] `sc.pl.dpt_groups_pseudotime`
    - [ ] `sc.pl.dpt_timeseries`
- [ ] Groupby
    - [x] `sc.pl.dotplot` @ivirshup 
    - [x] `sc.pl.matrixplot` #1808 @mbuttner 
    - [ ] `sc.pl.clustermap`
    - [x] `sc.pl.heatmap` #1809 @AnnaChristina
    - [x] `sc.pl.dendrogram` #1809 @AnnaChristina
    - [ ] `sc.pl.stacked_violin`
    - [ ] `sc.pl.tracksplot`
    - [x] `sc.pl.violin` #1814 @Hrovatin 
- [ ] Preprocessing
    - [ ] `sc.pl.filter_genes_dispersion`
    - [ ] `sc.pl.highest_expr_genes`
    - [ ] `sc.pl.highly_variable_genes`
- [ ] DE
    - [x] `sc.pl.rank_genes_groups` #1830 @mayarali
    - [x] `sc.pl.rank_genes_groups_dotplot` #1810 @LouisK92 #1529 @fidelram
    - [x] `sc.pl.rank_genes_groups_heatmap` #1830 @mayarali
    - [x] `sc.pl.rank_genes_groups_matrixplot` #1529 @fidelram
    - [ ] `sc.pl.rank_genes_groups_stacked_violin`
    - [ ] `sc.pl.rank_genes_groups_tracksplot`
    - [ ] `sc.pl.rank_genes_groups_violin`
- [ ] Misc/ to be classified
    - [ ] `sc.pl.ranking`
    - [ ] `sc.pl.scatter`
    - [ ] `sc.pl.sim`
    - [ ] `sc.pl.correlation_matrix`
    - [ ] `sc.pl.matrix`
- [ ] Time series (???)
    - [ ] `sc.pl.timeseries`
    - [ ] `sc.pl.timeseries_as_heatmap`
    - [ ] `sc.pl.timeseries_subplot`

### Other functions

- [x] `sc.pp.calculate_qc_metrics` @ivirshup (?)
- [x] `sc.tl.embedding_density` @ivirshup (?)
- [ ]  `sc.get.obs_df`
- [ ] `sc.get.rank_genes_groups_df`