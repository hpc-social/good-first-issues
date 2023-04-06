---
tags: ,enhancement
title: "Negative weights for KDE"
html_url: "https://github.com/lzkelley/kalepy/issues/16"
user: Pablobala
repo: lzkelley/kalepy
---

I wanted to use the kalepy package on a SWeighted distribution, so there are many events with negative weights and I can't normalize them as the distribution would change. There is a ValueError in kalepy/kde.py, line 214: "Invalid `weights` entries, all must be finite and > 0!".
I would want to know if there is the possibility to adapt the code to run with negative weights or if the method just not allow the use of negative weights for some reason. Could someone clarify this to me?

Thanks in advance and Kind Regards.