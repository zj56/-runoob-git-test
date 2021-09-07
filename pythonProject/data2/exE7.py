from numpy.core.fromnumeric import choose
from numpy.core.shape_base import _stack_dispatcher
import pandas as pd
from pyecharts.charts import *
from pyecharts.charts import Page
from pyecharts import options as opts
from pyecharts.charts import Line, Grid
from pyecharts.commons.utils import JsCode
line = Line()
vote_result = pd.read_csv("d:/ee/us-population-by-age.csv")
print(vote_result.head())
print(vote_result.info())
data_x = list(vote_result['year'])
y1 = list(vote_result['5-'])
result = []
for i in data_x:
    result.append(str(i))
y2 = list(vote_result['5_19'])
y3 = list(vote_result['20_44'])
y4 = list(vote_result['45_64'])
y5 = list(vote_result['65+'])

line.add_xaxis(result)
line.add_yaxis('line 1',
               y1,
               stack='stack',
               is_smooth=True,
               is_symbol_show=False,
               linestyle_opts=opts.LineStyleOpts(width=0),
               areastyle_opts=opts.AreaStyleOpts(
                   opacity=0.8,
                   color=JsCode("""
                                new echarts.graphic.LinearGradient(
                                    0, 0, 0, 1,
                                    [{offset: 0, color: 'rgba(128, 255, 165)'},
                                     {offset: 1, color: 'rgba(1, 191, 236)'}],
                                    false)
                                """)
               )
               )

line.add_yaxis('line 2',
               y2,
               stack='stack',
               is_smooth=True,
               is_symbol_show=False,
               linestyle_opts=opts.LineStyleOpts(width=0),
               areastyle_opts=opts.AreaStyleOpts(
                   opacity=0.8,
                   color=JsCode("""
                                new echarts.graphic.LinearGradient(
                                    0, 0, 0, 1,
                                    [{offset: 0, color: 'rgba(0, 221, 255)'},
                                     {offset: 1, color: 'rgba(77, 119, 255)'}],
                                    false)
                                """)
               )
               )

line.add_yaxis('line 3',
               y3,
               stack='stack',
               is_smooth=True,
               is_symbol_show=False,
               linestyle_opts=opts.LineStyleOpts(width=0),
               areastyle_opts=opts.AreaStyleOpts(
                   opacity=0.8,
                   color=JsCode("""
                                new echarts.graphic.LinearGradient(
                                    0, 0, 0, 1,
                                    [{offset: 0, color: 'rgba(55, 162, 255)'},
                                     {offset: 1, color: 'rgba(116, 21, 219)'}],
                                    false)
                                """)
               )
               )

line.add_yaxis('line 4',
                y4,
               stack='stack',
               is_smooth=True,
               is_symbol_show=False,
               linestyle_opts=opts.LineStyleOpts(width=0),
               areastyle_opts=opts.AreaStyleOpts(
                   opacity=0.8,
                   color=JsCode("""
                                new echarts.graphic.LinearGradient(
                                    0, 0, 0, 1,
                                    [{offset: 0, color: 'rgba(255, 0, 135)'},
                                     {offset: 1, color: 'rgba(135, 0, 157)'}],
                                    false)
                                """)
               )
               )

line.add_yaxis('line 5',
               y5,
               stack='stack',
               is_smooth=True,
               is_symbol_show=False,
               linestyle_opts=opts.LineStyleOpts(width=0),
               areastyle_opts=opts.AreaStyleOpts(
                   opacity=0.8,
                   color=JsCode("""
                                new echarts.graphic.LinearGradient(
                                    0, 0, 0, 1,
                                    [{offset: 0, color: 'rgba(255, 191, 0)'},
                                     {offset: 1, color: 'rgba(224, 62, 76)'}],
                                    false)
                                """)
               )
               )

line.set_global_opts(xaxis_opts=opts.AxisOpts(boundary_gap=False),
                     yaxis_opts=opts.AxisOpts(axisline_opts=opts.AxisLineOpts(is_show=False),
                                              axistick_opts=opts.AxisTickOpts(is_show=False),
                                              splitline_opts=opts.SplitLineOpts(is_show=True,
                                                                                linestyle_opts=opts.LineStyleOpts(color='#E0E6F1'))
                                                                                ),
                     tooltip_opts=opts.TooltipOpts(is_show=True, trigger='axis', axis_pointer_type='cross'),
                     title_opts=opts.TitleOpts(title="渐变堆叠面积图")
                     ) 

line.set_series_opts(opts.LabelOpts(is_show=False))
line.set_colors(colors=['#80FFA5', '#00DDFF', '#37A2FF', '#FF0087', '#FFBF00'])

grid = Grid(init_opts=opts.InitOpts(theme='white',width='980px', height='600px'))
grid.add(line, grid_opts=opts.GridOpts(pos_left='3%', pos_right='4%', pos_bottom='3%'))
grid.render('area.html')
