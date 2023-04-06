---
tags: ,enhancement
title: "Multi-Level Indexing and Compatibility with R's reticulate Library"
html_url: "https://github.com/mortonne/psifr/issues/9"
user: githubpsyche
repo: mortonne/psifr
---

Prima facie, `psifr` seems well-suited for use in R via its reticulate library. Even though it is written in Python, `psifr` is well-suited for R because its numerical outputs are Data Frames, rather than vectors or arrays as MATLAB-based functions tend to output. When using `reticulate`, R data frames are automatically converted to and from Python DataFrames. Moreover, the data format required for performing `psifr` or more hand-spun analyses is well suited for the kinds of operations you'd be doing with `ggplot` to make visualizations. 

These features should make use of the library in R relatively seamless. But since psifr heavily wields multi-index rows, etc, to do a lot of its analyses, it doesn't really work out that way. Operations like `fr.spc`, when called using reticulate, discard `subject` and `input` levels critical for performing downstream analyses, like actually plotting serial position curves.

I feel like that's kinda a shame, a missed opportunity? Adding an optional argument triggering `reset_index` as the last step of functions like these would probably sidestep this limitation while maintaining compatibility with downstream functions like `fr.plot_spc` (I've already tested as much for this function). `seaborn` and `pandas`'s various grouping steps seem to work just as well when identifying information like `subject` or `input` are in row indices _or_ columns. 

Of course R compatibility is outside the project's scope, and the overhead of performing `reset_index` over and over again might be significant, but adding an option to perform that within `psifr`'s functions would make it possible to, for example, add a page to the library's documentation called "Using Psifr in R" that shows it's as simple as the code I include below (i.e. almost exactly like it's used in Python), and potentially extend its reach across the research community. 

Just an idea.

```R
library(reticulate)
fr <- import("psifr.fr")

data <- read.csv("data.csv")
merged<- fr$merge_free_recall(data)
spc <- fr$spc(merged))
```