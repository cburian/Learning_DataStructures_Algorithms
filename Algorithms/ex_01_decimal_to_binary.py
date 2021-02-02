"""
Convert a decimal to a binary
"""


def convert_decimal_to_binary(number: int):
    binary_str = ''

    while number != 0:
        remainder = number % 2

        if remainder == 1:
            binary_str = '1' + binary_str
        else:
            binary_str = '0' + binary_str

        number //= 2

    return binary_str


# test:

print(convert_decimal_to_binary(6))
