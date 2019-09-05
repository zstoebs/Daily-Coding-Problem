"""
  @author Zach Stoebner
  @date 9-4-2019
  @details Generate a finite, but an arbitrarily large binary
		   tree quickly in O(1).

           That is, generate() should return a tree whose
           size is unbounded but finite.

"""

#Reference: https://stackoverflow.com/questions/49502112/construct-binary-tree-in-o1
#this question in ambiguous so not sure if the implementation in the thread is sufficient
#although, it makes sense and I assume it is so I'll implement it

class Node(object):

    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__ (self,node=None,cur_str=""):

        string = cur_str
        if node == None:
            string += str(self.data)
            left = self.left
            right = self.right
        else:
            string += str(node.data)
            left = node.left
            right = node.right

        if left == None and right == None:
            return string

        if left != None:
            string += self.__str__(left)

        string += "|"
        if right != None:
            string += self.__str__(right)

        return string


### RNG BORROWED FROM 8-9-2019.PY
#coin_flip
#Returns a binary value with a 50/50 chance for each
#Complexity:
def coin_flip(seed=42):

    global prev
    global a
    global b
    prev = seed
    a = 0b11000111
    b = 0b10101101

    while True:
        x = ((a * prev + b) / (a-b)) % 2
        prev = x
        yield int(x)

###  coin_flip tests
for _,rnd in zip(range(10),coin_flip()):
    print(rnd)

print()

def generate():

    global data
    data = 0

    data += 1
    if next(coin_flip()) == 1:
        return Node(data)

    if next(coin_flip()) == 0 and next(coin_flip()) == 0:
        return Node(data,left=generate(),right=None)
    elif next(coin_flip()) == 1 and next(coin_flip()) == 1:
        return Node(data,lef=None,right=generate())
    else:
        return Node(data)

### TESTS
tree = generate() #hits max recursion depth here 
print(tree)
print()
tree = generate()
print(tree)
print()
tree = generate()
print(tree)
