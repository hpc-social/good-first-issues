---
tags: 
title: "firstindex(enumerate(...)) not defined"
html_url: "https://github.com/JuliaLang/julia/issues/40704"
user: jamblejoe
repo: JuliaLang/julia
---

```
julia> firstindex(enumerate(1:3))
ERROR: MethodError: no method matching firstindex(::Base.Iterators.Enumerate{UnitRange{Int64}})
Closest candidates are:
  firstindex(::Any, ::Any) at abstractarray.jl:366
  firstindex(::Pair) at pair.jl:63
  firstindex(::AbstractChar) at char.jl:195
  ...
```

Shouldn't this be defined? The return of iterate(enumerate...) is a tuple of an index and the value of the original iterable. Shouldn't `firstindex` return the first index in that way?

I came across this because I wanted to parallelize a for loop with threads via
```
julia> for i in enumerate(2:5); @show i; end
i = (1, 2)
i = (2, 3)
i = (3, 4)
i = (4, 5)

julia> Threads.@threads for i in enumerate(2:5); @show i; end
ERROR: TaskFailedException
Stacktrace:
 [1] wait
   @ .\task.jl:317 [inlined]
 [2] threading_run(func::Function)
   @ Base.Threads .\threadingconstructs.jl:34
 [3] top-level scope
   @ .\threadingconstructs.jl:93

    nested task error: MethodError: no method matching firstindex(::Base.Iterators.Enumerate{UnitRange{Int64}})
    Closest candidates are:
      firstindex(::Any, ::Any) at abstractarray.jl:366
      firstindex(::Pair) at pair.jl:63
      firstindex(::AbstractChar) at char.jl:195
      ...
    Stacktrace:
     [1] (::var"#14#threadsfor_fun#7"{Base.Iterators.Enumerate{UnitRange{Int64}}})(onethread::Bool)
       @ Main .\threadingconstructs.jl:66
     [2] (::var"#14#threadsfor_fun#7"{Base.Iterators.Enumerate{UnitRange{Int64}}})()   
       @ Main .\threadingconstructs.jl:48

julia> 
``` 

```
julia> versioninfo()
Julia Version 1.6.0
Commit f9720dc2eb (2021-03-24 12:55 UTC)
Platform Info:
  OS: Windows (x86_64-w64-mingw32)
  CPU: Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz
  WORD_SIZE: 64
  LIBM: libopenlibm
  LLVM: libLLVM-11.0.1 (ORCJIT, skylake)
Environment:
  JULIA_EDITOR = "C:\Users\gnakerst\AppData\Local\atom\app-1.56.0\atom.exe"  -a
  JULIA_NUM_THREADS = 4
```