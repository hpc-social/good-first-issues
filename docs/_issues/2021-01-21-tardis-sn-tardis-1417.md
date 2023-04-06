---
tags: ,documentation,io,model,priority---medium
title: "Clean up custom abundance input and documentation"
html_url: "https://github.com/tardis-sn/tardis/issues/1417"
user: andrewfullard
repo: tardis-sn/tardis
---

#### Problem description

Currently the two custom input options are in the documentation "ascii" and "csv". Neither are truly descriptive of the file types used or the formatting requirements. 

I propose changing the "ascii" input type to be "complex_composition" (because it requires all isotopes from Z=0-30) and the "csv" input type to be "simple_composition" because it requires only isotope names in the header. The user should be able to choose a delimiter for either input file type as part of the configuration.

This would involve changes primarily to `tardis/io/model_reader.py` and the model input schema.