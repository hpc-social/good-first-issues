---
tags: Area---Plotting-🌺,Enhancement-✨
title: "pl.violin will not take \"hue\" kwarg for seaborn?"
html_url: "https://github.com/scverse/scanpy/issues/1174"
user: auesro
repo: scverse/scanpy
---

<!-- Please give a clear and concise description of what the bug is: -->
Trying to make a violin plot adding the seaborn hue argument will result in ValueError.
In adata, 'timepoint' and 'replicate' are categorical adata.obs containing floats and ints, respectively. 'timepoint' is the age of the embryo from which cells were isolated (9.5, 10.5, etc) and 'replicate' the number of the replica (1, 2, 3).

<!-- Put a minimal reproducible example that reproduces the bug in the code block below: -->
```
sc.pl.violin(adata, 'n_genes', jitter=0.4, groupby = 'timepoint', stripplot=False, hue='replicate')
```

<!-- Put your Error output in this code block (if applicable, else delete the block): -->
```
sc.pl.violin(adata, 'n_genes', jitter=0.4, groupby = 'timepoint', stripplot=False, hue='replicate')
Traceback (most recent call last):

  File "<ipython-input-5-756b321177a2>", line 1, in <module>
    sc.pl.violin(adata, 'n_genes', jitter=0.4, groupby = 'timepoint', stripplot=False, hue='replicate')

  File "/home/auesro/anaconda3/envs/Scanpy/lib/python3.7/site-packages/scanpy/plotting/_anndata.py", line 759, in violin
    **kwds,

  File "/home/auesro/anaconda3/envs/Scanpy/lib/python3.7/site-packages/seaborn/categorical.py", line 2393, in violinplot
    color, palette, saturation)

  File "/home/auesro/anaconda3/envs/Scanpy/lib/python3.7/site-packages/seaborn/categorical.py", line 559, in __init__
    self.establish_variables(x, y, hue, data, orient, order, hue_order)

  File "/home/auesro/anaconda3/envs/Scanpy/lib/python3.7/site-packages/seaborn/categorical.py", line 152, in establish_variables
    raise ValueError(err)

ValueError: Could not interpret input 'replicate'
```

#### Versions:
<!-- Output of scanpy.logging.print_versions() -->
> scanpy==1.4.6 anndata==0.7.1 umap==0.4.1 numpy==1.18.1 scipy==1.4.1 pandas==1.0.3 scikit-learn==0.22.2.post1 statsmodels==0.11.1 python-igraph==0.8.0