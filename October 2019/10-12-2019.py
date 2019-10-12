"""
@author Zach Stoebner
@date 10-12-2019
@descrip Implement a stack API using only a heap.
A stack implements the following methods:

push(item), which adds an element to the stack
pop(), which removes and returns the most recently
added element (or throws an error if there is nothing on the stack)
Recall that a heap has the following operations:

push(item), which adds a new key to the heap
pop(), which removes and returns the max value of the heap
"""

import heapq

class stack_heap:

    def __init__(self):
        self.heap = list()
        self.recent = None

    def push(self,item):
        heapq.heappush(self.heap)
        self.recent = item

    def pop(self):
        if len(self.heap) == 0:
            raise Exception("Underflow error: heap is empty")
        self.heap.remove(self.recent)
