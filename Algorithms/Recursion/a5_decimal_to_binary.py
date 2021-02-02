"""
convert decimal to binary

1. iterative
2. recursive
"""


def dec_to_bin_iter(nr: int):

    bin_str = ''
    while nr != 0:
        reminder = nr % 2
        if reminder == 1:
            bin_str = '1' + bin_str
        else:
            bin_str = '0' + bin_str
        nr //= 2
    return bin_str


def dec_to_bin_iter2(nr: int):

    bin_str = ''
    while nr != 0:
        bin_str = str(nr % 2) + bin_str
        nr //= 2
    return bin_str


# test
print('Convert decimal to binary - iterative: ', dec_to_bin_iter(10))
print('Convert decimal to binary - iterative: ', dec_to_bin_iter2(10))


def dec_to_bin_rec(nr):
    if nr >= 1:
        dec_to_bin_rec(nr // 2)
        print(str(nr % 2), end='')


dec_to_bin_rec(10)
print(' - Convert decimal to binary - recursive')
