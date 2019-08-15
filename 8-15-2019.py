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
#permute
#Note: finds all permutations of a given num
def permute(number,pivot=0,perms=[]):


    #helper function to swap
    def swap(number,i1,i2):
        number[i1],number[i2] = number[i2],number[i1]

    length = len(number)
    if pivot == length:
        perms.append(number)
        return perms
    else:
        for i in range(pivot,length):

            swap(number,i,pivot)

            perms = permute(number,pivot+1,perms)

            swap(number,i,pivot)

    return perms

#Having tried a few ways that I can think of and then even trying a proven algo,
#the permutations don't compute quickly.
print(permute([1,2,3]))
