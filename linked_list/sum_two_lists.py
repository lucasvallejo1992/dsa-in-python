from .linked_list import LinkedList

list1 = LinkedList()
list1.append(5)
list1.append(6)
list1.append(3)

list2 = LinkedList()
list2.append(8)
list2.append(4)
list2.append(2)

def sum_two_lists(self, other_list):
  node_first = self.head
  node_other = other_list.head

  sum_list = LinkedList()

  carry_over = 0
  while node_first or node_other:
    if not node_first:
      data_self = 0
    else:
      data_self = node_first.data
    if not node_other:
      data_other = 0 
    else:
      data_other = node_other.data
    sum_data = data_self + data_other + carry_over
    if sum_data >= 10:
      carry_over = 1
      remainder = sum_data % 10
      sum_list.append(remainder)
    else:
      carry_over = 0
      sum_list.append(sum_data)
    if node_first:
      node_first = node_first.next
    if node_other:
      node_other = node_other.next
  return sum_list

result_list = sum_two_lists(list1, list2)
result_list.print_list()