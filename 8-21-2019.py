"""
Author: Zach Stoebner
Created on: 8-21-2019
Descrip:

Given a list of integers and a number K,
return which contiguous elements of the
list sum to K.

For example, if the list is [1, 2, 3, 4, 5]
and K is 9, then it should return [2, 3, 4],
since 2 + 3 + 4 = 9.

"""

#contiguous = sharing a border --> so ints must be adjacent
#can start at the beginning and then move rightward
#uncertain if the list is sorted beforehand

#contig_sum
#Note: returns list of contiguous integers from list that equal k
#Complexity: O(n^2)
def contig_sum(ints,k):

    length = len(ints)

    #visit each number consecutively as starting point
    for i in range(length):

        visited = [ints[i]]
        nxt_i = i+1
        sum = ints[i]

        #add to running and check if equal
        while nxt_i < length and sum + ints[nxt_i] <= k:
            sum += ints[nxt_i]
            visited.append(ints[nxt_i])
            nxt_i += 1

        #if while loop exited because sum = k, return
        if sum == k:
            return visited

    #return null if no contig sum = k
    return None

### TESTS
ints = [1, 2, 3, 4, 5]
print(contig_sum(ints,9)) #[2,3,4]
ints = [10,3,114,8,7,6,7]
print(contig_sum(ints,20)) #[7,6,7]
print(contig_sum(ints,115)) #None
ints = []
print(contig_sum(ints,10)) #None
