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

    def insert_front(self, data):
        """insert data point at the front of the list
        time complexity = O(1)
        space complexity = O(1)"""
        new_node = SllNode(data)

        if self.__head:
            new_node.set_next(self.__head)
            self.__head = new_node
            return

        self.__head = new_node
        return

    def insert_front_improved(self, data):
        """better because does not matter if self.__head
        is None or another node.
        Steps are the same:
            1. instantiate new node
            2. set next for new node = self.__head
            3. set self.__head = new node
        time complexity = O(1)
        space complexity = O(1)"""
        new_node = SllNode(data)
        new_node.set_next(self.__head)
        self.__head = new_node

    def insert_rear(self, data):
        """insert data point at the end of the list (APPEND)
        time complexity = O(n)
        space complexity = O(1)"""
        new_node = SllNode(data)

        current = self.__head
        while current.get_next():
            current = current.get_next()

        current.set_next(new_node)

    def insert_before(self, data, node_index: int):
        """insert data before node index
        ! can not insert before zero
        ! if node_index > list length -> insert as last element

        ! stupid method - better: insert_at_position
        ! for the sake of exercise

        Args:
            data: data point
            node_index (int): any integer but NOT ZERO
                (can not insert before zero)

        NOT same thing as insert_at_position.
            ex: for empty list:
                1. insert_at_position: we can insert at position 0
                2. insert_before:      we can NOT insert before position 0"""

        try:
            # catch exception if not integer:
            if not isinstance(node_index, int):
                raise ValueError('node_index must be integer!')
            # catch exception if zero:
            if node_index == 0:
                raise ValueError('node_index must be greater than zero! '
                                 'Can not insert before position 0!')
        except ValueError as ve:
            print(ve)
            return

        if self.__head:

            new_node = SllNode(data)

            current = self.__head
            previous = current
            index = 0
            while current:
                if node_index == index:
                    new_node.set_next(previous.get_next())
                    previous.set_next(new_node)
                    return
                previous = current
                current = current.get_next()
                index += 1

            # if node_index > index => add to the end of the list:
            new_node.set_next(previous.get_next())
            previous.set_next(new_node)
            return

        # if empty list -> insert as first element:
        else:
            self.insert_front_improved(data)

    def insert_after(self, data, node_index: int):
        """insert data after node index"""
        pass

    def insert_at_position(self, data, position: int):
        """insert data at position"""
        pass
        # # if list is empty (head = None) and
        # # we have to insert at position 0 =>
        # # we add_front to an empty list:
        # elif self.__head is None and node_index == 0:
        # self.insert_front_improved(data)

    def remove_front(self):
        """remove the first element of the list
        time complexity = O(1)
        space complexity = O(1)"""

        if self.__head:
            self.__head = self.__head.get_next()
            return

        print('Empty list - Nothing to remove!')
        return

    def remove_rear(self):
        """remove the last element of the list
        We keep track

        time complexity = O(n)
        space complexity = O(1)"""

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
            if data == current.get_data():
                return index
            index += 1
            current = current.get_next()

        if not current:
            # print(f'"{data}" not found in list!')
            return -1

    def print_sll(self):
        print('===== Singly Linked List =====')

        if self.__head:
            index = 0
            print(f'| data at index {index}: {self.__head.get_data()} - HEAD')
            current = self.__head.get_next()

            while current:
                index += 1
                print(f'| data at index {index}: {current.get_data()}')
                current = current.get_next()
        else:
            print('Empty List!')
        print('==============================')
