---
tags: enhancement
title: "Add windows command line support to aligner"
html_url: "https://github.com/Martinsos/edlib/issues/94"
user: randrick
repo: Martinsos/edlib
---

You can get aligner to work on windows command line by inserting the following lines into aligner.ccp
after line 8:  #include \<queue\>
---
#ifdef _WIN32
#include "getopt.h"
#endif
---
#include "edlib.h"

Then adding getopt.h file.  The one I used is here: https://raw.githubusercontent.com/skandhurkat/Getopt-for-Visual-Studio/master/getopt.h although that's likely not the origin of the file.
