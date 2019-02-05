# coding:utf-8
class Stack(object):
    """ 栈 """
    def __init__(self):
        self.__list = []
    def push(self, item):
        """ 添加栈元素 """
        self.__list.append(item)
    def pop(self):
        """ 弹出栈元素 """
        return self.__list.pop()
    def peek(self):
        """ 返回栈元素 """
        if self.__list:
            return self.__list[-1]
        else:
            return None
    def is_empty(self):
        """ 判断栈元素是否为空 """
        return self.__list == []
    def size(self):
        """ 返回栈元素的个数 """
        return len(self.__list)
if __name__ == "__main__":
    s = Stack()