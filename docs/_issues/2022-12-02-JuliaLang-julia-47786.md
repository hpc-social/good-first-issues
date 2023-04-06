---
tags: ,dates,help-wanted
title: "Dates round/floor/ceil arguments switched"
html_url: "https://github.com/JuliaLang/julia/issues/47786"
user: jariji
repo: JuliaLang/julia
---

`round(T, x)` is the normal API, but in Dates.jl the arguments are reversed.

```jl
julia> ceil(today(), Week)
2022-12-05

julia> ceil(Week, today())
ERROR: MethodError: no method matching ceil(::Type{Week}, ::Date)
```