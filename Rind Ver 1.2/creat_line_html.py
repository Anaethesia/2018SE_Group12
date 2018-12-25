import  numpy as np
#import  pandas as pd
import  matplotlib.pyplot as plt
from pyecharts import Line
import  random
from pylab import mpl

from SE12_Crawler import *

#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def line(a,b,c):
    db = wrappedSQL("movie.db")
    year1=str(a)
    year2=str(b)
    year3=str(c)
    total_boxoffice1=[0,0,0,0,0,0,0,0,0,0,0,0]
    total_boxoffice2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total_boxoffice3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(9):
        dateValue = "Date like '"+str(a)+"-0"+str(i+1)+"%'"
        lst1 = db.SelData(Title='data', Value=dateValue)
        for item in lst1:
            total_boxoffice1[i] = total_boxoffice1[i] + float(item['BoxOffice'])
        dateValue = "Date like '"+str(b)+"-0"+str(i+1)+"%'"
        lst2 = db.SelData(Title='data', Value=dateValue)
        for item in lst2:
            total_boxoffice2[i] = total_boxoffice2[i] + float(item['BoxOffice'])
        dateValue = "Date like '"+str(c)+"-0"+str(i+1)+"%'"
        lst3 = db.SelData(Title='data', Value=dateValue)
        for item in lst3:
            total_boxoffice3[i] = total_boxoffice3[i] + float(item['BoxOffice'])
            
    for i in range(9,12):
        dateValue = "Date like '"+str(a)+"-"+str(i+1)+"%'"
        lst1 = db.SelData(Title='data', Value=dateValue)
        for item in lst1:
            total_boxoffice1[i] = total_boxoffice1[i] + float(item['BoxOffice'])
        dateValue = "Date like '"+str(b)+"-"+str(i+1)+"%'"
        lst2 = db.SelData(Title='data', Value=dateValue)
        for item in lst2:
            total_boxoffice2[i] = total_boxoffice2[i] + float(item['BoxOffice'])
        dateValue = "Date like '"+str(c)+"-"+str(i+1)+"%'"
        lst3 = db.SelData(Title='data', Value=dateValue)
        for item in lst3:
            total_boxoffice3[i] = total_boxoffice3[i] + float(item['BoxOffice'])


    columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    line=Line("票房变化趋势",width=600,height=450)
    line.add("%s" % year1, columns,total_boxoffice1,mark_point=["max","min"])
    line.add("%s" % year2, columns, total_boxoffice2, mark_point=["max", "min"])
    line.add("%s" % year3, columns, total_boxoffice3, mark_point=["max", "min"])
    line.render("Line.html")

if __name__ == "__main__":
    line(2016,2017,2018)