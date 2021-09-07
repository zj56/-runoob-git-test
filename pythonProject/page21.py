import random

import matplotlib
from matplotlib import pyplot as plt
from matplotlib import font_manager
import pylab as mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False

x = range(0,120)
y = [random.randint(20,35) for i in range(120)]
plt.figure(figsize=(20,8),dpi=80)
#调整x轴刻度
_x = list(x)
# _xtick_labels = ["hello,{}".format(i) for i in _x]
_xtick_labels = ["10h{}时".format(i) for i in range(60)]
_xtick_labels += ["11h{}m".format(i) for i in range(60)]
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("10点到12点每分钟的气温")
plt.xticks(_x[::3],_xtick_labels[::3],rotation=45)
plt.plot(x,y)
plt.show()
