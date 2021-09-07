import csv 
from matplotlib import pyplot as plt
import numpy as np
import pylab as mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False
filename = "D://VscodeSpace//pythonTest//data//hot-dog-places.csv"
bar_width = 0.3
data = []
with open (filename) as f:
    reader = csv.reader(f)
    for datarow in reader:
        # print(datarow)
        data.append(datarow)
datax = data[0]
plt.figure(figsize=(20,8),dpi=80)
data_A = list(map(float,data[1]))
data_B = list(map(float,data[2]))
data_C = list(map(float,data[3]))
data = np.array([data_B,data_C])
color_list = ['b','g','r']
X = np.arange(data.shape[1])
# print(data.shape[0])
# print(data.shape[1])

x_14 = list(range(2000,2011,1))
x_15 = list(i+bar_width for i in x_14)
plt.ylabel(range(0,141,20))
plt.bar(x_14,data_A,width=bar_width,label = "第一名")
plt.bar(x_15,data_B,width=bar_width,label = "第二名")
plt.bar(x_14,data_A,width=bar_width,yerr = 2,bottom=data_C,label='第三名')
plt.legend()
plt.show()


