---
tags: 
title: "Drop the name of returning, only keep type for single returning method"
html_url: "https://github.com/siavash-saki/tesspy/issues/39"
user: Zeroto521
repo: siavash-saki/tesspy
---

For the returning single data method and specify the name of returning.
It will cause confusion because of missing context.

I got confused when I first saw the documentation.
What is `df_qk_squares`, `df_h3_hexagons`, and so on?

I suggest deleting the name of returning.
The user doesn't need to know them. They work for the developer.

https://github.com/siavash-saki/tesspy/blob/2ed7c106834821848dfa8169ad01feea44932aea/tesspy/tessellation.py#L264-L267

```diff
 Returns 
 ------- 
- df_qk_squares : pandas.DataFrame
+ pandas.DataFrame
     Dataframe containing squares 
```

PS: the returning type of `Tessellation.squares` should be `GeoDataFrame`.