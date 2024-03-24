from .linked_list import LinkedList

linked_list = LinkedList()
linked_list.append("A")
linked_list.append("B")
linked_list.append("C")
linked_list.append("D")

print(linked_list.get_nth_from_last(2))