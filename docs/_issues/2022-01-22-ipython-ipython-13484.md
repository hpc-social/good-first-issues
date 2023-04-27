---
title: "Counters should display from most common to least common"
html_url: "https://github.com/ipython/ipython/issues/13484"
user: rhettinger
repo: ipython/ipython
---

IPython is not matching Python's decision to display *Counter* objects arranged by descending count. 

What regular Python does for repr and pprint:

```
$ python
Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from collections import Counter
>>> from pprint import pprint
>>> hist = Counter(red=3813, orange=4213, yellow=2024, green=5821, blue=1181, indigo=2350, violet=1337, white=8675, block=3099)
>>> hist
Counter({'white': 8675, 'green': 5821, 'orange': 4213, 'red': 3813, 'block': 3099, 'indigo': 2350, 'yellow': 2024, 'violet': 1337, 'blue': 1181})
>>> pprint(hist)
Counter({'white': 8675,
         'green': 5821,
         'orange': 4213,
         'red': 3813,
         'block': 3099,
         'indigo': 2350,
         'yellow': 2024,
         'violet': 1337,
         'blue': 1181})
```

What IPython does:

```
$ ipython
Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.0.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: %config TerminalInteractiveShell.autoformatter=None

In [2]: from collections import Counter

In [3]: hist = Counter(red=3813, orange=4213, yellow=2024, green=5821, blue=1181, indigo=2350, violet
   ...: =1337, white=8675, block=3099)
   ...:

In [4]: hist
Out[4]:
Counter({'red': 3813,
         'orange': 4213,
         'yellow': 2024,
         'green': 5821,
         'blue': 1181,
         'indigo': 2350,
         'violet': 1337,
         'white': 8675,
         'block': 3099})

In [5]: from pprint import pprint

In [6]: pprint(hist)
Counter({'white': 8675,
         'green': 5821,
         'orange': 4213,
         'red': 3813,
         'block': 3099,
         'indigo': 2350,
         'yellow': 2024,
         'violet': 1337,
         'blue': 1181})
```