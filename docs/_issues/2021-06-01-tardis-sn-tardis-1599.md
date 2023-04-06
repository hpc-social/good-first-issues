---
tags: ,documentation
title: "Improve list of papers using TARDIS"
html_url: "https://github.com/tardis-sn/tardis/issues/1599"
user: smithis7
repo: tardis-sn/tardis
---

**Is your feature request related to a problem? Please describe.**
Last year, we automated the process of generating references for papers that use tardis using [this notebook](https://github.com/tardis-sn/tardis/blob/master/docs/research/research_done_using_TARDIS/ads.ipynb). There are a few problems:
- While the notebook automates the list, the notebook is not automatically run, and thus the list still needs to be manually updated by manually running the notebook (this is not as easy of a fix as it may seem, as the notebook requires a private key in order to be run).
- The search criteria in the notebook returns extra papers that don't use TARDIS for any calculations, and also could potentially miss papers that use TARDIS for calculations.
- https://tardis-sn.github.io/tardis/zreferences.html also contains a list of studies using TARDIS which is redundant (though that list only contains a fraction of the papers that the notebook generates). I will add that this list is in a more noticeable location within the documentation, so perhaps we may want to move the notebook-generated list to that location.

**Describe the solution you'd like**
Any solution that would fix any/all of the above bullet points would be phenomenal! I believe that this would be a good project for a first-time contributor.