---
tags: ,help-wanted,package-nextclade_web,tfeat
title: "Warn users about about incompatibility with adblockers and Brave browser"
html_url: "https://github.com/nextstrain/nextclade/issues/439"
user: ivan-aksamentov
repo: nextstrain/nextclade
---

We had issues with adblocker browser extensions and Brave browser breaking Nextclade. Privacy protection features don't treat Nextclade's client-side computation model well.

Nextclade performs a lot of calculations in the browser, and uses WebWorkers and WebAssembly, the technologies that adblockers don't like. They may break features and make Nextclade to consume more memory.

I was not able to start analysis in Brave on Android - it crashes with out of memory error.
Also related: https://github.com/nextstrain/nextclade/issues/438

Perhaps we can warn Brave users that their browser is not supported and to recommend them to use a Chromium-based browser or Firefox.

We could detect Brave using [this API](https://github.com/nextstrain/nextclade/issues/438) and display a reactstrap alert or a popup dialog. Detecting adblockers though is harder and, as they are built to specifically avoid detction.

Popups should not interfere with "What's new" dialog.

Also, this might be controversial, as Nextclade is built with privacy in mind. We don't track users or send data to a server (we don't have any server). So using browser and adblocker detection (basically fingerprinting) goes somewhat against this idea.
