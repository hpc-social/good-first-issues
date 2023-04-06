---
tags: 
title: "Improve image labeling for large number of classes"
html_url: "https://github.com/palaimon/ipyannotator/issues/9"
user: ibayer
repo: palaimon/ipyannotator
---

Motivation
----------

ipyannotator currently support image labeling. However, for data sets with a very large number of classes it's very difficult to
quickly match the image to the right class.

Showing an visual representation for all possible classes and there textual description right next to the image could considerable improve the process. Currently only a textual or a visual representation can be displayed.

Explore the current difficulties
---------------------------------------

- run the notebook `nbs/01b_tutorial_image_classification.ipynb` with the data set `dataset = 'oxford_flowers'`

![image](https://user-images.githubusercontent.com/1497140/135070376-550a6d8c-2376-4755-a1db-e8ad542a8c68.png)

possible improvements:

- make it easy to show the class name instead of the number (requires mapping from class id to class name)
- show both visual and textual description
- if the data set is already annotated, provide an option to take the visual example right from the data set