---
tags: enhancement,help-wanted
title: "notebook container div still differs from \"classical\" Notebook experience"
html_url: "https://github.com/jupyter/notebook/issues/6388"
user: edthrn
repo: jupyter/notebook
---

### 1. Problem

Even though both UIs are currently very close, I still feel frustration when using RetroLab, mostly because of CSS discrepancies.

With the classical Notebook interface, the notebook `<div id="notebook-container">` kept left and right margin on small width windows, and increased in height as cells count grew.

It appears it is not the case with RetroLab latest version.


### 2. Proposed Solution

I would like to see the exact same UI on this `notebook-container` div, which is probably the most important of the whole document ; especially knowing that RetroLab will be used as [the next major version of the Notebook](https://github.com/jupyter/enhancement-proposals/blob/master/79-notebook-v7/notebook-v7.md). 

Unfortunately, my front-end engineering skills are very poor, so I won't be able to propose a PR myself :confused: 

### 3. Screen shots to illustrate the difference

Both screenshots are made with the same (small) window width.

**3.1 "Good ol' Notebook" has margins that makes the experience neater**

![image](https://user-images.githubusercontent.com/16775821/150679039-42c40438-1bca-470e-9491-6de615afc043.png)

---

**3.2 Retro Lab has no margins on small width screens**

![image](https://user-images.githubusercontent.com/16775821/150679240-623c5001-085c-46d4-9bc2-a884c48d841e.png)


