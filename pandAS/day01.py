import pandas as pd
t = pd.Series([1,2,31,12,3,4])
t2 = pd.Series([1,2,31,12,3,4],index=list("abcdef"))
temp_dict = {"name":"xiaohong","age":30,"tel":10086}
t3 = pd.Series(temp_dict)
print(t3)
# print(t3["age"])
# print(t3[0])
print(list(t3.values)[:2])