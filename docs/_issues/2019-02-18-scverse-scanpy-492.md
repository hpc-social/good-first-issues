---
tags: Enhancement-✨
title: "Regressing out genes"
html_url: "https://github.com/scverse/scanpy/issues/492"
user: joshuahwu
repo: scverse/scanpy
---

In Seurat, there is an option of selecting a list of genes in the pre-processing regressOut function. I was wondering if there was similar functionality in Scanpy. Doing something like below does not work for me as a lot of the cells have 0 expression, giving me a PerfectSeparationError.

`adata.obs[gene] = adata[:, adata.var_names==gene].X`
`sc.pp.regress_out(adata,gene)`

Any help would be appreciated. Thank you!