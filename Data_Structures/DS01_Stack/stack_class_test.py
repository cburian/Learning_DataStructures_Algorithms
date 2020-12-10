from Data_Structures.DS01_Stack.stack_class import Stack

# test Stack
my_s = Stack()
print(my_s.pop())
print('length: ', my_s.size())
print('is the stack empty: ', my_s.is_empty())
#
my_s.push('apple')
print(my_s.items)
my_s.push('banana')
print('peek: ', my_s.peek())
print('length: ', my_s.size())
print(my_s.items)
print('is the stack empty?: ', my_s.is_empty())
print('pop: ', my_s.pop())
print(my_s.items)
print('peek', my_s.peek())
