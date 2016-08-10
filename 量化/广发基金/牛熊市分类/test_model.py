from WindPy import w
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import cPickle

cout = open('test_result.txt', 'w')
w.start();

wsd_data=w.wsd("000300.SH", "amt,turn,pct_chg,pe_ttm,pb,roe,yoy_tr,yoy_or,yoyprofit,close", "2005-10-01", "2016-07-31", "Period=M;Days=Alldays;PriceAdj=F")
time=wsd_data.Times
amt=wsd_data.Data[0]
turn=wsd_data.Data[1]
pct_chg=wsd_data.Data[2]
pe_ttm=wsd_data.Data[3]
# pb=wsd_data.Data[4]
# roe=wsd_data.Data[5]
# yoy_tr=wsd_data.Data[6]
# yoy_or=wsd_data.Data[7]
# yoyprofit=wsd_data.Data[8]
close=wsd_data.Data[9]
nrows=len(time)
lable=0

# load the classifier
with open('lr_classifier.pkl', 'rb') as fid:
    model_loaded = cPickle.load(fid)

# generate train data
for i in range(3,nrows-1):
	start=close[i-2]
	end=close[i+1]
	gain=(float(end)/start)**(float(1)/3)
	if gain>1.03:
		lable=2
	elif gain<0.97:
		lable=0
	else:
		lable=1
	data=[amt[i],turn[i],pct_chg[i],pe_ttm[i]]
	test_data=[data]
	predict_lable=model_loaded.predict(test_data)
	predict_prob=model_loaded.predict_proba(test_data)
	cout.write(repr(time[i].year) + '-' + repr(time[i].month) + '\t' + repr(lable)  + '\t' + repr(predict_lable[0]) + '\t' + repr(predict_prob[0,0]) + '\t' + repr(predict_prob[0,1]) + '\t' + repr(predict_prob[0,2]) + '\n')
cout.flush()
cout.close()