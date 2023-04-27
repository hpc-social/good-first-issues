---
tags: bug
title: "`eachindex` should throw `DimensionMismatch` for differently sized tuples"
html_url: "https://github.com/JuliaLang/julia/issues/47898"
user: cafaxo
repo: JuliaLang/julia
---

Currently, we have
```
julia> eachindex((), (1,))
Base.OneTo(1)
```
From the documentation of `eachindex`, I expected a `DimensionMismatch` instead. Like this:
```
julia> eachindex(1:0, 1:1)
ERROR: DimensionMismatch: all inputs to eachindex must have the same indices, got Base.OneTo(0) and Base.OneTo(1)
```

(Previous discussion on slack: https://julialang.slack.com/archives/C6A044SQH/p1671032794309049)