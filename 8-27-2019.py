"""
Author: Zach Stoebner
Created on: 8-27-2019
Descrip:

Given two strings A and B, return whether
or not A can be shifted some number of
times to get B.

For example, if A is abcde and B is cdeab,
return true. If A is abc and B is acb,
return false.

"""

#shift
#Note: single rightshift on string param
#Complexity: O(3n) time + O(2n) space
def shift(s):
    length = len(s)

    str_list = list([])
    for letter in s:
         str_list.append(letter)

    holder = None
    for i in reversed(range(length)):

        if i == length-1:
            holder = str_list[i]
            str_list[i] = str_list[i-1]
        elif i == 0:
            str_list[i] = holder
        else:
            str_list[i] = str_list[i-1]

    new_str = ""
    for letter in str_list:
        new_str += letter

    return new_str

### SHIFT TESTS
s = "abcde"
n_str = shift(s)
print(n_str) #eabcd

#shiftable
#Note: returns bool of whether two strings
# can be shifted some number of times to get the other
#Complexity: O(n + n^2) time + O(n) space
def shiftable(s1,s2):

    if len(s1) == len(s2): #n

        start = s1
        for _ in s1: #n times
            start = shift(start) #O(n)
            if start == s2:
                return True
        return False
    return False

### TESTS
s1 = "abcde"
s2 = "cdeab"
print(shiftable(s1,s2)) #True
s1 = "abc"
s2 = "acb"
print(shiftable(s1,s2)) #False
s2 = "ac"
print(shiftable(s1,s2)) #False

#know that starting point could be the same
# and if same sequence from starting point, then True, else False

#better_shiftable
#Note: implements shiftable in O(n) time
#Complexity: O(n) time + O(1) space
def better_shiftable(s1,s2):

    length1 = len(s1) #n
    length2 = len(s2) #n

    #prelim condition
    if (length1 == length2):
        start = s1[0]

        #finding start point
        for i in range(length2): #O(n)

            if s2[i] == start:

                #comparing sequences
                s2_ind = i
                matching = 1
                for s1_ind in range(1,length1):

                    #wrapping around
                    s2_ind = (s2_ind + 1) % length2

                    #counting
                    if s1[s1_ind] == s2[s2_ind]:
                        matching += 1

                #if all match, return True
                if matching == length1:
                    return True

    #if no matching shift, return False
    return False

### TESTS
s1 = "abcde"
s2 = "cdeab"
print(better_shiftable(s1,s2)) #True
s1 = "abc"
s2 = "acb"
print(better_shiftable(s1,s2)) #False
s2 = "ac"
print(better_shiftable(s1,s2)) #False
s1 = "eaaaa"
s2 = "aaaae"
print(better_shiftable(s1,s2)) #True
