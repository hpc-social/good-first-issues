---
tags: Good-first-issue,typeStyle
title: "Use ReadImage and WriteImage functions where appropriate"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/2802"
user: dzenanz
repo: InsightSoftwareConsortium/ITK
---

Setting up a reader or a writer just to use them once in a straightforward way requires 5 lines of code, and it can be accomplished by using the appropriate convenience function. 

`itk::ReadImage` and `itk::WriteImage` are available since ITK 5.2.0. See https://github.com/InsightSoftwareConsortium/ITKSphinxExamples/pull/225
for an illustration of the changes required and https://github.com/InsightSoftwareConsortium/ITKSphinxExamples/issues/226 for further discussion.

This can be done piece-wise. A possible starting point are [bundled examples](https://github.com/InsightSoftwareConsortium/ITK/tree/master/Examples) which are used in the [software guide](https://github.com/InsightSoftwareConsortium/ITKSoftwareGuide/). @josetascon did a good job in [ITKSphinxExamples](https://github.com/InsightSoftwareConsortium/ITKSphinxExamples/commits?author=josetascon).
