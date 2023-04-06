---
tags: ,Documentation,Good-first-issue,backend-pgf,topic-text/fonts
title: "[Bug]: Warning: Font Family not found"
html_url: "https://github.com/matplotlib/matplotlib/issues/20850"
user: FranzForstmayr
repo: matplotlib/matplotlib
---

### Bug summary

Usign Latex fonts as recommended here throws a Warning:

```
findfont: Font family ['serif'] not found. Falling back to DejaVu Sans.
findfont: Generic family 'serif' not found because none of the following families were found: 
```

### Code for reproduction

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "serif",
    # Use LaTeX default serif font.
    "font.serif": [],
    # Use specific cursive fonts.
    "font.cursive": ["Comic Neue", "Comic Sans MS"],
})

plt.figure()
plt.plot([1,2,3,4])
plt.savefig('test.png')
plt.savefig('test.pgf')
```


### Actual outcome

The Bug is also visible in your Docs.
https://matplotlib.org/stable/gallery/userdemo/pgf_fonts.html



### Expected outcome

No Warning should get thrown everytime

### Operating system

Ubuntu

### Matplotlib Version

3.4.2

### Matplotlib Backend

TkAgg

### Python version

3.9.5

### Jupyter version

_No response_

### Other libraries

_No response_

### Installation

pip

### Conda channel

_No response_