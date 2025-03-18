#list.append(element)，在列表的末尾添加一个元素
#list.insert(index, element)，在指定位置之前插入一个元素。如果指定的位置大于列表长度，元素将被添加到列表末尾；如果索引为负数，则从列表末尾开始计算位置。
#del list[index]，删除列表中指定索引位置的元素。使用del语句会直接从列表中移除该元素，并且不会返回任何值。
#list.pop(index)或list.pop()，移除并返回列表中指定索引位置的元素。如果不提供索引，默认移除并返回列表最后一个元素。

#栈
class Stack:
    def __init__(self): #用于执行初始化操作，比如设置初始状态。
        self.stack = [] #初始化了一个空列表作为栈的基础数据结构

    def push(self,element): #添加元素
        self.stack.append(element)

    def pop(self): #移除元素
        return self.stack.pop()

    def get_top(self): #获取栈顶元素
        if len(self.stack) > 0: #如果栈非空，则取出栈顶元素
            return self.stack[-1]
        else:
            return None

    def __str__(self):
        # 返回栈的字符串表示形式
        return "Stack: " + str(self.stack)

stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
print(stack)