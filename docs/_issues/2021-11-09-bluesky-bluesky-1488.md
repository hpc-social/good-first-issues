---
tags: ,maintenance
title: "consolidate the describe / config caches in RunBundler"
html_url: "https://github.com/bluesky/bluesky/issues/1488"
user: tacaswell
repo: bluesky/bluesky
---

<!--- Provide a general summary of the issue in the Title above -->

While debugging #1487 I noticed that we have 4 caches that we always update in parallel (describe, and describe, values, ts for configuration).  
## Expected Behavior

No behavior changes.

## Current Behavior
<!--- If describing a bug, tell us what happens instead of the expected behavior -->
<!--- If suggesting a change/improvement, explain the difference from current behavior -->

High risk of latent or future bugs due to the 4 caches getting out of sync.

## Possible Solution
<!--- Not obligatory, but suggest a fix/reason for the bug, -->
<!--- or ideas how to implement the addition or change -->

Rather than tracking these as 4 dictionaries that we manually keep in sync, we should refactor this to be 1 dictionary with something structured (DataClass, SimpleNamespace, namedtuple, dict?) inside.  That way we can be sure if we need to invalidate one of them we can be sure we will invalidate all of them.

## Good first issue

This is good first issue to get into the guts of the RE/Bundler code.  It will involve reading and understanding the Bundler code, but should involve no behavior or API changes (and probably no new tests, assuming that more latent errors are not found ;) ) . 
