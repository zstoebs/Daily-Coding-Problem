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
    mx = count
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
                mx = max(count,mx)

            #if not consecutive, reset
            else:
                count = 1
            prev = int
    return mx

### TESTS
ints = [100, 4, 200, 1, 3, 2]
print(easy_solution(ints)) #4
ints = [1,2,3,4,100,101,102,103,104,105,106,107]
print(easy_solution(ints)) #8

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

#longest_sequence
#Note: returns length of longest consecutive sequence of elements
#Complexity: O(nlogn) time + O(n) space
### DOESN'T WORK BECAUSE ARRAY ISN'T SORTED FOR BIN SEARCH
def longest_sequence(ints):

    length = len(ints)

    #helper
    #Note: returns count of largest sequence
    def helper(ind,count=1):

        #getting next index
        next_ind = binary_search(ints,ints[ind]+1,0,length-1)
        print(next_ind)

        #if end of sequence, return
        if next_ind is None:
            return count
        #else increment and continue
        else:
            count += 1
            return helper(next_ind,count)


    count = 0
    for i in range(length):
        count = max(count,helper(i))
    return count

### TESTS
ints = [100, 4, 200, 1, 3, 2]
print()
print(longest_sequence(ints)) #1, should be 4

#hash_sequence
#Note: hashes values, and returns max count
#Complexity: O(n) time + O(n) space
# https://www.geeksforgeeks.org/longest-consecutive-subsequence/
def hash_sequence(ints):

    #python sets use hashes for constant time lookup
    hashes = set(ints)
    count = 0

    for int in ints:

        cur = int+1
        while cur in hashes:
            cur += 1

        count = max(count,cur-int)

    return count

ints = [ 4, 1, 3, 2,100,200]
print()
print(hash_sequence(ints))

#my_hash_solution
#Note: finds longest consecutive sequence via hashing by hand for my own education
#Complexity: O(9n/2) time + O(n) space --> O(n) total
def my_hash_solution(ints):

    hash_set = [None for _ in ints] #O(n)
    set_size = len(hash_set) #O(n)

    def my_hash_func(key,emplace=False,return_hash=False):

        hashed = False
        step = 0
        while not hashed:
            hash = (key//(step+1) + step) % set_size
            if emplace and hash_set[hash] is None:
                hash_set[hash] = key
                hashed = True
            if return_hash and hash_set[hash] == key:
                return hash
            if step > (set_size**2+1): #need a threshold to prevent infinite loop
                return False
            else:
                step += 1

    #mapping to hashes
    print("Hashing...")
    for int in ints: #O(n)
        my_hash_func(int,emplace=True)

    #counting longest sequence
    print("Finding longest sequence...")
    count = 0
    for int in ints: #O(n) + O(n/2) for avg case of while loop

        cur = int+1
        hash = my_hash_func(cur,return_hash=True)
        while hash_set[hash] == cur:
            cur += 1
            hash = my_hash_func(cur,return_hash=True)

        count = max(count,cur-int)

    return count

### TESTS
ints = [ 4, 1, 3, 2,100,200]
print()
print(my_hash_solution(ints))

### ADMIN SOLUTION
def longest_consecutive(self, nums):
    max_len = 0
    bounds = dict()
    for num in nums:
        if num in bounds:
            continue
        left_bound, right_bound = num, num
        if num - 1 in bounds:
            left_bound = bounds[num - 1][0]
        if num + 1 in bounds:
            right_bound = bounds[num + 1][1]
        bounds[num] = left_bound, right_bound
        bounds[left_bound] = left_bound, right_bound
        bounds[right_bound] = left_bound, right_bound
        max_len = max(right_bound - left_bound + 1, max_len)

    return max_len
    
