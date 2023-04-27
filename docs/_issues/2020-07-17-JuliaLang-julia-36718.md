---
tags: RNG,help-wanted,stdlib
title: "re-evaluate/remove `Random.UnsafeView`"
html_url: "https://github.com/JuliaLang/julia/issues/36718"
user: JeffBezanson
repo: JuliaLang/julia
---

I just noticed the `Random` stdlib has an `UnsafeView` type for filling arrays. With the new layout optimizations, this should no longer be necessary. We should try using the normal SubArray type for this. If it's still too slow/complex, then at least the type can be made safe by holding the underlying array directly instead of a `Ptr`.