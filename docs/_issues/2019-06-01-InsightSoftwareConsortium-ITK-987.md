---
tags: ,Good-first-issue,typeDesign
title: "Address Todo items in AzimuthElevationToCartesianTransform"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/987"
user: hjmjohnson
repo: InsightSoftwareConsortium/ITK
---

### Description

AzimuthElevationToCartesianTransform

 * \todo Is there any real value in allowing the user to template
 * over the scalar type?  Perhaps it should always be double, unless
 * there's a compatibility problem with the Point class.
 *
 * \todo Derive this class from TransformBase class.
 * Currently, this class derives from AffineTransform, although
 * it is not an affine transform.
 *
 * \todo Add a figure in the documentation that informs the formulas used in this class
 * that are used to transform Cartesian to azimuth-elevation-radius

### Expected behavior

Noted todo items should be removed from code base.

### Actual behavior

### Versions

ITK version 5.0.0 
