---
tags: enhancement,help-wanted,new-functionality
title: "Evaluate PDE solution"
html_url: "https://github.com/gridap/Gridap.jl/issues/345"
user: jw3126
repo: gridap/Gridap.jl
---

Thanks a lot for creating Gridap! Its awesome to have such a PDE package in pure julia. So say I solved a PDE using Gridap, 
how do I actually evaluate the solution?

```julia
# solve the trivial PDE
# u = sin

using Gridap
model = CartesianDiscreteModel((0,1),10)
f(pt) = sin(pt[1])
V0 = TestFESpace(
  reffe=:Lagrangian, order=2, valuetype=Float64,
  conformity=:H1, model=model, dirichlet_tags="boundary")
U = TrialFESpace(V0)
trian = Triangulation(model)
quad = CellQuadrature(trian, 2)
A(u, v) = u ⊙ v
b(v) = v*f
t_Ω = AffineFETerm(A,b,trian,quad)
op = AffineFEOperator(U,V0,t_Ω)
u = solve(op)
```
I tried the following, both of which did not work:
```julia
pt = [0.1]
u(pt)
evaluate(u, pt)
```