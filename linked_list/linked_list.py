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

  def merge_sorted(self, other_list):
    cur_self = self.head 
    cur_other = other_list.head
    sorted = None

    if not cur_self:
        return cur_other
    if not cur_other:
        return cur_self

    if cur_self and cur_other:
        if cur_self.data <= cur_other.data:
            sorted = cur_self 
            cur_self = sorted.next
        else:
            sorted = cur_other
            cur_other = sorted.next
        new_head = sorted 
    while cur_self and cur_other:
        if cur_self.data <= cur_other.data:
            sorted.next = cur_self 
            sorted = cur_self 
            cur_self = sorted.next
        else:
            sorted.next = cur_other
            sorted = cur_other
            cur_other = sorted.next
    if not cur_self:
        sorted.next = cur_other 
    if not cur_other:
        sorted.next = cur_self

    self.head = new_head     
    return self.head

  def remove_duplicates(self):
    cur = self.head
    prev = None
    dup_values = dict()

    while cur:
      if cur.data in dup_values:
        prev.next = cur.next
        cur = None
      else:
        dup_values[cur.data] = 1
        prev = cur
      cur = prev.next

  def get_nth_from_last(self, n):
    main_pointer = self.head
    ref_pointer = self.head

    if n > 0:
        count = 0
        while ref_pointer:
            count += 1
            if(count>=n):
                break
            ref_pointer = ref_pointer.next
            
        if not ref_pointer:
            print(str(n) + " is greater than the number of nodes in list.")
            return None

        while ref_pointer.next:
            main_pointer = main_pointer.next
            ref_pointer = ref_pointer.next
        return main_pointer.data
    else:
        return None
    
  def is_palindrome(self):
    slow = fast = self.head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    prev = None
    while slow:
      nxt = slow.next
      slow.next = prev
      prev = slow
      slow = nxt

    left = self.head
    right = prev
    while right:
      if left.data != right.data:
        return False
      left = left.next
      right = right.next

    return True