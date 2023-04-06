---
tags: ,Good-first-issue,typeEnhancement,typeInfrastructure
title: "Overload the stream insertion operator for types that are missing it"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/513"
user: jhlegarreta
repo: InsightSoftwareConsortium/ITK
---

### Description
Overload the stream insertion operator for types that are missing it.

### Expected behavior
To be able to print any data structure with a single line, e.g.:
```
os << indent << "MyStructure : " << m_MyStructure << std::endl;
```
### Actual behavior
Developer's are forced to iterate over such structures to get them printed (usually in the `PrintSelf` method), e.g.:
```
  while( it != m_CirclesList.end() )
    {
    os << indent << "[" << i << "]: " << *it << std::endl;
    ++it;
    ++i;
    }
```

### Additional information
Some fundamental ITK types (e.g. `IndexTypes`, `SizeType`, `SpacingType`, `OffsetType`,  `DirectionType`, `OffsetTable`, `RegionType`) either seem not to have such an overload or it is just because some filters (`itkImageConstIteratorWithIndex.h`, `itkImageIORegion.h`, `itkNeighborhood.h`,  `itkImportImageFilter.h`, `itkConstNeighborhoodIterator.h`, `itkImportImageFilter.hxx`, `itkDisplacementFieldJacobianDeterminantFilter.h`, `itkGaussianBlurImageFunction.h`, `itkEllipsoidInteriorExteriorSpatialFunction.h`) that declare ivars of such types are not using the correct types, since it looks weird that such fundamental types do not have the stream insertion operator overload.

Other more exotic type aliases (`GradientType`, `StrideTable`, `SeedsContainerType`, `WeightsType`, `ErrorArrayType`, `ExtentArrayType`) would also deserve some investigation, as well as other aliases that are not consistent with the toolkit convention for the intended use (e.g. `InputType` in `itkEllipsoidInteriorExteriorSpatialFunction.h`).

Finally, other data structures that are also missing such an overload are regular arrays, e.g.
```
double m_Sigma[ImageDimension2];
```
in `itkBSplineControlPointImageFunction.h` or `itkGaussianDerivativeImageFuncton.h`

or
```
double          m_Scale[NDimensions];
``` 
in `itkScalableAffineTransform.h`.

`std::list` types (e.g. `itkHoughTransform2DCirclesImageFilter.h` or `itkHoughTransform2DLinesImageFilter.h`).

Or `vnl_matrix` matrix (e.g. `itkBSplineScatteredDataPointSetToImageFilter.h`).

This is related to #512.
