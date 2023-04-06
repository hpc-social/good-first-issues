---
tags: ,Good-first-issue,typeDocumentation
title: "Reword the definition of Origin in SoftwareGuide"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/400"
user: phcerdan
repo: InsightSoftwareConsortium/ITK
---

itk.FFTPadImageFilter introduces negative indexes to its output image as a result of the padding internals.

Check the results of the piece of code in `Steps to Reproduce`. The results of `padded image after written and read` are correct. But the output of `padRegular` is intriguing for me, following the Software Guide, section`Defining origin and spacing`:

```
Dirac delta function located at the pixel center. Pixel spacing is measured between the pixel centers
and can be different along each dimension. The image origin is associated with the coordinates of
the first pixel in the image.
```

From that, I would expect that the origin of `padRegular` is modified, taking into account the new first index (negative), the correct origin would be the same that is read in `readPadded`.

What do you think, am I misunderstanding something?

### Steps to Reproduce
```python

import sys
import itk
try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve


def printImageInformation(image, title = ''):
    if title:
        print("** ", title, " **")
    print("Origin: ", image.GetOrigin())
    print("Spacing: ", image.GetSpacing())
    print("Index: ", image.GetLargestPossibleRegion().GetIndex())
    print("Size: ", image.GetLargestPossibleRegion().GetSize())
    print()

# Download data (3D)
filename = '005_32months_T2_RegT1_Reg2Atlas_ManualBrainMask_Stripped.nrrd'
if not os.path.exists(filename):
    url = 'https://data.kitware.com/api/v1/file/564a5b078d777f7522dbfaa6/download'
    urlretrieve(url, filename)

image = itk.imread(filename)
padFilter = itk.FFTPadImageFilter.New(Input=image)
padFilter.SetSizeGreatestPrimeFactor(2)
padFilter.Update()
padded = padFilter.GetOutput()
padded_filename = '/tmp/VOL_10_cropped_fftPadConstantWHAT.nrrd'
itk.imwrite(padded, padded_filename )
printImageInformation(image, 'cropped')
printImageInformation(padded, 'padRegular')

readPadded = itk.imread(padded_filename)
printImageInformation(readPadded, 'padded after written and read')
```
```
**  cropped  **
Origin:  itkPointD3 ([-6.835, -6.835, -6.835])
Spacing:  itkVectorD3 ([0.2734, 0.2734, 0.2734])
Index:  itkIndex3 ([0, 0, 0])
Size:  itkSize3 ([300, 350, 250])

**  padRegular  **
Origin:  itkPointD3 ([-6.835, -6.835, -6.835])
Spacing:  itkVectorD3 ([0.2734, 0.2734, 0.2734])
Index:  itkIndex3 ([-106, -81, -3])
Size:  itkSize3 ([512, 512, 256])

**  padded after written and read  **
Origin:  itkPointD3 ([-35.8154, -28.9804, -7.6552])
Spacing:  itkVectorD3 ([0.2734, 0.2734, 0.2734])
Index:  itkIndex3 ([0, 0, 0])
Size:  itkSize3 ([512, 512, 256])

```

