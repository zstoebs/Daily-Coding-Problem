"""
@author Zach Stoebner
@date 10-30-2019
@descrip Given a string s and a list of words words,
where each word is the same length, find all starting indices of
substrings in s that is a concatenation of every word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"],
return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since
there are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.
"""
import itertools

#sub_inds
#Returns a list of indices where a substring of all words consecutively from a list of word appear in a given string
#Complexity: O(n^2) where n is the number of words
def sub_inds(s="",words=list()):

    perms = list(itertools.permutations(words))

    inds = list()
    for perm in perms:
        ind = s.find(perm)
        if ind != -1:
            inds.append(ind)

    return inds

### TESTS
s = "dogcatcatcodecatdog"
words = ["cat", "dog"]
print(sub_inds(s,words))
s = "barfoobazbitbyte"
words = ["dog", "cat"]
print(sub_inds(s,words))
