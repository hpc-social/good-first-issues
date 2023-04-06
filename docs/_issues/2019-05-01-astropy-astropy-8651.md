---
tags: ,Docs,Hacktoberfest,Package-novice
title: "Add version changed for API changes"
html_url: "https://github.com/astropy/astropy/issues/8651"
user: taldcroft
repo: astropy/astropy
---

I find it useful (as done in e.g. numpy) to have the version when things changed or were added in the narrative / API docs. E.g. in relevant places we would see a comment like "Default time scale for epoch times like J2000 changed from UTC to TT in version 3.2". The point being that the change log is not where most people wind up when learning about a function or method.

@mhvk points out this is done with a sphinx directive `.. versionchanged:` in numpy.  Is that something astropy could just start using as a matter of policy?

(This was a by-product of discussion in #8600).

EDIT by @pllim and @bsipocz : Preferably, this is to be done in small batches, like one PR for a single version release for a single subpackage. And only as far as as 2.0 and not earlier.