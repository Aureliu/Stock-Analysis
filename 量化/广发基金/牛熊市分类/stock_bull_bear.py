from WindPy import w
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import cPickle

# start wind
w.start()

# load the classifier
with open('lr_classifier.pkl', 'rb') as fid:
    model_loaded = cPickle.load(fid)

print("\n")

while True:

	# Input date
	year, month, day = input('Please input  year,month,day (with a comma in between): \n')
	# if month==1:
	# 	last_year=year-1
	# 	last_month=12
	# else:
	# 	last_year=year
	# 	last_month=month-1
	# start_day=str(last_year)+'-'+str(last_month)+'-'+str(day)
	end_day=str(year)+'-'+str(month)+'-'+str(day)

	# get wind data
	wsd_data=w.wsd("000300.SH", "amt,turn,pct_chg,pe_ttm,pb,roe,yoy_tr,yoy_or,yoyprofit,close", "ED0M", end_day, "Period=M;Days=Alldays;PriceAdj=F")
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

	# generate train data
	data=[amt[0],turn[0],pct_chg[0],pe_ttm[0]]
	test_data=[data]
	predict_lable=model_loaded.predict(test_data)
	predict_prob=model_loaded.predict_proba(test_data)
	if predict_lable[0]==0:
		ans="bear"
	elif predict_lable[0]==1:
		ans="vibrate"
	else:
		ans="bull"
	print(repr(time[0].year) + '-' + repr(time[0].month) + '-' + repr(time[0].day) + '\t' + ans + '\n' + "Bear:"+repr(predict_prob[0,0]) + '\t' + "Vibrate:" + repr(predict_prob[0,1]) + '\t' + "Bull:" + repr(predict_prob[0,2]) + '\n')