# -*- coding: utf-8 -*- 
import string,os
#6月1号到10号，

file_package = os.getcwd()+"\data\\";
for k in range(1,10):
	wf = open(file_package+'2014060'+str(k)+'.txt','a')
	line_buff = ['0','0','0','0','0','0']
	line_last = '0'
	with open(file_package+'2014060'+str(k)+'.txt','r') as rf:
		for line in rf:
			line_new = line.split()
			if (line_new[0]!=line_buff[0]) | (line_new[5]!=line_buff[5]):
				if (line_new[0]==line_buff[0]) & (line_new[5]!=line_buff[5]):
					if line_last != '0':
						wf.writelines(line_last)
				wf.writelines(line)
				line_buff=line_new
			else:
				line_last = line
		wf.close()
		rf.close()
print 'finish'