---
tags: ,Good-first-issue,typeDocumentation
title: "Duplicate and non-existing Doxygen groups"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/3656"
user: jhlegarreta
repo: InsightSoftwareConsortium/ITK
---

### Description

A number of groups in the Doxygen documentation are either duplicates,e.g.
```
 * \ingroup ImageAdaptors
 * \ingroup ITKImageAdaptors
```

e.g. in class https://github.com/InsightSoftwareConsortium/ITK/blob/23da3dfa79152648f3d38050ee147df47f41ce0a/Modules/Core/ImageAdaptors/include/itkComplexConjugateImageAdaptor.h

and give rise to a Doxygen page that has a duplication of "ImageAdaptors" under the form of a "Group" and a "Module" in the group link row: https://itk.org/Doxygen/html/classitk_1_1ComplexConjugateImageAdaptor.html

![itkComplexConjugateAdaptor_doxygen](https://user-images.githubusercontent.com/5576557/192155527-7a154cb9-8b3c-4eff-a2fc-70ce8474628f.png)

or 
```
 * \ingroup Common
 * \ingroup ITKCommon
```

e.g. in class https://github.com/InsightSoftwareConsortium/ITK/blob/23da3dfa79152648f3d38050ee147df47f41ce0a/Modules/Core/Common/include/itkRandomVariateGeneratorBase.h

and give rise to a Doxygen page that somehow manages to filter the duplication in the group link row: https://itk.org/Doxygen/html/classitk_1_1Statistics_1_1RandomVariateGeneratorBase.html

![itkRandomVariateGeneratorBase_doxygen](https://user-images.githubusercontent.com/5576557/192155514-091889ed-c1d9-4db8-9eba-3f0616f5b9bf.png)

or do not exist:
```
 * \ingroup QEMeshModifierFunctions
 * (...)
 * \ingroup Functions
```

e.g. https://github.com/InsightSoftwareConsortium/ITK/blob/23da3dfa79152648f3d38050ee147df47f41ce0a/Modules/Core/QuadEdgeMesh/include/itkQuadEdgeMeshFunctionBase.h

or 
```
 * \ingroup IOFilters
```

e.g. https://github.com/InsightSoftwareConsortium/ITK/search?q=IOFilter&type=commits

The `ImageIO` group is also mentioned by several groups, but it is not defined:
https://itk.org/Doxygen/html/modules.html

in https://github.com/InsightSoftwareConsortium/ITK/blob/master/Documentation/Doxygen/Modules.dox

It should be grouped under the `IO` module/group, and the appropriate classes be marked as belonging to it.

### Expected information

Duplicate groups/modules should not exist. and non-existing groups should be created or removed.

### Actual information

Duplicate groups/modules are either not shown or shown leading to confusion. Non-existing groups cannot be created by Doxygen.

### Versions

`master`

### Additional Information

None.