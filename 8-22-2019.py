"""
Author: Zach Stoebner
Created on: 8-22-2019
Descrip:

Given a string and a set of characters,
return the shortest substring containing
all the characters in the set.

For example, given the string "figehaeci"
and the set of characters {a, e, i}, you
should return "aeci".

If there is no substring containing all
the characters in the set, return null.

"""

#substr_chars
#Note: returns shortest substring containing all chars in passed set
#Complexity: O(n^2) time + O(n) space
def substr_chars(string,char_set):

    length = len(string)
    cur_sub = None

    #finding a starting point
    for i in range(length): #n
        if string[i] in char_set:
            to_visit = char_set.copy()
            sub = str(string[i])
            to_visit.remove(string[i])

            #starting point found so continue till end of string
            j = i + 1
            while j < length: #n
                sub += string[j]

                if string[j] in to_visit:
                    to_visit.remove(string[j])

                #if shortest, make cur candidate
                if len(to_visit) == 0:
                    if cur_sub is None or len(sub) < len(cur_sub):
                        cur_sub = sub

                j += 1

    return cur_sub

string = "figehaeci"
chars = set(['a','e','i'])
print(substr_chars(string,chars)) #aeci
chars = set(['a','e','z'])
print(substr_chars(string,chars)) #None
chars.remove('z')
print(substr_chars(string, chars)) #ae
