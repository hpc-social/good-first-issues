---
tags: strings
title: "SubString: parentindices don't work"
html_url: "https://github.com/JuliaLang/julia/issues/49341"
user: aplavin
repo: JuliaLang/julia
---

For array views, `parentindices` return the view indices in the parent. However, this function doesn't work for string views:
```julia
julia> view([1,2,3], 2:3) |> parentindices
(2:3,)

julia> view("abc", 2:3) |> parentindices
ERROR: MethodError: no method matching parentindices(::SubString{String})
```
Would be very useful to support it too. For example, to retrieve substring locations after string functions like `split`.

`parentindices` should be computable from `SubString`, though it doesn't directly contain the range and I'm not sure how to compute it correctly given how strings are indexed:
```julia
julia> view("abc", 2:3) |> dump
SubString{String}
  string: String "abc"
  offset: Int64 1
  ncodeunits: Int64 2
```