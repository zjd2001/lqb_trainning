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

#li=[random.randint(0,1000) for i in range(1000)]
#print(li)
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

#li = [3,2,4,1,5,7,9,6,8]
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
#quick_sort(li,0,len(li)-1)
#print(li)


# 堆排序
#父为i，左孩子为2i+1，右孩子为2i+2。所有子的父都是(i-1)//2

# 堆向下调整，为堆顶那一个值找合适位置（此时除了堆顶值，其他值都是符合父比子大），（用于建堆（大根堆），对一个大堆中的每个小堆进行，最终整个大堆构造完成）
def sift(li, low, high):
    '''
    :param li: 列表
    :param low: 堆根节点的下标
    :param high: 堆最后一个元素的下标
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
        else:  # tmp比j所指的值大，把tmp放在此时i的位置上
            li[i] = tmp
            break
    else:
        li[i] = tmp  # j位置没数了，已经找到最后一层了，把tmp放在叶子节点上


#堆排序实现
def heap_sort(li):
    n=len(li)
    for i in range((n-2)//2,-1,-1): #因为每个子节点的父是(i-1)//2,而n是从0开始的下标，所以是n-2。-1是结束值，因为右不包所以结束在0，即堆顶。第二个-1是步长，即倒序。
        #i指建堆时 调整的部分（小子堆） 的根的下标
        #这样就倒着遍历了全部非叶节点
        sift(li,i,n-1) #将high值设置为整个堆的最后一个值，就可以达到sift函数中需要的效果，避免了每个部分（每个小子堆）要重新算high值的麻烦。
        #这样就倒着依次以非叶节点为小堆堆顶，将每个小堆建好，所有节点都符合了父比子大，最后大堆就建好了
    #建堆完成（建的是大根堆）

    #排序
    for i in range (n-1,-1,-1): #i指向当前堆的最后一个元素，倒序遍历至第一个元素
        li[0],li[i]=li[i],li[0] #将最后一个元素与堆顶交换，即将堆顶值（最大值）存在了列表最后一位，不断循环后列表后面就是有序区
        sift(li,0,i-1) #为换到堆顶的那个元素寻找合适位置，结果就是将当前无序区中的最大值换上了堆顶


#li=[i for i in range(100)]
#random.shuffle(li)
#print(li)

#heap_sort(li)
#print(li)


#使用堆排序库
import heapq

li=list(range(100))
random.shuffle(li)
#print(li)

#heapq.heapify(li) #建小根堆
#print(li)

#n=len(li)
#for i in range(n):
#    print(heapq.heappop(li),end=',') #heapq.heappop返回堆顶元素，同时确保剩余元素仍然保持小分堆属性


#topK问题：找出列表中前K大的数

#改成用于建立小根堆
def sift_topk(li, low, high):
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:
        if j + 1 <= high and li[j + 1] < li[j]:  #改为了<
            j = j + 1
        if li[j] < tmp: #改为了<
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp

def topk(li,k):
    heap=li[0:k] #取k个数建立初始堆
    for i in range((k-2)//2,-1,-1):
        sift_topk(heap,i,k-1) #heap变成了小根堆（k1），会把K1中最小的数换到堆顶
    #1.建立小根堆
    for i in range(k,len(li)-1): #遍历出了k1的剩下的列表
        if li[i]>heap[0]: #如果有比k1中最小的数大的
            heap[0]=li[i] #用这个数替换k1中最小的那个
            sift_topk(heap,0,k-1) #在进行一遍建堆，又把最小的数换到堆顶
    #2.遍历，最后前k大的数都存进了heap
    for i in range(k-1,-1,-1): #指向heap最后一位，倒序至第一位
        heap[0],heap[i]=heap[i],heap[0] #将最后一个元素与堆顶交换，即将堆顶值（最小值）存在了列表最后一位，不断循环后列表后面就是有序区
        sift_topk(heap,0,i-1) #为换到堆顶的那个元素寻找合适位置，结果就是将当前无序区中的最小值换上了堆顶
    #3.排序heap
    return heap

#print(topk(li,10))


#归并排序

#归并
#当无序列表从low~mid（左半区）有序，mid+1~high（右半区）也有序，对整个列表排序
def merge(li,low,mid,high):
    i=low
    j=mid+1
    ltmp=[] #临时列表
    while i<=mid and j<=high: #左右半区还有数
        if li[i]<li[j]: #从第一个数开始，两边相比，小的写进ltmp
            ltmp.append(li[i])
            i+=1 #然后在继续比
        else:
            ltmp.append(li[j])
            j+=1
    #while执行完，肯定有一边没数了
    while i<=mid:
        ltmp.append(li[i]) #右半区没了，将左半区剩的都写进去
        i+=1
    while j<=high:
        ltmp.append(li[j]) #左半区没了，将右半区剩的都写进去
        j+=1
    li[low:high+1]=ltmp #把ltmp中的重新写回li

#li=[4,8,2,6,7,3,1,5]
#merge(li,0,3,7)
#print(li)

#归并排序实现
def merge_sort(li,low,high):
    if low<high: #至少有两个元素
        mid=(low+high)//2 #拆分成两半
        merge_sort(li,low,mid) #先用递归不断拆分至单个元素
        merge_sort(li,mid+1,high) #一直都是li，因为输入的是下标，从列表里取一段
        merge(li,low,mid,high) #最后一轮递归完开始不断合并，实现排序

#merge_sort(li,0,7)
#print(li)


#希尔排序
def insert_sort_gap(li,gap): #由插入排序修改，gap指分组数。（其实就是把插入排序中所有的1改成了gap）
    #这个函数是对 跳跃分组后 每个组内元素同时进行插入排序（第一组第二个、第一个值比完了，比第二组第二个、第一个值..., 到第gap组第二个、第一个值比完了，再比第一组第三个、第二个值....)
    for i in range(gap,len(li)): #每组第一张牌都默认为有序区，所以从gap开始，即第一组的第二张牌开始
        tmp=li[i]  #待插入的牌
        j=i-gap #有序区的最后一个
        while j>=0 and li[j]>tmp: #若有序区的最后一个数比牌的值大
            li[j+gap]=li[j] #将有序区最后一个挪到同组的后一位
            j-=gap #j在同组内向前一位
        li[j+gap]=tmp #while循环结束时，是牌比它同组前一位大的时候，因为j在循环结束时代表的是同组里前一位，所以牌的最终位置应该在同组前一位之后即j+gap

def shell_sort(li): #排序实现
    d=len(li)//2 #初始分组的组数，每组只有两个元素
    while d>=1: #只要组数大于1
        insert_sort_gap(li,d) #就对每个组同时进行插入排序
        d//=2 #组数每次循环减少一半。
        #每轮结束后列表并没有完全有序，但更接近有序
        #最后一轮d=1，即完整的列表进行一遍插入排序

print(li)
shell_sort(li)
print(li)

#计数排序
def count_sort(li,max_count=100): #要知道列表中的最大值
    count=[0 for _ in range(max_count+1)]
    for val in li:
        count[val]+=1
    li.clear() #把li清空
    for ind,val in enumerate(count):
        for i in range(val):
            li.append(ind) #写回li