class Stack:
    """Stack implementation using a deque (collections) as
    a base for stack

    """
    def __init__(self):
        from collections import deque
        self.stack = deque()

    def push(self, item):
        """appends item to the top of the stack"""
        self.stack.append(item)

    def pop(self):
        """returns + removes last (top) item"""
        if self.stack:
            return self.stack.pop()
        return None

    def peek(self):
        """returns last item in the stack"""
        if self.stack:
            return self.stack[-1]
        return None

    def is_empty(self):
        """returns boolean value if stack is empty"""
        return len(self.stack) == 0

    def size(self):
        """returns integer - length of the stack"""
        return len(self.stack)

    def content(self):
        """returns the stack as a list"""
        stack_list = []
        for item in self.stack:
            stack_list.append(item)
        return stack_list

    def __str__(self):
        """returns the stack as string"""
        stack_list = ''
        for item in self.stack:
            stack_list += item
        return stack_list
