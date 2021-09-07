from numpy.core.fromnumeric import choose
import pandas as pd
from pyecharts.charts import *
from pyecharts.charts import Page
page = Page()
vote_result=pd.read_csv("d:/ee/presidential_approval_rate.csv")
# print(vote_result.info())
# print(vote_result.head())
bar = Bar()
x = list(vote_result["问题"])
print(x)
y1 = list(vote_result["支持"])
print(type(y1))
for i in y1:
    print(type(i))
y2 = list(vote_result["反对"])
print(y2)
y3 = list(vote_result["不发表意见"])
bar.add_xaxis(x)
bar.add_yaxis("A",y1,stack=True,color='oldlace')  #这里的color可以设置图的颜色
bar.add_yaxis("B",y2,stack=True,color='pink')
bar.add_yaxis("C",y3,stack=True,color='palevioletred')
page.add(bar)
page.render("bar1.html") #图的网页名称




