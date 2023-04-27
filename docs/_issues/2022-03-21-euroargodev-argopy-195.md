---
tags: internals,question,stale
title: "Upstream requirements management and policy"
html_url: "https://github.com/euroargodev/argopy/issues/195"
user: gmaze
repo: euroargodev/argopy
---

Since the beginning of argopy, we've kind of struggle to manage how the library interacts with its dependencies

**We need a proper mechanism, and policy ?, to handle support for a range of dependency versions**

New versions for xarray and fsspec are released every month. We've set-up [CI tests with conda env. using latest versions](https://github.com/euroargodev/argopy/actions/workflows/pytests-free.yml) so that breaking changes should be detected using deprecation warnings. 
**Would it be possible to automatically in GA collect and create an issue with future deprecation warnings, so that we can't miss them ?**

But at this point, **we don't know when we'll lost support for old versions.** I've created an [env file with minimal versions](https://github.com/euroargodev/argopy/blob/master/ci/requirements/py3.8-min-dep.yml) but CI tests are still missing.

Also, we're using a few modules just for 1 or 2 functions. For instance:
- erddapy is used as a URL formatter, not for requests
- scikit-learn is used only for preprocessing.LabelEncoder()
- packaging is used only to parse and compare other dependencies versions (and keep argopy working)
- and I think that dask is never imported !

I see some **contradictions** here between having as fewer as possible dependencies and yet simply use what's best and available out there in the community (and should be acknowledged for it)

