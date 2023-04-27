---
tags: enhancement,help-wanted
title: "cache files should be aware of EXOSIMS version"
html_url: "https://github.com/dsavransky/EXOSIMS/issues/215"
user: dsavransky
repo: dsavransky/EXOSIMS
---

Currently, cache files are completely EXOSIMS version agnostic, which could lead to things breaking when trying to reuse old cached products with newer versions.

EXOSISM should do a better job of keeping track of its code version.  I would like to generalize the logic currently in genOutSpec (gitRev) to do the following:
-If the code is from a github repository, return the commit string.  We could (probably should?) also check on uncommitted changes in key code (so, anything in EXOSIMS/EXOSIMS/*/*.py, excluding utils, maybe?) and modify the string accordingly. 
-If the code is not from a github repo, then there should be a global version reported (we should really have a global setup.py to track this).  
