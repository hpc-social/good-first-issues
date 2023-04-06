---
tags: enhancement
title: "create helper utilities for generating mean flow and demand files from previous runs"
html_url: "https://github.com/IMMM-SFA/mosartwmpy/issues/63"
user: thurber
repo: IMMM-SFA/mosartwmpy
---

Folks may want this rather than having to generate the entire reservoir parameters from `create_grand_parameters.py`.

The task would be to read in result data from a completed simulation, calculate the monthly average flow and demand at reservoir locations, and save to parquet format, ideally with appropriate metadata regarding the timeframe and inputs used in the simulation.

