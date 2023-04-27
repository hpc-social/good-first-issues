---
tags: help-wanted,tfeat
title: "Variable column width"
html_url: "https://github.com/nextstrain/nextclade/issues/112"
user: ivan-aksamentov
repo: nextstrain/nextclade
---

It would be nice to be able to change the width of particular columns. This would allow for example, to increase or decrease the size of the sequence name column, depending on a given naming convention and length of those names.

 - [ ] At first we may simply add it as an option in the settings dialog. 
 - [ ] Ideally, to make left and right borders of cells draggable, similar to how it's implemented in Excel and other spreadsheets. This might be tricky due to table virtualization (`react-window`).

We may go even further and to allow changing with of the entire table. This would require some tweaking of the page container styling and thorough testing across device sizes.
