from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        '''
        If there is capacity to spare, append the item to the tail
        '''
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        '''
        if at capacity, overwrite over the oldest item with the new item
        '''
        if self.storage.length == self.capacity:
            self.current.value = item
            '''
            Set the most recently added to the head since it was the most recently used 
            '''
            if self.current is self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

       
        '''
        iterate through each node and append the value to the buffer list
        '''
        pointer = self.storage.head
        while pointer:
            list_buffer_contents.append(pointer.value)
            pointer = pointer.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
