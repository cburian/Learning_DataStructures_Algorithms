"""
Using a deque data structure, write a function that
takes in an input string and returns:
    True if the string is a palindrome
    False if the string is not a palindrome
palindrome example:
    mom, level, kayak
"""

from Chapter3_The_Deque.ch3_01_deque_class import Deque


def check_palindrome(input_str):

    my_d = Deque()

    for char in input_str:
        my_d.add_rear(char)

    while my_d.size() >= 2:  # size of 1 or 0 means the string is a palindrome
        front_item = my_d.pop_front()
        rear_item = my_d.pop_rear()

        if front_item != rear_item:
            return False

    return True


# test:
print(check_palindrome('lvvel'))
