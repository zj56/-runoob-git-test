# import numpy as np
import random
import math
import datetime
import pandas as pd
from main_copy import pack_products_into_restrictions

item_sets = [[9, 9, 9], [2, 2, 2], [1, 1, 1], [1, 1, 1], [2, 2, 2]]
Box = (13, 17, 30)

item_sets.sort(key=lambda x: (x[0] * x[1] * x[2]), reverse=True)  # 将箱子按从大到小排列
item_sets = [sorted(i, reverse=True) for i in item_sets]  # 将箱子的摆放顺序统一

def exchange_item(items):  # 第一类邻域选择，随机交换两个物品
    s1, s2 = random.randint(0, len(items) - 1), random.randint(0, len(items) - 1)
    while s1 == s2:
        s2 = random.randint(0, len(item_sets) - 1)
    items[s1], items[s2], = items[s2], items[s1]
    return items

def exchange_direction(items):  # 第二类邻域选择，随机交换某个物品的方向
    s = random.randint(0, len(items) - 1)
    item = items[s]
    s_1, s_2 = random.randint(0, len(item) - 1), random.randint(0, len(item) - 1)
    while s_1 == s_2:
        s_2 = random.randint(0, len(item) - 1)
    item[s_1], item[s_2], = item[s_2], item[s_1]
    items[s] = item
    return items


def sa(alpha, t_set, items_sa, box_sa, markovlen):
    # alpha = 0.99
    # t = (1, 100)
    # m = 100
    min_t = t_set[0]
    t = t_set[1]
    valuecurrent = pack_products_into_restrictions(items_sa,box_sa)[0]
    valuebest = valuecurrent
    itemscurrent = items_sa
    result = []  # 记录迭代过程中的最优解
    while t > min_t:
        for i in range(markovlen):
            # 倒序+插段
            if random.random() > 0.5:  # 交换路径中的这2个节点的顺序
                itemsnew = exchange_item(items_sa)
            else:  # 交换次序
                itemsnew = exchange_direction(items_sa)

            valuenew, select_items = pack_products_into_restrictions(items_sa,box_sa)
            # print (valuenew)
            if valuenew >= valuecurrent:  # 接受该解
                r = 0
                # 更新solutioncurrent 和solutionbest
                valuecurrent = valuenew
                itemscurrent = itemsnew.copy()
                if valuenew >= valuebest:
                    valuebest = valuenew
                    itemsbest = select_items.copy()
            else:  # 按一定的概率接受该解
                if random.random() <= math.exp(-(valuecurrent - valuenew) / t):
                    # if np.random.rand() < (2/math.pi) * math.atan((valuenew - valuecurrent) * 0.000001*t):
                    valuecurrent = valuenew
                    itemscurrent = itemscurrent.copy()
                else:
                    itemsnew = itemscurrent.copy()
            t = alpha * t
        # result.append(itemsbest)
            print('temp:', t)
            print('itemsbest', itemsbest)
            print('valuebest', valuebest)

s1 = datetime.datetime.now()
# 原始货物尺寸如下
# [2.96 ,2.12 ,1.21],[1.05 ,1.05 ,1.05],
# [3.17 ,0.85 ,2.12],[5.08 ,0.95 ,1.05],
# [2.01 ,1.26 ,0.95],[1.32 ,0.64 ,0.84],
# [0.98 ,0.42 ,0.52],[2 ,1.3 ,0.95],
# [2.08 ,1.2 ,1.15],[1.5 ,1 ,1]
#原始集装箱尺寸如下
# [2.991 ,2.438 ,2.438],[2.991 ,2.438 ,2.438],[1.456 ,2.438 ,1.9],\
# [2.991 ,2.438 ,2.438],[2.991 ,2.438 ,2.438],[1.46 ,2.438 ,1.9],[2.235 ,2.743 ,2]
# 现为HW2、HW6、HW7、HW10的体积小于2m3，这4种类型货物选择集装箱。[1.05 ,1.05 ,1.05],[1.32 ,0.64 ,0.84],[0.98 ,0.42 ,0.52],[1.5 ,1 ,1]
#由于算法采用了随机数，所以每次运行的结果可能有微小差别
#集装箱一(2.991 ,2.438 ,2.438)数据过大，进行简化
sa(0.9, (0.8, 1), [[11 ,11 ,11],[13 ,6 ,8],[10 ,4 ,5],[15 ,10 ,10]], (30 ,24 ,24), 1)
#集装箱二
# sa(0.9, (0.8, 1), [[11 ,11 ,11],[13 ,6 ,8],[10 ,4 ,5],[15 ,10 ,10]], (30 ,24 ,24), 1)
#集装箱三
# sa(0.9, (0.8, 1), [[11 ,11 ,11],[13 ,6 ,8],[10 ,4 ,5],[15 ,10 ,10]], (15 ,24 ,19), 1)
#四
# sa(0.9, (0.8, 1), [[11 ,11 ,11],[13 ,6 ,8],[10 ,4 ,5],[15 ,10 ,10]], (30 ,24 ,24), 1)
#五
# sa(0.9, (0.8, 1), [[11 ,11 ,11],[13 ,6 ,8],[10 ,4 ,5],[15 ,10 ,10]], (30 ,24 ,24), 1)
#六
# sa(0.9, (0.8, 1), [[11 ,11 ,11],[13 ,6 ,8],[10 ,4 ,5],[15 ,10 ,10]], (15 ,24 ,19), 1)
#七
# sa(0.9, (0.8, 1), [[11 ,11 ,11],[13 ,6 ,8],[10 ,4 ,5],[15 ,10 ,10]], (22 ,27 ,20), 1)
#(15 ,24 ,19)类型集装箱利用率最高，因此选择(15 ,24 ,19)类型集装箱
# sa(0.9, (0.7, 1), [[30 ,21 ,12],[31 ,8 ,21],[50 ,10 ,10],[20 ,12 ,10],[20,13,10],[20,12,12],[15,24 ,19]\
#                   ,[15,24 ,19],[15,24 ,19],[15,24 ,19]], (180,80 ,130), 1)

s2 = datetime.datetime.now()
print('time:', s2 - s1)

#  pack_products_into_restrictions(item_sets, Box)
