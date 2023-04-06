---
tags: ,Bug-🐛
title: " f\"Values {list(not_found)}, from {list(indexer)}, \"      \"are not valid obs/ var names or indices.\""
html_url: "https://github.com/scverse/scanpy/issues/1487"
user: brianpenghe
repo: scverse/scanpy
---

This bug only occurred in 1.6.0 but not 1.5.0

I was running `scanpy 1.6.0` this:

`sc.tl.filter_rank_genes_groups(adata, groupby=obs,\
                    max_out_group_fraction=max_out_group_fraction,
                    min_fold_change=min_fold_change,use_raw=use_raw,
                    min_in_group_fraction=0.25,log=log)`

But got this error:

```
Filtering genes using: min_in_group_fraction: 0.25 min_fold_change: 2, max_out_group_fraction: 0.25

---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-91-d477dca208af> in <module>
      2                     max_out_group_fraction=max_out_group_fraction,
      3                     min_fold_change=min_fold_change,use_raw=use_raw,
----> 4                     min_in_group_fraction=0.25,log=log)

/usr/local/lib/python3.6/dist-packages/scanpy/tools/_rank_genes_groups.py in filter_rank_genes_groups(adata, key, groupby, use_raw, log, key_added, min_in_group_fraction, min_fold_change, max_out_group_fraction)
    725             var_names,
    726             groupby='__is_in_cluster__',
--> 727             use_raw=use_raw,
    728         )
    729 

/usr/local/lib/python3.6/dist-packages/scanpy/plotting/_anndata.py in _prepare_dataframe(adata, var_names, groupby, use_raw, log, num_categories, layer, gene_symbols)
   1808         matrix = adata.raw[:, var_names].X
   1809     else:
-> 1810         matrix = adata[:, var_names].X
   1811 
   1812     if issparse(matrix):

/usr/local/lib/python3.6/dist-packages/anndata/_core/anndata.py in __getitem__(self, index)
   1085     def __getitem__(self, index: Index) -> "AnnData":
   1086         """Returns a sliced view of the object."""
-> 1087         oidx, vidx = self._normalize_indices(index)
   1088         return AnnData(self, oidx=oidx, vidx=vidx, asview=True)
   1089 

/usr/local/lib/python3.6/dist-packages/anndata/_core/anndata.py in _normalize_indices(self, index)
   1066 
   1067     def _normalize_indices(self, index: Optional[Index]) -> Tuple[slice, slice]:
-> 1068         return _normalize_indices(index, self.obs_names, self.var_names)
   1069 
   1070     # TODO: this is not quite complete...

/usr/local/lib/python3.6/dist-packages/anndata/_core/index.py in _normalize_indices(index, names0, names1)
     33     ax0, ax1 = unpack_index(index)
     34     ax0 = _normalize_index(ax0, names0)
---> 35     ax1 = _normalize_index(ax1, names1)
     36     return ax0, ax1
     37 

/usr/local/lib/python3.6/dist-packages/anndata/_core/index.py in _normalize_index(indexer, index)
     99                 not_found = indexer[positions < 0]
    100                 raise KeyError(
--> 101                     f"Values {list(not_found)}, from {list(indexer)}, "
    102                     "are not valid obs/ var names or indices."
    103                 )

KeyError: "Values ['LINC00601', 'DPYS', 'AC136604.2', 'AC023137.1', 'MATN3', 'AL359921.1' 
...
 'FAM129C', 'TCL1A'], are not valid obs/ var names or indices."
```