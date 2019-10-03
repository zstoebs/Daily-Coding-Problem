"""
@author   Zach Stoebner
@date     9-29-2019
@descrip  Implement 3 stacks using a single list:

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass
"""

class Stack:
    def __init__(self):
        self.list = []
        self.tops = [None,None,None]
        self.lengths = [0,0,0]

    def pop(self, stack_number):
        stack = stack_number - 1
        assert stack >= 0 and stack <= 2

        if self.isEmpty(stack):
            raise BufferError("Underflow exception: stack is empty")

        start = self.tops[stack]
        end = self.lengths[stack]
        last = start + last - 1
        self.list.pop(last)

        self.lengths[stack] -= 1
        if self.lengths[stack] == 0:
            self.tops[stack] = None

    def push(self, item, stack_number):
        stack = stack_number-1
        assert stack >= 0 and stack <= 2
        if self.tops[stack] is None:
            length = len(self.list)
            self.list.append(item)
            self.tops[stack] = length
            self.lengths[stack] += 1
        else:
            start = self.tops[stack]
            end  = self.lengths[stack]
            index = start + end
            self.list.insert(index,item)
            self.lengths[stack] += 1

    def isEmpty(self,stack):
        return self.lengths[stack] == 0

    def printStk(self,stack_number):
            stack = stack_number-1
            assert stack >= 0 and stack <= 2

            if self.isEmpty(stack):
                print("None")
                return

            start = self.tops[stack]
            end = self.lengths[stack]
            stk = ""
            for i in range(start,end):
                stk += str(self.list[i])

            print(stk)


    def __str__(self):
        return str(self.list)

### TESTS
stk = Stack()
print(stk)
stk.push(1,2)
print(stk)
stk.printStk(1)
stk.printStk(2)
