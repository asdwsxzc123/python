# -*- coding: utf-8 -*-
class Node(object):
    """ 节点 """
    def __init__(self,elem):
        self.elem = elem
        self.next = None


# node = Node(100)
class SingleCircleLinkList(object):
    """ 单向循环链表 """
    def __init__(self, node=None):
        self._head = node
        if node:
            node.next = node
    def is_empty(self):
        """ 链表是否为空 """
        return self._head == None
    def length(self):
        """ 链表的长度 """
        # cur游标,用来移动遍历节点
        if self.is_empty():
            return 0
        cur = self._head
        # count
        count = 1
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count 
    def travel(self):
        """ 遍历整个链表 """
        if self.is_empty():
            return
        cur = self._head
        while cur.next != self._head:
            print(cur.elem)
            cur = cur.next
        # 推出循环
        print(cur.elem)
    def add(self, item):
        """ 链表头部添加元素 """
        node = Node(item)
        if self.is_empty():
            self._head = node 
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            # 退出循环,cur指向尾节点
            node.next = self._head
            self._head = node
            # cur.next =node
            cur.next = self._head
    def append(self, item):
        """ 链表尾部添加 """
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head
            cur.next = node
    def insert(self, pos, item):
        """ 指定位置添加 
        : pos 从0开始
        """ 
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        count = 0
        pre = self._head
        while count < (pos - 1):
            count +=1
            pre = pre.next
        node = Node(item)
        node.next = pre.next
        pre.next = node
    def remove(self, item):
        """ 删除节点 """
        cur = self._head
        if cur == None:
            return
        pre = None
        while cur.next != self._head:
            if cur.elem == item:
                # 先判断头结点
                if cur == self._head:
                    # 找尾节点
                    rear = self._head
                    while rear.next != self._head:
                        rear = rear.next
                    self._head = cur.next
                    rear.next = self._head
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
        if cur.elem == item: 
            if cur == self._head:
                # 链表只有一个节点
                self._head = None
            else:
                pre.next = cur.next
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
    ll = SingleCircleLinkList()
    ll.append(1)
    ll.append(2)
    # print(ll.is_empty())
    # print(ll.length())
    ll.append(3)
    ll.add(8)
    ll.insert(2,4)
    # ll.remove(4)
    ll.travel()