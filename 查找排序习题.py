#给两个字符串s和t，判断t是否为s的重新排列组合后的单词
#自己做的
def bubble_sort(li):
    for i in range(len(li)-1):#第i趟
        exchange=False
        for j in range(len(li)-i-1):#箭头位置
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                exchange=True

        if not exchange:#没有发生交换，说明目前的无序区本来就是有序的，不用再排了
            return

def judge_str(s,t):
    result=False
    s_list=list(s) #转换为列表
    t_list=list(t)
    bubble_sort(s_list)
    bubble_sort(t_list)
    if s_list==t_list:
        result=True
    return result

s=input("请输入s：")
t=input("请输入t：")
result=judge_str(s,t)
print(f"return {result}")

#答案1
class Solution:
    def isAnagram(self,s,t):
        """
        判断两个字符串是否为字母异位词
        :param s: str
        :param t: str
        :return: bool
        """
        ss=list(s)
        tt=list(t)
        ss.sort() #排序函数
        tt.sort()
        return ss==tt
#给一个m*n的二维列表，查找一个数是否存在。（每一行的列表从左向右已经排好，每一行第一个数比上一行最后一个数大。）

#给定一个列表和一个整数，找到两个数的下标，使得两数之和为给定的整数。保证有且只有一个结果。例如：列表[1,2,5,4]，目标整数3,1+2=3，结果为（0,1）。

