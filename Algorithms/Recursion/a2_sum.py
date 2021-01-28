"""
Write a function that given input n, sums
all non-negative integers up to n.

source: https://www.youtube.com/watch?v=ngCos392W4w&ab_channel=Reducible
"""

''' """""""""""""""""""""""" '''
"""     Iterative Method     """
''' """""""""""""""""""""""" '''


def sum_iterative(n):
    result = 0
    while n:
        result += n
        n -= 1
    return result


def sum_iterative2(n):
    result = 0
    for i in range(n + 1):
        result += i
    return result


# test:
print('Iterative Method 1: ', end=' ')
print(sum_iterative(5))
print('Iterative Method 2: ', end=' ')
print(sum_iterative2(5))


''' """"""""""""""""""""""""""" '''
"""     Mathematical Method     """
''' """"""""""""""""""""""""""" '''


def sum_mathematical(n):
    return (n+1) * n // 2


# test:
print('Mathematical Method: ', end=' ')
print(sum_mathematical(5))


''' """""""""""""""""""""""" '''
"""     Recursive Method     """
''' """""""""""""""""""""""" '''


def sum_recursive(n):
    if n == 0:
        return 0
    return sum_recursive(n-1) + n


# test:
print('Recursive Method: ', end=' ')
print(sum_recursive(5))
