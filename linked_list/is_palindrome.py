from .linked_list import LinkedList

linked_list = LinkedList()
linked_list.append("1")
linked_list.append("2")
linked_list.append("3")
linked_list.append("3")
linked_list.append("2")
linked_list.append("1")

print(linked_list.is_palindrome())