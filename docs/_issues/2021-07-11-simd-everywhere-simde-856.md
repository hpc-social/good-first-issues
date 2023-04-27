---
tags: enhancement
title: "Relaxed SIMD support"
html_url: "https://github.com/simd-everywhere/simde/issues/856"
user: nemequ
repo: simd-everywhere/simde
---

The WebAssembly people are working on a [relaxed SIMD](https://github.com/WebAssembly/relaxed-simd) proposal which mostly just provides alternatives for already-implemented functions, but allows for some differences between different implementations (e.g., allowing different results for out-of-range values, NaNs, *etc.*).

This should be pretty easy issue to resolve; we can mostly just copy the existing implementations and remove some special cases.

The specification is very much a work in progress so stuff may change, new instructions may be added, etc., but the goal for this issue is to just get SIMDe in sync with whatever the current proposal looks like.

I already did one instruction (swizzle), so all the infrastructure is in place, we just need implementations.