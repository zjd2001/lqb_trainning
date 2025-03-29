
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

#手动输入一个链表
#a = Node(1)
#b = Node(2)
#c = Node(3)
#a.next = b
#b.next = c

#print(a)
#print(a.item)
#print(a.next.next.item)


#创建链表

#头插法：在头节点上插
def create_linklist_head(li):
    head = Node(li[0]) #输入列表li的第一个值充当头节点
    for element in li[1:]: #遍历剩余元素
        node = Node(element) #创建一个新的Node实例，其值为当前元素，成为新节点
        node.next = head #将新节点的next指针指向当前头节点
        head = node #新节点成为新的头节点
    return head #返回链表的头节点指针。通过这个指针可以访问整个链表的所有节点

   #调用 create_linklist_head 并将结果存储在一个变量中，可以通过 lk 来访问链表中的所有节点
lk = create_linklist_head([1,2,3]) #每次迭代时，新节点都被插入到链表的头部。因此，对于输入 [1, 2, 3]，最终生成的链表顺序与原列表顺序相反，即链表的结构是 3 -> 2 -> 1

def print_linklist(lk): #链表的遍历，打印完整链表
    while lk:  #只要 lk 不是 None，即当前节点存在，就会继续执行循环体内的代码。当到达链表的末尾，即 lk.next 为 None 的节点后，lk 会变成 None，循环终止
        print(lk.item, end=',')
        lk = lk.next

#print_linklist(lk)


#尾插法：在尾节点上插
def create_linklist_tail(li):
    head = Node(li[0])
    tail = head #当前只有一个元素，尾就是头
    for element in li[1:]:
        node = Node(element)
        tail.next = node #将新节点作为尾的下一节点
        tail = node #新节点成为新的尾
    return head #返回头，只能通过头找到这个链表

lk2 = create_linklist_tail([1,2,3,6,8]) #尾插法是正序的
#print_linklist(lk2)


#链表的插入
#curNode是当前节点

#p.next = curNode.next   p是待插入curNode和curNode.next之间的节点
#curNode.next = p

#链表的删除
#p = curNode.next    p是待删除的元素
#curNode.next = curNode.next.next  将curNode连接到p之后的元素，修改了curNode的指针
#del p  删除p


#双链表，也可以从尾访问整个链表
class Node_b:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.prior = None #curNode.next指向curNode的指针

#双链表节点插入
#p.next = curNode.next
#curNode.next.prior = p
#p.prior = curNode
#curNode.next = p

#双链表节点删除
#p = curNode.next
#curNode.next = p.next
#p.next.prior = curNode
#del p