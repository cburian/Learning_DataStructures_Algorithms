from Data_Structures.PyCharm_DataStr.ll2_singly_linked_list import SLL


def test_list(sll):
    print('==== List TEST: ====')
    print()
    print('print list: ')
    print(sll)
    print()
    print('Test is_empty:')
    print(f'Is the list empty?: {sll.is_empty()}')
    print()
    print('Test search:')
    print('index of element: ', sll.search('a'))
    print()
    print('Test remove_front: ')
    sll.remove_front()
    print()
    print('Test remove_rear: ')
    sll.remove_rear()
    print()
    print('Test size:')
    print(sll.size())


if __name__ == '__main__':
    ll = SLL()
    ll.insert_before('x', 50)
    ll.print_sll()

    # test_list(ll)

    ll.insert_front('a')
    ll.insert_front_improved('b')
    ll.insert_rear('c')
    ll.print_sll()

    ll.insert_before('x', 0)
    ll.print_sll()

    # a = [1, 2, 3]
    # print(a)
    # a.insert(40, 'a')
    # print(a)
#
# print()
# sll.print_sll()
# # print(f'SLL size: {sll.size()}')
# # print(f'Is the list empty?: {sll.is_empty()}')
# #
# # print('aaaa', sll.search('f'))
#
