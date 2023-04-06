---
tags: ,bug
title: "storing dict in .h5ad should raise warning when keys include '/'"
html_url: "https://github.com/scverse/anndata/issues/603"
user: MxMstrmn
repo: scverse/anndata
---

I was not aware how .h5ad stores their dicts and it took me quite a bit to figure out why my stored `adata.uns['key']` was different from the original `adata.uns['key']`. Part of the problem was the large dataset which made examination of potential fail cases difficult. 

Eventuelly, I figured out that some molecular descriptors include the sequence '(+/-)'  which caused `anndata` to store the dict in a nested structure. I would suggest to check if keys include `'/'` and raise a warning such that the user is aware that the stored dictionary will not be identical to the original one. 


Minimal Code example that clarified the problem to me: 
```Python 
import scanpy as sc 
from anndata import AnnData 

adata = AnnData()
bucket_list = {
    'remember': 'trivia',
    'forget/whatIwantedtoremember': 42, 
}
adata.uns['bucket_list'] = bucket_list
sc.write('adata_test.h5ad', adata)

adata = sc.read('adata_test.h5ad')
adata.uns['bucket_list']

```
```console
 {'forget': {'whatIwantedtoremember': 42}, 'remember': 'trivia'}
```