---
tags: doc
title: "Improve documentation for `esc`"
html_url: "https://github.com/JuliaLang/julia/issues/37122"
user: goretkin
repo: JuliaLang/julia
---

```
esc(e)

  Only valid in the context of an Expr returned from a macro. Prevents the macro hygiene pass from turning embedded variables into gensym variables. See the Macros section of the Metaprogramming chapter of the manual for more details and examples.
```
I'm not sure what "valid" really means here, since

```julia
julia> esc(:(x, ))
:($(Expr(:escape, :((x,)))))
```

It could mean "you can't eval the resulting expression":

```julia
julia> eval(esc(:(x, )))
ERROR: syntax: invalid syntax (escape (call (core tuple) (outerref x)))
```

