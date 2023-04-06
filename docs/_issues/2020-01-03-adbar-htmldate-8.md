---
tags: ,up-for-grabs
title: "Test htmldate on further web pages and report bugs"
html_url: "https://github.com/adbar/htmldate/issues/8"
user: adbar
repo: adbar/htmldate
---

I have mostly tested `htmldate` on a set of  English, German and French web pages I had run into by surfing or during web crawls. There are definitely further web pages and cases in other languages for which the extraction of a date doesn't work so far.

Please install the `dateparser` library beforehand as it significantly extends linguistic coverage: `pip`or `pip3 install -U dateparser` or `pip install -U htmldate[all]`.

Corresponding bug reports can either be filed as a list in an issue like this one or in the code as XPath expressions in [core.py](https://github.com/adbar/htmldate/blob/master/htmldate/core.py#L48) (see `DATE_EXPRESSIONS` and `ADDITIONAL_EXPRESSIONS`).

Thanks!