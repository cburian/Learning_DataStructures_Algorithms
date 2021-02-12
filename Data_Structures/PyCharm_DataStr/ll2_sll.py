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
        return self.get_data()


class SLL:

    def __init__(self, nodes=None):
        """improve to take tuple, *args, one str """
        self.__head = None

        if hasattr(nodes, '__iter__'):
            if nodes:
                node = SllNode(data=nodes.pop(0))
                self.__head = node
                for elem in nodes:
                    node.set_next(SllNode(data=elem))
                    node = node.get_next()
        else:
            self.insert_front(nodes)

    def __repr__(self):
        node = self.__head
        nodes = []

        while node:
            print(node)
            nodes.append(node.get_data())
            node = node.get_next()

        # if 'None' not in nodes and self.__head:
        nodes.append('None')

        print(nodes)
        return ' -> '.join(nodes)

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

        if node:
            while node.get_next():
                node = node.get_next()
        node.set_next(SllNode(data))

    def insert_at_index(self, data, index: int):
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
        pass

    def is_empty(self):
        pass

    def search(self, data):
        pass

    def search_all(self, data):
        pass
