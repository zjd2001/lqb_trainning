# 斐波那契数列
def fibnacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibnacci(n-1)+fibnacci(n-2)

def fibnacci_no_rec(n):
    f = [0,1,1]
    if n > 2:
        for i in range(n-2): # 循环计算从第3项到第n项的斐波那契数
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]

#print(fibnacci(10))
#print(fibnacci_no_rec(100))


# 钢条切割问题：用最优子结构方法，子问题是最优，组合起来就是问题最优
p = [0,1,5,8,9,10,17,17,20,21,23,24,26,27,27,28,30,33,36,39,40] # 每个长度的钢条的价格

# 自顶向下的方法
def cut_rod_rec_1(p, n): # n是钢条长度
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rod_rec_1(p, i) + cut_rod_rec_1(p, n-i)) # 比较是不切大，还是切成两边，两边各自的最优拼起来大
    return res
# 这样会重复计算很多子结构
#print(cut_rod_rec_1(p, 9))

def cut_rod_rec_2(p, n):
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n+1):
            res = max(res, p[i] + cut_rod_rec_2(p, n-i)) # 可以理解为左边可以切，但是把切下来的归到右边去后，就一定会出现左边不切、右边切的最优情况
    return res

#print(cut_rod_rec_2(p, 10))

# 动态规划方法：自底向上
def cut_rod_dp(p, n):
    r = [0] # 把每个子结构最佳存起来,初始为长度0，收益0
    for i in range(1, n+1): # 循环钢条长度
        res = 0 # 存当前长度的钢条的最优价值
        for j in range(1, i+1): # 循环得到当前长度的钢条的不同切法，把最优存入r
            res = max(res, p[j] + r[i-j]) # 不需要递归，而是从r中找要切的半边的最优价格
        r.append(res)
    return r[n]

#print(cut_rod_dp(p, 20))

 # cut_rod_rec_1改写
def cut_rod_dp_2(p, n):
    r = [0]
    for i in range(1, n+1):
        res = p[i]
        for j in range(1, i):
            res = max(res, r[j] + r[i-j])
        r.append(res)
    return r[n]
#print(cut_rod_dp_2(p,10))