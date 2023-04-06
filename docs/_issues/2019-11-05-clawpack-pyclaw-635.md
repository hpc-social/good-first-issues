---
tags: ,Bug
title: "solution.Solution -- cannot pass `frame=` as kwarg"
html_url: "https://github.com/clawpack/pyclaw/issues/635"
user: rjleveque
repo: clawpack/pyclaw
---

I was having problems reading in a single frame of a solution using `solution.Solution` and finally tracked it down to the fact that although the first parameter of `Solution` is named `frame` you cannot call it using this as a kwarg, e.g. the two commands below should load the same frame but the second silently does nothing:

```
>>> from clawpack.pyclaw.solution import Solution

>>> framesoln = Solution(0, path='_output', file_format='ascii')
>>> len(framesoln.states)
18

>>> framesoln = Solution(frame=0, path='_output', file_format='ascii')
>>> len(framesoln.states)
0
```

The reason is that the code decides whether to read the solution based on this logic:
```
        if len(arg) == 1:
            # Load frame
            frame = arg[0]
```
Surely there's a better way to get the desired behavior but also allow specifying the key word?

And if this gets rewritten, would it be better to call this argument `frameno` for consistency with what we do in visclaw and other places, or is `frame` too heavily used elsewhere in pyclaw?