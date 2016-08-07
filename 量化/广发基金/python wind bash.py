wifi 账号：gfjj021，密码：gfjj8888

from WindPy import w

w.start();

#股市分类所用的特征提取。
wsd_data=w.wsd("000300.SH", "amt,turn,pct_chg,pe_ttm,pb,roe,yoy_tr,yoy_or,yoyprofit", "2006-01-01", "2016-07-31", "Period=M;Days=Alldays;PriceAdj=F")
#测试数据
wsd_data=w.wsd("000300.SH", "pb,yoy_or,yoy_tr,yoyprofit","2006-01-01", "2016-07-31", "ruleType=8;Period=Y;PriceAdj=F")

#双均线策略提取的hs300指数的收盘价。
wsd_data=w.wsd("000300.SH", "close", "2005-12-26", "2016-07-28", "PriceAdj=F")

