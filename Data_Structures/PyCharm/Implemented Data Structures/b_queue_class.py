class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        Takes in an item and inserts that item into the 0th
        index of the list that is representing the Queue

        Runtime is O(n) because inserting into the 0th
        index of a list forces all other items in the list
        to move one index to the right.
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        Returns and removes the front-most item of the Queue,
        represented by the last item in the list.

        The runtime is O(1), because indexing to the end of a
        list happens in constant time
        """
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        """
        Returns the last item in the list, the front-most
        item in teh queue.

        The runtime is constant because we're just indexing
        to the last item of the list and returning the value
        found there.
        """
        if self.items:
            return self.items[-1]

        return None

    def size(self):
        """
        Returns the size of the Queue, represented by the
        length of the list

        The runtime is constant time, because we're returning
        the length
        """
        return len(self.items)

    def is_empty(self):
        """
        Returns Boolean expressing whether or not the list
        representing the Queue is empty.

        Runs in constant time, because it's only checking
        for equality.
        """
        return self.items == []
