import numpy as np
from numpy.core.defchararray import equal
import pandas as pd
data=pd.read_csv(r"C:\Users\zj56\Desktop\新建文件夹\1.csv")
print(data.head())
print(data.info())
data.columns=list(range(0,10))
for i in range(0,9):
    for k in range(0,9):
        for j in range(0,15):
            # print(str(data.iloc[j:j+1,i]))
            # print(str(data.iloc[j:j+1,i+1]))
            # print("====")
            # print(data.iloc[j:j+1,i])j
            # print(str(data.iloc[j:j+1,i]))
            if(str(data.iloc[j:j+1,i]) is str(data.iloc[j:j+1,k])):
                print("ok")

# print(data.head())
s=np.zeros((15,10))
ss=pd.DataFrame(s)
# print(data.reset_index(drop=True))
print("==========")
# for i in range(0,10):
    # if(data.iloc[,])
    # print(data.iloc[1:2,i])
    # for j in range(0,13):
        # if(str(data.iloc[j:j+1,i])==str(data.iloc[j+1:j+2,i])):
        # print(data.iloc[j:j+1,i])
