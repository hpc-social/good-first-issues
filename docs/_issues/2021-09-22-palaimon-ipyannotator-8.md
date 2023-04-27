---
title: "Add support for class labeling of bbox"
html_url: "https://github.com/palaimon/ipyannotator/issues/8"
user: ibayer
repo: palaimon/ipyannotator
---

Motivation
----------

ipyannotator currently support single object location with a bounding box (bbox). However annotating the type / class of the object is currently not supported.

Develop and Integrate Class Labeled BBox Widget
-------------------------------------------------------------------

Suggested steps:

- explore `01c_tutorial_bbox.ipynb` to see the current bbox implementation in action
- extend `01_bbox_canvas.ipynb` with a new class `LabeledBBoxCanvas` which supports displaying and drawing of a class labeled bbox.
- duplicate `04_bbox_annotator.ipynb` as `04b_class_bbox_annotator.ipynb` and replace the `BBoxCanvas` with `LabeledBBoxCanvas`
