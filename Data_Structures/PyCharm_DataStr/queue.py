class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """takes an item and inserts it into the 0th index
        of the list """
        self.items.insert(0, item)

    def dequeue(self):
        """returns and removes the front most item in the queue,
        the last item in the list"""
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """returns the last item in the list, the front-most
        item in the queue"""
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """returns the size of the queue"""
        return len(self.items)

    def is_empty(self):
        """returns bool whether or not the queue is empty"""
        return self.items == []
