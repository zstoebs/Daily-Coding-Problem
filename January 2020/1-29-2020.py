"""
@author Zach Stoebner
@date 1-29-2020
@details Create a basic sentence checker that takes in a stream of characters and determines
whether they form valid sentences. If a sentence is valid, the program should print it out.

We can consider a sentence valid if it conforms to the following rules:

1. The sentence must start with a capital letter, followed by a lowercase letter or a space.
2. All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
3. There must be a single space between each word.
4. The sentence must end with a terminal mark immediately following a word.
"""

# sentence_check
# Checks if a sentence is valid
# Complexity: O(n)
def sentence_check(sent: str):

    seps = [",", ";", ":"]
    terms = [".", "?", "!", "‽"]

    spaced = sent.split(" ") #O(n)
    first = spaced[0]
    print(spaced)

    # checking 1 --> O(n)
    if not (first[0] >= "A" and first[0] <= "Z" and (len(first) == 1 or (first[1] >= "a" and first[1] <= "z"))):
        return 1, False

    #O(n)
    for ind, word in enumerate(spaced):

        # checking 3
        if word == "":
            return 2, False

        if ind == 0:
            word = word[1:]

        for i, let in enumerate(word):

            # # making sure that separators or a terminals are at the end of words
            # if (let in seps or let in terms) and i != n-1:
            #     return False

            # checking 2
            if not ((let >= "a" and let <= "z") or let in seps or let in terms):
                return 3, False

        # checking 4
        if ind == len(spaced)-1 and not word[-1] in terms:
            return 4, False

    return sent

### TESTS
print(sentence_check("This is a sentence.")) # True
print(sentence_check("This  is not a sentence.")) # False
print(sentence_check("Th:is is a sentence.")) # True
print(sentence_check("This is a not sentence. ")) # False
print(sentence_check("This is a not 1sentence.")) # False
