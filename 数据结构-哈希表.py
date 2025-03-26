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
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration
        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)
    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return "<<"+"，".join(map(str, self))+">>"