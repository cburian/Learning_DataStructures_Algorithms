from Data_Structures.DS01_Stack.stack_class import Stack


def balance(symbol_str):
    open_symbols = ['(', '[', '{']
    close_symbols = [')', ']', '}']

    my_stack = Stack()

    # measuring performance: Iterations:
    iteration = 0
    for s in symbol_str:
        if s in open_symbols:
            my_stack.push(s)
        if s in close_symbols:
            my_stack.pop()

        iteration += 1

    if my_stack.is_empty():
        return True, iteration

    return False, iteration


test_data = ['([{}])', '(([{])', '([]{}())', '(((())))',
             '[}([){]', '}[]{()}', '[(}[]{)]', '([]{}()))']

for test in test_data:
    print(balance(test))

"""
The solution is NOT good. The 7th test fails.
The first closed symbol it is not pushed, and 
because it is a close symbol, it pops the last
element of an empty list, which does no return
an error. 
"""
