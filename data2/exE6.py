from numpy.core.fromnumeric import choose
from numpy.core.shape_base import _stack_dispatcher
import pandas as pd
from pyecharts.charts import *
from pyecharts.charts import Page
page = Page()
vote_result=pd.read_csv("d:/ee/presidential_approval_rate.csv")
bar = Bar()
bar.add_xaxis(['支持','反对','不发表意见'])
for i in range(0,13):
    y_Axis=list(vote_result[i:i+1][['支持','反对','不发表意见']].values.flatten())
    y_Axiss=map(int,y_Axis)
    result = []
    for t in y_Axiss:
        result.append(t)
    bar.add_yaxis(str(i),result) 
    result=[]
page.add(bar)
page.render("bar3.html") #图的网页名称




