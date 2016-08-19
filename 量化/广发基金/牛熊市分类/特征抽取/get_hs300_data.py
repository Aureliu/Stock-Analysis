from WindPy import w
from datetime import datetime, timedelta
import xlrd

def generateDifference(raw_data=[]):
	length=len(raw_data)
	ans=[raw_data[0]]
	for i in range(1:length):
		ans[i]=raw_data[i]-raw_data[i-1]
	return raw_data

SelectKBest(lambda X, Y: array(map(lambda x:pearsonr(x, Y), X.T)).T, k=2).fit_transform(iris.data, iris.target)


cout = open('hs300_data.txt', 'w')
w.start();

data = xlrd.open_workbook('PB' + '.xlsx')
table = data.sheets()[0]
data2 = xlrd.open_workbook('roe' + '.xlsx')
table2 = data2.sheets()[0]

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
	cout.write(repr(lable) + '\t' + repr(amt[i]) + '\t' + repr(turn[i]) + '\t' 
		+ repr(pct_chg[i])  + '\t' + repr(pe_ttm[i])  + '\t' + repr(table.cell(i,3).value)  + '\t' + repr(table.cell(i,4).value)
		+ '\t' + repr(table2.cell(i-3,1).value) + '\t' + repr(table2.cell(i-3,2).value) + '\t' + repr(table2.cell(i-3,3).value)
		 + '\t' + repr(table.cell(i,6).value)  + '\t' + repr(table.cell(i,7).value) + '\n')
	#+ '\t' + repr(pb[i])  + '\t' + repr(roe[i])  + '\t' + repr(yoy_tr[i])  + '\t' + repr(yoy_or[i])  + '\t' + repr(yoyprofit[i])
cout.flush()
cout.close()