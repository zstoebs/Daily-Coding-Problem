"""
Author: Zach Stoebner
Created on: 8-18-2019
Descrip:

Given an unsorted array of integers,
find the length of the longest consecutive
elements sequence.

For example, given [100, 4, 200, 1, 3, 2],
the longest consecutive element sequence
is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

"""
#I'm assumung O(n) means O(n) runtime and O(n) space
#O(n) space means solving in place, max linear number of new data structures of equal length
#O(n) time means no sort and linear traversal
#can binary search through the array for consecutive ints, runs in log(n)
#could hash each entry into a table or use modulo ops???

#easy_solution
#Note: returns length of longest consecutive sequence
#Complexity: O(nlogn) time + O(1) space
def easy_solution(ints):
    length = len(ints)

    count = 0
    max = count
    prev = None
    for int in sorted(ints): #sort is O(nlogn) time

        #if first int, set
        if prev is None:
            prev = int
            count += 1
        else:
            # if consecutive, increment
            if int == prev+1:
                count += 1

                #if new max, set
                if count > max:
                    max = count
            #if not consecutive, reset
            else:
                count = 1
            prev = int
    return max

### TESTS
ints = [100, 4, 200, 1, 3, 2]
print(easy_solution(ints)) #4
ints = [1,2,3,4,100,101,102,103,104,105,106,107]
print(easy_solution(ints)) #8

#longest_sequence
#Note: returns length of longest consecutive sequence of elements
#Complexity: O(nlogn) time + O(n) space
def longest_sequence(ints):

    length = len(ints)

    #helper
    #Note: returns count of largest sequence
    def helper(arr,ind,count=1):

        #getting next index
        next_ind = binary_search(arr,arr[ind]+1,0,length-1)

        #if end of sequence, return
        if next_ind is None:
            return count
        #else increment and continue
        else:
            count +=1
            return helper(arr,next_ind,count)


    counts = []
    for i in range(length):
        counts.append(helper(ints,i))
    return max(counts)

### TESTS
ints = [100, 4, 200, 1, 3, 2]
print()
print(longest_sequence(ints)) #1, should be 4

#binary_search
#Note: returns index
#Complexity: O(logn) time + O(1) space
def binary_search(arr,target,low,high):

    if low <= high:

        mid = (low + high) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            return binary_search(arr,target,mid+1,high)
        else:
            return binary_search(arr,target,low,mid-1)
    else:
        return None

#testing binary_search
ints = [0,1,2,3,4,5,6]
print()
print(binary_search(ints,5,0,len(ints)-1)) #5
print(binary_search(ints,1,0,len(ints)-1)) #1
print(binary_search(ints,7,0,len(ints)-1)) #None
print(binary_search(ints,4,0,len(ints)-1)) #4
print(binary_search(ints,0,0,len(ints)-1)) #0
print(binary_search(ints,8,0,len(ints)-1)) #None
print(binary_search(ints,6,0,len(ints)-1)) #6
#bin search passes tests
