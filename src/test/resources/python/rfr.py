import math,getopt,os
from sklearn.ensemble import RandomForestRegressor

opts, args = getopt.getopt(sys.argv[1:], "", ["lat=", "lon="])

for opt, vaule in opts:
	if opt == '--lon':
		_lon = vaule
	elif opt == '--lat':
		_lat = vaule

A1 = []
b1 = []
file_package = os.getcwd()+"\data\\";
with open(file_package+'train1.txt','r') as rf:
	for line in rf:
		line_new = line.split(',')
		for i in range(len(line_new)):
			line_new[i] = float(line_new[i])
		A1.append(line_new[1:])
		b1.append(math.log10(line_new[0]))
A2 = []
b2 = []
with open(file_package+'train2.txt','r') as rf:
	for line in rf:
		line_new = line.split(',')
		for i in range(len(line_new)):
			line_new[i] = float(line_new[i])
		A2.append(line_new[1:])
		b2.append(math.log10(line_new[0]))
A3 = []
b3 = []
with open(file_package+'train3.txt','r') as rf:
	for line in rf:
		line_new = line.split(',')
		for i in range(len(line_new)):
			line_new[i] = float(line_new[i])
		A3.append(line_new[1:])
		b3.append(math.log10(line_new[0]))
A4 = []
b4 = []
with open(file_package+'train4.txt','r') as rf:
	for line in rf:
		line_new = line.split(',')
		for i in range(len(line_new)):
			line_new[i] = float(line_new[i])
		A4.append(line_new[1:])
		b4.append(math.log10(line_new[0]))
A5 = []
b5 = []
with open(file_package+'train5.txt','r') as rf:
	for line in rf:
		line_new = line.split(',')
		for i in range(len(line_new)):
			line_new[i] = float(line_new[i])
		A5.append(line_new[1:])
		b5.append(math.log10(line_new[0]))

A_train = A1 + A2 +A3 + A4
b_train = b1 + b2 +b3 + b4
A_test = A5
b_test = b5

rf = RandomForestRegressor()
rf.fit(A_train,b_train)
b_out = rf.predict(A_test)
print b_out
err = []
for i in range(len(b_out)):
	err.append(abs(b_out[i]-b_test[i])/b_test[i])

print sum(err)

print 1-sum(err)/len(err)#accuracy


		