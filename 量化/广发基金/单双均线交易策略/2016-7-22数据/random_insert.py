# coding=utf-8  

import xlrd
import string
import random
from datetime import datetime, timedelta

def adjustPosition(money,volumn,price,state):
	total=money+price*volumn
	#print '\n'+"Adjust 1:"+repr(total)
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

def maxDrawdown(list_value):
	#Offset is from 0
	nrows = len(list_value)
	max_drawdown=0
	max_point=0
	price=0
	drawdown=0
	day_of_max=0
	day_of_drawdown=0
	day_of_min=0
	for i in range(0,nrows):
		price=list_value[i]
		if(price>max_point):
			max_point=price
		else:
			drawdown=float(max_point-price)/max_point
			if drawdown>max_drawdown:
				max_drawdown=drawdown
	return max_drawdown

# Offset is from 0
cout = open('2016-7-22-Model-Dynamic-random-insert.txt', 'w')
data = xlrd.open_workbook('2016-7-22-Model' + '.xlsx')
table = data.sheets()[0]
nrows = 2365
for j in range(1,101):
	start=random.randint(3, nrows)  # Integer from 1 to 10, endpoints included
	state=1  ## money is available
	money=0.4
	flag=0
	start_day=start
	interest=0.03/365
	volumn=float(0.6)/table.cell(start,4).value
	start_price=decay_price=table.cell(start,4).value
	value_list = [1]
	for i in range(start,nrows):
		money+=money*interest
		decay_price=0.5*table.cell(i,4).value+0.5*decay_price
		flag_temp=table.cell(i,4).value>=table.cell(i,5).value
		#print money,volumn*table.cell(i,4).value
		if ((flag_temp is not flag) or ((i-start_day)>=10 and ((flag_temp and decay_price>start_price) or (not flag_temp and decay_price < start_price)))):
			#print i,flag_temp,flag_temp,
			if(flag_temp==1 and state<4):
				state+=1
				start_day=i
				flag=flag_temp
				start_price=table.cell(i,4).value
				money,volumn = adjustPosition(money,volumn,start_price,state)
			if(flag_temp==0 and state>1):
				state-=1
				start_day=i
				flag=flag_temp
				start_price=table.cell(i,4).value
				money,volumn = adjustPosition(money,volumn,start_price,state)
			value_list.append(money+volumn*table.cell(i,4).value)
	drawdown= maxDrawdown(value_list)
	start_date=table.cell_value(start,3)
	end_date=table.cell_value(nrows-1,3)
	money=money+volumn*table.cell(nrows-1,4).value
	year=(end_date-start_date)/365
	gain_model=money**(1/year)
	gain_wind=(table.cell(nrows-1,4).value/table.cell(start,4).value)**(1/year)
	print repr(j)+'\t'+repr(year) + '\t' + repr(table.cell(nrows-1,4)) + '\t' + repr(1/year) + '\t' + repr(gain_model)
	date=table.cell_value(start,3)
	time= datetime(*xlrd.xldate_as_tuple(date, 0))
	cout.write(repr(time.year) + '-' + repr(time.month)+ '-' + repr(time.day) + '\t' + repr(money)  + '\t' + repr(drawdown)  + '\t' + repr(gain_model-1)+ '\t' + repr(gain_wind-1) + '\n')
cout.flush()
cout.close()






