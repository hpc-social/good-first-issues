---
tags: ,error-messages
title: "Better error message for `convert(Type{Union{}}, ...)`"
html_url: "https://github.com/JuliaLang/julia/issues/40951"
user: eschnett
repo: JuliaLang/julia
---

I received this error message:
```
  MethodError: convert(::Type{Union{}}, ::Vector{Float32}) is ambiguous. Candidates:
    convert(::Type{T}, a::AbstractArray) where T<:Array in Base at array.jl:532
    convert(T::Type{var"#s79"} where var"#s79"<:BitArray, a::AbstractArray) in Base at bitarray.jl:577
    convert(T::Type{var"#s832"} where var"#s832"<:SparseArrays.SparseVector, m::AbstractVector{T} where T) in SparseArrays at /Users/eschnett/julia-1.6/share/julia/stdlib/v1.6/SparseArrays/src/sparsevector.jl:453
    convert(T::Type{var"#s832"} where var"#s832"<:SharedArrays.SharedArray, a::Array) in SharedArrays at /Users/eschnett/julia-1.6/share/julia/stdlib/v1.6/SharedArrays/src/SharedArrays.jl:377
    convert(::Type{Union{}}, x) in Base at essentials.jl:203
    convert(::Type{T}, arg) where T<:VecElement in Base at baseext.jl:8
  Possible fix, define
    convert(::Type{Union{}}, ::Vector{T} where T)
```

This is a confusing error message. Would it be possible to catch this as a special case in the definition of `convert`, and emit an error such as "Converting to `Union{}`" does not make sense; check your call site"?