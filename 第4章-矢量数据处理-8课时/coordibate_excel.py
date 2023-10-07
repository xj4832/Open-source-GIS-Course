import openpyxl
workbook = openpyxl.load_workbook('E:\QGIS课件\Open-source-GIS-Course-main_del\新建文件夹\坐标.xlsx')
worksheet = workbook['坐标']
name = []
for cellA in worksheet['A']:
    name.append(cellA.value)

longtitude = []
latitude = []
for cellC in worksheet['C']:
    longtitude.append(cellC.value)
for cellD in worksheet['D']:
    latitude.append(cellD.value)

#print(name)
#print(longtitude)
#print(latitude)
yncoorlon = 102.851
yncoorla = 24.841
sum_db = 0
sum_dn = 0
sum_xb = 0
sum_xn = 0
for i in range(1,40):
    if(longtitude[i]>yncoorlon and latitude[i]>yncoorla):
        print("%s在学校东北方"%name[i])
        sum_db += 1
    elif(longtitude[i]>yncoorlon and latitude[i]<yncoorla):
        print("%s在学校东南方"%name[i])
        sum_dn += 1
    elif(longtitude[i]<yncoorlon and latitude[i]>yncoorla):
        print("%s在学校西北方"%name[i])
        sum_xb += 1
    else:
        print("%s在学校西南方"%name[i])
        sum_xn += 1
print("东北:",sum_db)
print("东南:",sum_dn)
print("西北:",sum_xb)
print("西南:",sum_xn)
sum = sum_db+sum_dn+sum_xb+sum_xn
dbratio = sum_db/sum
dnratio = sum_dn/sum
xbratio = sum_xb/sum
xnratio = sum_xb/sum
print("东北占比:",dbratio)
print("东南占比:",dnratio)
print("西北占比:",xbratio)
print("西南占比:",xnratio)