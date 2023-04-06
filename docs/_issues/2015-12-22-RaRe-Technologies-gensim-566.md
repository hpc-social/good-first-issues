---
tags: Hacktoberfest,difficulty-easy,documentation
title: "Add API documentation for public class attributes"
html_url: "https://github.com/RaRe-Technologies/gensim/issues/566"
user: cscorley
repo: RaRe-Technologies/gensim
---

It would be better for API documentation if "public" class attributes, e.g. models.Doc2Vec.docvecs, were explicitly documented as part of the class with examples describing appropriate use. Hopefully, this would help mitigate questions such as [this one](https://groups.google.com/forum/#!topic/gensim/JRYhCt10AMw).

This could be achieved in a few ways with Sphinx:
1. Via `__init__` doc strings with [autoattribute](http://sphinx-doc.org/ext/autodoc.html#directive-autoattribute) ([example](http://stackoverflow.com/a/6061254))
2. Use Python properties
