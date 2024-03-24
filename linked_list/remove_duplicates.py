from .linked_list import LinkedList

# 1 -> 6 -> 1 -> 4 -> 2 -> 2 -> 4
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(6)
linked_list.append(1)
linked_list.append(4)
linked_list.append(2)
linked_list.append(2)
linked_list.append(4)

linked_list.remove_duplicates()
# 1 -> 6 -> 4 -> 2
linked_list.print_list()