#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Merge Sort

import utils


def sort(array, low, high):
    if low < high:
        mid = (low + high) / 2
        merge_sort(array, low, mid)
        merge_sort(array, mid + 1, high)
        merge(array, low, mid, high)
    return array


def merge(array, low, mid, high):
    left = array[low:mid + 1]
    right = array[mid + 1:high + 1]
    i = j = 0

    for k in range(low, high + 1):
        if i == len(left):
            array[k:high + 1] = right[j:]
            break
        elif j == len(right):
            array[k:high + 1] = left[i:]
            break
        else:
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1


if __name__ == "__main__":
    l = utils.generate_array(150)
    print l
    array = merge_sort(l, 0, len(l) - 1)
    print array
