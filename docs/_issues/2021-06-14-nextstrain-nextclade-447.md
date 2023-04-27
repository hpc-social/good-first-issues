---
tags: help-wanted,tfeat
title: "Warn users about memory consumption when they try to run on huge datasets"
html_url: "https://github.com/nextstrain/nextclade/issues/447"
user: ivan-aksamentov
repo: nextstrain/nextclade
---

We might want to give users a hint that Nextclade requires a lot of memory in case there are many sequences. 

We can simply take fasta files size and upon some threshold to show a reactstrap alert informing users about that fact and recommend them splitting their datasets in multiple chunks as well as common memory-freeing steps.

It is essential to explain that all computation is happening on their computer. Which is perhaps not intuitive, because users are not accustomed for web apps that do so.


Optionally, we might also correlate this with the amount of memory available, but this is not easy to detect and might be considered intrusive.
