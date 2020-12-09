from Chapter1_The_Stack.ch1_01_stack_class import Stack


def balance(symbol_str):

    symbol_pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    openers = symbol_pairs.keys()
    my_stack = Stack()

    index = 0
    while index < len(symbol_str):
        symbol = symbol_str[index]

        if symbol in openers:
            my_stack.push(symbol)
        else:  # the symbol is a closer

            # if the Stack is already empty, the
            # symbols are not balanced
            if my_stack.is_empty():
                return False, index

            # if there are still items in the
            # Stack, check for mis-match.
            else:
                top_item = my_stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False, index

        index += 1

    if my_stack.is_empty():
        return True, index

    return False, index


test_data = ['([{}])', '(([{])', '([]{}())', '(((())))',
             '[}([){]', '}[]{()}', '[(}[]{)]']

for test in test_data:
    print(balance(test))
