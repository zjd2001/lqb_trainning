list(map(int, input().split()))

#读取输入12345为[1,2,3,4,5]
list(map(int, input()))
def gcd(a, b):
    """计算两个数的最大公约数"""
    while b:
        a, b = b, a % b # gcd(a, b) = gcd(b, a % b)
    return a


# 快读模板
import sys
input = lambda:sys.stdin.readline().strip() # 之后正常用input


def is_prime(n):
    """判断一个数是否为质数"""
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: # 所有质数都可以表示为 6k ± 1 的形式（除了 2 和 3）。因此，我们只需要检查形如 6k - 1 和 6k + 1 的数是否能整除 n
            return False
        i += 6
    return True


def digit_sum(n):
    """计算整数 n 的各个数位上的数字之和"""
    return sum(int(digit) for digit in str(n))


# 输入二维矩阵
matrix = []
for _ in range(n):
    row = input().strip() # 去除首尾空格、换行
    matrix.append(list(row))
   #或者：
s = [input().strip() for _ in range(n)]


# 计算日期间天数差
from datetime import date
def main():
    a = list(map(int, input().split('-')))  # 输入格式不同，(2018-03-15、2018/03/15)则用这个办法统一转为[2018，03，15]
    b = list(map(int, input().split('-')))
    ans = days_between_dates(a, b)
    print(ans)
def days_between_dates(date1, date2):
    # 将列表转换为 datetime.date 对象
    dt1 = date(date1[0], date1[1], date1[2]) # 年、月、日
    dt2 = date(date2[0], date2[1], date2[2])
    delta = dt2 - dt1    # 计算日期差
    return abs(delta.days)    # 返回天数差（绝对值）


#li.pop(index) #按索引删除
#li.remove(Val) #按值删除第一个匹配的

#列表降序排序： li.sort(reverse=True）

#Excel算日期
#日期间隔：=结束日期-开始日期+1    =DATE(2025,5,4)-DATE(2025,1,1)+1
#星期计算：=WEEKDAY(日期单元格，2)    日期单元格内用2025-4-10格式


def chufa(a, b):
    #除法
    a1 = a // b # 向下取整
    a2 = (a + b - 1) // b # 向上取整
    return a1, a2


#求1-2025中0出现次数：excel下拉生成1-2025，粘贴至word，ctrl+h替换，查找内容0，替换为#，替换次数即答案（需要粘贴为文本格式）