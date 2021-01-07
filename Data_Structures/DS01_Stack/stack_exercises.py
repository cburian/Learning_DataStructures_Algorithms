class StackLst:
    def __init__(self):
        self.stack = []

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stask)

    def content(self):
        return self.stack


class StackDq:
    def __init__(self):
        from collections import deque
        self.stack = deque()

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def content(self):
        stack_list = []
        for e in self.stack:
            stack_list.append(e)
        return stack_list


"""
Write a function in python that can reverse a string 
using stack data structure.

example: 
reverse_string("We will conquer COVID-19") should return 
"91-DIVOC reuqnoc lliw eW"
"""


# def reverse_str(data: str):
#     original_data = StackDq(data)
#     reversed_data = ''
#
#     for _ in range(original_data.size()):
#         reversed_data += original_data.pop()
#
#     return reversed_data
#
#
# print(reverse_str('We will conquer COVID-19'))

"""
Write a function in python that checks if parenthesis in 
the string are balanced or not. 

Possible parentheses are "{}',"()" or "[]"

example:
is_balanced("({a+b})")     --> True
is_balanced("))((a+b}{")   --> False
is_balanced("((a+b))")     --> True
is_balanced("))")          --> False
is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
"""


def is_balanced(data: str):
    open_p = '([{'
    close_p = ')]}'
    stack = StackDq()

    for symbol in data:
        if symbol in open_p:
            stack.push(symbol)
        if symbol in close_p:
            symbol_index = close_p.index(symbol)
            if open_p[symbol_index] != stack.peek():
                return False
            else:
                stack.pop()
        # print(stack.content())
    return stack.is_empty()


def is_balanced2(data: str):
    s_dict = {')': '(', ']': '[', '}': '{'}
    stack = StackDq()
    iteration = 0

    for symbol in data:
        if symbol in s_dict.values():
            stack.push(symbol)
        if symbol in s_dict.keys():
            if stack.is_empty() or s_dict[symbol] != stack.peek():
                return False, iteration
            else:
                stack.pop()
        iteration += 1
        # print(stack.content())
    return stack.is_empty(), iteration


print(is_balanced2('(())'))
test_data = ['([{}])', '(([{])', '([]{}())', '(((())))',
             '[}([){]', '}[]{()}', '[(}[]{)]', '([]{}()))',
            "({a+b})", "))((a+b}{", "((a+b))", "((a+g))",
             "))", "[a+b]*(x+2y)*{gg+kk}"]
print('=====================')
for i, x in enumerate(test_data):
    print(f'test {i + 1}. with test value: {x}')
    print(is_balanced2(x))


"""
undo redo
"""