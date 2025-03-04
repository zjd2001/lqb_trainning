import random

#冒泡排序
def bubble_sort(li):
    for i in range(len(li)-1):#第i趟
        exchange=False
        for j in range(len(li)-i-1):#箭头位置
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                exchange=True
        print(li)
        if not exchange:#没有发生交换，说明目前的无序区本来就是有序的，不用再排了
            return

li=[random.randint(0,1000) for i in range(1000)]
print(li)
#bubble_sort(li)
#print(li)
#A=list(reversed(li))
#print(A)

#选择排序
def select_sort_sample(li): #用新列表存选出来的最小值,时间复杂度高
    li_new = []
    for i in range (len(li)):
        min_val = min(li)
        li_new.append(min_val) #把找出的最小值存在新列表里
        li.remove(min_val) #并从原列表删掉
    return li_new

#print(select_sort_sample(li))#select_sort_sample有返回值，即新的列表，所以可以这样

def select_sort(li):
    for i in range(len(li)-1): #i是第几趟，第1小、第2小.....
        min_loc = i #第一轮时假定最小的数是第一个
        for j in range (i+1,len(li)): #从第二个数开始找    将假定的最小数与无序区的数依次比较
            if li[j] < li[min_loc]: #找到了列表中比min_loc小的数，其角标为j，值为li[j]
                min_loc = j #更新最小值
        li[i] , li[min_loc] = li[min_loc] , li[i] #最后将真正的最小值与无序区第一个值i做交换,变为有序区的最后一位。第一轮即换到第一位，第i轮则是换到第i位

#select_sort(li)
#print(li)#select_sort没有返回值，是直接存在原列表里的


#插入排序
def insert_sort(li):
    for i in range(1,len(li)): #i表示无序区第一个数(需要插入有序区的牌）的下标,即总的轮次（第一轮是总的第一个数默认在有序区，下标为0，所以i从1开始，即无序区从总的第二个数开始）（最后一轮下标是len(li)-1,对应的数是列表最后一个数）
        tmp = li[i] #无序区第一个数的值，即需要插入有序区的牌的值
        j = i - 1 #即j初始值代表有序区最后一个数
        while j >= 0 and li[j] > tmp: #若有序区的最后一个数比牌的值大
            li[j+1] = li[j] #将有序区最后一个数向后挪一位，但此时牌并没有插入，而是等最后找到地方了才插进去
            j -= 1 #j向前一位，在下一轮比较有序区倒数第二个数。之后不断循环，直到有找到牌该放的位置。
        li[j+1] = tmp #while循环结束时，是牌比它前一位大的时候，因为j在循环结束时代表的是前一位，所以牌的最终位置应该在前一位之后即j+1。如果牌是最小的，那么当它比到最后一轮，li[0]>tmp成立，j=-1，下一个循环开启时因为j<0而停止，li[j+1]=li[0],牌被正确放在了第一位
        print(li)

li = [3,2,4,1,5,7,9,6,8]
#print(li)
#insert_sort(li)

#快速排序
def quick_sort(data,left,right):#data是待排序列表，left、right是列表左右下标
    if left<right:
        mid=partition(data,left,right)#归位函数，将列表第一个数放到它应该在的位置，这个位置把列表划分为左右两部分
        quick_sort(data,left,mid-1)#递归调用，对左部分反复进行上述操作
        quick_sort(data,mid+1,right)#递归调用，对右部分反复进行上述操作


def partition(data,left,right):#归位函数
    tmp=data[left]#需要归位的数（A）是列表中第一个数，想象把它取出来后就空出来一个位置
    while left<right:
        while left<right and data[right]>=tmp:#从右边开始找比A小的数
            right-=1#从右向左依次找，如果一直到right=left了都没找到，跳出这个while的同时也会跳出第一个while，此时left(right)的位置就是A应该在的位置了
        data[left]=data[right]#找到了就取出来放到左边的空位，则右边出现一个空位
        while left<right and data[left]<=tmp:#从左边开始找比A大的数
            left+=1#从左向右依次找，如果一直到right=left了都没找到，跳出这个while的同时也会跳出第一个while，此时right(left)的位置就是A应该在的位置了
        data[right]=data[left]#找到了就取出来放到右边的空位
    #直到left=right时，说明比A小的都去了左边，比A大的也都去了右边
    data[left]=tmp#此时这个位置就是A应该在的位置(不能去掉，虽然函数只返回left，但是函数是原地操作函数，直接修改了li）
    return left#将这个下标返回给quick_sort

#partition(li,0,len(li)-1)
#print(li)
quick_sort(li,0,len(li)-1)
print(li)


# 堆排序

# 堆向下调整，为堆顶那一个值找合适位置（此时除了堆顶值，其他值都是符合父比子大）
def sift(li, low, high):
    '''
    :param li: 列表
    :param low: 堆根节点位置
    :param high: 堆最后一个元素的位置
    :return:
    '''
    i = low  # i最开始指向根节点
    j = 2 * i + 1  # j初始为i的左孩子
    tmp = li[low]  # 把堆顶存起来，即需要调整位置的

    while j <= high:  # 只要j位置有数
        if j + 1 <= high and li[j + 1] > li[j]:  # 如果有右孩子且右孩子比左孩子大
            j = j + 1  # 将j指向右孩子
        if li[j] > tmp:  # 此时j所指的值大于tmp
            li[i] = li[j]  # 将这个孩子向上移
            i = j  # 往下看一层
            j = 2 * i + 1
        else:  # tmp比j所指的值大，把tmp放在i的位置上
            li[i] = tmp
            break
    else:
        li[i] = tmp  # j位置没数了，已经找到最后一层了，把tmp放在叶子节点上








