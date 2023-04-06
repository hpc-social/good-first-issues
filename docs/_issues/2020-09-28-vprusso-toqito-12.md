---
tags: enhancement
title: "Enhancement: Parallelize classical value of nonlocal game"
html_url: "https://github.com/vprusso/toqito/issues/12"
user: vprusso
repo: vprusso/toqito
---

The following loop inside of the `nonlocal_game.py` file under the `classical_value` function should be parallelized for large nonlocal games. 

```python
        for i in range(num_alice_outputs ** num_bob_inputs):
           ...
           tgval = np.sum(np.amax(pred_alice, axis=0))
            p_win = max(p_win, tgval)
        return p_win
```

This [parallelization is also performed in QETLAB](https://github.com/nathanieljohnston/QETLAB/blob/691036434e88a0bc26d6253d769d29a455dcb921/NonlocalGameValue.m#L128) where indeed the approach to calculating the classical value of a nonlocal game has been inspired from. 
