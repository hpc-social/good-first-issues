---
tags: Good-first-issue,typeDocumentation
title: "Save scientific work citations to a BibTeX file for ease of use in Doxygen"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/3662"
user: jhlegarreta
repo: InsightSoftwareConsortium/ITK
---

### Description

Citations to scientific works should be stored in a BibTeX file and Doxygen's `\cite` should be used to cite them in the documentation. Currently, there is a variety of syntaxes that are used to cite works across the documentation, ranging from no syntax highlight at all, code-style indentation, or paragraph, e.g.:
https://itk.org/Doxygen/html/classitk_1_1STAPLEImageFilter.html
https://itk.org/Doxygen/html/classitk_1_1ScalarChanAndVeseSparseLevelSetImageFilter.html
https://itk.org/Doxygen/html/classitk_1_1BSplineScatteredDataPointSetToImageFilter.html

### Expected information

Citatons should be hosted in a single BibTeX file so that they can easily be cross-referenced and reused across the documentation.

### Actual information

Citation styles are inconsistent and the same work might be cited differently/citations cannot be re-used.

### Versions

`master`

### Additional Information

Doxygen `\cite` command documentation:
https://doxygen.nl/manual/commands.html#cmdcite

The IJ works' bibtex files can actually be retrieved from the IJ website, so that would save some work. Maybe an script that gathers all references could be developed to have them all in a single file. The file could be dynamically updated e.g. every month.

IJ repository: https://github.com/InsightSoftwareConsortium/InsightJournal