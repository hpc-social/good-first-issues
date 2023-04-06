---
tags: ,Docs
title: "DOC: better explain the automatic alignment process"
html_url: "https://github.com/pandas-dev/pandas/issues/49939"
user: MarcoGorelli
repo: pandas-dev/pandas
---

### Pandas version checks

- [X] I have checked that the issue still exists on the latest versions of the docs on `main` [here](https://pandas.pydata.org/docs/dev/)


### Location of the documentation

Throughtout https://pandas.pydata.org/pandas-docs/stable/index.html

### Documentation problem

> I'd like to mention documentation again, for emphasis.  A someone who found the automatic data alignment 'confusing', I think I offer a unique perspective to this problem (at least on this thread).  For example, I'm currently dealing with numpy shape.  When looking at the documentation for np.shape it would have been helpful if it simply mentioned that it was row X columns when I looked np.shape rather the just "array dimensions" (same amount of characters!).  Smirk, if you wish, but these minor details here and there repeated can go along way to helping folks new to these frameworks out.
> 

Originally reported by @blazespinnaker [here](https://github.com/pandas-dev/pandas/pull/49694#issuecomment-1328701631)

### Suggested fix for documentation

> For this problem, a quick note in different operations such as sum could say 
> 
> `
> *Note automatic data alignment:  as with all pandas operations, automatic data alignment is performed.  If sum does not find values with matching indicies than NaN will used as the total.   
> `
> 
> An example would even be even more awesome.
> 
> 
> Note that my text is probably very poor, but ideally it would be written in a way to make alignment less confusing to new users.
> 
> 

Originally reported by @blazespinnaker [here](https://github.com/pandas-dev/pandas/pull/49694#issuecomment-1328701631)