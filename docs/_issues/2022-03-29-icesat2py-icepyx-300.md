---
tags: enhancement
title: "Extracting asc/descending tracks in high latitudes (regions 4 and 11)"
html_url: "https://github.com/icesat2py/icepyx/issues/300"
user: s2002365
repo: icesat2py/icepyx
---

Hi! It would be great to develop a way to extract just ascending or descending tracks when downloading data with icepyx from regions 4 and 11 (highest latitude regions).  Currently every granule in these two regions contains both ascending and descending tracks, but since we know which tracks are which it should be possible to distinguish them somehow at the point of order/download. @tsutterley had suggested separating the pieces by splitting at the minimum latitude. Open to suggestions and up for collaborating with others to implement this. 

![image](https://user-images.githubusercontent.com/59888842/160627172-fdff5f41-3f9a-4fba-bcbb-070d163751bb.png)
