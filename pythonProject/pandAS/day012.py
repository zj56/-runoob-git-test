import pandas as pd
import numpy as np
test=pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("WXYZ"))
print(test)
print(test.loc["a"])
d1={"name":["xiaogong","xas"],"age":[23,12],"tel":[11,121]}
t1 = pd.DataFrame(d1)
# print(t1)
# print(t1.columns)
# print(t1.values)
# print(t1.info())

