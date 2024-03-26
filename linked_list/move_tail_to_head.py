from .linked_list import LinkedList

linked_list = LinkedList()
linked_list.append("A")
linked_list.append("B")
linked_list.append("C")
linked_list.append("D")

linked_list.move_tail_to_head()

linked_list.print_list()