---
tags: Docs
title: "Fix capitalization among headings in documentation files"
html_url: "https://github.com/pandas-dev/pandas/issues/32550"
user: tonywu1999
repo: pandas-dev/pandas
---

In #26933, we made the capitalization of titles consistent. For example, a title used to be capitalized like, "This is the Section Title", and many of the titles in the _pandas_ documentation was changed to a correct format, like "This is the section title". 

In #31114, we made a script called `scripts/validate_rst_title_capitalization.py` that extracts all titles in the documentation, making sure that only the first letter of the sentence is uppercase, or words defined in a short list, like Series, DataFrame, etc.  The script also outputs how to fix the title as well. 

We validated capitalization is correct by integrating this script into CI (continuous integration).  The idea is that we should run this script through `ci/code_checks.sh`, and when title capitalization errors show up on CI, the user should fix those errors on the specified files.

To verify the code is working on your side, the command below instructs the program to validate the `doc/source/development/contributing.rst` file.  There should be no output from this command as this file as no capitalization errors:

`./scripts/validate_rst_title_capitalization.py doc/source/development/contributing.rst`

This command below instructs the program to validate both `doc/source/index.rst` and `doc/source/development/policies.rst` files.

```
./scripts/validate_rst_title_capitalization.py doc/source/index.rst doc/source/development/policies.rst
```

This command produces the output below:

```
doc/source/development/policies.rst:9:Heading capitalization formatted incorrectly. Please correctly capitalize "Version Policy" to "Version policy" 
doc/source/development/policies.rst:51:Heading capitalization formatted incorrectly. Please correctly capitalize "Python Support" to "Python support"
```

The goal of this issue is to correct the title capitalization of all files in the _pandas_ documentation. 
In order to see all titles that need to be validated in the documentation folder, one should run the following command below on the command line.   

`./scripts/validate_rst_title_capitalization.py doc/source`

This program validates all RST files in the doc/source folder.  Once all titles are all correctly validated, we would like to add the above command into the `ci/code_checks.sh` file.

Here's a checklist of all the files that had at least one incorrectly capitalized heading:

```
- [ ] doc/source/user_guide/timedeltas.rst
- [ ] doc/source/whatsnew/v0.7.0.rst
- [ ] doc/source/whatsnew/v0.23.4.rst
- [ ] doc/source/whatsnew/v0.6.0.rst
- [ ] doc/source/whatsnew/v1.0.2.rst
- [ ] doc/source/whatsnew/v0.18.0.rst
- [ ] doc/source/whatsnew/v0.16.2.rst
- [ ] doc/source/whatsnew/v0.7.1.rst
- [ ] doc/source/whatsnew/v0.8.0.rst
- [ ] doc/source/user_guide/integer_na.rst
- [ ] doc/source/reference/io.rst
- [ ] doc/source/user_guide/computation.rst
- [ ] doc/source/whatsnew/v0.16.0.rst
- [ ] doc/source/whatsnew/v0.23.2.rst
- [ ] doc/source/whatsnew/v0.12.0.rst
- [ ] doc/source/getting_started/10min.rst
- [ ] doc/source/user_guide/advanced.rst
- [ ] doc/source/reference/arrays.rst
- [ ] doc/source/development/maintaining.rst
- [ ] doc/source/user_guide/groupby.rst
- [ ] doc/source/user_guide/cookbook.rst
- [ ] doc/source/development/developer.rst
- [ ] doc/source/development/meeting.rst
- [ ] doc/source/getting_started/intro_tutorials/03_subset_data.rst
- [ ] doc/source/whatsnew/v0.4.x.rst
- [ ] doc/source/whatsnew/v0.16.1.rst
- [ ] doc/source/whatsnew/v1.0.0.rst
- [ ] doc/source/whatsnew/v0.23.1.rst
- [ ] doc/source/getting_started/tutorials.rst
- [ ] doc/source/reference/series.rst
- [ ] doc/source/getting_started/intro_tutorials/02_read_write.rst
- [ ] doc/source/whatsnew/v0.6.1.rst
- [ ] doc/source/whatsnew/v0.13.1.rst
- [ ] doc/source/whatsnew/v0.21.0.rst
- [ ] doc/source/reference/frame.rst
- [ ] doc/source/whatsnew/v0.20.0.rst
- [ ] doc/source/getting_started/intro_tutorials/09_timeseries.rst
- [ ] doc/source/whatsnew/index.rst
- [ ] doc/source/user_guide/merging.rst
- [ ] doc/source/whatsnew/v0.18.1.rst
- [ ] doc/source/user_guide/enhancingperf.rst
- [ ] doc/source/development/contributing_docstring.rst
- [ ] doc/source/whatsnew/v0.9.0.rst
- [ ] doc/source/whatsnew/v0.25.2.rst
- [ ] doc/source/development/extending.rst
- [ ] doc/source/reference/window.rst
- [ ] doc/source/whatsnew/v0.7.3.rst
- [ ] doc/source/user_guide/options.rst
- [ ] doc/source/ecosystem.rst
- [ ] doc/source/getting_started/intro_tutorials/01_table_oriented.rst
- [ ] doc/source/user_guide/categorical.rst
- [ ] doc/source/whatsnew/v0.14.1.rst
- [ ] doc/source/whatsnew/v0.19.0.rst
- [ ] doc/source/whatsnew/v0.20.2.rst
- [ ] doc/source/whatsnew/v0.24.0.rst
- [ ] doc/source/development/roadmap.rst
- [ ] doc/source/whatsnew/v0.17.0.rst
- [ ] doc/source/user_guide/boolean.rst
- [ ] doc/source/getting_started/comparison/comparison_with_r.rst
- [ ] doc/source/whatsnew/v0.17.1.rst
- [ ] doc/source/whatsnew/v0.22.0.rst
- [ ] doc/source/reference/indexing.rst
- [ ] doc/source/user_guide/missing_data.rst
- [ ] doc/source/getting_started/install.rst
- [ ] doc/source/user_guide/index.rst
- [ ] doc/source/user_guide/visualization.rst
- [ ] doc/source/getting_started/comparison/comparison_with_stata.rst
- [ ] doc/source/whatsnew/v0.19.1.rst
- [ ] doc/source/whatsnew/v0.15.1.rst
- [ ] doc/source/whatsnew/v0.10.0.rst
- [ ] doc/source/whatsnew/v0.19.2.rst
- [ ] doc/source/whatsnew/v0.25.3.rst
- [ ] doc/source/user_guide/gotchas.rst
- [ ] doc/source/whatsnew/v0.14.0.rst
- [ ] doc/source/user_guide/reshaping.rst
- [ ] doc/source/reference/groupby.rst
- [ ] doc/source/whatsnew/v0.23.3.rst
- [ ] doc/source/user_guide/timeseries.rst
- [ ] doc/source/whatsnew/v0.9.1.rst
- [ ] doc/source/getting_started/comparison/comparison_with_sql.rst
- [ ] doc/source/whatsnew/v0.24.1.rst
- [ ] doc/source/reference/index.rst
- [ ] doc/source/development/policies.rst
- [ ] doc/source/whatsnew/v0.21.1.rst
- [ ] doc/source/whatsnew/v0.20.3.rst
- [ ] doc/source/development/code_style.rst
- [ ] doc/source/user_guide/sparse.rst
- [ ] doc/source/whatsnew/v0.24.2.rst
- [ ] doc/source/whatsnew/v0.15.2.rst
- [ ] doc/source/whatsnew/v1.1.0.rst
- [ ] doc/source/reference/offset_frequency.rst
- [ ] doc/source/whatsnew/v1.0.1.rst
- [ ] doc/source/getting_started/basics.rst
- [ ] doc/source/whatsnew/v0.5.0.rst
- [ ] doc/source/user_guide/text.rst
- [ ] doc/source/user_guide/indexing.rst
- [ ] doc/source/whatsnew/v0.11.0.rst
- [ ] doc/source/whatsnew/v0.8.1.rst
- [ ] doc/source/getting_started/comparison/comparison_with_sas.rst
- [ ] doc/source/whatsnew/v0.23.0.rst
- [ ] doc/source/user_guide/io.rst
- [ ] doc/source/whatsnew/v0.25.1.rst
- [ ] doc/source/whatsnew/v0.13.0.rst
- [ ] doc/source/whatsnew/v0.25.0.rst
- [ ] doc/source/whatsnew/v0.15.0.rst
- [ ] doc/source/whatsnew/v0.10.1.rst
```