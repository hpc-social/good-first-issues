---
tags: Hacktoberfest,bug,difficulty-medium
title: "BleiCorpus after serialize cannot be loaded"
html_url: "https://github.com/RaRe-Technologies/gensim/issues/1171"
user: vincentmajor
repo: RaRe-Technologies/gensim
---

Python version 2.7.12
gensim version 0.13.2

I'm serializing my corpus into Blei LDA-C format using `corpora.BleiCorpus.serialize(filename, corpus)` which is then later used in a dynamic topic model, and not in python. (I know I can use the DTMModel wrapper, unrelated.)

If I need to come back and load the corpus back into Python I tried `corpora.BleiCorpus.load(filename)`, I get an unpickling error:

     ---------------------------------------------------------------------------
     UnpicklingError                           Traceback (most recent call last)
    <ipython-input-28-0dd15393a941> in <module>()
    ----> 1 test = corpora.BleiCorpus.load('corpus-mult.dat')

    /Applications/anaconda/envs/py27/lib/python2.7/site-packages/gensim/utils.pyc in load(cls, fname, mmap)
        246         compress, subname = SaveLoad._adapt_by_suffix(fname)
        247 
    --> 248         obj = unpickle(fname)
        249         obj._load_specials(fname, mmap, compress, subname)
        250         return obj

    /Applications/anaconda/envs/py27/lib/python2.7/site-packages/gensim/utils.pyc in unpickle(fname)
        909     with smart_open(fname) as f:
        910         # Because of loading from S3 load can't be used (missing readline in smart_open)
    --> 911         return _pickle.loads(f.read())
        912 
        913 

    UnpicklingError: invalid load key, '7'.

The only other argument to `load()` is `mmap` but I don't believe the arrays were stored separately and using `mmap='r'` doesn't help anyway.