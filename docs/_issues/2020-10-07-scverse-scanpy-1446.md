---
tags: ,Bug-🐛
title: "sc.tl.filter_rank_genes_groups gene name with NA"
html_url: "https://github.com/scverse/scanpy/issues/1446"
user: jphe
repo: scverse/scanpy
---

- [ ] I have checked that this issue has not already been reported.
- [ ] I have confirmed this bug exists on the latest version of scanpy.
- [ ] (optional) I have confirmed this bug exists on the master branch of scanpy.

---

**Note**: Please read [this guide](https://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports) detailing how to provide the necessary information for us to reproduce your bug.


### Minimal code sample (that we can copy&paste without having any data)

```python
sc.tl.rank_genes_groups(adata,'leiden', n_genes=10000,use_raw=False)
sc.tl.filter_rank_genes_groups(adata, min_fold_change=2,min_in_group_fraction=0.3,use_raw=False,key='rank_genes_groups')
sc.pl.rank_genes_groups_heatmap(adata, swap_axes=True, use_raw=False, cmap='bwr', dendrogram=True,n_genes=1000,
                                                standard_scale='var',key='rank_genes_groups_filtered')

df1=pd.DataFrame( {group + '_' + key[:1]: adata.uns['rank_genes_groups'][key][group]  for group in ['0','1'] for key in ['names','logfoldchanges']})
df2=pd.DataFrame( {group + '_' + key[:1]: adata.uns['rank_genes_groups_filtered'][key][group]  for group in ['0','1'] for key in ['names','logfoldchanges']})
```

```pytb
<img width="721" alt="image" src="https://user-images.githubusercontent.com/34993687/95295823-56e14b00-08aa-11eb-9b8d-6bbbd4221d10.png">



```

#### Versions

<details>

Hi,

I have run sc.tl.filter_rank_genes_groups() succssfully, but I find some gene names in adata.uns['rank_genes_groups_filtered']['names'] is na
<img width="996" alt="scanpy_bug" src="https://user-images.githubusercontent.com/34993687/95296453-61e8ab00-08ab-11eb-96aa-c8b6a2215d5c.png">
n,  but all gene names in adata.uns['rank_genes_groups']['names'] are correct. So, how could this happern?

Thanks,
Jphe
</details>