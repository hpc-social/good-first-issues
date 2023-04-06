---
tags: ,priority/nice-to-have,topic/query-builder,topic/testing
title: "Missing tests for some validation paths"
html_url: "https://github.com/aiidateam/aiida-core/issues/4931"
user: ramirezfranciscof
repo: aiidateam/aiida-core
---

As noticed in #4888, it appears that there are several validations that are performed in some parts of the `Querybuilder` but don't seem to be tested. It was also the case for some data plugins.

Let's use this issue to accumulate any other case we find; it would be a good idea to increase the coverage of these whenever possible.