class Stack:
    """Stack implementation using a list as a base for stack

    !!! Issue: list - dynamic array - reallocates memory
    """

    def __init__(self):
        self.stack = []

    def push(self, item):
        """appends item to the end of the list"""
        self.stack.append(item)

    def pop(self):
        """returns + removes last item (top item)"""
        if self.stack:
            return self.stack.pop()
        return None

    def peek(self):
        """returns last item in the list"""
        if self.stack:
            return self.stack[-1]
        return None

    def is_empty(self):
        """returns boolean value if stack is empty"""
        return self.stack == []

    def size(self):
        """returns integer - length of the list (stack)"""
        return len(self.stack)

    def content(self):
        """returns the list (stack)"""
        return self.stack
