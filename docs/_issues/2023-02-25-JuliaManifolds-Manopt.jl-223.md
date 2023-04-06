---
tags: ,enhancement
title: "High-lever interfaces starting with `solvername(M, obj, ...)`"
html_url: "https://github.com/JuliaManifolds/Manopt.jl/issues/223"
user: kellertuer
repo: JuliaManifolds/Manopt.jl
---

Since `ManoptExamples` will also provide objectives – and the fact that we have objectives, it might be nice to provide high-level interfaces accepting objectives so that we have

```
gradient_descent(M, f, grad_f, x0)
```

but also

```
gradient_descent(M, gradient_objective, x0)
```

The first could just construct the objective and pass to the second. Similarly for the in_place variants.
The lower one (objective) would define all defaults to have them in just one place.