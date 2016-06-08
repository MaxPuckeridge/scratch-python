#!/usr/bin/env python


def select(input_array, n):
    """Returns the nth highest number from the array."""
    m5m = median5median(input_array)

    left = []
    exact = []
    right = []

    for val in input_array:
        if val < m5m:
            left.append(val)
        elif val == m5m:
            exact.append(val)
        else:
            right.append(val)

    if n < len(left):
        return select(left, n)
    elif len(left) <= n < len(left) + len(exact):
        return m5m
    else:
        return select(right, n - len(left) - len(exact))


def median(input_array):
    """Returns the median of the array."""
    input_array.sort()
    return input_array[(len(input_array) - 1)/2]


def median5median(input_array):
    """Returns the median of medians for the array."""
    cumulative_medians = []
    sub_list = []

    index = 0
    while index < len(input_array):
        sub_list.append(input_array[index])
        if len(sub_list) is 5:
            cumulative_medians.append(median(sub_list))
            sub_list = []
        index += 1

    if len(sub_list) > 0:
        cumulative_medians.append(median(sub_list))
    return median(cumulative_medians)
