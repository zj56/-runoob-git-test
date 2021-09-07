import csv 
from matplotlib import pyplot as plt
filename = "D://VscodeSpace//pythonTest//data//hot-dog-contest-winners.csv"
datax = []
datay = []
bar_width = 0.7
with open (filename) as f:
    reader = csv.reader(f)
    for datarow in reader:
        if reader.line_num != 1:
            datay.append(float(datarow[2]))
            datax.append(datarow[0])
plt.xticks(range(0,70,10))
plt.figure(figsize=(20,8),dpi=80)
plt.bar(datax,datay,width=bar_width)
plt.grid(alpha = 0.3)
plt.show()

