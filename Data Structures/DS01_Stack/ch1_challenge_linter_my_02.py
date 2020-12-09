"""
Correcting the first solution
After check solution.
"""
from Chapter1_The_Stack.ch1_01_stack_class import Stack


def balance(symbol_str):

    symbol_pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    openers = symbol_pairs.keys()

    my_stack = Stack()

    # measuring performance: Iterations:
    index = 0
    for s in symbol_str:
        if s in openers:  # symbol = opener
            my_stack.push(s)
        else:  # symbol = closer
            # if the Stack is already empty, the
            # symbols are not balanced
            if my_stack.is_empty():
                return False, index
            # if still items in Stack, check for
            # a mis-match:
            else:
                top_item = my_stack.pop()
                if s != symbol_pairs[top_item]:
                    return False, index

        index += 1

    if my_stack.is_empty():
        return True, index

    return False, index


test_data = ['([{}])', '(([{])', '([]{}())', '(((())))',
             '[}([){]', '}[]{()}', '[(}[]{)]', '([]{}()))']

for test in test_data:
    print(balance(test))
