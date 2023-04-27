---
tags: help-wanted,tbug
title: "docs: broken image links on QC page"
html_url: "https://github.com/nextstrain/nextclade/issues/772"
user: victorlin
repo: nextstrain/nextclade
---

Example: https://docs.nextstrain.org/projects/nextclade/en/stable/user/algorithm/07-quality-control.html

https://github.com/nextstrain/nextclade/blob/ccf2a0429e239e29a20dd4da1148b908ed2d8515/docs/user/algorithm/07-quality-control.md?plain=1#L51

gets rendered as:

```html
<img alt="Identification of private mutations" src="/docs/user/assets/algo_private-muts.png">
```

and the absolute path is not valid in the context of docs.nextstrain.org/projects/nextclade.

<img width="500" alt="image" src="https://user-images.githubusercontent.com/13424970/165821143-1008337e-d052-4cec-8990-2914e75b8563.png">

---

However, this [Nextclade Web](https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-web.html) image

https://github.com/nextstrain/nextclade/blob/ccf2a0429e239e29a20dd4da1148b908ed2d8515/docs/user/nextclade-web.md?plain=1#L21

gets rendered with a different relative path which is fine:

```html
<img alt="Select virus" src="../_images/web_select-virus.png">
```

Any idea why one works but the other doesn't?