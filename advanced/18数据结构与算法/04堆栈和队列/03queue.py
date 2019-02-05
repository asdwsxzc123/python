# coding: utf-8
class Queue(object):
    """ 双队列 """
    def __init__(self):
        self.__list = []
    def enqueue(self, item):
        """ 往队列中添加一个item元素 """
        self.__list.append(item)
    def dequeue(self):
        """ 从队列头部删除一个元素 """
        return self.__list.pop(0)
    def is_empty(self):
        """ 判断队列是否为空 """
        return self.__list == []
    def size(self):
        """ 队列的长度 """
        return len(self.__list)