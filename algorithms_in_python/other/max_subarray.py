#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Max Subarray


def find_max_crossing_subarray(array, low, mid, high):
    max_left = max_right = float("-inf")
    left_sum = float("-inf")
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += array[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = float("-inf")
    sum = 0
    for j in range(mid + 1, high):
        sum += array[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return max_left, max_right, left_sum + right_sum


def find_max_subarray(array, low, high):
    if high == low:
        return low, high, array[low]
    else:
        mid = (low + high) / 2
        left_low, left_high, left_sum = find_max_subarray(array, low, mid)
        right_low, right_high, right_sum = find_max_subarray(array, mid + 1,
                                                             high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(array,
                                                                      low,
                                                                      mid,
                                                                      high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum
