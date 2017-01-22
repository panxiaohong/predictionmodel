# -*- coding: utf-8 -*- 
import math
import string
import os
import sys
reload( sys )
sys.setdefaultencoding('gbk')
type = sys.getfilesystemencoding()
#.decode('utf-8').encode(type)

#---------ini data--------
kilo = 1000   # 3000m circle
bias = 5000   # about house


#--------lon,lat->distance-------
def l2d(lon1,lat1,lon2,lat2):
	#float->rad
	lon1,lat1,lon2,lat2 = map(math.radians,[lon1,lat1,lon2,lat2])	
	#haversine公式
	d_lon = lon2 - lon1
	d_lat = lat2 - lat1
	a = math.sin(d_lat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon/2)**2
	c = 2 * math.asin(math.sqrt(a))
	r = 6371
	ans = c*r*1000
	return ans

#--------price&population---------input float return float
def pp(lon,lat):
	ans = []
	price = 0
	population = 0
	c_pr = 0
	with open(r'E:\social_data_new\house\Beijing_h.csv','r') as rf:
		for line in rf:
			line_new = line.split(',')
			pricepp = float(line_new[-4])
			if line_new[-3] == '':
				populationpp = 0
			else:
				populationpp = int(line_new[-3])
			lonpp = float(line_new[-2])
			latpp = float(line_new[-1][0:-2])
			if l2d(lon,lat,lonpp,latpp)<(kilo+bias):
				if pricepp != 0:
					price = price + pricepp
					c_pr = c_pr + 1 
				#if line_new[3] != '暂无'.decode('utf-8').encode(type):
				population = population + populationpp

		rf.close()
	if c_pr != 0:
		price = price/c_pr
		c_pr = 0
	ans.append(price)
	ans.append(population)
	return ans  #return int but not string
	
#--------POI--------input float return int
def poi(lon,lat):
	ans = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#lenth = 22

	with open(r'E:\social_data_new\BeijingPOI\bjpoi.txt','r') as rf:
		for line in rf:
			line_new = line.split(',')
			if l2d(lon,lat,float(line_new[2]),float(line_new[3]))<kilo:
				keyword = line_new[4].split(';')[0]
				if keyword == '餐饮服务'.decode('utf-8').encode(type):
					ans[0] = ans[0] + 1
				elif keyword == '道路附属设施'.decode('utf-8').encode(type):
					ans[1] = ans[1] + 1
				elif keyword == '地名地址信息'.decode('utf-8').encode(type):
					ans[2] = ans[2] + 1
				elif keyword == '风景名胜'.decode('utf-8').encode(type):
					ans[3] = ans[3] + 1
				elif keyword == '公共设施'.decode('utf-8').encode(type):
					ans[4] = ans[4] + 1
				elif keyword == '公司企业'.decode('utf-8').encode(type):
					ans[5] = ans[5] + 1
				elif keyword == '购物服务'.decode('utf-8').encode(type):
					ans[6] = ans[6] + 1
				elif keyword == '交通设施服务'.decode('utf-8').encode(type):
					ans[7] = ans[7] + 1
				elif keyword == '金融保险服务'.decode('utf-8').encode(type):
					ans[8] = ans[8] + 1
				elif keyword == '科教文化服务'.decode('utf-8').encode(type):
					ans[9] = ans[9] + 1
				elif keyword == '摩托车服务'.decode('utf-8').encode(type):
					ans[10] = ans[10] + 1
				elif keyword == '汽车服务'.decode('utf-8').encode(type):
					ans[11] = ans[11] + 1
				elif keyword == '汽车维修'.decode('utf-8').encode(type):
					ans[12] = ans[12] + 1
				elif keyword == '汽车销售'.decode('utf-8').encode(type):
					ans[13] = ans[13] + 1
				elif keyword == '商务住宅'.decode('utf-8').encode(type):
					ans[14] = ans[14] + 1
				elif keyword == '生活服务'.decode('utf-8').encode(type):
					ans[15] = ans[15] + 1
				elif keyword == '体育休闲服务'.decode('utf-8').encode(type):
					ans[16] = ans[16] + 1
				elif keyword == '通行设施'.decode('utf-8').encode(type):
					ans[17] = ans[17] + 1
				elif keyword == '医疗保健服务'.decode('utf-8').encode(type):
					ans[18] = ans[18] + 1
				elif keyword == '政府机构及社会团体'.decode('utf-8').encode(type):
					ans[19] = ans[19] + 1
				elif keyword == '住宿服务'.decode('utf-8').encode(type):
					ans[20] = ans[20] + 1
				else:
					ans[21] = ans[21] + 1
		rf.close()		
	return ans
	
	
#--------gps--------input float return int
def gps(lon,lat):	
	ans = [0,0]
	with open(r'E:\social_data_new\BJGPS_updown\20140607.txt','r') as rf:
		for line in rf:
			line_new = line.split()
			#lat lon not lon lat
			if l2d(lon,lat,float(line_new[4]),float(line_new[3]))<kilo:
				if 10<int(line_new[2].split(':')[0])<22:
					if line_new[5] == 'up':
						ans[0] = ans[0] + 1
					else:
						ans[1] = ans[1] + 1
		rf.close()
	return ans
'''
#--------gps--------input float return int
def gps(lon,lat):
	
	ans = [0,0,0,0]
	ans[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # weekday 24h up
	ans[1] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # weekday 24h down
	ans[2] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # weekend 24h up
	ans[3] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # weekend 24h down
	#20140602-06 monday-friday 
	with open(r'E:\social_data_new\BJGPS_updown\20140604.txt','r') as rf:
		for line in rf:
			line_new = line.split()
			#lat lon not lon lat
			if l2d(lon,lat,float(line_new[4]),float(line_new[3]))<kilo:
				if line_new[2].split(':')[0]=='00':
					if line_new[5] == 'up':
						ans[0][0] = ans[0][0] + 1
					else: ans[1][0] = ans[1][0] + 1
				if line_new[2].split(':')[0]=='01':
					if line_new[5] == 'up':
						ans[0][1] = ans[0][1] + 1
					else: ans[1][1] = ans[1][1] + 1
				if line_new[2].split(':')[0]=='02':
					if line_new[5] == 'up':
						ans[0][2] = ans[0][2] + 1
					else: ans[1][2] = ans[1][2] + 1
				if line_new[2].split(':')[0]=='03':
					if line_new[5] == 'up':
						ans[0][3] = ans[0][3] + 1
					else: ans[1][3] = ans[1][3] + 1
				if line_new[2].split(':')[0]=='04':
					if line_new[5] == 'up':
						ans[0][4] = ans[0][4] + 1
					else: ans[1][4] = ans[1][4] + 1
				if line_new[2].split(':')[0]=='05':
					if line_new[5] == 'up':
						ans[0][5] = ans[0][5] + 1
					else: ans[1][5] = ans[1][5] + 1
				if line_new[2].split(':')[0]=='06':
					if line_new[5] == 'up':
						ans[0][6] = ans[0][6] + 1
					else: ans[1][6] = ans[1][6] + 1
				if line_new[2].split(':')[0]=='07':
					if line_new[5] == 'up':
						ans[0][7] = ans[0][7] + 1
					else: ans[1][7] = ans[1][7] + 1
				if line_new[2].split(':')[0]=='08':
					if line_new[5] == 'up':
						ans[0][8] = ans[0][8] + 1
					else: ans[1][8] = ans[1][8] + 1
				if line_new[2].split(':')[0]=='09':
					if line_new[5] == 'up':
						ans[0][9] = ans[0][9] + 1
					else: ans[1][9] = ans[1][9] + 1
				if line_new[2].split(':')[0]=='10':
					if line_new[5] == 'up':
						ans[0][10] = ans[0][10] + 1
					else: ans[1][10] = ans[1][10] + 1
				if line_new[2].split(':')[0]=='11':
					if line_new[5] == 'up':
						ans[0][11] = ans[0][11] + 1
					else: ans[1][11] = ans[1][11] + 1
				if line_new[2].split(':')[0]=='12':
					if line_new[5] == 'up':
						ans[0][12] = ans[0][12] + 1
					else: ans[1][12] = ans[1][12] + 1
				if line_new[2].split(':')[0]=='13':
					if line_new[5] == 'up':
						ans[0][13] = ans[0][13] + 1
					else: ans[1][13] = ans[1][13] + 1
				if line_new[2].split(':')[0]=='14':
					if line_new[5] == 'up':
						ans[0][14] = ans[0][14] + 1
					else: ans[1][14] = ans[1][14] + 1
				if line_new[2].split(':')[0]=='15':
					if line_new[5] == 'up':
						ans[0][15] = ans[0][15] + 1
					else: ans[1][15] = ans[1][15] + 1
				if line_new[2].split(':')[0]=='16':
					if line_new[5] == 'up':
						ans[0][16] = ans[0][16] + 1
					else: ans[1][16] = ans[1][16] + 1
				if line_new[2].split(':')[0]=='17':
					if line_new[5] == 'up':
						ans[0][17] = ans[0][17] + 1
					else: ans[1][17] = ans[1][17] + 1
				if line_new[2].split(':')[0]=='18':
					if line_new[5] == 'up':
						ans[0][18] = ans[0][18] + 1
					else: ans[1][18] = ans[1][18] + 1
				if line_new[2].split(':')[0]=='19':
					if line_new[5] == 'up':
						ans[0][19] = ans[0][19] + 1
					else: ans[1][19] = ans[1][19] + 1
				if line_new[2].split(':')[0]=='20':
					if line_new[5] == 'up':
						ans[0][20] = ans[0][20] + 1
					else: ans[1][20] = ans[1][20] + 1
				if line_new[2].split(':')[0]=='21':
					if line_new[5] == 'up':
						ans[0][21] = ans[0][21] + 1
					else: ans[1][21] = ans[1][21] + 1
				if line_new[2].split(':')[0]=='22':
					if line_new[5] == 'up':
						ans[0][22] = ans[0][22] + 1
					else: ans[1][22] = ans[1][22] + 1
				if line_new[2].split(':')[0]=='23':
					if line_new[5] == 'up':
						ans[0][23] = ans[0][23] + 1
					else: ans[1][23] = ans[1][23] + 1				
		rf.close()	


				


	with open(r'E:\social_data_new\BJGPS_updown\20140607.txt','r') as rf:
		for line in rf:
			line_new = line.split()
			#lat lon not lon lat
			if l2d(lon,lat,float(line_new[4]),float(line_new[3]))<kilo:
				if line_new[2].split(':')[0]=='00':
					if line_new[5] == 'up':
						ans[2][0] = ans[2][0] + 1
					else: ans[3][0] = ans[3][0] + 1
				if line_new[2].split(':')[0]=='01':
					if line_new[5] == 'up':
						ans[2][1] = ans[2][1] + 1
					else: ans[3][1] = ans[3][1] + 1
				if line_new[2].split(':')[0]=='02':
					if line_new[5] == 'up':
						ans[2][2] = ans[2][2] + 1
					else: ans[3][2] = ans[3][2] + 1
				if line_new[2].split(':')[0]=='03':
					if line_new[5] == 'up':
						ans[2][3] = ans[2][3] + 1
					else: ans[3][3] = ans[3][3] + 1
				if line_new[2].split(':')[0]=='04':
					if line_new[5] == 'up':
						ans[2][4] = ans[2][4] + 1
					else: ans[3][4] = ans[3][4] + 1
				if line_new[2].split(':')[0]=='05':
					if line_new[5] == 'up':
						ans[2][5] = ans[2][5] + 1
					else: ans[3][5] = ans[3][5] + 1
				if line_new[2].split(':')[0]=='06':
					if line_new[5] == 'up':
						ans[2][6] = ans[2][6] + 1
					else: ans[3][6] = ans[3][6] + 1
				if line_new[2].split(':')[0]=='07':
					if line_new[5] == 'up':
						ans[2][7] = ans[2][7] + 1
					else: ans[3][7] = ans[3][7] + 1
				if line_new[2].split(':')[0]=='08':
					if line_new[5] == 'up':
						ans[2][8] = ans[2][8] + 1
					else: ans[3][8] = ans[3][8] + 1
				if line_new[2].split(':')[0]=='09':
					if line_new[5] == 'up':
						ans[2][9] = ans[2][9] + 1
					else: ans[3][9] = ans[3][9] + 1
				if line_new[2].split(':')[0]=='10':
					if line_new[5] == 'up':
						ans[2][10] = ans[2][10] + 1
					else: ans[3][10] = ans[3][10] + 1
				if line_new[2].split(':')[0]=='11':
					if line_new[5] == 'up':
						ans[2][11] = ans[2][11] + 1
					else: ans[3][11] = ans[3][11] + 1
				if line_new[2].split(':')[0]=='12':
					if line_new[5] == 'up':
						ans[2][12] = ans[2][12] + 1
					else: ans[3][12] = ans[3][12] + 1
				if line_new[2].split(':')[0]=='13':
					if line_new[5] == 'up':
						ans[2][13] = ans[2][13] + 1
					else: ans[3][13] = ans[3][13] + 1
				if line_new[2].split(':')[0]=='14':
					if line_new[5] == 'up':
						ans[2][14] = ans[2][14] + 1
					else: ans[3][14] = ans[3][14] + 1
				if line_new[2].split(':')[0]=='15':
					if line_new[5] == 'up':
						ans[2][15] = ans[2][15] + 1
					else: ans[3][15] = ans[3][15] + 1
				if line_new[2].split(':')[0]=='16':
					if line_new[5] == 'up':
						ans[2][16] = ans[2][16] + 1
					else: ans[3][16] = ans[3][16] + 1
				if line_new[2].split(':')[0]=='17':
					if line_new[5] == 'up':
						ans[2][17] = ans[2][17] + 1
					else: ans[3][17] = ans[3][17] + 1
				if line_new[2].split(':')[0]=='18':
					if line_new[5] == 'up':
						ans[2][18] = ans[2][18] + 1
					else: ans[3][18] = ans[3][18] + 1
				if line_new[2].split(':')[0]=='19':
					if line_new[5] == 'up':
						ans[2][19] = ans[2][19] + 1
					else: ans[3][19] = ans[3][19] + 1
				if line_new[2].split(':')[0]=='20':
					if line_new[5] == 'up':
						ans[2][20] = ans[2][20] + 1
					else: ans[3][20] = ans[3][20] + 1
				if line_new[2].split(':')[0]=='21':
					if line_new[5] == 'up':
						ans[2][21] = ans[2][21] + 1
					else: ans[3][21] = ans[3][21] + 1
				if line_new[2].split(':')[0]=='22':
					if line_new[5] == 'up':
						ans[2][22] = ans[2][22] + 1
					else: ans[3][22] = ans[3][22] + 1
				if line_new[2].split(':')[0]=='23':
					if line_new[5] == 'up':
						ans[2][23] = ans[2][23] + 1
					else: ans[3][23] = ans[3][23] + 1				
		rf.close()	
	return ans
'''

#--------update res--------	
#主程序入口

lon_r = 121.5#............前段传递的经度................
lat_r = 31.2#............前段传递的经度................
line_new = []
pp_r = pp(lon_r,lat_r)
line_new.append(7,str(pp_r[0]))   #line_new[9]
line_new.append(8,str(pp_r[1]))   #line_new[10]

tt = 9
poi_r = poi(lon_r,lat_r)
for i in range(len(poi_r)-1):
	line_new.append(9+i,str(poi_r[i]))
	tt = tt+1

gps_r = gps(lon_r,lat_r)
line_new.append(tt,str(gps_r[0]))
line_new.append(tt+1,str(gps_r[1]))
#print line_new
line_w.append(line_new[4])
line_w.append(line_new[6])
for i in range(7,len(line_new)-2):
	line_w.append(line_new[i])
print line_w#.................将周围环境数据根据经纬度对应出来..............
wf.writelines(','.join(line_w))
wf.writelines('\n')



