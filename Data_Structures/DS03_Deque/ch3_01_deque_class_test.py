from Chapter3_The_Deque.ch3_01_deque_class import Deque

my_d = Deque()
print(my_d.items)

my_d.add_front('a')
print(my_d.items)

my_d.add_front(1)
my_d.add_rear('z')
print(my_d.items)
