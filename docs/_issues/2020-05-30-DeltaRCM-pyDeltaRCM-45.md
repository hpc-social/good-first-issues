---
tags: ,enhancement
title: "Implement \"rich\" output in console and logging"
html_url: "https://github.com/DeltaRCM/pyDeltaRCM/issues/45"
user: amoodie
repo: DeltaRCM/pyDeltaRCM
---

There is currently a "logger" implemented all over the code, which I guess spits out to a txt file. It would be a good two-for-one to implement the `rich` console logger ([link here](https://github.com/willmcgugan/rich#console-logging)), to write to console and to file every time the logger is called in the current code. We should also log to file every time we raise a warning.

Currently, we sometimes print things to console, sometimes log things to file, sometimes warn things, and sometimes a combination of the three. We should make this consistent based on the `verbose` flag. relates to #40 