"""
Author: Zach Stoebner
Created on: 8-11-2019
Descrip:

We're given a hashmap associating each
courseId key with a list of courseIds values,
which represents that the prerequisites of
courseId are courseIds. Return a sorted
ordering of courses such that we can finish
all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'],
 'CSC200': ['CSC100'], 'CSC100': []}, should
 return ['CSC100', 'CSC200', 'CSCS300'].

"""

#know that this RST poset is a Hasse diagram
#valid ordering is a poset, otherwise invalid
#can encode a Hasse diagram as a tree
def courseOrder(courseIds=dict()):

    #finding Hasse base and placing upper nodes in list of unvisited
    keys_left = []
    hasse = Hasse()
    for k,v in courseIds.items():

        #preprocessing Hasse base into Hasse diagram,
        #no need to include in unvisited keys list
        if len(v) == 0:
            hasse.root.add(k)
        else:
            keys_left.append(k)

    #if no fundamental course in given dict, invalid poset
    if len(keys_left) == len(courseIds):
        return None

    #filling in Hasse diagram
    state = True
    while (state == True and len(keys_left) != 0):
        state = False
        to_remove = []
        for key in keys_left:
            for prereq in courseIds[key]:
                if hasse.place(key,prereq):
                    to_remove.append(key)
                    state = True
        for key in to_remove:
            keys_left.remove(key)

    #if all courseIds don't fit into a Hasse diagram, not a poset so invalid
    if len(keys_left) != 0:
        return None
    else:
        rev_order = hasse.sorted_ordering()
        rev_order.reverse()
        return rev_order

class Node(object):

    #constructor
    #Note: including arg vector assumed to be children
    def __init__(self,data,*argv):
        self.data = data #assuming string type for this problem
        self.children = [] #list for tuples of children
        for arg in argv:
            self.children.append(Node(arg))

    #add
    #Note: pairs key and a node with key as data
    def add(self,key):
        self.children.append(Node(key))

class Hasse(object):

    #constructor
    #Note: contains root to point to least nodes
    def __init__(self):
        self.root = Node('root')

    #place
    #Note: recursively places children in appropriate node directory
    def place(self,key,prior,cur_node=None):

        #setting cur to root if initial recursive iteration
        if cur_node == None:
            cur_node = self.root

        if cur_node.data == prior:
            cur_node.add(key)
            return True
        elif len(cur_node.children) == 0:
            return False
        else:
            for child in cur_node.children:
                if self.place(key,prior,child):
                    return True
            return False

    #sorted_ordering
    #Note: returns a descending sorted ordering from greatest element to least
    def sorted_ordering(self,cur_node=None):

        #setting cur to root if initial recursive iteration
        if cur_node == None:
            cur_node = self.root

        #traverses to greatest element and ends with least
        if len(cur_node.children) == 0:
            return [cur_node.data]
        else:
            order = list()
            for child in cur_node.children:
                order.extend(self.sorted_ordering(child))
            if (cur_node.data != self.root.data):
                order.append(cur_node.data)
            return order

##TESTS

#given valid ordering
test1 = {'CSC300': ['CSC100', 'CSC200'],
 'CSC200': ['CSC100'], 'CSC100': []}
print(courseOrder(test1))
#['CSC100', 'CSC200', 'CSC300']

#invalid ordering, no fundamental course
test2 = {'CSC300': ['CSC100', 'CSC200'],
 'CSC200': ['CSC100']}
print(courseOrder(test2))
#None

#valid
test3 = {7:[5,6,4,3,2,1],5:[4,3,2,1],
6:[4,3,2,1],4:[2,3,1],2:[1],3:[1],1:[]}
print(courseOrder(test3))
#[1, 3, 2, 4, 6, 5, 7]

#valid
#this test doesn't work and I don't know why
test4 = {7:[5,6,4,3,2,1,0],5:[4,3,2,1,0],
6:[4,3,2,1,0],4:[2,3,1,0],2:[1,0],3:[1],1:[],0:[]}
print(courseOrder(test4))
"""
['CSC100', 'CSC200', 'CSC300']
None
[1, 3, 2, 4, 6, 5, 7]
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-1-d609e77cd60b> in <module>
    145 test4 = {7:[5,6,4,3,2,1,0],5:[4,3,2,1,0],
    146 6:[4,3,2,1,0],4:[2,3,1,0],2:[1,0],3:[1],1:[],0:[]}
--> 147 print(courseOrder(test4))

<ipython-input-1-d609e77cd60b> in courseOrder(courseIds)
     51                     state = True
     52         for key in to_remove:
---> 53             keys_left.remove(key)
     54
     55     #if all courseIds don't fit into a Hasse diagram, not a poset so invalid

ValueError: list.remove(x): x not in list
"""

###ADMIN SOLUTION
def courses_to_take(course_to_prereqs):
    # Copy list values into a set for faster removal.
    course_to_prereqs = {c: set(p) for c, p in course_to_prereqs.items()}

    todo = [c for c, p in course_to_prereqs.items() if not p]

    # Used to find courses D which have C as a prerequiste
    prereq_to_coures = {}
    for course in course_to_prereqs:
        for prereq in course_to_prereqs[course]:
            if prereq not in prereq_to_coures:
                prereq_to_coures[prereq] = []

            prereq_to_coures[prereq].append(course)

    result = [] # courses we need to take in order

    while todo:
        prereq = todo.pop()
        result.append(prereq)

        # Find which courses are now free to take

        for c in prereq_to_coures.get(prereq, []):
            course_to_prereqs[c].remove(prereq)
            if not course_to_prereqs[c]:
                todo.append(c)

    # Cicrcular dependency
    if len(result) < len(course_to_prereqs):
        return None
    return result
