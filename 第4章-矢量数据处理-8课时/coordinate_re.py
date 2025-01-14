#判断方位
import re
clas1 = ['顾舒扬，来自浙江省杭州市（经度：120.27047，纬度：30.18751，海拔：10米）。',
'周全，来自四川省乐山市（ 经度:103.7654,纬度:29.5522 ,海拔：320米）。',
'余金珂，来自四川省乐山市（ 经度:103.7654,纬度:29.5522 ,海拔：320米）。',
'张钰婷，来自甘肃省金昌市（经度：102.1946，纬度：38.5258，海拔：1400米）。',
'吕杭，来自云南省红河州蒙自市（精度：103.13，纬度：23.03，海拔：1307米）。',
'魏宇涵，来自福建省泉州市（经度：118.2649，纬度：24.2642，海拔：165米）。',
'胡晟昊，来自湖北省襄阳市（经度：110.453，纬度：31.133，海拔：302米）。',]
clas2 = ['蔡熠，来自福建省莆田市（ 经度:119°00′27″,纬度:24°08′44″,海拔：24米）。',
'杨彭武，来自云南省昆明市（经度：102.850，纬度：24.827，海拔：2008米）。',
'卢玉，来自云南省曲靖市（经度：103.7947，维度：25.4961，海拔：2000米）。',
'李晓涛，来自浙江省杭州市（经度：120.27047，纬度：30.18751，海拔：10米）。',
'尹鹏翔，来自山东省日照市（经度：118.250，纬度：35.416，海拔：27米）。',
'任康妮，来自山西省吕梁市（经度：111.144，纬度：37.518，海拔：1161米）。',
'岩叫，来自云南省景洪市（经度：100°25′E，纬度：21°27′N）。',]
clas3 = ['陈禹彤，来自内蒙古赤峰市（ 经度:118.525814,纬度:42.152350 ,海拔：320米）。',
'姜春阳，来自内蒙古赤峰市（经度：116.170，维度：41.120，海拔：2000米）。',
'林丹妮，来自浙江省温州市（经度:120.4373，纬度:27.7247，海拔：119米）。',
'李齐力，来自湖北省仙桃市（经度：113.450，纬度：30.336，海拔：21.5米）。',
'李良瑞，来自四川省成都市（经度：103.40，纬度：30.54，海拔：594米）。',
'任昶旭，来自山东省潍坊市（经度：119.107，纬度：36.70925，海拔：23米）。',
'王盈怡，来自湖南省娄底市（经度：110.1278，纬度：27.4567，海报：170米）。',]
clas4 = ['连思强，来自福建省莆田市（经度：118.68，纬度：25.37，海拔：78米）。',
'连军瑜，来自福建省泉州市（经度：118.37°E，纬度：24.54°N，海拔：301米）。',
'张宇航，来自重庆市綦江区（经度：106.550°E，纬度：29.570°N，海拔：237米）。',
'刘明岳，来自内蒙古赤峰市（经度：116.170，维度：41.120，海拔：2000米）。',
'牟兵，来自四川省泸州市（经度：105.08.52E，纬度：28.26.18N，海拔：649米）。',
'李世鑫，来自云南省昭通市（经度：103°.68′，纬度：27.37′，海拔：1685米）。',
'邓灿，来自湖北省黄冈市（经度：115.95°E, 纬度:30.076°N，海拔:39米）。',]
clas5 = ['陈鑫，来自湖北省黄冈市 （经度：114.87°E，纬度：30.44°N，海拔：90米）。',
'杨玲坪，来自云南省大理白族自治州（经度：100.2117°E，纬度：25.6126°N，海拔：2019米）。',
'奚剑波，来自重庆市潼南（经度：106.55°E，纬度：25.6126°N，海拔：238米）。',
'蒋志颖，来自云南省大理白族自治州（经度：100.2117°E，纬度：25.6126°N，海拔：2019米）。',
'李毓梁，来自云南省昭通市（经度：103.717，纬度：27.338，海拔：1685米）。',
'陈龙，来自云南省曲靖市（经度：103.80，纬度：25.50，海拔：2000米）。',
'涂世彤，来自云南省昭通市（ 经度:103.7065,纬度:27.3200 ,海拔：1685米）。',]
clas6 = ['刘可一，来自河南省郑州市（经度：113°39E，纬度：34°48N，海拔：108米）。',
'娜海，来自云南省普洱市（经度：100.45，纬度：22.40，海拔：2350米）。',
'聂梦婷，来自重庆市（经度：106.33E，维度：29.35N，海拔：221米）。',
'赵秋月，来自广西靖西市（经度：105.45°E，纬度：23.56°N，海拔：750米）。']
yncoorlon = 102.851
yncoorla = 24.841
longtitude = []
latitude = []
sum = 0
for string in clas3:
    num = re.findall(r'\d+\.+\d+',string)
    longtitude.append(float(num[0]))
    latitude.append(float(num[1]))
print(longtitude)
print(latitude)
for string in clas3:
    match = re.search(r'([\u4e00-\u9fff]+)，',string)
    for i in range(0,len(longtitude)):
        if(longtitude[i]>yncoorlon):
            if(latitude[i]>yncoorla):
                print("%s在学校东北方" % match.group(1))
            else:
                print("%s在学校东南方" % match.group(1))
            sum += 1
        else:
            if(latitude[i]>yncoorla):
                print("%s在学校西北方" % match.group(1))
            else:
                print("%s在学校西南方" % match.group(1))
            sum += 1
        break
print(sum)



        