#只能从一端插入，另一端删除 先进先出
#队尾进，队首出，队首指针指向第一个元素前一个位置，队尾指针指向最后一个元素

#队列实现：环形队列
"""
如一个长度maxsize=12的队列，下表为0-11，到11了回到0
队首指针前进1：front = (front + 1)%maxsize , 这样在0-10时，模完是下一位，如（0+1）%12=1。而（11+1）%12=0，正好循环回去
队尾指针前进1：rear = (rear+1)%maxsize
队空条件：rear == front
队满条件：(rear + 1)%maxsize == front , 即队尾距队首只差一次前进时
"""

#实现队列
class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0 #队尾指针
        self.front = 0 #队首指针

    def push(self, element): #插入元素
        if not self.is_filled(): #若队不满
            self.rear = (self.rear+1) % self.size #队尾指针前进1
            self.queue[self.rear] = element #把元素插入队尾
        else:
            raise IndexError("Queue is filled")

    def pop(self): #取出元素
        if not self.is_empty(): #若队不空
            self.front = (self.front + 1) % self.size #队首指针前进1
            return self.queue[self.front] #返回队首元素,之后它会被循环回来的队尾 输入的新元素覆盖
        else:
            raise IndexError("Queue is empty.")

    def is_empty(self):
        return self.rear ==self.front #判断队空

    def is_filled(self):
        return (self.rear + 1) % self.size == self.front #判断队满

    def __str__(self):
        if self.is_empty():
            return "[]"

        # 展示队列中的实际元素，忽略未使用的空间
        elements = []
        idx = (self.front + 1) % self.size #第一个元素
        while idx != (self.rear + 1) % self.size: #只要没到队尾指针的后一个位置
            elements.append(self.queue[idx]) #取出元素放入elements
            idx = (idx + 1) % self.size #指向下一个元素

        return "[" + ", ".join(map(str, elements)) + "]"


q=Queue(5)
for i in range(4): #放入0-4五个元素
    q.push(i)
print(q.pop())
q.push(4)
print(q)

#双向队列：两端都支持进队出队

#使用python内置队列模块
from collections import deque

#q = deque([1,2,3], 5) #创建队列,  参数：初始进队元素、最大长度
#q.append(4) #队尾进队
#q.popleft() #队首出队
#print(q.popleft())

#用于双向队列
#q.appendleft(1) #队首进队
#q.pop() #队尾出队

#打印文件后五行
def tail(n):
    with open('test', 'r') as f:
        q=deque(f,n)
    return q

print(tail(5))
for line in tail(5):
    print(line, end='')