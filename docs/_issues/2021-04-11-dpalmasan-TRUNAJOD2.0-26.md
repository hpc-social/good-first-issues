---
tags: ,enhancement
title: "Implement Guiraud\u2019s Index"
html_url: "https://github.com/dpalmasan/TRUNAJOD2.0/issues/26"
user: dpalmasan
repo: dpalmasan/TRUNAJOD2.0
---

This is a lexical diversity measurement that penalizes number of words. It is computed as:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=GI=\displaystyle\frac{v}{\sqrt{N}}">
</p>

Where <img src="https://render.githubusercontent.com/render/math?math=v"> is the number of distinct words in the text, and <img src="https://render.githubusercontent.com/render/math?math=N"> is the total number of words in the text.

Unit tests should be added as well.

Docs should be updated as well, adding the following reference:

```bib
@misc{herdan1961problemes,
  title={Probl{\`e}mes et m{\'e}thodes de la statistique linguistique},
  author={Herdan, Gustav},
  year={1961},
  publisher={JSTOR}
}
```