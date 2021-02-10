class Node:

    # __data: None

    def __init__(self, data):
        self.__data = data

    def __repr__(self):
        return f'Node obj. - data = {self.__data}'

    def get_data(self):
        return self.__data

    def set_data(self, new_data):
        self.__data = new_data
