---
tags: Feature-Request,Python,code-quality,help-wanted
title: "Auto-Update setup.py's release version upon github release"
html_url: "https://github.com/ianfhunter/GNOLL/issues/146"
user: ianfhunter
repo: ianfhunter/GNOLL
---

**Is your feature request related to a problem? Please describe.**
I always forget to update setup.py's version when making a github release - then the pip package does not get deployed

**Describe the solution you'd like**
Take the git tag (https://github.com/orgs/community/discussions/26686) and replace it in the code before the publication step of the github action

**Describe alternatives you've considered**
Can do it manually in the meanwhile

**Additional context**
