---
tags: Docs,Indexing
title: "DOC: Reindexing behaviour of dataframe column-assignment missing"
html_url: "https://github.com/pandas-dev/pandas/issues/39845"
user: fish-face
repo: pandas-dev/pandas
---

#### Location of the documentation

`pandas.core.indexing.IndexingMixin.loc`
`pandas.DataFrame.__setitem__`

#### Documentation problem

When assigning a `Series` through `df[...] = ...` or `df.loc[...] = `, the `Series`' index is expanded to conform to the `DataFrame`'s, and then values are added according to the index:

```python3
In [1]: df
Out[1]: 
   a
0  1
1  2
2  3

In [2]: df['b'] = pd.Series({1: 'b'})
In [3]: df
Out[3]: 
   a    b
0  1  NaN
1  2    b
2  3  NaN

In [4]: se = pd.Series({2: 'zero', 1: 'one', 0: 'two'})      
# NOTE: Order is preserved and reflected in the Series' order
In [5]: se
Out[5]: 
2    zero
1     one
0     two
dtype: object
In [6]: df['d'] = se
# NOTE: values have been reordered according to the df's index
In [7]: df
Out[8]: 
   a    b    d
0  1  NaN  two
1  2    b  one
2  3  NaN zero
```
(But in contrast:
```python3
In [4]: df['c'] = {1: 'c'} 
<traceback omitted>
ValueError: Length of values (1) does not match length of index (3)
```
)

As far as I can tell, this is not really documented. In the case of `__setitem__` there is *no* API documentation at all, and one is left only with the "Selecting and Indexing Data" guide's examples. In the case of `.loc` there is mention that if using a `Series` as *input*, "The index of the key will be aligned before masking," but this is not what we're doing here. Neither set of examples indicates the behaviour when adding a new column or part of column: the only hints I could find in the guide about [setting with enlargement](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#setting-with-enlargement) added a series whose index was the same as the existing index. This means that it is not clear what order the data will end up in the dataframe and where `NaN`s will be added.

In the case of `.loc` in general the API documentation, although it does exist, is fairly scant. There is a link to the user guide, but personally I think this is pretty important behaviour to document in the reference.

#### Suggested fix for documentation

* Add documentation for `__setitem__` and in particular the behaviour of reindexing `Series`.
* Update documentation for `.loc` to more completely describe the behaviour obtained when *assigning* to `.loc[]`, and include at least one example of assigning to a partial column. Alternatively add this to the user guide. Perhaps something like the following, plus an example like those above:

When assigning a `Series` to a `DataFrame`, either via `.loc` or via the `[]` operator, values of the `Series` will be added to the dataframe according to their index. Values in the `Series` whose label does not appear in the `DataFrame` will not be added, and labels missing from the `Series`' index will be `NaN`. This also means that the order that data appears in the resulting `DataFrame` could be different from the order in the `Series`.