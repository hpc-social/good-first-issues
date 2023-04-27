---
title: "Information for new contributors \u2013 update"
html_url: "https://github.com/pandas-dev/pandas/issues/49275"
user: noatamir
repo: pandas-dev/pandas
---

Hi folks,

Welcome! If you are new contributor, here are some links to resources to get you started:

 - [Contributors documentation](https://pandas.pydata.org/docs/dev/development/contributing.html)
   - [Create a development environment for working on pandas](https://pandas.pydata.org/docs/dev/development/contributing_environment.html)
   - [Contributing to the documentation](https://pandas.pydata.org/docs/dev/development/contributing_documentation.html)
   - [Contributing to the codebase](https://pandas.pydata.org/docs/dev/development/contributing_codebase.html)
   - [Helping with issue triage](https://pandas.pydata.org/docs/dev/development/maintaining.html#issue-triage)

Please also consider joining our [contributors' community](https://pandas.pydata.org/docs/dev/development/community.html), where folks connect with each to resolve issues and discuss ongoing work.

If something isn't clear, or doesn't go smoothly, then you can ask in our contributors' community or [raise an issue](https://github.com/pandas-dev/pandas/issues/new/choose).

As we continue to evolve contributing to pandas, you can check back here for updates in the list below. Thank you for being a part of pandas!

Recent updates:
 - 2023.02.24: The pytest arguments `--skip-slow`, `--skip-network`, and `--skip-db` have been removed (#51490). You can use `-m "not slow and not network and not db"` with pytest instead. See [Running the test suite](https://pandas.pydata.org/pandas-docs/dev/development/contributing_codebase.html?highlight=slow#running-the-test-suite) for a full example.
 - 2022.10.24: We decided to remove the milestone “contributors welcome” across the entire project. That means that if you see an activity like _"@xyz removed this from the Contributions Welcome milestone X days ago"_ on issues tagged with _good first issue_, or any other label really, it's safe to ignore it. Please go ahead and contribute to any issue you are interested in.
