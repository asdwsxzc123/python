# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None
    
class DoubuleLikList(object):
    """ 双链表 """
    def __init__(self):
        self._head = None
    def is_empty(self):
        """ 链表是否为空 """
        return self._head == None
    def length(self):
        """ 链表的长度 """
        # cur游标,用来移动遍历节点
        cur = self._head
        # count
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count 
    def travel(self):
        """ 遍历整个链表 """
        cur = self._head
        while cur != None:
            print(cur.elem)
            cur = cur.next
    def add(self, item):
        """ 链表头部添加元素 """
        node = Node(item)
        node.next = self._head
        self._head = node
        node.next.prev = node
    def append(self, item):
        """ 链表尾部添加 """
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur
    def insert(self, pos, item):
        """ 指定位置添加 
        : pos 从0开始
        """ 
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            cur = self._head
            count = 0
            while count < (pos - 1):
                count +=1
                cur = cur.next
            node = Node(item)
            node.next = cur.next
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node 
        
    def remove(self, item):
        """ 删除节点 """
        cur = self._head
        if cur == None:
            return False
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断头结点
                if cur == self._head:
                    self._head = cur.next
                    if cur.next:
                        # 判断链表是否只有一个节点
                        cur.next.prev = None
                else:
                    cur.pre.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next
    def search(self, item):
        """ 查找节点是否存在 """
        cur = self._head
        if cur == None:
            return False
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == "__main__":
    dl = DoubuleLikList()