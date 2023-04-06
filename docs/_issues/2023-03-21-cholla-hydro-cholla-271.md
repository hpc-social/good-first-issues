---
tags: ,code-cleanup,enhancement,refactor
title: "Convert all indexing variables to `size_t`/`ptrdiff_t` "
html_url: "https://github.com/cholla-hydro/cholla/issues/271"
user: bcaddy
repo: cholla-hydro/cholla
---

Currently many of the indexing variables we use are of type 'int' when they should be `size_t` (or `ptrdiff_t` if they're a difference). This could potentially lead to issues with the range of `int` as the size of VRAM on GPUs grows and this change would allow us to enable the following clang-tidy checks:

- `bugprone-implicit-widening-of-multiplication-result`
- `bugprone-narrowing-conversions` (alias of `cppcoreguidelines-narrowing-conversions`)

This conversion wouldn't be too difficult but would be time consuming and would be a good project for a new student/collaborator to become familiar with the code.

See [this discussion](https://github.com/cholla-hydro/cholla/discussions/217#discussioncomment-5360242) for the original discussion on the topic.