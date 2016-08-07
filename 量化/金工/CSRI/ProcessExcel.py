# coding=utf-8  

import xlrd
import string
# Offset is from 0
dic = dict()
industry_name = dict()
cout = open('Result.txt', 'w')
data = xlrd.open_workbook('201303' + '.xlsx')
table = data.sheets()[0]
nrows = table.nrows
old = ''
for i in range(2,nrows):
	industry = table.cell(i,1).value
	if(industry == ''):
		industry = old
	else:
		old =  industry
		industry_name[industry] = table.cell(i,2).value
	industry = int(industry)
	index = int(table.cell(i,3).value)
	dic [index] = industry
table = data.sheets()[1]
nrows = table.nrows
for i in range(2,nrows):
	industry = table.cell(i,1).value
	if(industry == ''):
		industry = old
	else:
		old =  industry
		industry_name[industry] = table.cell(i,2).value
	industry = int(industry)
	index = int(table.cell(i,3).value)
	dic [index] = industry

FileName = ['201304','201401','201402','201403','201404','201501','201502','201503','201504',]
timemap = dict({'201304':'20140102','201401':'20140403','201402':'20140701','201403':'20141013','201404':'20150122','201501':'20150504','201502':'20150720','201503':'20151027','201504':'20160304'})
for name in FileName:
	data = xlrd.open_workbook(name + '.xlsx')
	table = data.sheets()[0]
	nrows = table.nrows
	for i in range(2,nrows):
		industry = table.cell(i,1).value
		if(industry == ''):
			industry = old
		else:
			old =  industry
		industry = int(industry)
		index = int(table.cell(i,3).value)
		if not index in dic:
			dic [index] = industry
			#print str(index) + '\t' + str(industry) + '\t' + timemap[industry]
		if dic [index] != industry:
			#print 'OK'
			oldindustry = dic [index]
			dic [index] = industry
			sup = 0
			if len(str(index)) < 6:
				sup = 6 - len(str(index))
			cout.write( sup * '0' + str(index) + '\t' + table.cell(i,4).value.encode("utf-8") + '\t' + str(oldindustry)  + '\t' + industry_name[oldindustry].encode("utf-8") + '\t' + str(industry) + '\t' + industry_name[industry].encode("utf-8") + '\t' + name + '\t' + timemap[name] + '\n')
	table = data.sheets()[1]
	nrows = table.nrows
	for i in range(2,nrows):
		industry = table.cell(i,1).value
		if(industry == ''):
			industry = old
		else:
			old =  industry
		industry = int(industry)
		index = int(table.cell(i,3).value)
		if not index in dic:
			dic [index] = industry
			#print str(index) + '\t' + str(industry) + '\t' + timemap[industry]
		if dic [index] != industry:
			#print 'OK'
			oldindustry = dic [index]
			dic [index] = industry
			sup = 0
			if len(str(index)) < 6:
				sup = 6 - len(str(index))
			#print sup * '0'  + str(index) + '\t' + str(table.cell(i,4).value) + '\t' + str(oldindustry)  + '\t' + industry_name[oldindustry] + '\t' + str(industry) + '\t' + industry_name[industry]  + '\t' + name + '\t' + timemap[name] + '\n'
			cout.write( sup * '0' + str(index) + '\t' + table.cell(i,4).value.encode("utf-8") + '\t' + str(oldindustry)  + '\t' + industry_name[oldindustry].encode("utf-8") + '\t' + str(industry) + '\t' + industry_name[industry].encode("utf-8") + '\t' + name + '\t' + timemap[name] + '\n')

cout.flush()
cout.close()
