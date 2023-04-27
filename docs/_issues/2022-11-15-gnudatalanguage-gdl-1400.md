---
tags: Low-priority,enhancement
title: "help,/files does not show open files"
html_url: "https://github.com/gnudatalanguage/gdl/issues/1400"
user: brandy125
repo: gnudatalanguage/gdl
---

Why the user luns are not shown?

```
bash$ touch eraseme
bash$ idl
IDL> openr,1,'eraseme'
IDL> help,/files
Unit   Attributes                              Name
1      Read                                  eraseme
IDL> exit
bash$ gdl
GDL> openr,1,'eraseme'
GDL> help,/files
 maxUserLun : 99 fileUnits.size() : 128
GDL>
```