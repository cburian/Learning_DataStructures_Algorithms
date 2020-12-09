"""
Using a deque data structure, write a function that
takes in an input string and returns:
    True if the string is a palindrome
    False if the string is not a palindrome
palindrome example:
    mom, level, kayak
"""

from Chapter3_The_Deque.ch3_01_deque_class import Deque


def check_palindrome(word):

    word_dq = Deque()
    for c in word:
        word_dq.add_rear(c)
    print(word_dq.items)

    flag = False
    while word_dq.size() > 1:
        if word_dq.pop_front() == word_dq.pop_rear():
            flag = True
        else:
            flag = False

    return flag


print(check_palindrome('lvvel'))
