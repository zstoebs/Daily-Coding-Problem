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

### ADMIN SOLUTION
def min_distance(text, word0, word1):
    text_words = [w.strip() for w in text.split(' ')]
    print text_words

    word0_indices = [i for i, w in enumerate(text_words) if w == word0]
    word1_indices = [i for i, w in enumerate(text_words) if w == word1]

    if not word0_indices or not word1_indices: # one of the words doesn't exist.
        return float('inf')

    i = j = 0

    min_distance = abs(word0_indices[i] - word1_indices[j])

    while i < len(word0_indices) and j < len(word1_indices):

        current_distance = abs(word0_indices[i] - word1_indices[j])
        min_distance = min(min_distance, current_distance)

        if word0_indices[i] < word1_indices[j]:
            i += 1
        else:
            j += 1
    return min_distance - 1 # Don't count the last step to get to word1
