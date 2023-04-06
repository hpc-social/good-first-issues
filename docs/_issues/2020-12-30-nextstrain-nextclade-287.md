---
tags: ,help-wanted,priohigh,tbug,tfeat
title: "Prevent tooltip content from going outside the screen"
html_url: "https://github.com/nextstrain/nextclade/issues/287"
user: ivan-aksamentov
repo: nextstrain/nextclade
---

In some cases, where there is a lot of data to display, and on smaller screens, tooltip go out of viewport bounds and are trimmed.

We want to improve the layout of tooltips such that all the information is always visible. And it all the information does not fit, we need to gracefully truncate the content (starting with the least important),  e.g. with ellipsis, or by removing sections.

![01](https://user-images.githubusercontent.com/9403403/103371392-9dbc9680-4acf-11eb-8090-c2861ec84d44.png)
![02](https://user-images.githubusercontent.com/9403403/103371397-a01ef080-4acf-11eb-89ff-3d1965905293.png)
