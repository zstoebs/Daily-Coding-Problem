"""
@author Zach Stoebner
@date 9-14-2019
@descrip Write a function that rotates a list by k elements.
          For example, [1, 2, 3, 4, 5, 6] rotated by two becomes
          [3, 4, 5, 6, 1, 2]. Try solving this without creating
          a copy of the list. How many swap or move operations
          do you need?
"""
#this can easily be implemented by a queue in O(n), assuming list append in python is in Theta(1)
#this requires n move ops

#rotate_copy
#Note: rotates a list counter clockwise by k elements, but creates a copy of the list
#Complexity: O(n)
def rotate_copy(ll,k):

    length = len(ll)
    q = list([])

    for i in range(k,length):
        q.append(ll[i])

    for i in range(k):
        q.append(ll[i])

    return q

ll = [1, 2, 3, 4, 5, 6]
print(rotate_copy(ll,2)) #[3, 4, 5, 6, 1, 2]

############################################
#can implement without creating a copy by appending then popping the first k values
#only requires k move ops

#rotate_nocopy
#Note: rotates a list in place counter clockwise by k elements
#Complexity: O(k)
def rotate_nocopy(ll,k):

    for i in range(k):
        ll.append(ll[i])
        ll.pop(i)

    return ll
ll = [1, 2, 3, 4, 5, 6]
print(rotate_copy(ll,2)) #[3, 4, 5, 6, 1, 2]
