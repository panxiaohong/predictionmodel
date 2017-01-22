from sklearn.ensemble import RandomForestRegressor
import math

A1 = []
b1 = []
with open(r'E:\social_data_new\res_bj\coffee\star\train1.txt','r') as rf:
	for line in rf:
		line_new = line.split(',')
		for i in range(len(line_new)):
			line_new[i] = float(line_new[i])
		A1.append(line_new[1:])
		b1.append(math.log10(line_new[0]))
A2 = []
b2 = []
with open(r'E:\social_data_new\res_bj\coffee\star\train2.txt','r') as rf:
	for line in rf:
		line_new = line.split(',')
		for i in range(len(line_new)):
			line_new[i] = float(line_new[i])
		A2.append(line_new[1:])
		b2.append(math.log10(line_new[0]))
A3 = []
b3 = []
with open(r'E:\social_data_new\res_bj\coffee\star\train3.txt','r') as rf:
	for line in rf:
		line_new = line.split(',')
		for i in range(len(line_new)):
			line_new[i] = float(line_new[i])
		A3.append(line_new[1:])
		b3.append(math.log10(line_new[0]))
A4 = []
b4 = []
with open(r'E:\social_data_new\res_bj\coffee\star\train4.txt','r') as rf:
	for line in rf:
		line_new = line.split(',')
		for i in range(len(line_new)):
			line_new[i] = float(line_new[i])
		A4.append(line_new[1:])
		b4.append(math.log10(line_new[0]))
A5 = []
b5 = []
with open(r'E:\social_data_new\res_bj\coffee\star\train5.txt','r') as rf:
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
err = []
for i in range(len(b_out)):
	err.append(abs(b_out[i]-b_test[i])/b_test[i])

print 1-sum(err)/len(err)#accuracy


		