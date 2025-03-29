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
                    return
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


    # 删除
    # node是待删除节点
    def __remove_node_1(self, node):
        # 情况1：node是叶子节点
            # 直接删掉
        if not node.parent: # node没有父节点，即它既是叶子又是根，只有它一个节点
            self.root = None
        if node == node.parent.lchild: # node是父的左孩子
            node.parent.lchild = None
            node.parent = None
        else: # node是右孩子
            node.parent.rchild = None
            node.parent = None

    def __remove_node_21(self, node):
        # 情况2.1：node只有一个左孩子
            # 用这个左孩子顶替node
        if not node.parent: # node为根
            self.root = node.lchild # node的左孩子成为根
            node.lchild.parent = None
        elif node == node.parent.lchild: # node为父的左孩子
            node.parent.lchild = node.lchild # 删掉node后，要把node的左孩子连给父节点
            node.lchild.parent = node.parent
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):
        # 情况2.2：node只有一个右孩子
            # 用这个右孩子顶node
        if not node.parent:
            self.root = node.rchild
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        if self.root: # 不是空树
            node = self.query_no_rec(val) # 查询到要删除值的位置
            if not node: # 不存在
                return False
            if not node.lchild and not node.rchild: # 情况1
                self.__remove_node_1(node)
            elif not node.rchild: # 情况2.1
                self.__remove_node_21(node)
            elif not node.lchild: # 情况2.2
                self.__remove_node_22(node)
            else:
                # 情况3：node两个孩子都有
                    # 将node的右子树中的最小节点拿过来替换node，并从原处删除

                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild # 如果有左孩子，说明还不是右子树中最小的，找到右子树的最后一个左孩子就是整个右子树最小的

                node.data = min_node.data # 代替node节点的值，所以不用重新连接父子关系

                # 把min_node从原处删掉
                if min_node.rchild: # min_node有右孩子
                    self.__remove_node_22(min_node)
                else: # min_node是叶子节点
                    self.__remove_node_1(min_node)


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

"""
删除
tree = BST([1,4,2,5,3,8,6,9,7])
tree.in_order(tree.root)
print("")

tree.delete(4)
tree.in_order(tree.root)
"""


# AVL树：自平衡的二叉搜索树（查找、插入效率高）
# 根的左右子树的高度之差绝对值不超过1，且跟的左右子树都是平衡二叉树

class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0 # 平衡因子：右树高度减去左树，绝对值不能大于1

class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

    #插入导致不平衡后，需要通过旋转重新平衡
    #左旋：不平衡是由于对根的右孩子的右子树的插入导致的
    def rotate_left(self, p, c):
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p

        c.lchild = p
        p.parent = c

        p.bf = 0 # 更新bf
        c.bf = 0

        return c # 返回旋转后子树根c

    #右旋：不平衡是由于对根的左孩子的左子树的插入导致的
    def rotate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p

        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0

        return c

    # 右旋-左旋：不平衡是由于对根的右孩子的左子树的插入导致的
    def roate_right_left(self, p, c):
        g = c.lchild

        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        if g.bf > 0: #插入到了s3上
            p.bf = -1
            c.bf = 0
        elif g.bf < 0: #插入到了s2上
            p.bf = 0
            c.bf = 1
        else: # s1-4都是空，插入的实际上是g
            p.bf = 0
            c.bf = 0

        return g

    # 左旋-右旋：不平衡是由于对根的左孩子的右子树的插入导致的
    def rotate_left_right(self, p, c):
        g = c.rchild

        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.lchild = p
        p.parent = g

        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:
            p.bf = 0
            c.bf = 0

        return g


    def insert_no_rec(self, val):

        # 1.插入，和BST的插入基本一样
        p = self.root
        if not p:  # 空树
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p

                    node = p.lchild # 不同：添加node存储插入的节点位置
                    break

            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p

                    node = p.rchild
                    break

            else:
                return

        # 2.更新平衡因子
        while node.parent: # node.parent不空
            if node.parent.lchild == node: # 传递是从左子树来，左子树更沉了
                # 插入后node.parent的bf应减1
                if node.parent.bf < 0: # 原来node.parent的bf是-1，则插入后变成了-2。需要做旋转
                    # 做旋转
                    # 看node哪边沉
                    g = node.parent.parent # 为了连接旋转之后的子树               #node不是插入的叶子吗，为什么成了中间节点:插入阶段,node 指向插入的叶子节点.更新平衡因子阶段,node 从叶子节点开始逐层向上移动，指向每一层正在处理的节点
                    x = node.parent # 旋转前子树的根
                    if node.bf > 0:                                            #node.bf不会等于0吗：意味着当前节点的左右子树高度相等，这种情况不会直接导致父节点的 bf 变为 -2 或 2
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                    # 之后还需要把n和g连起来
                elif node.parent.bf > 0: # 原来node.parent的bf是1，则插入后变成0.   #为什么是原来的，此时不是已经插入了变成0了吗:因为插入后还没更新过bf，此时bf还是之前的1
                    node.parent.bf = 0
                    break
                else: # 原来的node.parent.bf是0，插入后变成-1
                    node.parent.bf = -1
                    node = node.parent # 再向上走一层，看还有没有出现需要旋转的
                    continue

            else: # 传递是从右子树来的，右子树更沉了
                # 插入后node.parent的bf应加1
                if node.parent.bf > 0: # 原来node.parent的bf是1，则插入后变成了2。需要做旋转
                    # 做旋转
                    # 看node哪边沉
                    g = node.parent.parent
                    x = node.parent
                    if node.bf < 0: #左边沉
                        n = self.roate_right_left(node.parent, node)
                    else: # 右边沉
                        n = self.rotate_left(node.parent, node)
                elif node.parent.bf < 0: # 原来node.parent的bf是-1，则插入后变成了0
                    node.parent.bf = 0
                    break
                else: # 原来的node.parent.bf是0，插入后变成1
                    node.parent.bf = 1
                    node = node.parent
                    continue

            # 连接旋转后的子树
            n.parent = g # n是子树新的根，x是子树旋转前的根
            if g: # g不空
                if x == g.lchild: # 子树原本是上一节点的左子树
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else:
                self.root = n
                break

tree = AVLTree([9,8,7,6,5,4,3,2,1])
tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)