---
tags: help-wanted,tfeat
title: "Add progress indicators for URL-based fetching"
html_url: "https://github.com/nextstrain/nextclade/issues/270"
user: ivan-aksamentov
repo: nextstrain/nextclade
---

Users can provide remotely hosted data through URL parameters (see #203, #247) and fetching this data currently happens during the app initialization, before the App component first renders. This means that all users can see during fetching is the generic loading spinner. This spinner might be shown for an extended period of time, depending on data size and connection speed. This is not a great user experience.

Instead, when navigation to a URL with data parameters occurs, we might want to acknowledge the fact that the app has received and understood these these parameters, and that fetching have started, to inform user better about what's happening in background and prompt them to wait.

Even better, we might show the progress indicators for each file being fetched.


A possible implementation would need to move the URL processing and data fetching to some time after initialization. Of course, all that should happen asynchronously. We mostly use redux-saga for async effects, so a new saga or a few seems to be the most suitable here.
