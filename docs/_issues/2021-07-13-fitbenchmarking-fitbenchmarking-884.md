---
tags: Enhancement,Good-first-issue
title: "Optional extra columns for displaying additional info, such as number of parameters and number of data points in result tables"
html_url: "https://github.com/fitbenchmarking/fitbenchmarking/issues/884"
user: Anders-Markvardsen
repo: fitbenchmarking/fitbenchmarking
---

**Is your feature request related to a problem? Please describe.**
Discussed with @BenPetersRAL recently, and based on questions from Nick Gould after a presentation by @jess-farmer recently, where Nick was asking from viewing table results what are the number of fitting parameters for each of the Benchmark problems? 

You can get this information by clicking on each of the Benchmark problems. However, here the feature request is to make this optionally more visible. Specifically the feature request is to allow optional extra columns in the tables, which e.g. can be: the number of parameters, number of data points, and so on, although in this issue suggest limit this to: number of parameters and number of data points. 

The main user facing output of FitBenchmarking is the table outputs and the purpose of this issue is the enhance this experience; allowing the user to optionally add extra columns, which are important to them and for when they present results to otherwise/or themselves.

**Describe the solution you'd like**
I am unsure how to best implement this. Options include: 1) add options which can be set in `.ini` setting files such as `all_software.ini` and `options_template.ini` 2) allow users to interactively add such columns in table result web pages.

**Describe alternatives you've considered**
For the Benchmark problems we ship, create a document page with CI that displays summary information about the benchmark problems we support. Not as nice as if this info displayed directly in tables, but maybe fine. This would require creating a script for this and maintaining this script.
