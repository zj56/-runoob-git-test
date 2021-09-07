import matplotlib
from matplotlib import pyplot as plt
from matplotlib import font_manager
import pylab as mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False
x = range(11,31)
a = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
b = [1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]
_xtick_label = ["{}岁".format(i) for i in range(11,31)]
_ytick_label = ["{}个".format(j) for j in range(0,7)]
plt.figure(figsize=(20,8),dpi=80)
plt.xlabel("年纪")
plt.ylabel("女朋友数量")
plt.xticks(list(x),_xtick_label,rotation=45)
plt.yticks(list(range(min(a),max(a)+1)),_ytick_label)
plt.grid(alpha=0.1)
plt.plot(x,a,label = "自己",color="cyan",linestyle=":")
plt.plot(x,b,label="同桌",linestyle="--")
#添加图例
plt.legend()
plt.show()
