from WindPy import w

cout = open('hs300.txt', 'w')

w.start();
wsd_data=w.wsd("000300.SH", "close", "2006-04-14", "2016-07-28", "PriceAdj=F")
time=wsd_data.Times
close=wsd_data.Data[0]
nrows=len(time)
for i in range(0,nrows):
	cout.write(repr(time[i].year) + '-' + repr(time[i].month) + '-' + repr(time[i].day) + '\t' + repr(close[i]) + '\n')
cout.flush()
cout.close()