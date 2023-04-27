---
tags: documentation,help-wanted
title: "Is azimuth to be specified from true or magnetic north?"
html_url: "https://github.com/pvlib/pvlib-python/issues/1593"
user: ertong
repo: pvlib/pvlib-python
---

I'm playing with FixedMount array model and trying to optimize tilt and azimuth. It should be a standard task  and the results should be predictable.

I expect to have the optimal azimuth to be 180, but receive 172.4 ... exactly the difference between true and magnetic pole in my location.

So it looks like, the library is designed for magnetic north ... but it looks like it is better to have true one.

Anyway, I could not find anywhere in the docs which north is used. 

In any case, I think, it should be explicitly stated and consistent throughout the library.