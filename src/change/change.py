#!/usr/bin/python

# Set 6 - 2
# http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2008/assignments/


def make_change(denominations, C):
    """ Returns an array of the change needed to make C from the set of possible denominations.
        E.g.,
          make_change([1, 5, 10, 17], 34)
          >> [17, 17]

          make_change([1, 5, 10, 17], 33)
          >> [1, 5, 10, 17]
    """

    # sorting helps us bail quicker in the for loop below.
    denominations.sort()

    # memoization of best_change
    change_arr = {0: []}

    def best_change(R):
        if R not in change_arr:
            min_change = None
            for denomination in denominations:
                if denomination == R:
                    min_change = [denomination]
                    break
                elif denomination < R:
                    this_change = [denomination] + best_change(R - denomination)
                    if not min_change or len(min_change) > len(this_change):
                        min_change = this_change
                else:
                    break
            change_arr[R] = min_change
        return change_arr[R]

    # bottom up
    for D in range(C):
        best_change(D)

    return best_change(C)
