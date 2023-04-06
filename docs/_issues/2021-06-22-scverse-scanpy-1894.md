---
tags: ,Area-–-Performance-🐌,Enhancement-✨
title: "_sparse_nanmean is inefficient"
html_url: "https://github.com/scverse/scanpy/issues/1894"
user: ivirshup
repo: scverse/scanpy
---

`_sparse_nanmean` makes two copies of the data matrix and performs a set index operation on a sparse array. It could be much faster by not doing this things.

Noticed while reviewing #1890.

<details>
<summary> possible solution </summary>

```python
from numba import njit, prange
import numpy as np

@njit(parallel=True)
def nanmean_lowlevel(data, indices, indptr, shape):
    N, M = shape
    sums = np.zeros(N, dtype=np.float64)
    nans = np.zeros(N, dtype=np.int64)
    for i in prange(N):
        start = indptr[i]
        stop = indptr[i+1]
        window = data[start:stop]
        n_nan = np.int64(0)
        i_sum = np.float64(0.)
        for j_val in window:
            if np.isnan(j_val):
                n_nan += 1
            else:
                i_sum += j_val
        sums[i] = i_sum
        nans[i] = n_nan
    sums /= (M - nans)
    return sums
```

Has more error from dense reference compared to current solution, not sure why. Something about the sums being different.

</details>
