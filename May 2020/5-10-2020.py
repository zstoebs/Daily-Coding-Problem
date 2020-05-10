"""
@author Zach Stoebner
@date 5-10-2020
@details A quack is a data structure combining properties of both stacks and queues.
It can be viewed as a list of elements written left to right such that three operations are
possible:

push(x): add a new item x to the left end of the list
pop(): remove and return the item on the left end of the list
pull(): remove the item on the right end of the list.
Implement a quack using three stacks and O(1) additional memory, so that the amortized time
for any push, pop, or pull operation is O(1).
"""

# https://codereview.stackexchange.com/questions/85598/quack-the-revolutionary-new-data-structure

class quack:

    def __init__(self):

        # 3 stacks
        self.left = []
        self.right = []
        self.middle = []
        self.size = 0

    def push(self, x):
        self.left += [x]
        self.middle += [x]
        self.size += 1

    def pop(self):
        # all items pulled prior to this call
        if self.size == 0:
            raise BufferError("Underflow: No elements. Can't pop.")

         # in case a pull occurs and pops all elements from middle to right just before a pop
        if len(self.middle) > 0:
            self.middle.pop()

        self.size -= 1
        return self.left.pop()

    def pull(self):
        # all items popped prior to this call
        if self.size == 0:
            raise BufferError("Underflow: No elements. Can't pull.")

        if len(self.right) == 0:
            while len(self.middle) > 0:
                self.right += [self.middle.pop()]

        self.size -= 1
        return self.right.pop()

### TESTS
q = quack()
for num in range(100):
    q.push(num)
print(q.left)
for num in range(10):
    print(q.pop())
for num in range(91):
    print(q.pull())
