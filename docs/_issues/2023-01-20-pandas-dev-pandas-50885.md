---
tags: ,Web
title: "WEB: Better management of releases in the pandas home page"
html_url: "https://github.com/pandas-dev/pandas/issues/50885"
user: datapythonista
repo: pandas-dev/pandas
---

In the [pandas home page](https://pandas.pydata.org/) we show the released versions, both in the `Latest version` box, and the `Previous versions` list.

Obtaining the releases is done [here](https://github.com/pandas-dev/pandas/blob/main/web/pandas_web.py#L206). So far, the function is pretty simple, just sorting the releases by date, and assuming the last one by date it's the latest.

While this makes sense, we're planning to release 2.0 shortly, and it's likely that we release 1.5.4 after it. With the current implementation and after those releases, we'd list 1.5.4 as the latest release, which is not great since we expect users to use 2.0, which is not the latest by date, but the newest in terms of features.

The idea is to improve the current implementation to be smarter, and not use the date, but use the version number. This can be done with [version.parse](https://packaging.pypa.io/en/latest/version.html#packaging.version.parse).

Since we are implementing this, I think besides detecting the latest version, it can make sense to also filter obsolete versions from the long list of releases. For example, 1.5.3 is the same version as 1.5.2, 1.5.1 and 1.5.0 but with bugs fixed. There is no reason a user would want to install any 1.5 version except the last one. 1.4.4 is a reasonable version, since users may have code using that version that they didn't migrate yet to be compatible with 1.5. But 1.4.3, 1.4.2, 1.4.1 and 1.4.0 shouldn't be used, so probably better to not have them in the list.

I don't think we have any tests for the script that generates the website. But since the new implementation is not trivial, it'd be good to have it tested. Maybe just a `tests/test_pandas_web.py` in the same directory as the script, and calling pytest on that directory in the documentation build is the best option.