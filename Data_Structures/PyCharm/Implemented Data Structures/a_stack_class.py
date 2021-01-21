class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Accepts an item as a parameter and
        appends it to the end of the list.
        Returns nothing

        The runtime for this method is O(1), or
        constant time, because appending to the
        end of a list happens in constant time.
        """
        self.items.append(item)

    def pop(self):
        """
        Returns and removes the last item from the
        list, which is also the top item of the Stack

        The runtime is constant time, because all it
        does is index to the last item of the list.
        """
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        """
        This method returns the last item in the list,
        which is also the item at the top of the Stack.

        Runs in constant time because indexing into a
        list is done in constant time.
        """
        if self.items:
            return self.items[-1]

        return None

    def size(self):
        """
        Returns the length of the list that is
        representing the Stack.

        This method is constant time because finding the
        length of a list is also constant time.
        """
        return len(self.items)

    def is_empty(self):
        """
        Returns a Boolean value whether or not the
        Stack is empty.

        Testing for equality happens in constant time.
        """

        return self.items == []
