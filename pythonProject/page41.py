from matplotlib import pyplot as plt
import pylab as mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False
a = ["战狼2","速度与\n激情8","功夫瑜伽","西游伏妖篇","变形金刚5：\n最后的骑士","摔跤吧！\n爸爸","加勒比海盗5\n：死无对证","金刚：骷髅岛","极限特工：\n终极回归","生化危机6：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：\n殊死一战","蜘蛛侠：\n英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]
b=[56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]
plt.figure(figsize=(20,15),dpi=80)
plt.bar(range(len(a)),b,width=0.3)
plt.xticks(range(len(a)),a,rotation="45")
plt.savefig("./movie.png")
plt.show()
