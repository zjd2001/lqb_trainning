# 模拟文件系统
class Node: #表示文件系统中的一个节点（默认是文件夹）
    def __init__(self, name, type='dir'):
        self.name = name # 文件名
        self.type = type # "dir" or "file" 类型，即文件夹或文件
        self.children = [] # 子节点列表，用于存储文件夹或文件
        self.parent = None # 父节点，用于回溯目录结构

    def __repr__(self):
        return self.name #定义了当打印 Node 对象时的输出格式，直接返回 name

class FileSystemTree:
    def __init__(self):
        self.root = Node("/") # 根目录，初始化为一个名为 / 的 Node 对象
        self.now = self.root # 当前所在目录，初始为根目录

    def mkdir(self, name): # 创建一个新的文件夹
        if name[-1] != "/": # 如果输入的 name 不以 / 结尾，则自动补上 /
            name += "/"
        node = Node(name) # 创建新文件夹，并将其添加到当前目录的 children 列表中，新创建的文件夹的 parent 指向当前目录。
        self.now.children.append(node)
        node.parent = self.now

    def ls(self): # 返回当前目录的所有子节点（文件夹或文件）
        return self.now.children

    def cd(self, name): # 用于切换当前目录。
        if name[-1] != "/":
            name += "/"
        if name == "../": # 将当前目录切换到父目录
            self.now = self.now.parent
            return
        for child in self.now.children: # 遍历当前目录的子节点，找到匹配的文件夹并切换到该目录
            if child.name == name:
                self.now = child
                return
        raise ValueError("invalid dir") # 无效目录

"""
tree = FileSystemTree()
tree.mkdir("var/")
tree.mkdir("bin/")
tree.mkdir("usr/")
# 在根目录下依次创建三个文件夹：var/、bin/ 和 usr/

tree.cd("bin/")
tree.mkdir("python/")
# 切换到 bin/ 目录，在 bin/ 下创建一个子文件夹 python/

tree.cd("../") # 切换回父目录（即根目录 /）
print(tree.ls()) # 执行 ls()，返回根目录下的所有子节点
"""


# 二叉树
class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None # 左孩子
        self.rchild = None # 右孩子
        self.parent = None

a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e

#print(root.lchild.rchild.data)


# 二叉树的遍历
# 前序遍历
def pre_order(root): # root 是二叉树的根节点，表示从该节点开始进行前序遍历
    if root: # 当前节点是否为非空
        print(root.data, end=',')
        pre_order(root.lchild) # 递归调用,实现了对左子树的前序遍历
        pre_order(root.rchild)

#pre_order(root)

#中序遍历
def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=',')
        in_order(root.rchild)

#in_order(root)

#后序遍历
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=',')

#post_order(root)

#层次遍历
from collections import deque

def leval_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0: # 只要队不空
        node = queue.popleft() # 从队列左侧出队一个节点,并打印
        print(node.data, end=',')
        # 将该节点的左子节点和右子节点依次加入队列（如果存在）
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)
    # 循环直到队列为空，表示所有节点都已访问完毕

#leval_order(root)


#二叉搜索树：对任意根或子根，左子树都比根小，右子树都比根大
class BST:
    def __init__(self, li=None):
        self.root = None
        if li: # 输入列表存在
            for val in li:
                self.insert_no_rec(val) # 循环插入

    # 插入，新节点总是作为叶子节点插入
    # 递归实现插入
    def insert(self, node, val): # node：要插入的节点,初始为根用于递归  val：需要插入的值
        if not node: # 节点为空
            node = BiTreeNode(val) # 直接插入
        elif val < node.data: #node不为空时与val比较，此后node指当前正在处理的子树的根节点
            node.lchild = self.insert(node.lchild, val) # val应插入到左子树中
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val) # val应插入到右子树中
            node.rchild.parent = node
        return node

    # 不使用递归实现插入
    def insert_no_rec(self, val):
        p = self.root # 指向当前节点的指针，从根节点开始，逐步遍历树以找到合适的位置插入新值
        if not p: # 空树
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data: # 要插入的值 val 小于当前节点的值 p.data，则应该插入到左子树
                if p.lchild:
                    p = p.lchild # 如果左子节点存在，则移动指针 p 到左子节点继续查找
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p # 如果左子节点不存在，则创建一个新节点，赋值为 val，并将其设置为当前节点的左子节点，同时设置其父节点为 p。
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return # 要插入的值 val 等于当前节点的值 p.data，则直接退出函数。这表明不允许插入重复值

    # 查询
    # 使用递归
    def query(self, node, val): # 需要查询的值val，node初始为根节点用于递归，后为正在比较的节点
        if not node:
            return None
        if node.data < val:
            return self.query(node.rchild, val)
        elif node.dta > val:
            return self.query(node.lchild, val)
        else:
            return node # val所在节点

    # 不使用递归
    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None # p是空的，说明没有找到

    # 前序遍历
    def pre_order(self, root):
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    # 中序遍历
    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=',')
            self.in_order(root.rchild)

    # 后序遍历
    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=',')

"""
插入
tree = BST([4,6,7,9,2,1,3,5,8])
tree.post_order(tree.root)
print("")
tree.in_order(tree.root)
print("")
tree.post_order(tree.root)
"""

"""
查询
import random

li = list(range(0, 500, 2))
random.shuffle(li)

tree = BST(li)
print(tree.query_no_rec(3))
"""
