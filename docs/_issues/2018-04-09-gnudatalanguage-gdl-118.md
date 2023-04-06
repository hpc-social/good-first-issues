---
tags: ,help-wanted
title: "Testsuite change from procedures to functions"
html_url: "https://github.com/gnudatalanguage/gdl/issues/118"
user: slayoo
repo: gnudatalanguage/gdl
---

As reported by @olebole on SF.net (https://sourceforge.net/p/gnudatalanguage/feature-requests/143/):

Currently, the test suite consists of procedures that do an exit, status=1 in case of failure. This has the drawback than one cannot run all of them in one go. For me, this would be important since I would like to call them as Python unit test cases (build test when creating a Debian Python GDL package, and CI unit test).

It would be nice if they could all be converted to functions that return zero on success and non-zero on failure.