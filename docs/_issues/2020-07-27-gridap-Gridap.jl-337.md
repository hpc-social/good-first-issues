---
tags: ,enhancement,help-wanted,new-functionality
title: "Adjoints of FEOperators"
html_url: "https://github.com/gridap/Gridap.jl/issues/337"
user: santiagobadia
repo: gridap/Gridap.jl
---

@fverdugo @oriolcg We want to create adjoints of `FEOperator`s. In this sense, I propose a method like
```
adj_op = Adjoint(op,uh)
```
where `op` is a `FEOperator`, `uh` is the solution. We have discussed to include there the `RHS`, but it would be misleading, it has nothing to do with the adjoint. Instead, I would return a `AffineFEOperator` with zero right hand side and create a method that takes `adj_op` and the `rhs` separately.

The internal implementation of this adj_op can be:

1. If `op` is a `AffineFEOperator`, we can consider as the most general method, to take the corresponding sparse matrix and perform a lazy `Julia` transpose. However, I think that this is probably not what we want for some particular implementation of the matrix (e.g., when using PETSc arrays, etc). In those cases, more concrete versions of the transpose, e.g., non-lazy versions, will be needed.

2. If `op` is a `FEOperatorFromTerms`, to define the transpose of this operator that does exactly the same as the `FEOperatorFromTerms` but tranposes the local element matrix before its assembly. Since it is a _minor_ change in the implementation of `FEOperatorFromTerms`, I would probably use a trait to implement this.