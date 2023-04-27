---
tags: display-and-printing
title: "Confusing test failure display for KeySet"
html_url: "https://github.com/JuliaLang/julia/issues/40188"
user: fonsp
repo: JuliaLang/julia
---

_Julia 1.6.0-rc3_

runtests.jl:
```julia
using Test

d = Dict("hello" => "world")
@test keys(d) == ["hello"]
```

Test output:
```
     Testing Running tests...
Test Failed at /Users/fons/Documents/Pluto.jl/test/runtests.jl:4
  Expression: keys(d) == ["hello"]
   Evaluated: ["hello"] == ["hello"]
ERROR: LoadError: There was an error during testing
in expression starting at /Users/fons/Documents/Pluto.jl/test/runtests.jl:4
```