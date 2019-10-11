"""
@author Zach Stoebner
@date 10-11-2019
@descrip Find an efficient algorithm to find the
smallest distance (measured in number of words)
between any two given words in a string.

For example, given words "hello", and "world" and
a text content of "dog cat hello cat dog dog hello cat world",
return 1 because there's only one word "cat" in between the two words.
"""

#word_distance
#Returns the distance in words b/w two given words in a sentence
#Complexity: O(n) time
def word_distance(phrase,word1,word2):

    part = phrase.split()

    dist = 0
    pivot = None
    for word in part:
        if pivot == None:
            if word == word1 or word == word2:
                pivot = word
        elif word == word1 or word == word2:
            if word == pivot:
                dist = 0
            else:
                return dist
        else:
            dist += 1
    return None

### TESTS
phrase = "dog cat hello cat dog dog hello cat world"
word1 = "hello"
word2 = "world"
print(word_distance(phrase,word1,word2)) #1
