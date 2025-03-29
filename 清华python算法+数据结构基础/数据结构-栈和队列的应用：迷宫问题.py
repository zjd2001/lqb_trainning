#1为墙，0为路
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x,y: (x+1, y), #往下走
    lambda x,y: (x-1, y), #往上走
    lambda x,y: (x, y-1),
    lambda x,y: (x, y+1)
]

#栈：深度优先搜索。从一个节点开始，任意找下一个能走的点，找到不能走的点时，退回上一个点寻找其他方向的点。使用栈存储当前路径
def maze_path_stack(x1, y1, x2, y2): #起点坐标和终点坐标
    stack = []
    stack.append((x1, y1))
    while(len(stack) > 0):
        curNode = stack[-1] #当前节点的x,y坐标
        if curNode[0] == x2 and curNode[1] == y2:
            #到终点了
            for p in stack:
                print(p)
            return True

        for dir in dirs: #对dirs里的每个方向依次进行尝试
            nextNode = dir(curNode[0], curNode[1]) #按当前x,y坐标，依次尝试dirs里的下一节点
            if maze[nextNode[0]][nextNode[1]] == 0: # 下一个节点能走
                stack.append(nextNode) #加到栈里
                maze[nextNode[0]][nextNode[1]] = 2 #2表示已经走过
                break #结束for循环
        else: #下一个节点不能走
            maze[nextNode[0]][nextNode[1]] = 2 #标记为2
            stack.pop() #回退
    else:
        print("没有路")
        return False

#print(maze_path_stack(1,1,8,8))


#队列：广度优先搜索。从有一个节点开始，寻找所有接下来可以走的点，继续不断寻找，直到找到出口。使用队列存储当前正在考虑的节点。走过的节点都已经出队
from collections import deque

def maze_path_queue(x1, y1, x2, y2):
    queue = deque() #创建队列queue
    queue.append((x1, y1, -1)) #将起点存入队列(三元组)，第三位-1是父节点的下标，起点下标是0，所以父节点设为-1
    path = [] #存出队的节点，用来最后还原路径

    while len(queue) > 0: #队不空，说明不是所有分支都是死胡同
        curNode = queue.popleft() #队首（当前节点）出队，并用变量curNode表示(当前可能有多个分支的节点等待前进，就从队里依次出来判断）
        path.append(curNode) #存入列表path

        if curNode[0] == x2 and curNode[1] ==y2:
            #找到终点
            print_r(path)
            return True

        for dir in dirs: #对dirs里的每个方向依次进行尝试
            nextNode = dir(curNode[0], curNode[1]) #下一节点坐标
            if maze[nextNode[0]][nextNode[1]] == 0: #下一节点能走
                queue.append((nextNode[0], nextNode[1], len(path) - 1)) #放入队列，并记录其父节点下标：path中的最后一个元素是当前节点（即下一节点的父节点），其下标为len(path)-1
                maze[nextNode[0]][nextNode[1]] = 2 #标记为已经走过

    else: #队空时，说明所有分支都是死胡同
        print("没有路")
        return False

def print_r(path):
    curNode = path[-1] #终点
    real_path = [] #存真正的路径

    while curNode[2] != -1: #curNode中第三列不为-1，即不是起点
        real_path.append((curNode[0], curNode[1])) #存入节点坐标，或表示为curNode[0:2]
        curNode = path[curNode[2]] #从path中找到父节点(再找到父节点的父节点...不断循环存入real_path，这样就把走通的路径还原出来了)

    #循环到curNode=-1停止，此时起点还没放入
    real_path.append(curNode[0:2]) #放入起点

    real_path.reverse() #将其倒序
    #print(real_path)
    for node in real_path:
       print(node) #打印路径

print(maze_path_queue(1,1,8,8))