"""
Author: Zach Stoebner
Created on: 8-14-2019
Descrip:

Given a number represented by a list of digits,
find the next greater permutation of a number,
 in terms of lexicographic ordering. If there
 is not greater permutation possible, return
 the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return
[1,3,2]. The list [1,3,2] should return [2,1,3].
 The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating
 extra memory (disregarding the input memory)?

"""

#goal is to perform permutation in place
#know that sorted list is smallest permutation,
#therefore, reversed sorted list is greatest permutation
#need two nested functions to piggy back recursive calls off each other
def next_greatest_perm(number):

    ### AS START INDEX GETS SMALLER,
    ### NUMBER WILL CONVERGE TO NEXT GREATEST PERMUTATION OF INITIAL NUMBER
    def backward_swap(number,start_ind):

        for i in reversed(range(start_ind)):
            for nxt_i in reversed(range(i)):
                #if last number is greater than next digit,
                #swapping will increase to next permutation
                if number[i] > number[nxt_i]:
                    #swap in place
                    number[i],number[nxt_i] = number[nxt_i],number[i]
                    #go back down number to move to next lowest permutation
                    return forward_swap(number,nxt_i)
        return sorted(number)


    def forward_swap(number,start_ind):

        for i in range(start_ind+1,len(number)):
            for nxt_i in range(i+1,len(number)):
                #if last number is greater than next digit,
                #swapping will increase to next permutation
                if number[i] > number[nxt_i]:
                    #swap in place
                    number[i],number[nxt_i] = number[nxt_i],number[i]
                    #go back down number to move to next greatest permutation
                    return forward_swap(number,nxt_i)
        return number


    return backward_swap(number,len(number))


### TESTS
print(next_greatest_perm([1,2,3])) #[1,3,2]
print(next_greatest_perm([1,3,2])) #[2,1,3]
print(next_greatest_perm([3,2,1])) #[1,2,3]
print(next_greatest_perm([1,2])) #[2,1]
print(next_greatest_perm([1,0,0,4])) #[1,0,4,0]
