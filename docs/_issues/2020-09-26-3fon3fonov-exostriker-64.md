---
tags: ,bug,external-package-problem,help-wanted
title: "The X11 connection broke (error 1). Did the X11 server die?"
html_url: "https://github.com/3fon3fonov/exostriker/issues/64"
user: 3fon3fonov
repo: 3fon3fonov/exostriker
---

This is one very serious bug, which I am trying to solve for some time. 

It appears when a locally saved session is exported to cluster/server for MCMC/NS run using many CPUs. 

The session loads on the local machine and on the server with no problem. When the MCMC/NS is done the new saved session with the samples is exported via e.g. scp/rsync and most of the time works fine. However, somewhat randomly, some output sessions with MCMC/NS cannot be opened anymore.

At import at the GUI am getting:

The X11 connection broke (error 1). Did the X11 server die?


Any help with this will be highly appreciated!

