---
tags: 
title: "Improvements of IntVar Views"
html_url: "https://github.com/chocoteam/choco-solver/issues/564"
user: arnaud-m
repo: chocoteam/choco-solver
---

Let x be a integer variable. The following views are available:

- scale view: s(x) = a*x  (a >= -1)
- minus view:  m(x) = -x
- offset view: t(x) = x + b

Here are two natural improvements
- [ ] extend the scale view for any a.
- [ ]  propose an affine view: f(x) = a*x + b

Experienced with choco-solver-_*{4.0.6}*_

