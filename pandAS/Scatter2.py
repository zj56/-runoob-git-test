from pyecharts import options as opts
from pyecharts.charts import Scatter
import pandas as pd
import numpy as np

crime = pd.read_csv("d:/ee/crimeRatesByState.csv")
# print(crime.head())
# print(crime.info())
x_data = crime['murder']
y_data = crime['burglary']
c = (
    Scatter()
    .add_xaxis(x_data)
    .add_yaxis("", y_data,color = np.random.rand(len(crime.murder.tolist()).all))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Scatter-VisualMap(Size)"),
        visualmap_opts=opts.VisualMapOpts(type_="size", max_=600, min_=10),
        
        
    
    )
)
