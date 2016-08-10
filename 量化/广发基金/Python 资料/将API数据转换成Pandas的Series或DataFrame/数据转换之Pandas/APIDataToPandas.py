# -*- coding:utf-8 -*-
#Python 3.5.0
from WindPy import w
import pandas as pd
import datetime
w.start();

# 取数据的命令如何写可以用命令生成器来辅助完成
wsd_data=w.wsd("000001.SZ", "open,high,low,close", "2015-12-10", "2015-12-22", "Fill=Previous")

#演示如何将api返回的数据装入Pandas的Series
open=pd.Series(wsd_data.Data[0])
high=pd.Series(wsd_data.Data[1])
low=pd.Series(wsd_data.Data[2])
close=pd.Series(wsd_data.Data[3])

print('open:/n',open)
print('high:/n',high)
print('low:/n',low)
print('close:/n',close)

#演示如何将api返回的数据装入Pandas的DataFrame
fm=pd.DataFrame(wsd_data.Data,index=wsd_data.Fields,columns=wsd_data.Times)
fm=fm.T #将矩阵转置
print('fm:/n',fm)
