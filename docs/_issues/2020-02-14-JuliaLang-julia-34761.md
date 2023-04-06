---
tags: doc
title: "Better documentation for `methods`"
html_url: "https://github.com/JuliaLang/julia/issues/34761"
user: Nosferican
repo: JuliaLang/julia
---

I believe `methods` should have a bit more of information, consider,
```
struct A end
methods(A)
struct B{T} end
methods(B)
methods(B{Int})
struct C{T}
    C(x) = new{Int}(0)
end
methods(C)
```
Basically the way that methods are collected / match isn