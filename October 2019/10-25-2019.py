"""
@author Zach Stoebner
@date 10-25-2019
@descrip Given a list of words, find all pairs of unique indices such that
the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"],
return [(0, 1), (1, 0), (2, 3)].
"""
# I can think of how to solve this in O(n^2) time
# A faster way to solve this may be storing the reverse of each to find pairs and otherwise checking sequentially if a pair is a palindrome

#palindromes
#Returns a list of indices s.t. the concatenation of the words at those indices is a palindrome
#Complexity: O(n^2)
def palindromes(words=list()):

    #is_palindrome
    #Helper fnc that returns bool --> checks if passed word is a palindrome
    #Complexity: O(n)
    def is_palindrome(word=""):

        i = 0
        j = len(word) - 1
        while i <= j:
            if word[i] != word[j]:
                return False

            i += 1
            j -= 1

        return True

    indices = list()
    i = 0
    length = len(words)
    while i < length:

        j = 0
        while j < length:
            potential = words[i] + words[j]

            if j != i and is_palindrome(potential):
                indices.append(tuple([i,j]))
            j += 1

        i += 1
    return indices

### TESTS
t1 = ["code", "edoc", "da", "d"]
print(palindromes(t1)) # [(0, 1), (1, 0), (2, 3)]
