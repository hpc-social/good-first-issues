---
tags: ,enhancement
title: "EXECUTE: support for the third argument (quiet execution)"
html_url: "https://github.com/gnudatalanguage/gdl/issues/83"
user: slayoo
repo: gnudatalanguage/gdl
---

As reported on SF.net: https://sourceforge.net/p/gnudatalanguage/feature-requests/80/

```
IDL> $cat ex3.pro
pro ex3sub
nonexistent
end
pro ex3, arg3
a = execute('ex3sub', 1, arg3)
end
IDL> ex3, 0
% Attempt to call undefined procedure/function: 'NONEXISTENT'.
IDL> ex3, 1
IDL> 
```