---
tags: help-wanted,idl/gdl-only
title: "SOBEL & clang : many complains; tests mising for SOBEL, PREWITT & ROBERTS"
html_url: "https://github.com/gnudatalanguage/gdl/issues/507"
user: alaingdl
repo: gnudatalanguage/gdl
---

as reported by @GillesDuvert , when compiled with clang, many warnings reported on SOBEL()

```
/Users/travis/build/gnudatalanguage/gdl/src/math_fun_ac.cpp:771:19: warning: taking the absolute value of unsigned type 'unsigned int' has no effect [-Wabsolute-value]

             a =   labs ((*p0)[j+1+nbX*(k+1)]+2*(*p0)[j+1+nbX*k]+(*p0)[j+1+nbX*(k-1)]

                   ^

/Users/travis/build/gnudatalanguage/gdl/src/math_fun_ac.cpp:810:9: note: in instantiation of function template specialization 'lib::Sobel_Template<Data_<SpDULong>, Data_<SpDULong>, long>' requested here

         return Sobel_Template<DULongGDL>(static_cast<DULongGDL*> (p0),a);

                ^
```
no tests in testsuite for SOBEL, PREWITT & ROBERTS
