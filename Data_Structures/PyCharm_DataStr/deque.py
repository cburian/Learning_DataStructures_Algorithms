class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def pop_front(self):
        if self.items:
            return self.items.pop(0)
        return None

    def pop_rear(self):
        if self.items:
            return self.items.pop()
        return None

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek_front(self):
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        if self.items:
            return self.items[-1]
        return None
