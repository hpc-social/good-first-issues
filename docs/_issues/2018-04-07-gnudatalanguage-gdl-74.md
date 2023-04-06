---
tags: 
title: "using gnulib instead of some compatibility hacks "
html_url: "https://github.com/gnudatalanguage/gdl/issues/74"
user: slayoo
repo: gnudatalanguage/gdl
---

As reported on SF.net (https://sourceforge.net/p/gnudatalanguage/feature-requests/112/):

gnulib (https://www.gnu.org/software/gnulib/manual/gnulib.html) should provide us with a more elegant alternative for such hacks as:

```
datatypes.hpp:
// isfinite & isinf for Solaris
#if defined(__sun__)
# include <ieeefp.h>
# define isfinite finite
# ifndef isinf
# define isinf(x) (!finite(x) && x==x)
# endif
#endif
```

See also https://github.com/gnudatalanguage/gdl/issues/17