from Data_Structures.PyCharm_DataStr.ll2_singly_linked_list import SllNode, SLL


a = SllNode('a')
b = SllNode('b')
c = SllNode('c')
d = SllNode('d')

sll = SLL()

print(sll)
print(f'Is the list empty?: {sll.is_empty()}')

sll.add_front(a)
print(sll)

sll.add_front_improved(b)
print(sll)

sll.add_rear(c)
print(sll)
sll.print_sll()
print(f'SLL size: {sll.size()}')
print(f'Is the list empty?: {sll.is_empty()}')

print('aaaa', sll.search('a'))
