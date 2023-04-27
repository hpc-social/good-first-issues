---
tags: complex
title: "mod(::Complex{<:Integer}, ::Integer) and div etc."
html_url: "https://github.com/JuliaLang/julia/issues/37376"
user: stevengj
repo: JuliaLang/julia
---

As [discussed on discourse](https://discourse.julialang.org/t/extend-mod-first-argument-to-gaussian-integers), this seems like the only sensible definition:
```
mod(z::Complex{<:Integer}, n::Integer) = Complex(mod(real(z), n), mod(imag(z), n))
```
and similarly for `div`, `rem` (and probably `divrem`).   

Should be easy to create a patch (much simpler than #35374): just add the 1-line definitions analogous to the one above, docs, news, and a test.
