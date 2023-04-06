---
tags: ,bug
title: "Inconsistent rounding for parameters in savename"
html_url: "https://github.com/JuliaDynamics/DrWatson.jl/issues/350"
user: cumberworth
repo: JuliaDynamics/DrWatson.jl
---

When using `savename`, some unexpected behaviour can happen when using some parameter values with the `sigdigits` keyword. This seems to be due to the fact that `savename` uses the `round` function to format numbers, which is designed for outputting numbers as strings. One issue occurs when using very small or large numbers, and is due to [a known bug in `round`](https://github.com/JuliaLang/julia/issues/33428), but is machine specific.

For example,
```
julia> savename("test", (p1=3.6e-23,), sigdigits=1)
"test_p1=4.0000000000000004e-23"
```
but for one order of magnitude larger
```
julia> savename("test", (p1=3.6e-22,), sigdigits=1)
"test_p1=4e-22"
```

Additionally, while it may round the correct number of significant digits, the output will not necessarily represent the specified number of significant digits. Specifically, this occurs when there should be additional zeros, which are either not be added to the given number, or are dropped when the number rounds to something that can be represented with fewer digits. For example,
```
julia> savename("test", (p1=3.5e-6,), sigdigits=4)
"test_p1=3.5e-6"
julia> savename("test", (p1=3.4999e-6,), sigdigits=4)
"test_p1=3.5e-6"
```

It would probably be more robust to use string formatting methods, for example the [Printf.@sprintf](https://docs.julialang.org/en/v1/stdlib/Printf/#Printf.@sprintf) macro, to produce the final string after using the `round` function.

I am using DrWatson v2.9.1 and julia version 1.7.3.
