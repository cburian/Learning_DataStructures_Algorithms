class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        """
        Takes an item as a parameter and inserts it into the 0th
        index of the list that is representing the Deque

        The runtime is linear or O(n), because every time you
        insert into the front of a list, all the other items
        in the list need to shift one position to the right.
        """
        self.items.insert(0, item)

    def add_rear(self, item):
        """
        Takes an item as a parameter and appends it to the end
        of the list that is representing the Deque

        The runtime is constant or O(1), because every time you
        insert into the end of a list, is constant time.
        """
        self.items.append(item)

    def pop_front(self):
        """
        Removes and returns an item from the front of the
        list that is representing the Deque.

        The runtime is O(n), because all items have to be moved
        to the left.
        """
        if self.items:
            return self.items.pop(0)
        return None

    def pop_rear(self):
        """
        Removes and returns an item from the end of the
        list that is representing the Deque.

        The runtime is O(1), because removing an item from
        the end takes constant time.
        """
        if self.items:
            return self.items.pop()
        return None

    def is_empty(self):
        """
        Returns True if the list that represents the Deque
        is empty and False if is not empty

        The run time is O(1).
        """
        return self.items == []

    def size(self):
        """
        Returns the length of the list that represents the Deque

        The runtime is O(1).
        """
        return len(self.items)

    def peek_front(self):
        """
        Returns the first item in the list.

        The runtime is O(1).
        """
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        """
        Returns the last item in the list.

        The runtime is O(1).
        """
        if self.items:
            return self.items[-1]
        return None
