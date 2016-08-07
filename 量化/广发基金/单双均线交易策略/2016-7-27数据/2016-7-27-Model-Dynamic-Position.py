# coding=utf-8  

import xlrd
import string

def adjustPosition(money,volumn,price,state):
	total=money+price*volumn
	alpha=0
	if(state==1):
		alpha=0.6
	elif(state==2):
		alpha=0.7
	elif(state==3):
		alpha=0.8
	else:
		alpha=0.9
	money=total*(1-alpha)
	volumn=total*alpha/price
	return money,volumn

# Offset is from 0
cout = open('2016-7-27-Model-result-Dynamic.txt', 'w')
data = xlrd.open_workbook('2016-7-27-Model' + '.xlsx')
table = data.sheets()[0]
nrows = table.nrows
state=1  ## money is available
money=0.4
flag=0
start_day=3
interest=0.03/365
volumn=float(0.6)/table.cell(3,2).value
start_price=decay_price=table.cell(3,4).value
for i in range(3,nrows):
	money+=money*interest
	decay_price=0.5*table.cell(i,4).value+0.5*decay_price
	flag_temp=table.cell(i,4).value>=table.cell(i,5).value

	print money,volumn*table.cell(i,4).value
	if ((flag_temp is not flag) or ((i-start_day)>=10 and ((flag_temp and decay_price>start_price) or (not flag_temp and decay_price < start_price)))):
		print i,flag_temp,flag_temp,
		if(flag_temp==1 and state<4):
			state+=1
			start_day=i
			flag=flag_temp
			start_price=table.cell(i,4).value
			money,volumn = adjustPosition(money,volumn,table.cell(i,2).value,state)
		if(flag_temp==0 and state>1):
			state-=1
			start_day=i
			flag=flag_temp
			start_price=table.cell(i,4).value
			money,volumn = adjustPosition(money,volumn,table.cell(i,2).value,state)
	cout.write(repr(table.cell(i,4).value) + '\t' + repr(money+volumn*table.cell(i,2).value) + '\n')
cout.flush()
cout.close()






