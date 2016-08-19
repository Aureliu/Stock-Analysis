import xlrd

cout = open('hs300_stock.txt', 'w')

data = xlrd.open_workbook('composition' + '.xlsx')
table1 = data.sheets()[0]
table2 = data.sheets()[1]

stock_set=set()
nrows = table1.nrows
for i in range(1,nrows-1):
	stock_set.add(table1.cell(i,1).value.encode("utf-8"))

nrows = table2.nrows
for i in range(1,nrows-1):
	stock = table2.cell(i,1).value.encode("utf-8")
	if stock in stock_set:
		cout.write(stock+ '\n')

cout.flush()
cout.close()
