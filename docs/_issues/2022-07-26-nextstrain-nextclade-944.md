---
tags: help-wanted,tfeat
title: "Filter for un-mutated bases"
html_url: "https://github.com/nextstrain/nextclade/issues/944"
user: emmahodcroft
repo: nextstrain/nextclade
---

It's very cool that one can use the filter to look for sequences which have a particular AA or nuc change, but it would also be cool to filter for sequences that _don't_ have the change - particularly useful if you have a bunch of sequences with the mutation and want to find the few exceptions.

For example, for mutation `S:K147E` one can use `S:147E` or `S:K147E` to find sequences with this mutation. It would be nice to be able to use `S:K147` or `S:147K` (or even `S:147`) to look for the un-mutated form.