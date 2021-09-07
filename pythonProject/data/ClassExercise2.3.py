import numpy as np
import matplotlib.pyplot as plt
import csv
import sys

from numpy.lib.polynomial import polyval
filename = "D://VscodeSpace//pythonTest//data//unemployment-rate-1948-2010.csv"
xa = []
ya = []
with open(filename) as f:
    reader = csv.reader(f)
    for datarow in reader:
        if reader.line_num != 1:
            print(reader.line_num,datarow)
            ya.append(float(datarow[3]))
            xa.append(int(datarow[1]))
plt.figure(figsize=(20,8),dpi=80)
plt.scatter(xa[:], ya[:], s=10,c='g',marker='o',alpha=0.5)
ploy = np.polyfit(xa,ya,deg = 3)
plt.plot(xa,np.polyval(ploy,xa))
plt.show()
