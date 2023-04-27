---
tags: CI,enhancement,ergonomics,help-wanted,needs-discussion,priority/low,question,security,suggestions
title: "Use more helpful package tools"
html_url: "https://github.com/Materials-Consortia/optimade-python-tools/issues/950"
user: CasperWA
repo: Materials-Consortia/optimade-python-tools
---

In the [OPTIMADE Gateway](https://github.com/Materials-Consortia/optimade-gateway) I've started using more package tools to cover issues that may occur with regards to security, static typing and linting.

I've essentially implemented CI and pre-commit hooks for `bandit`, `safety`, `pylint`, and `mypy`, along with keeping `black` and removing `flake8`.

These tools try to ensure we don't implement exploitable holes in the server, as well as make sure the types we write for parameters match up with what is used. `safety` also checks known vulnerability issues for our dependencies.

Furthermore, as is seen in the [FastAPI repository](https://github.com/tiangolo/fastapi/blob/master/pyproject.toml) itself, we can combine a lot of repo config and setup files into `pyproject.toml`, and only use that one file; nice! :)

Essentially, this issue represents a "clean up" of the repository, to keep ourselves in check, try to get better development and PRs, as well as ensure we provide a good and safe package for end-users.