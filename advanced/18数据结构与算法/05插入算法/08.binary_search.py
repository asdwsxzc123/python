# coding: utf-8
def binary_search(alist, item):
    """ 二分查找 递归 """
    n = len(alist)
    if n > 0:
        mid = n / 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            binary_search(alist[:mid], item)
        else:
            binary_search(alist[mid+1:], item)
    return False

def binary_search2(alist, item):
    """ 二分查找 非递归 """
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False
