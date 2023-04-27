---
tags: accelerated-implementation
title: "Merge implementations from \"missing SSE implementations\" to NEON"
html_url: "https://github.com/simd-everywhere/simde/issues/855"
user: nemequ
repo: simd-everywhere/simde
---

http://www.alfredklomp.com/programming/sse-intrinsics/ has a great list of implementations of "missing"  SSE instructions.

Unlike SSE, NEON isn't missing a lot of this functionality, so we should steal that code and use it to implement parts of the NEON API.  For example:

 * `_mm_cmple_epu8` → `vcleq_u8` (see 5906cc923b5ba8044e49d9cadb66373550e58758)
 * `_mm_cmpge_epu8` → `vcgeq_u8`
 * `_mm_cmpgt_epu8` → `vcgtq_u8`
 * `_mm_min_epu16` → `vminq_u16`
 * `_mm_absdiff_epu8` → `vabdq_u8`
 * `_mm_bswap_epi16` → `vrev16q_u16`/`vrev16q_s16`

We can also use the same techniques for a bunch of other functions which that page doesn't explicitly include (e.g., `vcleq_u16`/`vcleq_u32`/`vcleq_u64` can all use the same technique as `_mm_cmple_epu8`, though 16/32-bit versions require SSE4.1 and 64-bit requires AVX-512VL).

Many of the same implementations could also be used in WASM (`wasm_u8x16_le`, `wasm_u8x16_ge`, `wasm_u8x16_gt`, `wasm_u16x8_min`, *etc.*).

There are also a few functions which *are* present in later versions of SSE, but can be emulated with earlier versions.  We should make sure our implementations of SSE also have these versions, too.

As an example, 5906cc923b5ba8044e49d9cadb66373550e58758 implements `vcleq_u*` using the code from `_mm_cmple_epu8`.