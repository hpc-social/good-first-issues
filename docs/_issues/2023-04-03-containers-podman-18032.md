---
tags: Good-First-Issue,kind/feature,quadlet
title: "Quadlet should search subdirectories for the unit search path"
html_url: "https://github.com/containers/podman/issues/18032"
user: Nitrousoxide
repo: containers/podman
---

### Feature request description

Right now Quadlet will search:
/etc/containers/systemd/
/usr/share/containers/systemd/

for rootful container definitions and:
~/.config/containers/systemd/

for non-root container definitions.  However, it will not recursively check subdirectories under these paths.  For a sufficiently large set of containers/networks/volumes this can create a very long and flat list with no (or very little) organization which makes parsing how the containers might be grouped difficult.  It also leads to excessively long lists when attempting to navigate the path and pick out the *.container files to edit.  Allowing the user to create subdirectories to group arbitrary containers/pods together for ease of reference by a human would make management of the files significantly easier. 

Quadlet could still pull together the list of all the relevant .container .volume and .kube files in the origin path and treat them as a flat list when spinning up services, but allowing subdirectories will make human readability much better for larger deployments.

### Suggest potential solution

Allow Quadlet to search subdirectories for *.container *.volume, *.network and *.kube files in the search path.

### Have you considered any alternatives?

A clear and concise description of any alternative solutions or features you've considered.

### Additional context

Add any other context or screenshots about the feature request here.