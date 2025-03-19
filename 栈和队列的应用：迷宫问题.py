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


#栈：深度优先搜索。从一个节点开始，任意找下一个能走的点，找到不能走的点时，退回上一个点寻找其他方向的点。使用栈存储当前路径

dirs = [
    lambda x,y: (x+1, y), #往下走
    lambda x,y: (x-1, y), #往上走
    lambda x,y: (x, y-1),
    lambda x,y: (x, y+1)
]

def maze_path(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    while(len(stack) > 0):
        curNode = stack[-1] #当前节点的x,y坐标
        for dir in dirs: #搜索下一步四个方向
            nextNode = dir(curNode[0], curNode[1]) #按当前x,y坐标搜索
            if maze[nextNode[0]][nextNode[1]] == 0: #下一个节点能走
                stack.append(nextNode)



