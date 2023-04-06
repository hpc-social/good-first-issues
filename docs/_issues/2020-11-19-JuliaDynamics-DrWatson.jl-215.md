---
tags: ,bug,savename
title: "Savename expand for nested structs is not working"
html_url: "https://github.com/JuliaDynamics/DrWatson.jl/issues/215"
user: sebastianpech
repo: JuliaDynamics/DrWatson.jl
---

As `savename` works for structs, I think it should also be possible to expand them. This doesn't work at the moment because of
https://github.com/JuliaDynamics/DrWatson.jl/blob/1eece239953ab2a5aa6de1c9cb67236df0665264/src/naming.jl#L119
which, unless defined for the struct, throws an error for non-iterable types.