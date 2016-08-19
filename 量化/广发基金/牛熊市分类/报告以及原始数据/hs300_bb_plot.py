# coding=utf-8  

import numpy as np
import matplotlib.pyplot as plt
import itertools
import matplotlib.patches as mpatches
import xlrd

data = xlrd.open_workbook('bull_bear_data' + '.xlsx')
table = data.sheets()[0]

nrows=table.nrows
color_list=["g", "b", "r"]
lable_color=[]
time_show=[]
close_show=[]
close=[]
time=[]
for i in range(1,nrows):
	label=int(table.cell(i,10).value)
	lable_color.append(color_list[label])
	close.append(table.cell(i,11).value)
	time.append(i)
	if i%6==0:
		time_show.append(table.cell(i,0).value)
	else:
		time_show.append('')
	if i%5==0:
		close_show.append(table.cell(i,11).value)
	else:
		close_show.append('')

	#+ '\t' + repr(pb[i])  + '\t' + repr(roe[i])  + '\t' + repr(yoy_tr[i])  + '\t' + repr(yoy_or[i])  + '\t' + repr(yoyprofit[i])


# add legend to the graph.
plt.figure(1,figsize=(16,8))
red_patch = mpatches.Patch(color='r', label='bull')
green_patch = mpatches.Patch(color='g', label='bear')
blue_patch = mpatches.Patch(color='b', label='vibrate')
plt.legend(handles=[red_patch, green_patch, blue_patch])

plt.scatter(time,close,color=lable_color,linewidth=5)
plt.plot(time,close,color='black',linewidth=1)
plt.xlabel("Time(s)")
plt.ylabel("colsing price at the end of month")
plt.title("closing price with bull and bear label")
for i, txt in enumerate(time_show):
    plt.annotate(txt, (time[i],close[i]))
# for i, txt in enumerate(close_show):
#     plt.annotate(txt, (time[i],close[i]))
plt.show()