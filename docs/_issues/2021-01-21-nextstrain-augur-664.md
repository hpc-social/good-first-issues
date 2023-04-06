---
tags: ,bug,documentation,please-take-this-issue
title: "Developer documentation lacks complete installation instructions"
html_url: "https://github.com/nextstrain/augur/issues/664"
user: huddlej
repo: nextstrain/augur
---

Our current developer documentation (in `docs/contribute/DEV_DOCS.md`) lacks information about how to setup a complete development environment that includes bioinformatics tools like mafft, etc. that are required to test augur. This documentation is not prominent in the README nor is it accessible from the main RTD interface at docs.nextstrain.org.

To fix this issue, I propose that we:

  - Add a new top-level heading to the README for "Contributing to Augur" after the "Quickstart" that links to the contributor's guide and the developer documentation.
  - Update the developer documentation to include a full explanation of how to clone the source code, create a development environment, and install the development version of Augur.
  - Expose the developer documentation through the main Augur docs as a top-level link in the table of contents above the Python API.
  - Update the "[Install from source](https://docs.nextstrain.org/projects/augur/en/stable/installation/installation.html#install-from-source)" section of the Augur installation guide to link to the developer's guide. This supports the use case where a user looks for how to install Augur from source code with the intention to contribute to the project.
