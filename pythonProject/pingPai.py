from pyecharts.charts import *
from pyecharts import options as opts
import pyecharts.options as opts
from pyecharts.charts import Line
from pandas.core import series
import pandas as pd
data=pd.read_excel("D:/mydocument/MATLAB/ww.xlsx")
# print(data)
yeasData=data["B8"]

x=['a1','a2','a3','a4','a5','a6','a7','a8']
line=(
    Line()
    .add_xaxis(xaxis_data=x)
    .set_global_opts(title_opts=opts.TitleOpts(title="Line-多折线重叠"))
)
for i in range(1,len(data)):
    if data.iloc[i,1]==1:
        line.add_yaxis(series_name=i,y_axis=data.iloc[i,2:10],is_smooth=True,symbol_size=0,color='green')
    if data.iloc[i,1]==2:
        line.add_yaxis(series_name=i,y_axis=data.iloc[i,2:10],is_smooth=True,symbol_size=0,color='orange')
    else:
        line.add_yaxis(series_name=i,y_axis=data.iloc[i,2:10],is_smooth=True,symbol_size=0,color='blue')
line.render('D:/mydocument/MATLAB/pinPai.html')