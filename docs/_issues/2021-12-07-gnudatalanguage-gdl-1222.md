---
tags: ,Low-priority,cleanup
title: "cleanup switch in hdf5_fun.cpp"
html_url: "https://github.com/gnudatalanguage/gdl/issues/1222"
user: alaingdl
repo: gnudatalanguage/gdl
---

Hi. Not urgent, not critical ... Could someone (@ogressel  ?) takes the time to help Clang on that : 

```
[ 16%] Building CXX object src/CMakeFiles/gdl.dir/hdf5_fun.cpp.o
/Users/alaingdl/GDL/last-gdl/src/hdf5_fun.cpp:407:13: warning: 16 enumeration values not handled in switch: 'H5I_UNINIT', 'H5I_BADID', 'H5I_FILE'... [-Wswitch]
    switch( H5Iget_type(loc_id) ) {
            ^
/Users/alaingdl/GDL/last-gdl/src/hdf5_fun.cpp:407:13: note: add missing switch cases
    switch( H5Iget_type(loc_id) ) {
            ^
1 warning generated.

```

Thanks !

A.