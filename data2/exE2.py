from pandas.core import series
from pyecharts.charts import Pie 
from pyecharts import options as opts
import pandas as pd
vote_result=pd.read_csv("d:/ee/vote_result.csv")
field = vote_result["感兴趣的领域"]
NumberOfVotes = vote_result["票数"]

def pie_with_custom_label():
    pie = Pie(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    pie.add("", [list(z) for z in zip(field,NumberOfVotes)])
    pie.set_series_opts(
        # 自定义数据标签
        label_opts=opts.LabelOpts(position='top',
                                  color='red',
                                  font_family='Arial',
                                  font_size=12,
                                  font_style='italic',
                                  interval=1,
                                  formatter='{b}:{d}%'
                                  )
    )

    return pie


chart = pie_with_custom_label()
chart.render('pie1.html')