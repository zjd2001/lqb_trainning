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
#p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
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
        for j in range(1, i+1): # 循环得到当前长度的钢条的不同切法，把最优存入res
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


# 存储最大价格和切割方法
def cut_rod_extend(p, n):
    r = [0]
    s = [0]
    for i in range(1, n+1):
        res_r = 0 # 记录最大价格
        res_s = 0 # 最大价格时对应方案的左边不切割部分的长度
        for j in range(1, i+1):
            if p[j] + r[i-j] > res_r:
                res_r = p[j] + r[i-j]
                res_s = j
        r.append(res_r)
        s.append(res_s)
    return r[n], s

def cut_rod_solution(p, n): # 把最佳切割方法详细列出来，因为cut_rod_extend只能得到左半不切部分，要找右半要切的部分应该被切成什么，例如：9的左半是3，那么右半就是6， 再去看6,6的左半是6，右半是0.则9=3+6
    r, s = cut_rod_extend(p, n)
    ans = []
    while n > 0:
        ans.append(s[n])
        n -= s[n]
    return ans
"""
n = input("请输入钢条长度：")
n = int(n)
r, s = cut_rod_extend(p, n)
a = cut_rod_solution(p, n)
print(f"长度为{n}的钢条的最佳切割方案是{a}，最大价值是{r}。")
"""


# 最长公共子序列
# 找出lcs长度
def lcs_length(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]: # i，j位置上的字符匹配的时候，单元格数值来自左上方+1
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    return c[m][n]

# 添加回溯，找出c[m][n]是从哪来的
def lcs(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [['·' for _ in range(n + 1)] for _ in range(m + 1)] # 记录箭头方向，即单元格的值来自哪里
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]: # i，j位置上的字符匹配的时候，单元格数值来自左上方+1
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = '↖'
            elif c[i-1][j] >= c[i][j-1]: # 来自上方
                c[i][j] = c[i-1][j]
                b[i][j] = '↑'
            else:
                c[i][j] = c[i][j-1] # 来自左方
                b[i][j] = '←'
    return c[m][n], b

# 回溯找到匹配的字母
def lcs_trackback(x, y):
    c, b = lcs(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == '↖': # 来自左上方=>匹配
            res.append(x[i-1])
            i -= 1
            j -= 1
        elif b[i][j] == '↑': # 来自上方=>不匹配
            i -= 1
        else: # 来自左方=>不匹配
            j -= 1
    return "".join(reversed(res))

c, b = lcs("ABCBDAB", "BDCABA")
print(c)
for _ in b:
    print(_)
print(lcs_trackback("ABCBDAB", "BDCABA"))