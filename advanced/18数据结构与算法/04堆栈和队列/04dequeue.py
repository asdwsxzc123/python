# coding: utf-8
class Deque(object):
    """ 双端队列 """
    def __init__(self):
        self.__list = []
    def add_front(self, item):
        """  往列表头部添元素 """
        self.__list.insert(0, item)
    def add_rear(self, item):
        """ 往列表尾部添元素 """
        self.__list.append(item)
    def pop_front(self):
        """ 往列表头部弹出元素 """
        return self.__list.pop(0)
    def pop_rear(self):
        """ 往列表尾部弹出元素 """
        return self.__list.pop()
    def is_empty(self):
        """ 判断一个队列是否为空 """
        return self.__list == []
    def size(self):
        """ 长度 """
        return len(self.__list)