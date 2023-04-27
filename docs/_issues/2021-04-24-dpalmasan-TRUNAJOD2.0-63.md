---
tags: usability
title: "Implement universal POS tags ratio"
html_url: "https://github.com/dpalmasan/TRUNAJOD2.0/issues/63"
user: dpalmasan
repo: dpalmasan/TRUNAJOD2.0
---

SpaCy tokens can contain universal POS tags and detailed POS tags, both properties in a spacy `Token` are `pos_` and `tag_` respectively. Currently, the function `pos_ratio` is kind of misleading as in the docstring it is describing `pos_` tags, but computing ratio using `tag_`. This ticket is to fix this and implement a similar function using universal POS tags.


https://github.com/dpalmasan/TRUNAJOD2.0/blob/master/src/TRUNAJOD/surface_proxies.py#L515

**Acceptance Criteria**

- Docstring is updated properly
- Functionality to compute `pos_ratio` based on universal POS tag is added.