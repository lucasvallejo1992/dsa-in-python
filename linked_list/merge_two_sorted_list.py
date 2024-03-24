from .linked_list import LinkedList

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

linked_list_1.append('A')
linked_list_1.append('C')
linked_list_1.append('D')
linked_list_1.append('G')
linked_list_1.append('Z')

linked_list_2.append('B')
linked_list_2.append('F')
linked_list_2.append('H')
linked_list_2.append('J')
linked_list_2.append('K')

linked_list_1.merge_sorted(linked_list_2)
linked_list_1.print_list()