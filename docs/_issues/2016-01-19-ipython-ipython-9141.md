---
title: "Do we remember why utils.io.IOStream exists?"
html_url: "https://github.com/ipython/ipython/issues/9141"
user: takluyver
repo: ipython/ipython
---

`IPython.utils.io` has stdin, stdout and stderr attributes which wrap the corresponding stream objects from `sys` in an `IOStream` instance. Then certain odd places around the codebase, such as oinspect, do `print(..., file=io.stdout)`, while other places don't.

I assume that this was originally supposed to provide an indirection layer so stdout/stderr could easily be redirected. However:
- Things that redirect stdout/stderr typically replace them directly in `sys` - they have to, because not all printing is directed through the `IPython.utils.io` objects. There are backup copies of the original objects as e.g. `sys.__stdout__`, so replacing `sys.stdout` is not destructive.
- When `sys.std*` is replaced, `io.std*` still has a reference to the original `sys.std*` objects, so it doesn't respect the redirection. See issue #8669, and I also just ran into this trying to use colorama in #9118.

I'm proposing that we deprecate `io.std*`, and move all uses of it in our own code to `sys.std*`. Does anyone know of a reason _not_ to do this?

Ping @fperez, because I'm pretty sure this code has been around longer than I've been on the project.
