class Node(object):
    """ 节点 """
    def __init__(self,elem):
        self.elem = elem
        self.next = None


# node = Node(100)
class SingleLinkList(object):
    """ 单链表 """
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
            print(cur.elem, end=" ")
            cur = cur.next
    def add(self, item):
        """ 链表头部添加元素 """
        node = Node(item)
        cur = self._head
        while cur.next != self._head:
            cur = cur.next
        node
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
    def insert(self, pos, item):
        """ 指定位置添加 """
        pass
    def remove(self, item):
        """ 删除节点 """
        pass
    def search(self, item):
        """ 查找节点是否存在 """
        pass
if __name__ == "__main__":
    ll = SingleLinkList()
    ll.append(1)
    ll.append(2)
    print(ll.is_empty())
    print(ll.length())
    ll.append(3)