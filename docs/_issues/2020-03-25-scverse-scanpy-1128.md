---
tags: 
title: "Issues with ingest"
html_url: "https://github.com/scverse/scanpy/issues/1128"
user: andrea-tango
repo: scverse/scanpy
---

Hi all,

I am trying to use `ingest` to integrate different datasets.
I found a couple of issues.

- `ingest` requires that the `var_names` are the same in the reference and the new object. I can select the intersection between the datasets; however, it requires that the genes are in the same order `if not ref_var_names.equals(new_var_names)`. I think this `if` could be modified using `set` (e.g., `len(set(ref_var_names).difference(set(new_var_names))) == 0`). I tried to order the `.var` dataframe, but the `.X` remains the same. In such a way, the expression of the genes does not correspond to the correct one. I can generate a dataframe and recreate the `.X`, but it could be very nice that the `.X` will be modified according to `.var` or `.obs` modifications (i.e., ordering). 

- although it is possible to set `embedding_method=umap`, `ingest` requires the PCA components. I used autoencoders instead of PCA, and I cannot run `ingest` only considering the UMAP. Can you fix it? 

Thank you in advance.
Best,
Andrea