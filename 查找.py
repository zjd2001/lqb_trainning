#顺序查找
def linear_search(li,val): #从列表li里找val
    for ind ,v in enumerate(li): #同时获取列表中每个元素的索引 ind 及其值 v
        if v==val:
            return ind #返回下标
    else:
        return None


#二分查找 要先排序
def binary_search(li,val):
    left=0#标签从0开始
    right=len(li)-1
    while left<=right:#候选区有值
        mid=(left+right)//2
        if li[mid]==val:
            return mid
        elif li[mid]>val:#待找值在mid左侧
            right=mid-1
        else:#li[mid]<val 待找值在mid右侧
            left=mid+1
    return None

A=[1,2,3,4,5,6,7,8,9]
print(linear_search(A,3))




