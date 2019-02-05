# coding: utf-8
def merge_sort(alist):
    """ 归并算法 """
    n = len(alist)
    if n <= 1:
        return
    mid = n // 2
    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])
    # 将两个有序的子序列合并成为一个新的整体
    left_pointer, right_pointer = 0,0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer]
    result += right_li[right_pointer]
    return result