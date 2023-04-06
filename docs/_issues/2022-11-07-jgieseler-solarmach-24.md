---
tags: enhancement
title: "Provide option to move the legend and logo"
html_url: "https://github.com/jgieseler/solarmach/issues/24"
user: jgieseler
repo: jgieseler/solarmach
---

Provide option(s) to allow the user to easily move the position of the legend and the Solar-MACH logo. They are defined using matplotlib:
``` python 
# legend
leg1 = ax.legend(loc=(1.2, 0.7), fontsize=13)

#logo
ax.text(0.94, 0.16, 'Solar-MACH', fontfamily='DejaVu Serif', fontsize=28,
        ha='right', va='bottom', transform=fig.transFigure)
ax.text(0.94, 0.12, 'https://solar-mach.github.io', fontfamily='DejaVu Sans', fontsize=18,
        ha='right', va='bottom', transform=fig.transFigure)
```
Maybe the best approach is to follow matplotlib's standard legend placement, that look like the following. The location can be provided by an integer or by a string like 'lower right':
![image](https://user-images.githubusercontent.com/39489154/200272773-a689330a-4abd-423b-9a7b-200cc39727cd.png)

So, for solarmach, the example in Python (the streamlit version would use GUI elements, e.g., a dropdown menu for each variable) would look like:
``` python
# locations provided by y and x position, e.g. 'upper right'
fig, ax = sm.plot(loc_legend='lower left', loc_logo='center right')
```
Note that in Python, it should already now be possible to change those locations by using the option to return the matplotlib figure object and modify it afterwards, but this is not straightforward.
