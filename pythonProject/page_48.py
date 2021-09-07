from matplotlib import pyplot as plt
import pylab as mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False
interval = [0,5,10,15,20,25,30,35,40,45,60,90,150]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]
# print(len(interval),len(width),len(quantity))

_x = [i-0.5 for i in range(13)]
_xtick_labels = interval
plt.grid()
plt.xticks(_x,_xtick_labels)
plt.bar(range(12),quantity,1)
plt.show()