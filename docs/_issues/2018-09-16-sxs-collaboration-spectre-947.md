---
tags: ,enhancement
title: "Use MakeString to instead of stringstream where possible"
html_url: "https://github.com/sxs-collaboration/spectre/issues/947"
user: nilsdeppe
repo: sxs-collaboration/spectre
---

# Feature Request:

I'm adding a PR for a `MakeString` class that will allow `const std::string t = MakeString{} << blah;`. We can use this to replace the old-style `std::stringstream ss; ss << blah; const std::string t = ss.str();` throughout the code.
