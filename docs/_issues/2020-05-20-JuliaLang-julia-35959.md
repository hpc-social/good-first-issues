---
tags: doc
title: "docs for redirect_std* assume too much background knowledge"
html_url: "https://github.com/JuliaLang/julia/issues/35959"
user: evanfields
repo: JuliaLang/julia
---

**Summary**

The inline docs for `redirect_stdout` and `redirect_stderr` assume a lot of background knowledge about pipes, streams, processes, C interop, etc. A beginner or intermediate user might have reason to use these functions without also having this background knowledge. Further, the manual / online docs don't contain explanations or examples. [Unless I am overlooking something obvious there?]

**Examples**
Note: the questions below are questions a non-expert user might have; I'm not trying to use the issue tracker as a Q&A.
```
help?> redirect_stdout
  redirect_stdout([stream]) -> (rd, wr)

  Create a pipe to which all C and Julia level stdout output will be redirected. Returns a tuple (rd, wr) representing the pipe ends. Data
  written to stdout may now be read from the rd end of the pipe. The wr end is given for convenience in case the old stdout object was cached
  by the user and needs to be replaced elsewhere.

  If called with the optional stream argument, then returns stream itself.

  