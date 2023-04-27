---
tags: feature,help-wanted
title: "Allow data w missing modalities upon request"
html_url: "https://github.com/ivadomed/ivadomed/issues/809"
user: charleygros
repo: ivadomed/ivadomed
---

We have implemented this [input-level dropout](https://github.com/ivadomed/ivadomed/pull/705), which simulates missing modalities.

Some datasets already have missing modalities, so no real need to trigger it, eg [here](https://github.com/ivadomed/ivadomed/issues/808#issuecomment-848856451).

It would be great to allow missing modalities, upon request in the config file, eg by applying the same strategy than the "input level dropout" appraoch.

This feature could also be used for testing the "input level dropout" on real datasets.