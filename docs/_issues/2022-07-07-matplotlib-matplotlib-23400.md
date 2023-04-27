---
tags: Good-first-issue
title: "Only upload failed images on failure"
html_url: "https://github.com/matplotlib/matplotlib/issues/23400"
user: tacaswell
repo: matplotlib/matplotlib
---

Currently when a job fails on GHA we upload all 109 MB across ~7k files which takes a surprisingly long time.  What we really want is just the images that failed and the computed difference.

This is labeled as "good first issue" because there are no API designs here (it is all configuring CI).

Steps:

 - sort out how to identify the failed test images (there is a systematic naming convention)
 -  explain that to the uploader workflow (or just delete all of the non-failed fails!)
