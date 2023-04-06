---
tags: Enhancement,Good-first-issue,RPC
title: "NaN returned during exchange maintenance  "
html_url: "https://github.com/freqtrade/freqtrade/issues/3221"
user: sanket-k
repo: freqtrade/freqtrade
---

## Step 1: Have you search for this issue before posting it?
yes

If you have discovered a bug in the bot, please [search our issue tracker](https://github.com/freqtrade/freqtrade/issues?q=is%3Aissue). 
If it hasn't been reported, please create a new issue.

## Step 2: Describe your environment
  * platform: Docker - latest build(Digest:sha256:3e8fe20bf6aaad9095e1ba0924ce2af3368cc55d1fe41eebb546a73a124fb77f) 
  * Operating system: ____
  * Python Version: _____ (`python -V`)
  * CCXT version: _____ (`pip freeze | grep ccxt`)
  * Branch: Master | Develop
  * Last Commit ID: _____ (`git log --format="%H" -n 1`)
   
  
## Step 3: Describe the problem:
the exchange binance was under maintenance from 2020/04/25 02:00 AM (UTC)  - 06:00 (UTC) - https://binance.zendesk.com/hc/en-us/articles/360042668671-Binance-System-Upgrade-Notice-2020-04-25-

observed that the bot returned nan% for profit in /status, and the /performance field was empty.
![image](https://user-images.githubusercontent.com/23406725/80302240-7e45cf00-87c6-11ea-98f6-4a7d73da96d5.png)

note:  Also in the earlier builds this response wasn't present.

If the exchange is down could we return the exchange is under maintenance rather than nan, or previous values??


