from Data_Structures.PyCharm_DataStr.ll1_node import Node


class SllNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node

    def __repr__(self):
        return str(self.get_data())


class SLL:

    def __init__(self, nodes: list = None):
        """
        Args:
            nodes: list

        ! improve to take:
        tuple, *args, string, string of len = 1, integer
        """
        self.__head = None

        if nodes:
            node = SllNode(data=nodes.pop(0))
            self.__head = node
            for elem in nodes:
                node.set_next(SllNode(data=elem))
                node = node.get_next()

    def __repr__(self):

        node = self.__head
        nodes = []

        while node:
            # print(node.get_data())
            nodes.append(str(node.get_data()))
            node = node.get_next()

        # if 'None' not in nodes and self.__head:
        nodes.append('None')

        return ' -> '.join(nodes)

    def show(self):
        """shows liked list as list"""
        node = self.__head
        nodes = []

        while node:
            nodes.append(str(node.get_data()))
            node = node.get_next()

        print(nodes)

    def __iter__(self):
        node = self.__head
        while node:
            yield node
            node = node.get_next()

    def insert_front(self, data):
        """Inserts data at the front of the list.

        Args:
            data: data to be inserted at the front of the list

        Steps:
            1. instantiate new node
            2. set next for new node = self.__head
            3. set self.__head = new node
        time complexity = O(1)
        space complexity = O(1)"""
        new_node = SllNode(data)
        new_node.set_next(self.__head)
        self.__head = new_node

    def insert_rear(self, data):
        node = self.__head

        if node is None:
            self.__head = SllNode(data)
            return

        while node.get_next():
            node = node.get_next()
        node.set_next(SllNode(data))

    def insert_rear2(self, data):

        if self.__head is None:
            self.__head = SllNode(data)
            return

        for current_node in self:
            pass
        node = SllNode(data)
        current_node.set_next(node)

    def insert_at_index(self, data, index: int):

        # index < 0 or
        # index not integer or
        # index greater than list size:
        if not isinstance(index, int):
            raise ValueError('Index must be integer.')
        if index < 0:
            raise ValueError('Can not insert at negative index.')
        if index > self.size():
            raise Exception(f'Index greater than list size. '
                            f'Can not insert at index: {index} for '
                            f'a list of size: {self.size()}')

        node = SllNode(data)

        # if list is empty:
        if self.__head is None:
            self.__head = node
            return

        # if index = 0 insert at the front of the list:
        if index == 0:
            self.insert_front(data)
            return

        # if index = size of list -> insert at back of list:
        if index == self.size():
            self.insert_rear2(data)
            return

        current_index = 0
        previous_node = self.__head

        for current_node in self:
            if current_index == index:
                node.set_next(current_node)
                previous_node.set_next(node)
                return
            current_index += 1
            previous_node = current_node

    def insert_before_index(self, new_node, index):
        pass

    def insert_after_index(self, new_node, index):
        pass

    def insert_before_data(self, new_node, data_reference):
        pass

    def insert_after_data(self, new_node, data_reference):
        pass

    def replace_data(self, data_to_insert, data_to_delete):
        pass

    def remove_front(self, data):
        pass

    def remove_rear(self, data):
        pass

    def remove_at_index(self, index: int):
        pass

    def remove_value_front(self, data):
        pass

    def remove_value_rear(self, data):
        pass

    def remove_values(self, data):
        pass

    def size(self):
        node = self.__head
        length = 0

        while node:
            length += 1
            node = node.get_next()

        return length

    def is_empty(self):
        return self.__head is None

    def search(self, data):
        pass

    def search_all(self, data):
        pass
