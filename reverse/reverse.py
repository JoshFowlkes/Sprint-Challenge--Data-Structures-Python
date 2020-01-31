class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  
  
  
  def reverse_list(self):
   '''
   In the case of an empty list
   '''
   if self.head is None or self.head.get_next() is None:
     return
   else:
     '''
     Otherwise we want to take a list from 1,2,3, and turn it into 3,2,1
     '''
     left = self.head
     temp = left.get_next()
     left.set_next(None)
     while temp and temp.get_next():
       '''
       Using a temporary, will set the left.get_next to the temporary, then the temporary to the right, then reverse through
       the entire list. Will loop until there are no more to the right of it.
       '''
       right = temp.get_next()
       temp.set_next(left)
       left = temp
       temp = right
     '''
     Setting New Head 
     '''
     temp.set_next(left) 
     self.head = temp
  
