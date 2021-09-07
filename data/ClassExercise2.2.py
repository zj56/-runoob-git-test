from matplotlib import pyplot as plt
import csv
filename = "D://VscodeSpace//pythonTest//data//world-population.csv"
datax = []
datay = []
with open (filename) as f:
    reader = csv.reader(f)
    for datarow in reader:
        if reader.line_num != 1 :
            print (reader.line_num,datarow)
            datax.append(int(datarow[0]))
            datay.append(int(datarow[1]))
            # print(type())
plt.figure(figsize=(20,8),dpi=80)
plt.plot(datax, datay, 'o--', color='black')
plt.grid(alpha = 0.3)
plt.show()
