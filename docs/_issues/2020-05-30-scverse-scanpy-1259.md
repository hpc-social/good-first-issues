---
tags: 
title: "ValueError: cannot convert float NaN to integer"
html_url: "https://github.com/scverse/scanpy/issues/1259"
user: sygongcode
repo: scverse/scanpy
---

Hello, everyone,

I am working om fly model. And I have met a problem when I was doing QC step use function pp.calculate_qc_metrics. I have got this error. Can anyone help me? Thanks. The code as follows: 

```python
adata.var['mt'] = adata.var_names.str.startswith('mt:')  # annotate the group of mitochondrial genes as 'mt'
sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)
```

```pytb
ValueError                                Traceback (most recent call last)
<ipython-input-34-455e630e3278> in <module>
      1 adata.var['mt'] = adata.var_names.str.startswith('mt:')  # annotate the group of mitochondrial genes as 'mt'
----> 2 sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)

~\anaconda3\lib\site-packages\scanpy\preprocessing\_qc.py in calculate_qc_metrics(adata, expr_type, var_type, qc_vars, percent_top, layer, use_raw, inplace, log1p, parallel)
    294         inplace=inplace,
    295         X=X,
--> 296         log1p=log1p,
    297     )
    298     var_metrics = describe_var(

~\anaconda3\lib\site-packages\scanpy\preprocessing\_qc.py in describe_obs(adata, expr_type, var_type, qc_vars, percent_top, layer, use_raw, log1p, inplace, X, parallel)
    119     for qc_var in qc_vars:
    120         obs_metrics[f"total_{expr_type}_{qc_var}"] = (
--> 121             X[:, adata.var[qc_var].values].sum(axis=1)
    122         )
    123         if log1p:

~\anaconda3\lib\site-packages\scipy\sparse\_index.py in __getitem__(self, key)
     51                 return self._get_sliceXslice(row, col)
     52             elif col.ndim == 1:
---> 53                 return self._get_sliceXarray(row, col)
     54             raise IndexError('index results in >2 dimensions')
     55         elif row.ndim == 1:

~\anaconda3\lib\site-packages\scipy\sparse\csr.py in _get_sliceXarray(self, row, col)
    314 
    315     def _get_sliceXarray(self, row, col):
--> 316         return self._major_slice(row)._minor_index_fancy(col)
    317 
    318     def _get_arrayXint(self, row, col):

~\anaconda3\lib\site-packages\scipy\sparse\compressed.py in _minor_index_fancy(self, idx)
    735         """
    736         idx_dtype = self.indices.dtype
--> 737         idx = np.asarray(idx, dtype=idx_dtype).ravel()
    738 
    739         M, N = self._swap(self.shape)

~\anaconda3\lib\site-packages\numpy\core\_asarray.py in asarray(a, dtype, order)
     83 
     84     """
---> 85     return array(a, dtype, copy=False, order=order)
     86 
     87 

ValueError: cannot convert float NaN to integer
```