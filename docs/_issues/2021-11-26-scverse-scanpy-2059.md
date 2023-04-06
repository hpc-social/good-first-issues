---
tags: ,Area---Plotting-🌺,Enhancement-✨
title: "limit number of loadings in pl.pca_loadings"
html_url: "https://github.com/scverse/scanpy/issues/2059"
user: Yves33
repo: scverse/scanpy
---

In pl.pca_loagings(), there should be an option to limit the number of points plotted (basically n_points from ranking)

Why: I recently used the AnnData/scanpy suite to perform some analysis on a low number of genes (less than 30, amplified by qRT-PCR).
As the number of features is less than 30 (30 being the default value for n_points in ranking(adata,*args,**kwargs), the loadings appear twice on the sc.pl.loadings() graph.
(the slices [0:15] and 5:20] are overlapping, in case you have only 20 genes.

definition should be:
```
def pca_loadings(
    adata: AnnData,
    components: Union[str, Sequence[int], None] = None,
    n_points=30,
    include_lowest: bool = True,
    show: Optional[bool] = None,
    save: Union[str, bool, None] = None,
):
```

and later in implementation
```
ranking(
        adata,
        'varm',
        'PCs',
        npoints=npoints,
        indices=components,
        include_lowest=include_lowest,
    )
```