from Data_Structures.PyCharm_DataStr.ll1_node import Node


class SllNode(Node):

    # __next: None

    def __init__(self, data):
        super().__init__(data)
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class SLL:

    head: None

    def __init__(self):
        self.__head = None

    def __repr__(self):
        return f'SLL object - head = {self.__head}'

    def add_front(self, data):
        new_node = SllNode(data)

        if self.__head:
            new_node.set_next(self.__head)
            self.__head = new_node
            return

        self.__head = new_node
        return

    def add_front_improved(self, data):

        new_node = SllNode(data)
        new_node.set_next(self.__head)
        self.__head = new_node

    def add_rear(self, data):
        new_node = SllNode(data)

        current = self.__head
        while current.get_next():
            current = current.get_next()

        current.set_next(new_node)

    def add_before(self, node_index):
        pass

    def add_after(self, node_index):
        pass

    def remove_front(self):

        if self.__head:
            self.__head = self.__head.get_next()
            return

        print('Empty list - Nothing to remove!')
        return

    def remove_rear(self):

        # empty list:
        if self.__head:

            # one element:
            if self.__head.get_next():

                # n > 1 element:
                current = self.__head
                previous = current
                while current:
                    previous = current
                    current = current.get_next()
                previous.set_next(None)

            self.__head = None
            return

        print('Empty list - Nothing to remove!')
        return

    def remove_before(self, node_index):
        """remove node before index"""
        pass

    def remove_after(self, node_index):
        """remove node after index"""
        pass

    def remove_value_front(self, value):
        """remove the first instance of a value"""
        pass

    def remove_value_rear(self, value):
        """remove last instance of a value"""
        pass

    def remove_values(self, value):
        """remove all instances of given value"""
        pass

    def size(self):
        """returns the size of the list"""
        current = self.__head
        size = 0
        while current:
            size += 1
            current = current.get_next()
        return size

    def is_empty(self):
        """returns True if list is empty, False otherwise"""
        return self.__head is None

    def search(self, data):
        """returns the index of data"""
        current = self.__head
        index = 0
        while current:
            print(current.get_data(), type(current.get_data()))
            if data == current.get_data():
                return index
            index += 1
            current = current.get_next()

        if not index:
            print(f'{data} not found in list!')
            return

    def print_sll(self):
        print('=== Singly Linked List Object ===')

        if self.__head:
            print(f'head data: {self.__head.get_data()}')
            current = self.__head.get_next()
            while current:
                print(f'data: {current.get_data()}')
                current = current.get_next()
        else:
            print('Empty List!')
        print('=================================')
