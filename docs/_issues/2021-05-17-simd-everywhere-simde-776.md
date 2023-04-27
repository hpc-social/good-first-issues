---
tags: GSoC/Outreachy-ideas,accelerated-implementation
title: "Add optimized implementations to WASM SIMD128"
html_url: "https://github.com/simd-everywhere/simde/issues/776"
user: nemequ
repo: simd-everywhere/simde
---

Currently, there are a lot of implementations in WASM are missing; when I added support I was really just trying to get the portable implementations done, so even some obvious implementations (such as shuffle/convert-based implementations) are missing.

The [WASM SIMD issue tracker](https://github.com/WebAssembly/simd/issues) has lots of great info on possible implementations; each time an instruction was proposed implementations for at least some architectures were included.  They're in assembly so they'll need to be converted to intrinsics, but but this could be a good opportunity for someone to familiarize themselves with assembly a bit…

I think the best thing to do there would be to look at [the specification](https://github.com/WebAssembly/simd/blob/main/proposals/simd/SIMD.md) tracker to find the name of the instruction, then search in the issue tracker for that project for the instruction name. For example, [bitmask](https://github.com/WebAssembly/simd/issues?q=bitmask). There might be a lot of issues to wade through (there are for bitmask ☹), but something like WebAssembly/simd#368 is what you're after, at least for `i64x2.bitmask`.

For x86, you can then head over to the IIG and search for the instruction they mention to figure out which intrinsic(s) it maps to. For example, [MOVMSKPD](https://software.intel.com/sites/landingpage/IntrinsicsGuide/#text=MOVMSKPD).  For Arm you can mostly do the same with the [NEON Intrinsics Reference](https://developer.arm.com/architectures/instruction-sets/simd-isas/neon/intrinsics), for example [SQXTN](https://developer.arm.com/architectures/instruction-sets/simd-isas/neon/intrinsics?search=sqxtn).

Compiler Explorer can be a great resource to help figure out which intrinsics to use, and how to map the arguments. For example, https://godbolt.org/z/T8zMTaanY. Even if you don't know assembly, with a little trial and error you should be able to get everything to match with what is in WASM SIMD's issue tracker.

The other thing you can do while you're working on that is to look at functions from other ISAs which we cover to make sure those contain the optimized versions as well. For example, for bitmask, there is a good chance that `simde_mm_movemask_pd` doesn't contain an Arm implementation as good as the one in that post.

There is also a good chance that SIMDe *will* have good implementations in another ISA (such as `simde_mm_movemask_pd`).  While I think the x86 and AArch64 implementations in WASM SIMD's issue tracker will probably be the same or better, this can be a good way to find implementations for other architectures, such as POWER or z/Architecture.

FInally, [WAV](https://github.com/nemequ/wav) has some good portable-ish (often clang-specific, but not architecture-specific) implementations; it would be great to check there, too.  Some of them require clang's `__builtin_shufflevector`, whereas for ohers the number of elements in the input vectors is equal to the number of elements in the output vectors so they could work with GCC's `__builtin_shuffle` (and therefore SIMDe's `SIMDE_SHUFFLE_VECTOR_` abstraction).