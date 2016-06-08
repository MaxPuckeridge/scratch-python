#!/usr/bin/python

# Set 6 - 1
# http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2008/assignments/

memoize_data = {}


def fib_recursive(n):
    """Calculates the fibonacci number, using a recursive process."""
    if n > 1:
        return fib_recursive(n - 1) + fib_recursive(n - 2)
    return n


def fib_memoize(n):
    """Calculates the fibonacci number, using a recursive process, with memoization."""
    if n not in memoize_data:
        if n > 1:
            memoize_data[n] = fib_memoize(n - 1) + fib_memoize(n - 2)
        else:
            memoize_data[n] = n
    return memoize_data[n]


def fib_bottom_up(n):
    """Calculates the fibonacci number, using a bottom-up process."""
    arr = []

    i = 0
    while i <= n:
        if i > 1:
            arr.append(arr[i - 1] + arr[i - 2])
        else:
            arr.append(i)
        i += 1

    return arr[i - 1]


def fib_in_place(n):
    """Calculates the fibonacci number, using an in-place bottom up approach."""
    if n < 2:
        return n

    arr = [0, 1]
    i = 1
    while i < n:
        total = arr[0] + arr[1]
        arr = [arr[1], total]
        i += 1

    return arr[1]
