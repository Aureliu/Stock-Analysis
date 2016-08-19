from WindPy import w
from datetime import datetime, timedelta
import xlrd

cout = open('hs300_result.txt', 'w')
w.start()

data = xlrd.open_workbook('PB' + '.xlsx')
table = data.sheets()[0]

wsd_data=w.wsd("000300.SH", "amt,turn,pct_chg,pe_ttm,pb,roe,yoy_tr,yoy_or,yoyprofit,close", "2005-10-01", "2016-08-31", "Period=M;Days=Alldays;PriceAdj=F")
time=wsd_data.Times
amt=wsd_data.Data[0]
turn=wsd_data.Data[1]
pct_chg=wsd_data.Data[2]
pe_ttm=wsd_data.Data[3]
close=wsd_data.Data[9]
nrows=len(time)
lable=0


for i in range(3,nrows-1):

	# three month, two before 3%
	# start=close[i-2]
	# end=close[i+1]
	# gain=(float(end)/start)**(float(1)/3)# three month

	# two months 3%
	start=close[i-1]
	end=close[i+1]
	gain=(float(end)/start)**(float(1)/2)# three month

	# # three months, one before 3%
	# start=close[i-1]
	# end=close[i+2]
	# gain=(float(end)/start)**(float(1)/3)# three month

	if gain>1.03:
		lable=2
	elif gain<0.97:
		lable=0
	else:
		lable=1
	cout.write(repr(time[i].year) + '-' + repr(time[i].month) + '\t' + repr(amt[i]) + '\t' + repr(turn[i]) + '\t' 
		+ repr(pct_chg[i])  + '\t' + repr(pe_ttm[i]) + '\t' + repr(table.cell(i,3).value)  + '\t' + repr(table.cell(i,4).value)  + '\t' + repr(lable) + '\t' + repr(close[i]) + '\t' + repr(start) + '\t' + repr(end) + '\t' + repr(gain)+ '\n')
	#+ '\t' + repr(pb[i])  + '\t' + repr(roe[i])  + '\t' + repr(yoy_tr[i])  + '\t' + repr(yoy_or[i])  + '\t' + repr(yoyprofit[i])
cout.flush()
cout.close()