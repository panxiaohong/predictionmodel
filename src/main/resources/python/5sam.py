# -*- coding: utf-8 -*- 

import random
#ss='\coffee'

count = 0
with open(r'E:\social_data_new\res_bj\coffee\shangdao\sdcoffee_log_t.txt','r') as rf:
	for line in rf:
		count = count+1

line_num = count
e = int(round(line_num*0.2))
a = range(1,line_num+1)
random.shuffle(a)
b1 = a[:e]
b2 = a[e:2*e]
b3 = a[2*e:3*e]
b4 = a[3*e:4*e]
b5 = a[4*e:]

wf_b1 = open(r'E:\social_data_new\res_bj\coffee\shangdao\t5\train1.txt','a')
wf_b2 = open(r'E:\social_data_new\res_bj\coffee\shangdao\t5\train2.txt','a')
wf_b3 = open(r'E:\social_data_new\res_bj\coffee\shangdao\t5\train3.txt','a')
wf_b4 = open(r'E:\social_data_new\res_bj\coffee\shangdao\t5\train4.txt','a')
wf_b5 = open(r'E:\social_data_new\res_bj\coffee\shangdao\t5\train5.txt','a')


c = 1
with open(r'E:\social_data_new\res_bj\coffee\shangdao\sdcoffee_log_t.txt','r') as rf:
	for line in rf:
		if c in b1:
			c = c + 1
			wf_b1.writelines(line)
		elif c in b2:
			c = c + 1
			wf_b2.writelines(line)
		elif c in b3:
			c = c + 1
			wf_b3.writelines(line)
		elif c in b4:
			c = c + 1
			wf_b4.writelines(line)
		elif c in b5:
			c = c + 1
			wf_b5.writelines(line)
		else:
			c = c + 1
			print 11111111
	wf_b1.close()
	wf_b2.close()
	wf_b3.close()
	wf_b4.close()
	wf_b5.close()
	rf.close()
print 'finish'

'''
c = 1
i = 0
flag = 0

wf_train = open(r'E:\social_data_new\res_bj'+ss+'\\t\data_train.txt','a')
wf_test = open(r'E:\social_data_new\res_bj'+ss+'\\t\data_test.txt','a')
with open(r'E:\social_data_new\res_bj'+ss+ss+'_log_t.txt','r') as rf:
	for line in rf:
		if (c == b[i])and(flag == 0):
			wf_test.writelines(line)
			c = c + 1			
			i = i + 1
			if i == len(b):
				flag = 1
				i = 0
		else:
			wf_train.writelines(line)
			c = c + 1
	wf_test.close()
	wf_train.close()
	rf.close()
print 'finish'
'''