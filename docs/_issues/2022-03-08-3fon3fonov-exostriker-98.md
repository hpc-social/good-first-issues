---
tags: external-package-problem,unclear
title: "qt.qpa.plugin: Could not load the Qt platform plugin \"xcb\" in \"\" even though it was found. (Ubuntu related?)"
html_url: "https://github.com/3fon3fonov/exostriker/issues/98"
user: 3fon3fonov
repo: 3fon3fonov/exostriker
---

I have seen this "bug" in Linux/Ubuntu machines, but is probably not limited to Ubuntu.


```
$ python3.8 exostriker_gui.py

qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even
though it was found.
This application failed to start because no Qt platform plugin could be
initialized. Reinstalling the application may fix this problem.

Available platform plugins are: eglfs, linuxfb, minimal, minimalegl,
offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl,
wayland-xcomposite-glx, webgl, xcb.
```

The fix was found on the internet, but I have not spent much time to understand the problem. 


`sudo apt install libxkbcommon-x11-0`

or

`sudo apt install libxcb-xinerama0`

Obviously, there is some missing X11 libraries in some Ubuntu installs.





