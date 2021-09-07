from matplotlib import pyplot as plt
import pylab as mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False
a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]
bar_width = 0.3
x_14 = list(range(len(a)))
x_15 = list(i+bar_width for i in x_14)
x_16 = list(i+bar_width*2 for i in x_14)
plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(a)),b_14,width=bar_width,label="14号")
plt.bar(x_15,b_15,width=bar_width,label="15号")
plt.bar(x_16,b_16,width=bar_width,label="16号")
plt.legend()
#设置x轴刻度
plt.xticks(x_15,a)
plt.show()
