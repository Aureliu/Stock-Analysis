from datetime import datetime, timedelta
import xlrd
import string

# Offset is from 0
cout = open('discount.txt', 'w')

data = xlrd.open_workbook('discount rate' + '.xlsx')
table = data.sheets()[1]
nrows = table.nrows
month=10
total=0.0
number=0.0
for i in range(2,nrows):
	date=table.cell_value(i,0)
	time = datetime(*xlrd.xldate_as_tuple(date, 0))
	if time.month==month:
		total+=table.cell_value(i,1)
		number+=1
	else:
		cout.write(repr(time.year) + '-' + repr(month)+'\t'+repr(total/number)+'\n')
		total=table.cell_value(i,1)
		number=1
		month=time.month
cout.write(repr(time.year) + '-' + repr(month)+'\t'+repr(total/number)+'\n')

table = data.sheets()[0]
nrows = table.nrows
month=4
total=0.0
number=0.0
for i in range(2,nrows):
	date=table.cell_value(i,0)
	time = datetime(*xlrd.xldate_as_tuple(date, 0))
	if time.month==month:
		total+=table.cell_value(i,1)
		number+=1
	else:
		cout.write(repr(time.year) + '-' + repr(month)+'\t'+repr(total/number)+'\n')
		total=table.cell_value(i,1)
		number=1
		month=time.month
cout.write(repr(time.year) + '-' + repr(month)+'\t'+repr(total/number)+'\n')

cout.flush()
cout.close()


