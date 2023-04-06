---
tags: ,enhancement,help-wanted,question
title: "Using OAUTH2 to authenticate with ORCID"
html_url: "https://github.com/euroargodev/argopy/issues/243"
user: gmaze
repo: euroargodev/argopy
---

ORCID is used by the Argo community to populate netcdf files with operators information.
Ifremer is implementing access to the Argo-CTD reference database for DMQC by erddap with an ORCID authentification.
We therefore need to be able to authenticate users in argopy.

The expected API could look like this:

```python
import argopy
argopy.authenticate(service='orcid', user=USER, password=PASSWORD)
```
or simply:

```python
import argopy
argopy.authenticate()
```

After authentification, argopy will be able to send erddap requests with the user orcid id.
but I'm not sure this will be enough on the server side to determine user access right to the proected dataset.
