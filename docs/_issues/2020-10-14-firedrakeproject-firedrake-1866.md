---
tags: ,complex
title: "Use `PetscRealPart` and `PetscImaginaryPart` in supermeshing.py"
html_url: "https://github.com/firedrakeproject/firedrake/issues/1866"
user: ReubenHill
repo: firedrakeproject/firedrake
---

> Since we are using `PetscScalar` we should probably use `PetscRealPart` and `PetscImaginaryPart`.

This would be instead of

```
real_simplex[d*i+j] = creal(simplex[d*i+j]);
imag_simplex[d*i+j] = cimag(simplex[d*i+j]);
```
in `static void seperate_real_and_imag(PetscScalar *simplex, double *real_simplex, double *imag_simplex, int d)` - [permalink here](https://github.com/firedrakeproject/firedrake/blob/fecd3830a0e3ebfe78a7a6963eede9eab33e2d3e/firedrake/supermeshing.py#L220-L221).

_Originally posted by @djanekovic in https://github.com/firedrakeproject/firedrake/pull/1696#discussion_r500089095_