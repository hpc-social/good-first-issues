---
tags: enhancement,ergonomics,priority/low,server,transformers
title: "Smarter error messages from the filtertransformer"
html_url: "https://github.com/Materials-Consortia/optimade-python-tools/issues/795"
user: ml-evs
repo: Materials-Consortia/optimade-python-tools
---

Consider the following gotcha:

The references endpoint has a `year` field which could be useful to query on. Unfortunately in our interpretation of BiBTeX, all fields are strings, so the queries

`example.org/v1/references/?filter=year > 2015` or `example.org/v1/references?filter=year = 2015`

return empty results (for the MongoTransformer, at least).

Another example would be the wrong value type in the comparison, e.g. querying filtering a list for equality with an integer or a string:

`example.org/v1/structures?filter = elements = "Ag,Cl"`

which also just returns empty results without an error.

This may be specific to the MongoDB backend as elasticsearch is much more strongly typed. 

Soon we will hopefully have field data types be accessible to the transformer via the mapper (see upcoming PR). We could then review/use the rules from the validator on which data types can be queried with which operators to provide better error messages from the base transformer directly (pseudo-code below). Likewise with the types of the values themselves.

```python
class BaseTransformer(lark.Transformer):

    def property_first_comparison(self, prop, op, value):
        if op not in self.allowed_ops[self.get_type(prop)]:
             raise BadRequest(f"Cannot apply filter with {op} on {prop})
        if not isinstance(value, self.get_type(prop)):
             try:
                  value = self.get_type(prop)(value)
             except ValueError:
                  raise BadRequest(f"Cannot coerce {value} into property type")

class MongoTransformer(BaseTransformer):

    def property_first_comparison(self, prop, op, value):
        super().property_first_comparison(prop, op, value) # is there a shortcut for super().<current_fn>?

        # do actual transformation
    
```
