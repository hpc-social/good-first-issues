---
tags: complex,maths
title: "Extend floor (round, etc) to Complex numbers"
html_url: "https://github.com/JuliaLang/julia/issues/42060"
user: danilo-bc
repo: JuliaLang/julia
---

I was recently porting a Matlab example to julia and I realized there's no direct equivalence.

I extended the floor function in my code snippet by doing:
```julia
import Base.floor
floor(x::Complex) = floor(real(x)::Real) + 1im*floor(imag(x)::Real)
```

I'm not sure if this would be a welcome addition, but it would surely make Julia code more similar to other well-used scientific software.
