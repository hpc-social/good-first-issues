---
tags: enhancement
title: "Trimming links with length less than scene pixel resolution"
html_url: "https://github.com/VeinsOfTheEarth/RivGraph/issues/11"
user: Lvulis
repo: jonschwenk/RivGraph
---

I ran into the following issue. There is a link present which is so small that when I rasterize my links json in R that it literally has no points (some kind of interpolation issue probably). It's visible in the image below. So the link is caused because there are an excess number of links here in part due to these small islands. It has a length of 30sqrt(2), so basically 2 nodes which are diagonally adjacent on a 30-m resolution grid. I found 4 total links like this on the scene.

I see two solutions: 
- better CN mask (remove small islands!) which will prevent this from occurring in the first place
- Some kind of link length checker in the prune_nodes? If you can compute length of line features and the length is < 1 or 2 pix or something should be merged with nearest link? Generally the algorithm would go:
Compute all link lengths
For all link lengths < cutoff (say 2 pix) {
   remove the link. Combine the two nodes to be one node
   Connections of new node will be downstream/upstream neighbors (should max be 4 neighbors?)


![image](https://user-images.githubusercontent.com/18738680/78747254-d69f5480-791d-11ea-864b-749be2c64a76.png)

More examples below:
![image](https://user-images.githubusercontent.com/18738680/78748745-9e017a00-7921-11ea-901b-f87376e95d58.png)


![image](https://user-images.githubusercontent.com/18738680/78748769-abb6ff80-7921-11ea-9a40-0940937d93c8.png)

![image](https://user-images.githubusercontent.com/18738680/78748799-bc677580-7921-11ea-9ef7-d27285a3e4a0.png)


