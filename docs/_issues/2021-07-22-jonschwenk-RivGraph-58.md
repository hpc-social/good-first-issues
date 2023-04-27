---
title: "Fix deprecation warning"
html_url: "https://github.com/VeinsOfTheEarth/RivGraph/issues/58"
user: jonschwenk
repo: jonschwenk/RivGraph
---

`im_utils.regionprops()` prints this warning upon each initial call: 
```
...\rivgraph\im_utils.py:657: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
  out[prop] = np.array(coords)
```
We should fix this.