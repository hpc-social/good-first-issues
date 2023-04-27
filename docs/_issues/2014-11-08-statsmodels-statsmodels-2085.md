---
tags: comp-graphics,comp-tsa,type-enh
title: "modify the appearance of the ACF PLOT function when using subplots"
html_url: "https://github.com/statsmodels/statsmodels/issues/2085"
user: aviPython
repo: statsmodels/statsmodels
---

Hi!
I'm using statsmodels (0.6.0) on Python 2.7, and i'd like to plot several autocorrelation functions  as subplots. Each subplot represents the autocorrelation for different data on each month so i'd like to compare them visually. 

Now, the problem is that unlike other functions (which I easily subplot using Matplolib), here I am not able to add a lagend, add xlabel or use other common features in plotting. It seems that `ACF` plot in statsmodels has fixed and "anchored" properties, like the title "Autocorrelation" cannot be removed (or at least I couldn't find a way). The reason i'd like to remove it is that it appears on the head of each subplot and covers the axis of the plots above it.

Here is the subplots figure that I got:
![figure_1](https://cloud.githubusercontent.com/assets/8626306/4964906/1842c884-6774-11e4-84b8-a9367b8c0fd4.png)

Moreover, It would be helpful to add legends to mark each month and add "Lag" on the bottom of the figure. 
the following functions didn't work:

```
plt.legend(['January'] ,loc='upper right', fontsize = 'x-small')
plt.xticks(visible=False)
plt.xlabel('Lag')
```

Does anybody know if such changes are feasible and if yes how to do it?  

P.S
for the figure above I used the following:

```
fig, axes = plt.subplots(5,1)
fig = sm.graphics.tsa.plot_acf(ts1['2013/01/01 00:00:00':'2013/01/02 23:59:59'], lags= 86400, ax=axes[0])
fig = sm.graphics.tsa.plot_acf(ts2['2013/02/01 00:00:00':'2013/02/02 23:59:59'], lags= 86400, ax=axes[1])
fig = sm.graphics.tsa.plot_acf(ts3['2013/03/01 00:00:00':'2013/03/02 23:59:59'], lags= 86400, ax=axes[2])
fig = sm.graphics.tsa.plot_acf(ts4['2013/04/01 00:00:00':'2013/04/02 23:59:59'], lags= 86400, ax=axes[3])
fig = sm.graphics.tsa.plot_acf(ts5['2013/05/01 00:00:00':'2013/05/02 23:59:59'], lags= 86400, ax=axes[4])
```
