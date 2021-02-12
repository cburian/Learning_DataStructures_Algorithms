from Data_Structures.PyCharm_DataStr.ll2_sll import SLL, SllNode


# ll = SLL(['1', '2', '3'])
# ll = SLL(1)
# ll = SLL([1, 2])
ll = SLL()
# ll.insert_rear(['a'])
# ll.insert_rear('b')
print(ll)
ll.show()

print('empty? ', ll.is_empty())
print('size: ', ll.size())
print()

ll.insert_front('1')
ll.show()
ll.insert_rear2('2')
ll.show()
ll.insert_front('0')
ll.show()
ll.insert_rear2('3')
ll.show()
ll.insert_at_index('888', index=4)
ll.show()
