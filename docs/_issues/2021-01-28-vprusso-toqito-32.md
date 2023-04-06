---
tags: ,feature-request
title: "Feature: Channel dimensions"
html_url: "https://github.com/vprusso/toqito/issues/32"
user: vprusso
repo: vprusso/toqito
---

Given a quantum channel, compute the input, output, and environment dimensions of the quantum channel. 

The channel should be provided as input as either a Choi matrix or a `List` or Kraus operators. 

In spirit, the approach for computing these dimensions align with the QETLAB function `superoperator_dims` found [here](http://www.qetlab.com/Superoperator_dims).

For reference, here is some code written that partially implements the solution:

```python
def channel_dim(phi, allow_rect=True, dim=None):
    if isinstance(phi, list):
        pass

    else:
        r, c = phi.shape
        da = np.array([np.round(np.sqrt(r)), np.round(np.sqrt(c))])
        db = da

        if dim is None:
            dim = np.array([da.conj().T, db.conj().T])

        dim = expand_dim(dim)

        if r != c and not allow_rect:
            raise ValueError("ERR")
        if dim[0, 0] * dim[0, 1] != r or dim[1, 0] * dim[1, 1] != c:
            raise ValueError("ERR")

        # TODO calc environ dim

    # Finally put DIM back into DA and DB
    if allow_rect:
        da = np.array([dim[0, 0], dim[1, 0]])
        db = np.array([dim[0, 1], dim[1, 1]])
    else:
        da = dim[0, 0]
        db = dim[0, 1]

    return da, db
    
def expand_dim(dim):
    sz = dim.shape
    if np.max(sz) == 1:
        return np.array([[dim, dim], [dim, dim]])
    elif np.min(sz) == 1:
        return np.array([[dim[:].conj().T], [dim[:].conj().T]])
    elif np.max(sz) == 2:
        return dim
    else:
        raise ValueError("Error")    
```
