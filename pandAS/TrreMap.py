from itertools import groupby
import pandas as pd
birth = pd.read_csv("d:/ee/birth-rate.csv")
birth.dropna(subset=['2008'], inplace=True)
dirt = {}
data = list(round(birth['2008'], 1))
range_num = []
for k, g in groupby(sorted(data), key=lambda x: int(x)):
    lst = map(str, list(map(lambda y: divmod(int(y * 10), 10)[1], list(g))))
    dirt[k] = ' '.join(lst)
    range_num.append(k)
num = list(range(range_num[0], range_num[-1], 2))
for i in num:
    a = ''
    for k in sorted(dirt.keys()):
        if 0 <= k - i <= 1:
          a = a + ' ' + dirt[k]
        elif k - i > 1:
           break
    print(str(i).rjust(5), '|', a)
