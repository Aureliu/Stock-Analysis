from datetime import datetime, timedelta
import xlrd
import string
# Offset is from 0
data = xlrd.open_workbook('2016-7-29-single' + '.xlsx')
table = data.sheets()[0]
nrows = table.nrows
max_drawdown=0
max_point=0
price=0
drawdown=0
day_of_max=0
day_of_drawdown=0
day_of_min=0
for i in range(3,nrows):
	price=table.cell(i,9).value
	if(price>max_point):
		max_point=price
		date=table.cell_value(i,3)
		day_of_max = datetime(*xlrd.xldate_as_tuple(date, 0))
	else:
		drawdown=float(max_point-price)/max_point
		if drawdown>max_drawdown:
			max_drawdown=drawdown
			date=table.cell_value(i,3)
			day_of_min= datetime(*xlrd.xldate_as_tuple(date, 0))
			day_of_drawdown=day_of_max
print max_drawdown,day_of_drawdown,day_of_min