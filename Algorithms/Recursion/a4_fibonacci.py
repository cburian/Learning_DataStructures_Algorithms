"""
Fibonacci

fibonacci sequence: 0 1 1 2 3 5 8
position:           0 1 2 3 4 5 6
"""


def fibonacci_iterative(n):
    x = 0
    y = 1

    if n == 0:
        return n

    for i in range(1, n):
        x, y = y, x + y

    return y


# test:
print('Fibonacci iterative: ', fibonacci_iterative(10))


def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# test:
print('Fibonacci recursive: ', fibonacci_recursive(10))
