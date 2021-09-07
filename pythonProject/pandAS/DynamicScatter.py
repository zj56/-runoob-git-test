from pyecharts.charts import EffectScatter
from pyecharts.globals import SymbolType
import pandas as pd
import numpy as np
import seaborn as sns
crime = pd.read_csv("d:/ee/crimeRatesByState.csv")
crime2 = crime[(crime.state != "United States") & (crime.state !=
"DIstrict of Columbia")] 
g = sns.jointplot(x = 'murder',y = 'burglary',data=crime2,kind="reg",size=5,ratio=3,color="g")
es = EffectScatter().set_global_opts(title_opts={"text":"动态散点图实例"})
es.add_xaxis(crime2['murder'])
es.add_yaxis("arrow_sample",crime2['burglary'],symbol=SymbolType.ARROW)
crime2 = crime2.drop(['state'],axis=1)
crime2 = crime2.drop(['population'],axis=1)
g = sns.pairplot(crime2)
es.render('1.html')
