---
tags: ,priority
title: "add test to determine if WoERatioCategoricalEncoder returns an error when the probability in the denominator is 0"
html_url: "https://github.com/feature-engine/feature_engine/issues/56"
user: solegalli
repo: feature-engine/feature_engine
---

At the moment the test is commented out:
https://github.com/solegalli/feature_engine/blob/master/tests/test_encoding/test_woe_encoder.py#L112

the aim is to test this bit of code [here](https://github.com/solegalli/feature_engine/blob/master/feature_engine/encoding/woe.py#L205)

I think the test should work, and I commented out because I changed the error for a warning. But now, we decided to go back to returning an error.

So in short, the aim is to corroborate that the commented out test checks the intended bit of code and if yes, uncomment it, otherwise, replace it by the suitable test.
