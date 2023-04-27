---
title: "Include an integer `setindex` for `NamedTuple`"
html_url: "https://github.com/JuliaLang/julia/issues/43155"
user: rafaqz
repo: JuliaLang/julia
---

We have both `Symbol` and `Int` `getindex` for a `NamedTuple`, but only `Symbol` `setindex`. 

Is there a reason for this? its seems like we should have both in both cases.
