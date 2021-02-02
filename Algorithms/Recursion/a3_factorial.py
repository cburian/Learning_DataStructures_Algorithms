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
    if n == 0:
        return 1
    return factorial_recursive(n-1) * n


# test
print('Factorial recursive: ', end='')
print(factorial_recursive(4))


# ======= dynamic programming =======
def factorial(n, memory={0: 1, 1: 1}):
    """Calculates factorial using dynamic programming.

    Args:
        n: the natural number that is the input for the algorithm.
        memory: the results dictionary will be updated with each function call.
    Returns:
        factorial of number n.
    """
    if n in memory:
        return memory[n]
    else:
        memory[n] = n * factorial(n-1)
        return memory[n]


print(factorial(4))
