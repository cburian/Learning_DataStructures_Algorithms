"""
Write a function in python that can
reverse a string using stack data structure

example: reverse_string("We will conquer COVID-19")
        should return "91-DIVOC reuqnoc lliw eW"
"""


# from Data_Structures.PyCharm_DataStr.stack_list import Stack
from Data_Structures.PyCharm_DataStr.stack_deque import Stack


def reverse_str(data: str) -> Stack:

    original = Stack()
    for character in data:
        original.push(character)

    reversed_data = Stack()
    for _ in data:
        reversed_data.push(original.pop())

    return reversed_data


my_str = "We will conquer COVID-19"

print(reverse_str(my_str))
