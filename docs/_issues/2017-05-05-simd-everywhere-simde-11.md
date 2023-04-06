---
tags: GSoC/Outreachy-ideas,help-wanted,instruction-set-support
title: "MSA functions"
html_url: "https://github.com/simd-everywhere/simde/issues/11"
user: nemequ
repo: simd-everywhere/simde
---

 * https://www.mips.com/products/architectures/ase/simd/
 * https://gcc.gnu.org/onlinedocs/gcc/MIPS-SIMD-Architecture-_0028MSA_0029-Support.html
 * https://github.com/llvm/llvm-project/blob/main/clang/lib/Headers/msa.h

For progress information, see https://github.com/simd-everywhere/implementation-status/blob/main/msa.md

Due to QEMU bugs we can't just use the versions shipped with Debian to test.  The latest git works, though, and the docker image can be configured to download and compile it.  Use `QEMU_GIT=y ./docker/simde-dev.sh` (or, if you already have a docker image built, `QEMU_GIT=y BUILD_IMAGE=y ./docker/simde-dev.sh` to force a rebuild) to get it.

Once you have qemu from git, you can use the `mips64el+msa-gcc-10` build to target MSA and generate test vectors.