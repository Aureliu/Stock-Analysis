from WindPy import w
import xlrd
from operator import add
from operator import truediv


cout = open('roe.txt', 'w')
w.start();

# sum of profit and equity
net_profit=[0]*44
equity=[0]*44

# add list of each stock 
with open("hs300_stock.txt") as fl:
    for stock in fl:
    	wsd_data=w.wsd(stock, "qfa_np_belongto_parcomsh,eqy_belongto_parcomsh", "2005-10-01", "2016-07-31", "rptType=1;Period=Q;Days=Alldays;PriceAdj=F")
    	net_profit=map(add, net_profit, wsd_data.Data[0])
    	equity=map(add, equity, wsd_data.Data[1])

time=wsd_data.Times
roe = map(truediv, net_profit, equity)
nrows=len(roe)
for i in range(0,nrows):
	cout.write(repr(time[i].year) + '-' + repr(time[i].month-2) + '\t' + repr(net_profit[i]) + '\t' + repr(equity[i]) + '\t' + repr(roe[i]) + '\n')
	cout.write(repr(time[i].year) + '-' + repr(time[i].month-1) + '\t' + repr(net_profit[i]) + '\t' + repr(equity[i]) + '\t' + repr(roe[i]) + '\n')
	cout.write(repr(time[i].year) + '-' + repr(time[i].month) + '\t' + repr(net_profit[i]) + '\t' + repr(equity[i]) + '\t' + repr(roe[i]) + '\n')

cout.flush()
cout.close()

