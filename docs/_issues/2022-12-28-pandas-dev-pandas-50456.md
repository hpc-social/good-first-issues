---
tags: ,Bug,IO-JSON
title: "BUG: JSON serialization with orient split fails roundtrip with MultiIndex"
html_url: "https://github.com/pandas-dev/pandas/issues/50456"
user: datapythonista
repo: pandas-dev/pandas
---

When saving a DataFrame to JSON with `orient='split'` and then loading it again, the loaded dataframe is different from the original if columns are a multiindex.

```python
>>> df = DataFrame([[1, 2], [3, 4]],
...                columns=pd.MultiIndex.from_arrays([["2022", "2022"], ['JAN', 'FEB']]))
>>> df
  2022    
   JAN FEB
0    1   2
1    3   4

>>> read_json(df.to_json(orient='split'), orient='split')
  2022 JAN
  2022 FEB
0    1   2
1    3   4
```

The problem seems to be that the JSON stores the format as `{"columns":[["2022","JAN"],["2022","FEB"]], ...}`, but when creating the loaded DataFrame the `columns` value is passes as that, and `DataFrame(data, columns=[["2022","JAN"],["2022","FEB"]])` produces the incorrect result.

We can fix this by either changing how data is stored in the JSON, or how the dataframe is created. Personally, I think it makes more sense to store the data in the JSON in the way expected by the dataframe constructor.

CC: @MarcoGorelli 