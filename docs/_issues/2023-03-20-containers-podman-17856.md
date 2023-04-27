---
tags: Good-First-Issue,kind/feature
title: "allow to set loglevel for healthcheck"
html_url: "https://github.com/containers/podman/issues/17856"
user: nolange
repo: containers/podman
---

### Feature request description

Currently our server logs are mostly full of healthcheck output, making them hard to navigate.

### Suggest potential solution

I would want the healthcheck service to run with `LogLevelMax=notice`, this would remove the normal output, inclusive the started/stopped messages from systemd itself.

I believe this should be the default, but there could be an option for `podman run` to override the loglevel for healtchecks.

### Have you considered any alternatives?

Filtering the log, but this is cumbersome.

### Additional context

_No response_