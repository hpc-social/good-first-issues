---
tags: ,Feature-Request,units
title: "Space between value and unit"
html_url: "https://github.com/astropy/astropy/issues/7455"
user: astrofrog
repo: astropy/astropy
---

Currently, ``Angle.to_string`` doesn't include a space between the value and unit:

```python
In [30]: from astropy.coordinates import Angle

In [31]: a = Angle(3, 'deg')

In [32]: a.to_string(unit='mas')
Out[32]: '1.08e+07mas'
```

I think there are cases where it would make sense to allow a space to be included, so this is a feature request to add a boolean keyword argument to optionally add a space.

Note that Quantity does include a space by default so maybe actually we should just change the default and not add an option?

```python
In [17]: str(3 * u.mas)
Out[17]: '3.0 mas'
```