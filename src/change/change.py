#!/usr/bin/python

import math

# Set 6 - 2
# http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2008/assignments/


def make_change(denominations, C):
    if C is 0:
        return []

    possible_combinations = []
    for value in denominations:
        if value is C:
            possible_combinations.append([value])
        elif value < C:
            combination = [value]
            combination.extend(make_change(denominations, C - value))
            possible_combinations.append(combination)

    if len(possible_combinations) is 0:
        raise Exception("Change is smaller than the minimum denomination.")

    min_combination = possible_combinations[0]
    cumulative_min = len(min_combination)
    for combination in possible_combinations:
        current_min = len(combination)
        if current_min < cumulative_min:
            cumulative_min = current_min
            min_combination = combination

    return min_combination


if __name__ == '__main__':
    print make_change()
