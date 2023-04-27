---
tags: enhancement
title: "reimplement MEMORY (at least for 64-bit Linux) using wait() calls"
html_url: "https://github.com/gnudatalanguage/gdl/issues/206"
user: slayoo
repo: gnudatalanguage/gdl
---

As reported on SF.net (https://sourceforge.net/p/gnudatalanguage/bugs/522/):

- in OSX, SunOS and with 32bits Linux, we know how to monitor the RAM usage and freeing, but it doesn't seem to work reliably on 64-bit Linuces
- the GNU time utility is able to measure the memory usage by making use of the information available via wait() calls - perhaps it could be used to implement it. Here's the source: http://ftp.de.debian.org/debian/pool/main/t/time/time_1.7-24.debian.tar.gz