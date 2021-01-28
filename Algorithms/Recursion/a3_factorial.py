"""

"""


def factorial_iterative(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


# test
print('Factorial iterative: ', end='')
print(factorial_iterative(4))


def factorial_recursive(n):
    if n == 1:
        return 1
    return factorial_recursive(n-1) * n


# test
print('Factorial recursive: ', end='')
print(factorial_recursive(4))
