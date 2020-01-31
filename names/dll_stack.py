import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    '''
    a Stack is First in Last out
    Using a line of people example, its like someone cutting to the front of 
    the line, and then going first ahead of all the others
    '''
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        '''
        Much like Quene except this adds to the head rather than add to the back
        '''
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        '''
        Remove item from the head of the stack
        '''
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        '''
        Return the number of items in the stack
        '''
        return self.size
