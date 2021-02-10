from Data_Structures.PyCharm_DataStr.ll2_singly_linked_list import SllNode, SLL


sll = SLL()

print(sll)
print()
print(f'Is the list empty?: {sll.is_empty()}')

sll.add_front('a')
print()
print(sll)
print('+++')
sll.print_sll()
print('+++')

sll.add_front_improved('b')
print()
print(sll)

sll.add_rear('c')
print()
print(sll)

print()
sll.print_sll()
# print(f'SLL size: {sll.size()}')
# print(f'Is the list empty?: {sll.is_empty()}')
#
print('aaaa', sll.search('a'))

