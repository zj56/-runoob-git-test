from pyecharts.charts   import Polar
from pyecharts.charts import Bar,Scatter3D
from pyecharts.charts import Page
from pyecharts import options as opts
import csv
page = Page()
filename="D:\VscodeSpace\pythonTest\data\hot-dog-places.csv"
datax = list()
datay = list()
with open (filename) as f:
    r = csv.reader(f)
    for row in r:
        datax.append(row)
radius = datax[0]
y1 = datax[1]
y2 = datax[2]
y3 = datax[3]
print(radius)
# polar = Polar().set_global_opts(title_opts={"text":"极坐标"})
# polar.add_schema(radiusaxis_opts=opts.RadiusAxisOpts(data=radius,type_="category"))
# polar.add("A",y1,type_='bar',stack="stack()")
# polar.add("B",y2,type_='bar',stack="stack()")
# polar.add("C",y3,type_='bar',stack="stack()")
# polar.render_notebook()
# polar.render()
polar = Polar().set_global_opts(title_opts={"text":"图2"})
polar.add_schema(angleaxis_opts=opts.AngleAxisOpts(data=radius,type_="category"))
polar.add("A",y1,type_='bar',stack="stack()")
polar.add("B",y2,type_='bar',stack="stack()")
polar.add("C",y3,type_='bar',stack="stack()")
polar.render_notebook()
polar.render()
