---
tags: help-wanted,tbug
title: "Fix warnings in docs build"
html_url: "https://github.com/nextstrain/nextclade/issues/506"
user: ivan-aksamentov
repo: nextstrain/nextclade
---

Ths docs build produces a lot of warnings

When running
```
make docker-docs
```
here is a relevant part of the output:

```
checking consistency... /home/user/src/docs/README.md: WARNING: document isn't included in any toctree
/home/user/src/docs/dev/developers-guide-cli.md: WARNING: document isn't included in any toctree
/home/user/src/docs/dev/developers-guide-web.md: WARNING: document isn't included in any toctree
/home/user/src/docs/dev/setup-clion-debugging.md: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] user/terminology                                                                                                                                                                                                        
/home/user/src/docs/dev/developers-guide-cli.md:3: WARNING: None:any reference target not found: ../../docs/dev/developers-guide-web
/home/user/src/docs/dev/developers-guide-web.md:5: WARNING: None:any reference target not found: ../../docs/dev/developers-guide-cli
/home/user/src/docs/dev/developers-guide-web.md:15: WARNING: None:any reference target not found: ../../docs/dev/developers-guide-cli
/home/user/src/docs/dev/developers-guide-web.md:54: WARNING: None:any reference target not found: ../../docs/dev/developers-guide-cli
/home/user/src/docs/user/algorithm/01-sequence-alignment.md:5: WARNING: None:any reference target not found: nextclade-cli
/home/user/src/docs/user/algorithm/02-translation.md:5: WARNING: None:any reference target not found: nextclade-web
/home/user/src/docs/user/algorithm/02-translation.md:5: WARNING: None:any reference target not found: nextclade-web
/home/user/src/docs/user/algorithm/02-translation.md:5: WARNING: None:any reference target not found: nextclade-cli
/home/user/src/docs/user/algorithm/02-translation.md:5: WARNING: None:any reference target not found: nextalign-cli
/home/user/src/docs/user/algorithm/02-translation.md:5: WARNING: None:any reference target not found: nextclade-cli
/home/user/src/docs/user/algorithm/03-mutation-calling.md:5: WARNING: None:any reference target not found: nextclade-web
/home/user/src/docs/user/algorithm/03-mutation-calling.md:7: WARNING: None:any reference target not found: nextclade-web
/home/user/src/docs/user/algorithm/03-mutation-calling.md:11: WARNING: None:any reference target not found: nextclade-web
/home/user/src/docs/user/algorithm/03-mutation-calling.md:11: WARNING: None:any reference target not found: nextclade-cli
/home/user/src/docs/user/input-files.md:91: WARNING: Pygments lexer name 'tsv' is not known
/home/user/src/docs/user/input-files.md:123: WARNING: Pygments lexer name 'csv' is not known
/home/user/src/docs/user/nextalign-cli.md:163: WARNING: None:any reference target not found: algorithm
/home/user/src/docs/user/nextclade-cli.md:5: WARNING: None:any reference target not found: algorithm
/home/user/src/docs/user/nextclade-cli.md:179: WARNING: None:any reference target not found: algorithm
/home/user/src/docs/user/nextclade-web.md:156: WARNING: None:any reference target not found: algorithm
```


Some of these warnings because of the files in `docs/dev`, which are dev docs and should not be included. But no matter what I add to `exclude_patterns` it still complains. Current config is:

https://github.com/nextstrain/nextclade/blob/15daff812fbaa8aff54ca8b7b846fe0cacc90850/docs/conf.py#L47-L53

The renaming warnings might be because of broken links and this seems to be important.
