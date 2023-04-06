---
tags: ,speculative
title: "username() function (analogous to homedir())"
html_url: "https://github.com/JuliaLang/julia/issues/48302"
user: stevengj
repo: JuliaLang/julia
---

As recently commented [on discourse](https://discourse.julialang.org/t/how-to-get-username/93023?u=stevengj), it would be nice to have a `username()` function analogous to `homedir()`, similar to Python's [getpass.getuser](https://docs.python.org/3/library/getpass.html#getpass.getuser).

Just as `homedir()` checks environment variables like `HOME` before calling `getpwuid`, Python's `getpass.getuser` checks several environment variables before interrogating the `passwd` struct.

We can do the same thing in Julia.  An example implementation is [here](https://discourse.julialang.org/t/how-to-get-username/93023/6?u=stevengj).   Note also that we already have `Libc.getpwuid(Libc.getuid(), true).username` to extract the passwd data.

It's not entirely clear to me if Python's sequence of environment variables `("LOGNAME", "USER", "LNAME",  "USERNAME")` is the right choice, or if it's some legacy thing that they implemented in 1993 and can no longer change.  Would be good to investigate this carefully.   Would be good to survey some other modern languages too.  We might also want a flag to tell it to ignore the environment variables.

Since we already basically have this functionality, but it requires low-level knowledge to call correctly, it seems like a good candidate for something to have a better API for in Base.  Marking as "good first issue" since coding-wise it should be easy (most of the work is already done) once we decide whether we want this and precisely what we want.