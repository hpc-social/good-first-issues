---
tags: ,easy
title: "CSVY Parsers Should Be Incorporated to Model Readers"
html_url: "https://github.com/tardis-sn/tardis/issues/1911"
user: marxwillia
repo: tardis-sn/tardis
---

Currently, the CSVY parser functions are located with the parsers in tardis/io/parsers, but those functions belong in the tardis/io/model_reader.py file.  Please move all CSVY related parser functions to the model reader file.  Note that this will cause import statements to break and some tests to fail, so these things need to be fixed as well.
