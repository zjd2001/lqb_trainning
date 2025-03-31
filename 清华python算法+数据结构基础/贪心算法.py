# 找零问题：找出去的总张数最少
t = [100, 50, 20, 5, 1] # 面额

def change(t, n):
    m = [0 for _ in range(len(t))] # 存每个面额找出去的张数
    for i, money in enumerate(t):
        m[i] = n // money # 376//100=3，即需要找三张一百
        n = n % money # 376%100=76，即剩下还需要找的前
    return m, n

#print(change(t, 376))

# 分数背包问题
goods = [(60, 10), (120, 30), (100, 20)] # 每个商品的价格和重量
goods.sort(key=lambda x: x[0]/x[1], reverse=True) #按单位价值降序排序
#print(goods)
def fractional_backpack(goods, w): # w是背包容量
    m = [0 for _ in range(len(goods))] # 存每种商品拿多少走
    total_v = 0 # 装走的总价值
    for i, (prize, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            total_v += prize
            w -= weight
        else:
            m[i] = w / weight # 这种商品只能拿一部分，背包就被装满了
            total_v += m[i] * prize
            w = 0
            break
    return total_v, m

#print(fractional_backpack(goods, 50))



# 拼接最大数字问题
from functools import cmp_to_key
li = [32, 94, 128, 128, 6, 71]

def number_join(li):
    li = list(map(str, li)) # 变成字符串        其中map(function, iterable)，对li每个元素应用str函数转换为字符串，list将其转换为列表
    li.sort(key=cmp_to_key(xy_cmp)) # cmp_to_key 是一个工具函数，它将传统的比较函数（返回 -1、0 或 1 的函数）转换为适用于 key 参数的函数
    return "".join(li)

def xy_cmp(x, y):
    if x+y < y+x:
        return 1
    elif x+y > y+x:
        return -1
    else:
        return 0

print(number_join(li))