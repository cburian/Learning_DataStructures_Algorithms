"""
greatest common divisor

"""


def gcd(a, b):

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


# test:
print(gcd(120, 90))


def gcd2(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


# test
print(gcd2(5, 4))
