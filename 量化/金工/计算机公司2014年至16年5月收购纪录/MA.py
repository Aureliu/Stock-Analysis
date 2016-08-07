# coding=utf-8  

import xlrd
import string
# Offset is from 0
stock_index = set()
cout = open('Seleted_MAII.txt','w')
data = xlrd.open_workbook("计算机公司" + '.xlsx')
table = data.sheets()[0]
nrows = table.nrows
for i in range(0, nrows):
	stock_index.add(table.cell(i,0).value)

#cout = open('并购事件.xlsx', 'w')
data = xlrd.open_workbook('并购事件' + '.xlsx')
table = data.sheets()[0]
nrows = table.nrows
for i in range(1, nrows):
	flag = False
	for s in stock_index:
		if s in table.cell(i,2).value:
			flag = True;
			break;
	if(flag):
		for j in range(table.ncols):
			cout.write( table.row_values(i)[j].encode("utf-8") + '\t')
		cout.write('\n')