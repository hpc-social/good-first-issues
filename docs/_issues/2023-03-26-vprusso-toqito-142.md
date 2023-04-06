---
tags: ,feature-request
title: "Feature: Check for linearly independent / dependent vectors"
html_url: "https://github.com/vprusso/toqito/issues/142"
user: vprusso
repo: vprusso/toqito
---

Given a collection of vectors, determine if they are linearly independent or not. Something like the following:

```python
import numpy as np
from toqito.matrix_ops import vec

def is_linearly_independent(vectors) -> bool:
    """Determine if all of the states in the ensemble are linearly independent."""
    vecs = tuple([vec(vector) for vector in vectors])
    mat = np.array(vecs).T

    return np.alltrue(np.linalg.matrix_rank(mat) == len(vecs))
```

Adding tests and documentation for the feature would also be required (as it is done for the other functions in `toqito` as well. 