#实现链表
class LinkList:
    class Node: #嵌套类，表示链表中的节点
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator: #定义迭代器类，支持对链表的迭代操作
        def __init__(self, node): #初始化一个节点Node
            self.node = node
        def __next__(self):
            if self.node: #如果当前节点存在
                cur_node = self.node #保存当前节点为 cur_node
                self.node = cur_node.next #将 self.node 移动到下一个节点
                return cur_node.item #返回当前节点的数据
            else:
                raise StopIteration
        def __iter__(self):
            return self #返回自身实例 self，使得迭代器可以被多次使用

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable) #如果传入了可迭代对象 iterable，调用 self.extend(iterable) 方法将其中的元素添加到链表中

    def append(self, obj): #向链表末尾添加一个新节点，存储数据为 obj
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable): #接收一个可迭代对象 iterable，将其每个元素依次添加到链表末尾。
        for obj in iterable:
            self.append(obj)

    def find_o(self, obj): #查找链表中是否存在某个值为 obj 的节点。
        for n in self: #调用迭代器遍历链表
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head) #返回一个 LinkListIterator 实例，从链表的头节点开始迭代,使链表可以支持for循环

    def __repr__(self):
        return "<<"+"，".join(map(str, self))+">>" #提供链表的直观字符串表示


#创建哈希表
class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.T = [LinkList() for i in range (self.size)] #self.T 将是一个长度为 self.size 的列表，列表的每个元素都是一个空的链表对象

    def h(self, k):
        return k % self.size #哈希函数

    def insert(self, k):
        i = self.h(k) #哈希函数算出存储位置
        if self.find(k):
            print("Duplicated Insert") #重复插入
        else:
            self.T[i].append(k) #插入存储位置的链表中

    def find(self, k):
        i = self.h(k) #哈希函数算出存储位置
        return self.T[i].find_o(k) #通过链表查找到在链表中的位置


ht = HashTable()

ht.insert(0)
ht.insert(1)
ht.insert(3)
ht.insert(102)
ht.insert(508)

print(",".join(map(str, ht.T)))
print(ht.find(3))