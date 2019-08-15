"""
Author: Zach Stoebner
Created on: 8-15-2019
Descrip:

Given a number in the form of a list of digits,
return all possible permutations.

For example, given [1,2,3], return [[1,2,3],
[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].

"""
"""
Heap's Algorithm:

procedure generate(k : integer, A : array of any):
    if k = 1 then
        output(A)
    else
        // Generate permutations with kth unaltered
        // Initially k == length(A)
        generate(k - 1, A)

        // Generate permutations for kth swapped with each k-1 initial
        for i := 0; i < k-1; i += 1 do
            // Swap choice dependent on parity of k (even or odd)
            if k is even then
                swap(A[i], A[k-1]) // zero-indexed, the kth is at k-1
            else
                swap(A[0], A[k-1])
            end if
            generate(k - 1, A)

        end for
    end if
"""
#permute1
#Note: finds all permutations of a given num
def permute1(number,pivot=0,perms=[]):

    #helper function to swap
    def swap(number,i1,i2):
        number[i1],number[i2] = number[i2],number[i1]

    length = len(number)
    if pivot == length:
        perms.append(list(number))
        return perms
    else:
        for i in range(pivot,length):

            swap(number,i,pivot)

            perms = permute1(number,pivot+1,perms)

            swap(number,i,pivot)

    return perms

def permute2(number,pivot=0,perms=[]):
    #helper function to swap
    def swap(number,i1,i2):
        number[i1],number[i2] = number[i2],number[i1]

    length = len(number)
    i = pivot
    while i < length:
        swap(number,i,pivot)
        perms = permute2(number,pivot+1,perms)
        swap(number,i,pivot)
        i += 1
    return perms

#Heap's Algorithm
def Heap(number,k=None,perms=[]):

    if k is None:
        k = len(number)

    #helper function to swap
    def swap(number,i1,i2):
        number[i1],number[i2] = number[i2],number[i1]

    if k == 1:
        if perms.count(list(number)) == 0:
            perms.append(list(number))
        return perms
    else:
        perms = Heap(number,k-1,perms)

        for i in range(k):

            if k % 2 == 0:
                swap(number,i,k-1)
            else:
                swap(number,0,k-1)

            perms = Heap(number,k-1,perms)
    return perms

#these work now
print(Heap([1,2,3]))
print(permute1([1,2,3]))

#this one doesn't work
print(permute2([1,2,3]))
