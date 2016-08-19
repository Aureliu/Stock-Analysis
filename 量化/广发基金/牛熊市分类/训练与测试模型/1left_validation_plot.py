import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import cPickle
import itertools
import matplotlib.patches as mpatches
import xlrd


data = xlrd.open_workbook('raw_data' + '.xlsx')
table = data.sheets()[0]
nrows=table.nrows
raw_data=[]
label=[]
color_list=["g", "b", "r","y"]
lable_color=[]
label_color_with_wrong=[]
close=[]
time=[]
correct_number=0

for i in range(0,nrows):
	label.append(table.cell(i,0).value)
	data_point=[]
	for j in range(1,5):
		data_point.append(table.cell(i,j).value)
	raw_data.append(data_point)
	close.append(table.cell(i,12).value)

for i in range(0,nrows):
	test_data=[]
	train_data=[]
	train_lable=[]
	for j in range(0,nrows):
		if j == i:
			test_data.append(raw_data[j])
		else:
			train_data.append(raw_data[j])
			train_lable.append(label[j])
	#Train LR model
	lrmodel=linear_model.LogisticRegression(C=1, penalty='l1')
	lrmodel.fit(train_data,train_lable)
	predict_label=lrmodel.predict(test_data)
	if predict_label[0]==label[i]:
		label_color_with_wrong.append(color_list[int(predict_label[0])])
		correct_number+=1
	else:
		label_color_with_wrong.append(color_list[3])
	lable_color.append(color_list[int(predict_label[0])])
	time.append(i)
	print str(i)+"th test has done!"

	#+ '\t' + repr(pb[i])  + '\t' + repr(roe[i])  + '\t' + repr(yoy_tr[i])  + '\t' + repr(yoy_or[i])  + '\t' + repr(yoyprofit[i])
print correct_number
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
# for i, txt in enumerate(time_show):
#     plt.annotate(txt, (time[i],close[i]))
# for i, txt in enumerate(close_show):
#     plt.annotate(txt, (time[i],close[i]))
plt.show()

plt.figure(1,figsize=(16,8))
red_patch = mpatches.Patch(color='r', label='bull')
green_patch = mpatches.Patch(color='g', label='bear')
blue_patch = mpatches.Patch(color='b', label='vibrate')
yellow_patch = mpatches.Patch(color='y', label='wrong')
plt.legend(handles=[red_patch, green_patch, blue_patch,yellow_patch])
plt.scatter(time,close,color=label_color_with_wrong,linewidth=5)
plt.plot(time,close,color='black',linewidth=1)
plt.xlabel("Time(s)")
plt.ylabel("colsing price at the end of month")
plt.title("closing price with bull and bear label")
# for i, txt in enumerate(time_show):
#     plt.annotate(txt, (time[i],close[i]))
# for i, txt in enumerate(close_show):
#     plt.annotate(txt, (time[i],close[i]))
plt.show()
