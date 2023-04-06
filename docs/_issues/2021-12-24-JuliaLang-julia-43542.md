---
tags: ,Hacktoberfest,performance
title: "objectid takes arbitrarily long"
html_url: "https://github.com/JuliaLang/julia/issues/43542"
user: cooijmanstim
repo: JuliaLang/julia
---

<!--
If you have a question please search or post to our Discourse site: https://discourse.julialang.org.
We use the GitHub issue tracker for bug reports and feature requests only.

If you're submitting a bug report, be sure to include as much relevant information as
possible, including a minimal reproducible example and the output of `versioninfo()`.
If you're experiencing a problem with a particular package, open an issue on that
package's repository instead.

Thanks for contributing to the Julia project!
-->

In the following code, I construct a large deeply nested DAG and then call `objectid` on the root node. I'm expecting this to be instant, but instead the call to `objectid` takes time proportional to the size of the data structure. With the size 100 used below it probably won't return ever.

```julia
struct Foo
  x::Any
  y::Any
end
function test()
  foo = Foo(nothing, nothing)
  for i in 1:100
    foo = Foo(foo, foo)
  end
  println(1)
  println(objectid(foo))
  println(2)
end
test()
```

Version info:

```
julia> versioninfo()
Julia Version 1.7.0
Commit 3bf9d17731 (2021-11-30 12:12 UTC)
Platform Info:
  OS: Linux (x86_64-pc-linux-gnu)
  CPU: Intel(R) Core(TM) i5-5300U CPU @ 2.30GHz
  WORD_SIZE: 64
  LIBM: libopenlibm
  LLVM: libLLVM-12.0.1 (ORCJIT, broadwell)
```