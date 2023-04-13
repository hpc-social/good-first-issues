---
tags: help-wanted
title: "Improve test coverage by moving self-tests"
html_url: "https://github.com/biopython/biopython/issues/820"
user: peterjc
repo: biopython/biopython
---

Many of the Python files in Biopython still have self-tests at the end which are executed if the file is run directly via the idiom:

``` python
if __name__ == "__main__":
    print("Running a quick self-test")
    ...
```

This is bad for several reasons - these tests are not being run routinely via our buildbot [*Update: We stopped using buildbot, but now have AppVeyor instead*] or TravisCI (and therefore if the test breaks, we don't know about it), they are not counted on the coverage report https://codecov.io/github/biopython/biopython/ (and in fact actively reduce the coverage score [*Update: We configured codecov to ignore the self tests*]), and moreover with Python 3 making subtle changes to imports, some of these self tests have accidentally become Python 2 only.

This is a tracking issue to encourage more commits like these which move these self-tests under `Tests/test_XXX.py` using the unittest framework instead:
- eb0c7ab903882587f3ece06e51e15c6e68855cc9
- da5a414819fdaef1fc9eb3a713fb00f92030889e

Or, in some cases using a doctest instead makes sense:
- 9242f12a65fb1d6bdc82f8201531662fb63a101b

In those cases, we're left with a stub like this which is useful when working directly on a file's doctests:

``` python
if __name__ == "__main__":
    from Bio._utils import run_doctest
    run_doctest(verbose=0)
```
