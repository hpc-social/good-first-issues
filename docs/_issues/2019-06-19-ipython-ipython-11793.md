---
title: "lsmagic returns JSON which makes for awkward UX in JupyterLab"
html_url: "https://github.com/ipython/ipython/issues/11793"
user: fperez
repo: ipython/ipython
---

I'm not sure why `lsmagic` needs to return a JSON data structure by default - but the end result is that in JupyterLab, it becomes kind of useless... In Classic calling `%lsmagic` produces (clipped for simplicity):

![image](https://user-images.githubusercontent.com/57394/59727806-1dd02380-91ec-11e9-92a7-9f5a367763f5.png)

while in Lab, this is the output:

![image](https://user-images.githubusercontent.com/57394/59727824-35a7a780-91ec-11e9-992c-3a361f52b5fe.png)

Lab defaults to showing JSON reprs when available, which typically makes sense, so while this is a change in behavior re. Classic, I'm inclined to think it's a good step forward.

Users can get the text via

![image](https://user-images.githubusercontent.com/57394/59727854-5e2fa180-91ec-11e9-90c0-5340eb2f1f92.png)

but that's  a pretty awkward experience.  Do we really need `lsmagic` to produce JSON by default? It seems to me that generating plain text would be fine most of the time, perhaps with a `--json/-j` option for JSON output when desired?