from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker
import pandas as pd
vote_result=pd.read_csv("d:/ee/vote_result.csv")
field = vote_result["感兴趣的领域"]
NumberOfVotes = vote_result["票数"]

def pie_custom_radius():
    pie = Pie(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    pie.add("",
            [list(z) for z in zip(field,NumberOfVotes)],
            # 设置半径范围，0%-100%
            radius=["40%", "75%"])
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


chart = pie_custom_radius()
chart.render('pie2.html')