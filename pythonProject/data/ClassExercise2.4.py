import csv
import matplotlib.pyplot as plt
filename = "D://VscodeSpace//pythonTest//data//flowingdata_subscribers.csv"
datay = []
with open(filename) as f:
    reader = csv.reader(f)
    for datarow in reader:
        if reader.line_num != 1:
            datay.append(int(datarow[1]))
datax = list(range(1,len(datay)+1))
print(type(datay[1]))
plt.yticks(range(10000,30000,2500))
plt.scatter(datax,datay,s=50,c='r',marker='o',alpha=0.5)
plt.show()