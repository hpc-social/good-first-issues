---
tags: ,bug,c++-only
title: "input conversion reading string (or files?) with windows-style line ends (\"\\r\\n\")"
html_url: "https://github.com/gnudatalanguage/gdl/issues/215"
user: slayoo
repo: gnudatalanguage/gdl
---

As reported by @davidh-ssec on SF.net (https://sourceforge.net/p/gnudatalanguage/bugs/651/):

```
IDL> data2 = fltarr(1,2)
IDL> s2 = '5 ' + string([13B, 10B]) + '5 ' + string([13B, 10B])
IDL> reads,s2,data2
IDL> print,data2
      5.00000
      5.00000
```

```
GDL> data2 = fltarr(1,2)
GDL> s2 = '5 ' + string([13B, 10B]) + '5 ' + string([13B, 10B])
GDL> reads,s2,data2
% Input conversion error.
GDL> print,data2
      5.00000
     -1.00000
```