# -*- coding:utf-8 -*-
# Author:jqzhang
# Editdate:2015-12-21
from WindPy import w
import pymssql
from datetime import datetime

server = 'WIND-PUB010\SQLEXPRESS'
user = 'jqzhang'
password = 'wind'
dt=datetime.now()
w.start();

# 命令如何写可以用命令生成器来辅助完成
# 定义打印输出函数，用来展示数据使用
#连接数据库
conn = pymssql.connect(server, user, password, 'pymssql')
cursor = conn.cursor()
cursor.execute("""
IF OBJECT_ID('stockprice', 'U') IS NOT NULL
    DROP TABLE stockprice
CREATE TABLE stockprice (
    secid VARCHAR(20) NOT NULL,
    tradedate VARCHAR(50),
    openprice VARCHAR(50),
    highprice VARCHAR(50),
    lowprice VARCHAR(50),
    closeprice VARCHAR(50),
    volume VARCHAR(50),
    amt VARCHAR(50),
    )
""")
sql = "INSERT INTO stockprice VALUES (%s, %s, %d, %d, %d, %d, %d, %d)"

# 通过wset来取数据集数据
print('\n\n'+'-----通过wset来取数据集数据,获取全部A股代码列表-----'+'\n')
wsetdata=w.wset('SectorConstituent','date=20160116;sectorId=a001010100000000;field=wind_code')
print(wsetdata)

for j in range(0,len(wsetdata.Data[0])):
    # 通过wsd来提取时间序列数据，比如取开高低收成交量，成交额数据
    print "\n\n-----第 %i 次通过wsd来提取 %s 开高低收成交量数据-----\n" %(j,str(wsetdata.Data[0][j]))
    wssdata=w.wss(str(wsetdata.Data[0][j]),'ipo_date')
    wsddata1=w.wsd(str(wsetdata.Data[0][j]), "open,high,low,close,volume,amt", wssdata.Data[0][0], dt, "Fill=Previous")
    if wsddata1.ErrorCode!=0:
        continue
    print wsddata1
    for i in range(0,len(wsddata1.Data[0])):
        sqllist=[]
        sqltuple=()
        sqllist.append(str(wsetdata.Data[0][j]))
        if len(wsddata1.Times)>1:
            sqllist.append(wsddata1.Times[i].strftime('%Y%m%d'))
        for k in range(0, len(wsddata1.Fields)):
            sqllist.append(wsddata1.Data[k][i])
        sqltuple=tuple(sqllist)
        cursor.execute(sql,sqltuple)
    conn.commit()
conn.close()



