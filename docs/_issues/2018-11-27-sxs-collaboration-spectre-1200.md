---
tags: enhancement
title: "Use Coordinates tag to get rid of template parameters in Domain tags"
html_url: "https://github.com/sxs-collaboration/spectre/issues/1200"
user: nilsvu
repo: sxs-collaboration/spectre
---

# Feature request:

I think we can remove the `SourceCoordsTag` of `Tags::MappedCoordinates` and `Tags::InverseJacobian` now that we have the `Tags::Coordinates`. For instance, we could replace `SourceCoordsTag` with `Tags::Coordinates<MapTag::type::dim, MapTag::type::source_frame>` in both of these tags.

This will touch a significant number of files, so I bring this up as an issue.

### Component:

- [x] Code
