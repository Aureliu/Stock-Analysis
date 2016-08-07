# coding=utf-8  

from WindPy import w
import numpy as np
import matplotlib.pyplot as plt

cout = open('hs300_data.txt', 'w')
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
lable_list = [3,3,3]
lable=0
for i in range(3,nrows-1):
	start=close[i-2]
	end=close[i+1]
	gain=(float(end)/start)**(0.2)
	if gain>1.03:
		lable=2
	elif gain<0.97:
		lable=0
	else:
		lable=1
	lable_list.append(lable+1)
	cout.write(repr(lable) + '\t' + repr(amt[i]) + '\t' + repr(turn[i]) + '\t' 
		+ repr(pct_chg[i])  + '\t' + repr(pe_ttm[i]) + '\n')
	#+ '\t' + repr(pb[i])  + '\t' + repr(roe[i])  + '\t' + repr(yoy_tr[i])  + '\t' + repr(yoy_or[i])  + '\t' + repr(yoyprofit[i])
cout.flush()
cout.close()

lable_list.append(3)

amt_lable=[elem *1000000000000 for elem in lable_list]
plt.figure(figsize=(8,4))
plt.plot(time,amt,label="$amt$",color="red",linewidth=2)
plt.plot(time,amt_lable,"b--",label="$lable$")
plt.xlabel("Time(s)")
plt.ylabel("amt")
plt.title("Relation between amt and market")
plt.legend()
plt.show()

turn_lable=[elem *20 for elem in lable_list]
plt.figure(figsize=(8,4))
plt.plot(time,turn,label="$turn$",color="red",linewidth=2)
plt.plot(time,turn_lable,"b--",label="$lable$")
plt.xlabel("Time(s)")
plt.ylabel("turn")
plt.title("Relation between Turn and market")
#plt.ylim(-0.2,3.2)
plt.legend()
plt.show()

pct_lable=[elem *20-40 for elem in lable_list]
plt.figure(figsize=(8,4))
plt.plot(time,pct_chg,label="$pct_chg$",color="red",linewidth=2)
plt.plot(time,pct_lable,"b--",label="$lable$")
plt.xlabel("Time(s)")
plt.ylabel("pct chg")
plt.title("Relation between PCT_CHG and market")
#plt.ylim(-0.2,3.2)
plt.legend()
plt.show()

pe_lable=[elem *10 for elem in lable_list]
plt.figure(figsize=(8,4))
plt.plot(time,pe_ttm,label="$pe_ttm$",color="red",linewidth=2)
plt.plot(time,pe_lable,"b--",label="$lable$")
plt.xlabel("Time(s)")
plt.ylabel("pe_ttm")
plt.title("Relation between TTM PE and market")
#plt.ylim(-0.2,3.2)
plt.legend()
plt.show()