---
tags: ,Docs
title: "DOC: Simplify pandas theme footer"
html_url: "https://github.com/pandas-dev/pandas/issues/51536"
user: datapythonista
repo: pandas-dev/pandas
---

The sphinx theme that we're using didn't let us specify what exactly to show in our footer in the configuration file. So, what we did was to create a custom template to overwrite everything. Seems like now they [changed](https://github.com/pydata/pydata-sphinx-theme/pull/1184) this in their end, and we should be able to implement in our end the footer we want without requiring the extra template. I didn't check in detail, so some research is needed to see if this is really possible.

Their changes haven't been released yet, so we can't really get this into production until they do. But we can get the PR ready by temporary changing the pydata-sphinx-theme dependency to the git version.