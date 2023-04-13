---
tags: collections
title: "Add `haskey` for `Tuple`"
html_url: "https://github.com/JuliaLang/julia/issues/35516"
user: simonschoelly
repo: JuliaLang/julia
---

Currently `haskey` is defined for `NamedTuple` but not for `Tuple`. Would it make sense to also add this for tuples? After all, `keys(::Tuple)` is also defined.

Code would then probably look like this
```julia
    haskey(t::Tuple, key) = isdefined(t, key)
```
Related: https://github.com/JuliaLang/julia/issues/32898