---
tags: ,codegen,latency
title: "better calling convention for large numbers of arguments"
html_url: "https://github.com/JuliaLang/julia/issues/44417"
user: JeffBezanson
repo: JuliaLang/julia
---

Currently, we mostly map julia function arguments directly to LLVM arguments regardless of how many there are. That probably causes us to hit some pathological cases, since LLVM is not likely to care about or optimize handling 1000 arguments, since most front-ends do not generate that.

For example:
```
julia> fields = [:($(Symbol("var$i"))::Int) for i in 1:1000];

julia> @eval struct x
           $(fields...)
           end

julia> @time @eval x(fill(1,1000)...)
  0.482531 seconds (39.92 k allocations: 2.195 MiB, 99.91% compilation time)
```
... which goes down to 0.16 seconds with -O0. There may be multiple issues (for example there seems to be too much time in dead store elimination), but we should probably use an array for the tail of the argument list.

This is not exactly *easy*, but could be a good relatively small project for somebody who wants to get started on the compiler.
