# coding:utf-8
def quick_sort(alist, first, last):
    """ 快速排序 """
    if first >= last:
        return
    n = len(alist)
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # high左移
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        while low < high and  alist[high] < mid_value:
            low += 1
        alist[high] = alist[low]
    # 从循环退出时,low==high
    alist[low] = mid_value

    # 对low左边的列表执行快速排序
    quick_sort(alist, first, low-1)

    # 对low右边的列表排序
    quick_sort(alist, low+1, last)
    