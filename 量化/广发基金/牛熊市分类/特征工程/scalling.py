import xlrd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import GradientBoostingClassifier
from numpy import vstack, array, nan
from minepy import MINE
from scipy.stats import pearsonr
from sklearn.feature_selection import chi2

def mic(x, y):
	m = MINE()
	m.compute_score(x, y)
	return (m.mic(), 0.5)

data = xlrd.open_workbook('raw_data' + '.xlsx')
table = data.sheets()[0]

cout = open('processed_data.txt', 'w')

nrows=table.nrows
raw_data=[]
label=[]

for i in range(0,nrows):
	label.append(table.cell(i,0).value)
	data_point=[]
	for j in range(1,12):
		data_point.append(table.cell(i,j).value)
	raw_data.append(data_point)

norm_data=StandardScaler().fit_transform(raw_data)
scale_data=MinMaxScaler().fit_transform(norm_data)
SelectKBest(lambda X, Y: array(map(lambda x:pearsonr(x, Y), X.T)).T, k='all').fit_transform(scale_data, label)
SelectKBest(chi2, k=2).fit_transform(raw_data, label)
SelectKBest(lambda X, Y: array(map(lambda x:mic(x, Y), X.T)).T, k=2).fit_transform(raw_data, label)
SelectFromModel(GradientBoostingClassifier()).fit_transform(raw_data, label)
#poly_data=PolynomialFeatures().fit_transform(scale_data)
output_data=poly_data

length=len(output_data[0])
for i in range(0,nrows):
	cout.write(str(label[i])+'\t')
	#print str(i)
	for j in range(0,length):	
		#print '\t'+str(j)+'\n'
		cout.write(str(output_data[i][j])+'\t')
	cout.write('\n')
cout.write('\n')
cout.flush()
cout.close()