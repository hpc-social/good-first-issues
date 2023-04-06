---
tags: ,State-Machine,Testing,bug
title: "Make sure testing is covering entire state machine"
html_url: "https://github.com/panoptes/POCS/issues/645"
user: wtgee
repo: panoptes/POCS
---

During testing of POCS we are having errors in the states that the pocs instance is handling. Since the tests just look for conditions at startup and shutdown of pocs it fails to recognize that a test is not exercising the code completely. Mostly revealed through coverage tests.