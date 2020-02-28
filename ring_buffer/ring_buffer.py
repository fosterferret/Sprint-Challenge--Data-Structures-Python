from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            self.current.value = item
            self.current = self.current.next if self.current.next else self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        curr_node = self.storage.head
        while curr_node:
            list_buffer_contents.append(curr_node.value)
            curr_node = curr_node.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.current = 0

    def append(self, item):
        self.storage[self.current] = item
        self.current += 1
        if self.current > len(self.storage) - 1:
            self.current = 0

    def get(self):
        return list(filter(None, self.storage))


# With arrays, accessing elements occurs in constant time while you get linear time for linked lists. However, deletion and insertion operations are not as efficient in arrays since they involve a lot of migrations.
