import pyecharts.options as opts
from pyecharts.charts import Scatter
import pandas as pd
import numpy as np

crime = pd.read_csv("d:/ee/crimeRatesByState.csv")
# print(crime.head())
# print(crime.info())
x_data = crime['murder']
y_data = crime['burglary']
# data.sort(key=lambda x: x[0])
# x_data = [d[0] for d in data]
# y_data = [d[1] for d in data]

(
    Scatter(init_opts=opts.InitOpts(width="1600px", height="1000px"))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        y_axis=y_data,
        symbol_size=20,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_series_opts()
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(
            type_="value", splitline_opts=opts.SplitLineOpts(is_show=True)
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        tooltip_opts=opts.TooltipOpts(is_show=False),
    )
    .render("basic_scatter_chart.html")
)
