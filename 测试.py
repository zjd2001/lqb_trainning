import sys

input = lambda: sys.stdin.readline().strip()

from datetime import date


def main():
    a = list(map(int, input().split('-')))
    b = list(map(int, input().split('-')))
    ans = days_between_dates(a, b)
    print(ans)

def days_between_dates(date1_list, date2_list):
    # 将列表转换为 datetime.date 对象
    dt1 = date(date1_list[0], date1_list[1], date1_list[2])
    dt2 = date(date2_list[0], date2_list[1], date2_list[2])

    # 计算日期差
    delta = dt2 - dt1

    # 返回天数差（绝对值）
    return abs(delta.days)


if __name__ == "__main__":
    main()

