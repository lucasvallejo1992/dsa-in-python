class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def print_list(self):
    cur_node = self.head
    print_value = ""
    while cur_node:
      print_value += str(cur_node.data) + ("" if cur_node.next == None else " -> ")
      cur_node = cur_node.next
    print(print_value)

  def append(self, data):
    new_node = Node(data)

    if self.head is None:
      self.head = new_node
      return 

    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node

  def delete(self, value):
    cur_node = self.head

    if cur_node and cur_node.data == value:
      self.head = cur_node.next
      return

    prev_node = None

    while cur_node and cur_node.data != value:
      prev_node = cur_node
      cur_node = cur_node.next

    if cur_node is None:
      return

    prev_node.next = cur_node.next
  
  def prepend(self, data):
    new_node = Node(data)

    new_node.next = self.head
    self.head = new_node

  def insert_after_node(self, prev_node, data):
    if not prev_node:
      print("Previous node does not exist.")
      return
    if not isinstance(prev_node, Node):
      print("Previous node is not a Node object.")
      return

    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node_at(self, position):
    if self.head is None:
      return

    cur_node = self.head
    if position == 0:
      self.head = cur_node.next
      return

    prev_node = None
    count = 0
    while cur_node and count != position:
      if cur_node.next is None:
        print("Position out of range.")
        return
      prev_node = cur_node
      cur_node = cur_node.next
      count += 1
    
    if cur_node is None:
      return
    
    prev_node.next = cur_node.next

  def swap_nodes(self, key_1, key_2):
    if key_1 == key_2:
      return 

    prev_1 = None 
    curr_1 = self.head 
    while curr_1 and curr_1.data != key_1:
      prev_1 = curr_1 
      curr_1 = curr_1.next

    prev_2 = None 
    curr_2 = self.head 
    while curr_2 and curr_2.data != key_2:
      prev_2 = curr_2 
      curr_2 = curr_2.next

    if not curr_1 or not curr_2:
      return 

    if prev_1:
      prev_1.next = curr_2
    else:
      self.head = curr_2

    if prev_2:
        prev_2.next = curr_1
    else:
        self.head = curr_1

    curr_1.next, curr_2.next = curr_2.next, curr_1.next
  
  def reverse(self):
    prev = None 
    cur = self.head
    while cur:
      nxt = cur.next
      cur.next = prev
      prev = cur 
      cur = nxt 
    self.head = prev

  def length(self):
    cur_node = self.head
    count = 0
    while cur_node:
      count += 1
      cur_node = cur_node.next
    return count
