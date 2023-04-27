---
tags: Difficulty-Medium,Documentation-build,Good-first-issue
title: "[MNT]: Specify ordering in file in gallery folder"
html_url: "https://github.com/matplotlib/matplotlib/issues/25032"
user: story645
repo: matplotlib/matplotlib
---

> Since we wrote this extension to do the ordering, there's no reason we can't change it to read from `README.txt` in each directory. We could have it look for something that _looks_ like a comment to reST so it does nothing in the sphinx-gallery-processed reST without having to do anything extra.
_Originally posted by @QuLogic in https://github.com/matplotlib/matplotlib/issues/24746#issuecomment-1396482343_

I think it's a relatively good first issue following #25028 because each readme can be parsed into its respective gallery list. Steps involved are 
1. figure out the reST comment notation that allows for easy specification of ordering + a consistent sentinel for placing unsorted files
2. write a parser that translates the set of comments into a list that preserves the order (including sentinel)
3. parse each file into its respective list in https://github.com/matplotlib/matplotlib/blob/be7ea76c49f19ce48958de82a82b3951d9b7f0d2/doc/sphinxext/gallery_order.py#L48
4. add documentation on doing this ordering to https://github.com/matplotlib/matplotlib/blob/main/doc/devel/documenting_mpl.rst?plain=1#L933

Medium difficulty because some familiarity with sphinx would be helpful, but not strictly necessary. I think a medium to advanced version of this would be implementing a `.. gallery-toc` [custom directive](https://www.sphinx-doc.org/en/master/development/tutorials/index.html#extension-tutorials-index)

 And yes, down the line we should maybe spin a maintain docs page off from the writing docs page. 

An alternative to using the readme is using a special purpose 'gallery_order' file https://github.com/matplotlib/matplotlib/issues/24746#issuecomment-1399116931
            