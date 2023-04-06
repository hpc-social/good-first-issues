---
tags: ,enhancement,stale
title: "Longer cache expiration delay in options"
html_url: "https://github.com/euroargodev/argopy/issues/196"
user: gmaze
repo: euroargodev/argopy
---

Argopy uses a refresh rate for cache of 1 day, since this is the update frequency of the Ifremer erddap and GDAC ftp.
But some users may not need the most recent data, or simply a longer latency in data refresh rate.

So would it be possible to add an option to control the cache expiration delay? 

#### Example

```python
argopy.set_options(cache_expiration=86400*10)
```
