---
tags: ,documentation,enhancement
title: "Automatic island filtering by island vs channel size."
html_url: "https://github.com/VeinsOfTheEarth/RivGraph/issues/12"
user: Lvulis
repo: jonschwenk/RivGraph
---

It would be very useful to have channels which are not really "channels" removed from the channel mask for a more accurate DCN to be extracted. We want narrow islands to be removed but only channels who are too narrow for the channel they are in. This is because we want bifurcations, not flow around some sandbars that are large enough. 

One way to do this could be removing any island whose length is less than the width of the channel it is. Could do this simply thru hole filling below a certain threshold. However we need to KNOW how wide the channel to do this. 

My initial idea/way to tackle it.
Run thru channel extraction and get channel widths. Then compute the size of islands in every channel. Apply a threshold (L_I > L_C), for any island objects that don't meet this criteria remove them by filling in the holes in the channel mask. L_I could be max radius or could be sqrt(Area). Then have to basically use the cleaned up channel mask and start back from beginning?!?!

Jon you suggested something of working in raster space - maybe a trick using the distance transform to estimate island width and channel width, and then blanking out islands whose max dist is lower than than channel width up or downstream.