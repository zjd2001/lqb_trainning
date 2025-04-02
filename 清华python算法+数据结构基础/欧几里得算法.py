# 求最大公约数
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcd_no_rec(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

# 实现分数约分、加法
class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = self.gcd_no_rec(a, b) # 最大公约数
        self.a /= x
        self.b /= x

    def gcd_no_rec(self, a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    # 最小公倍数
    def zgs(self, a, b):
        x = self.gcd_no_rec(a, b)
        return x * (a / x) * (b / x)

    # 分数加法
    def __add__(self, other):
        a = self.a
        b = self.b   # self.a 和 self.b：表示当前分数对象的分子和分母
        c = other.a  # other.a 和 other.b：表示另一个分数对象的分子和分母
        d = other.b
        fenmu = self.zgs(b, d)
        fenzi = a * (fenmu / b) + c * (fenmu / d)
        return Fraction(fenzi, fenmu)

    def __str__(self):
        return "%d/%d" % (self.a, self.b)

a = Fraction(1, 3) # 1/3
b = Fraction(1, 2) # 1/2
print(a+b)