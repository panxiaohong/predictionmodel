# -*- coding: utf-8 -*-
import math, os, sys,pickle
import config as Config
from MySqlConn import Mysql

kilo = Config.KILO  # 3000m circle
bias = Config.BIAS  # about house


# --------lon,lat->distance-------
def l2d(lon1, lat1, lon2, lat2):
    # float->rad
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    # haversine公式
    d_lon = lon2 - lon1
    d_lat = lat2 - lat1
    a = math.sin(d_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371
    ans = c * r * 1000
    return ans


# --------price&population---------input float return float
def pp(lon, lat):
    ans = []
    price = 0
    population = 0
    mysql = Mysql()
    result = mysql.getAll("select  * from shelter_info where rooms_total >=0 AND price >=0")
    c_pr = len(result)
    for shelterInfo in result:
        if l2d(lon, lat, shelterInfo['lon'], shelterInfo['lat']) < (kilo + bias):
            price = price + shelterInfo['price']
            population = population + shelterInfo['rooms_total']
    mysql.dispose()

    if c_pr != 0:
        price = price / c_pr
    ans.append(price)
    ans.append(population)
    mysql.dispose()
    return ans  # return int but not string  # --------POI--------input float return int


def poi(lon, lat):
    mysql = Mysql()
    result = mysql.getAll("select  lon,lat,provider_tag from poi")
    tags = mysql.getAll("select id,tag from shop_tag")
    tagsLenders = len(tags)
    ans = [0] * (tagsLenders + 1)
    for poi in result:
        if l2d(lon, lat, poi['lon'], poi['lat']) < kilo:
            keyword = poi['provider_tag'].split(';')[0]
            for tag in tags:
                if tag['tag'] == keyword:
                    ans[tag['id'] - 1] = ans[tag['id'] - 1] + 1
                else:
                    ans[tagsLenders] = ans[tagsLenders] + 1
    mysql.dispose()

    return ans  # --------gps--------input float return int


def gps(lon, lat):
    ans = [0] * 2
    mysql = Mysql()
    result = mysql.getAll(
        "SELECT lon,lat,action  from predict.taxi_info  where date_format(taxi_info.time,'%H') BETWEEN 10 and 22")
    for taxiInfo in result:
        if l2d(lon, lat, taxiInfo['lon'], taxiInfo['lat']) < kilo:
            if taxiInfo['action'] == 'up':
                ans[0] = ans[0] + 1
            else:
                ans[1] = ans[1] + 1

    return ans


def main(params):
    line_new = []
    lon_r = params['lon']
    lat_r = params['lat']
    avgPrice = params['avgPrice']
    pp_r = pp(lon_r, lat_r)
    line_new.append((7, str(pp_r[0])))  # line_new[9]
    line_new.append((8, str(pp_r[1])))  # line_new[10]

    tt = 9
    poi_r = poi(lon_r, lat_r)
    for i in range(len(poi_r) - 1):
        line_new.append((9 + i, str(poi_r[i])))
        tt = tt + 1

    gps_r = gps(lon_r, lat_r)
    line_new.append((tt, str(gps_r[0])))
    line_new.append((tt + 1, str(gps_r[1])))
    line_w = []
    line_w.append(line_new[4])
    line_w.append(line_new[6])
    for i in range(7, len(line_new) - 2):
        line_w.append(line_new[i])
    print line_w
    return line_w


if __name__ == '__main__':
    pre=pickle.load(rf.pickle)
