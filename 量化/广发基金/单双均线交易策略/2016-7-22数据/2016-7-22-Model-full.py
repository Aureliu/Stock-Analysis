# coding=utf-8  

import xlrd
import string
# Offset is from 0
cout = open('2016-7-22-Model-result.txt', 'w')
data = xlrd.open_workbook('2016-7-22-Model' + '.xlsx')
table = data.sheets()[0]
nrows = table.nrows
flag=1
money=1
volumn=0
for i in range(3,nrows):
	if(flag and table.cell(i,4).value>=table.cell(i,5).value):
		volumn=float(money)/table.cell(i,4).value
		money=0
		flag=0
	if(not flag and table.cell(i,4).value<table.cell(i,5).value):
		flag=1
		money=table.cell(i,4).value*volumn
		volumn-0
	temp=volumn*table.cell(i,4).value
	if(money):
		cout.write(repr(table.cell(i,4).value) + '\t' + repr(money) + '\n')
	else:
		cout.write(repr(table.cell(i,4).value) + '\t' + repr(temp) + '\n')
cout.flush()
cout.close()



