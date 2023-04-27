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

  │ Note
  │
  │  stream must be a TTY, a Pipe, or a socket.
```
What is a pipe? What is a stream? What's a TTY? What is C level stdout? (Keep in mind many non-expert users have no reason to interact with C _at all_ while using Julia.) 

If `redirect_stdout` creates a pipe, then what does calling it with a stream (which may itself be a pipe) do?

The non-expert user might then look for docs on the types of objects that `stream` can be:
```
help?> Pipe
  Construct an uninitialized Pipe object.

  The appropriate end of the pipe will be automatically initialized if the object is used in process spawning. This can be useful to easily
  obtain references in process pipelines, e.g.:

  julia> err = Pipe()

  # After this `err` will be initialized and you may read `foo`'s
  # stderr from the `err` pipe.
  julia> run(pipeline(pipeline(`foo`, stderr=err), `cat`), wait=false)

help?> TTY
  No documentation found.

  Binding TTY does not exist.
```
The `Pipe` docs assume the reader already knows what a pipe is. (As well as process pipelines.) There aren't obviously `TTY` docs, and `?Base.TTY` is just a structure description. 

Maybe the non-expert user wants to experiment, so tries something like `redirect_stdout(Pipe())`. That throws a method error, which surely is surprising since the docs say `redirect_stdout` can be called with a `Pipe` argument.

**Suggestions**
Shockingly, the non-expert user above is me. I've been using Julia as my main language since 2015, but lack the context to understand the above docs. Through extensive trial and error I was able to accomplish the particular (simple) use case I needed, but it took a long time and felt like a pretty hostile user experience. Here are some things that would have helped me:
* Some simple examples in the inline documentation, particularly for the most obvious non-sophisticated use cases such as redirecting stdout to a file.
* Brief one-sentence descriptions of relevant concepts in the IO documentation. For example, https://docs.julialang.org/en/v1/manual/networking-and-streams/# is pretty terse and starts off with `Julia provides a rich interface to deal with streaming I/O objects such as terminals, pipes and TCP sockets.` Yikes if you're not familiar with terminals, pipes, and TCP sockets. If there's a more basic doc page, a link would have been appreciated. Otherwise, defining terms could have helped. A page which does this well is https://docs.julialang.org/en/v1/manual/functions/. `In Julia, a function is an object that maps a tuple of argument values to a return value. Julia functions are not pure mathematical functions, in the sense that functions can alter and be affected by the global state of the program.`
* If helpful manual pages exist, references to these pages in the inline docs.

**Apology**
I know the best practice is to improve the docs after you're confused, but I still feel totally out of my depth with logging and output in Julia that I'm nowhere near able to open a doc PR.
