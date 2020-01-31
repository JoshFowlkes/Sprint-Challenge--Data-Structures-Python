import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


# a quene is first in first out(FIFO)
    # ie if theres a line of people waiting for something, the new person
    # enters at the back of the line, and doesnt get served until the 
    # people ahead of him have gotten served first
# a stack is first in last out

''' Python lists not allowed for this weeks assignments  '''

class Queue:
    '''
    A Queue is first in first out
    '''
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        '''
        Add an item to the back of the Quene
        '''
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        '''
        Remove an item from the front of the Quene
        '''
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        '''
        Return the number of items in the Quene
        '''
        return self.size
