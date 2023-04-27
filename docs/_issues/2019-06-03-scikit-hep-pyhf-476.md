---
tags: feat/enhancement
title: "Consider adding __repr__ methods to all classes"
html_url: "https://github.com/scikit-hep/pyhf/issues/476"
user: matthewfeickert
repo: scikit-hep/pyhf
---

# Description

For future debugging instances (I'm thinking mostly of users who are debugging,  but also for the core devs) it could be quite useful to have [`__repr__`](https://docs.python.org/3/library/functions.html#repr) methods for all relevant classes that return something simple but useful such as the string representation of the constructor call for that class with the `__init__` arguments.

So perhaps something along the lines of

```python
class ExampleClass:
    def __init__(self, arg_1, **kwargs):
        self.attribute_1 = arg_1
        # Don't do this 
        self.kwargs = None
        if kwargs:
            self.kwargs = kwargs

    def __repr__(self):
        args = '{args}'.format(args=self.attribute_1)
        if self.kwargs:
            args += ', ' + ', '.join(
                str(k) + '=' + str(v) for k, v in self.kwargs.items()
            )
        return '{class_name}({args}) at {address}'.format(
            class_name=self.__class__.__name__, args=args, address=hex(id(self))
        )
```
(The above is a bad way to deal with `kwargs`, but I can fix that later, as this gets the idea)