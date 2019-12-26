"""
@author Zach Stoebner
@date 12-23-2019
@descrip You come across a dictionary of sorted words in a language you've never seen before.
Write a program that returns the correct order of letters in this language.

For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return ['x', 'z', 'w', 'y'].
"""

"""
This problem seems ill-formed. What happens when one word is really long with letters that
don't appear in any other word after some index, or if each word has a separate set of letters unseen
elsewhere? The wording of the problem assumes a lot about the dictionary, particularly that it is complete.
If there are letters that are unorderable, then I could partition them into a separate set
and return that as well.
"""

# alpha_order
# Given a dictionary of words, returns the constituent letters in sorted order
# Complexity: O()
def alpha_order(dc=dict()):

    # initializing the data structures
    letter_order = []
    letter_words = dict()
    letters = set()
    for word in dc:
        let = word[0]
        if let not in letter_order:
            letter_order.append(let)
        letters.add(let)
        if let in letter_words.keys():
            letter_words[let].append(word[1:])
        else:
            try:
                letter_words[let] = [word[1:]]
            except IndexError:
                pass

    # finding the ordering
    remove = []
    for letter in letter_words.keys():
        # remove all letters that only have one word
        if len(letter_words[letter]) == 1:
            letters.discard(letter)

            # grabbing any letters that were extra
            for let in letter_words[letter][0]:
                if let != '':
                    letters.add(let)
            remove.append(letter)
    for letter in remove:
        del letter_words[letter]

    # process the batch of words index by index
    for letter in letter_words.keys():
        words = letter_words[letter]
        while len(words) > 0:
            order = ""
            i = 0
            for word in words:
                order += word[0]
                words[i] = word[1:]
                i += 1
            for _ in range(words.count("")):
                words.remove("")

            # emplace ordering into letter_order list
            length = len(order)
            i = 0
            place_letter = ''
            letters.add(c for c in order)
            for c in order:
                if c in letter_order:
                    place_letter = c
                    break
                i += 1
            if place_letter != '':
                for c in order[:i]:
                    if c not in letter_order:
                        ind = letter_order.index(place_letter)
                        letter_order.insert(ind,c)
    return letter_order

### TESTS
print(alpha_order(['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'])) #['x', 'z', 'w', 'y']

### ADMIN SOLUTION
# They solve the language with a topological sort. It doesn't handle the criteria mentioned above.
def create_graph(words):
    letters = set(''.join(words))
    graph = {letter: [] for letter in letters}

    for pair in zip(words, words[1:]):
        for before, after in zip(*pair):
            if before != after:
                graph[before].append(after)
                break

    return graph

from collections import deque

def visit(letter, graph, visited, order):
    visited.add(letter)

    for next_letter in graph[letter]:
        if next_letter not in visited:
            visit(next_letter, graph, visited, order)

    order.appendleft(letter)

def toposort(graph):
    visited = set()
    order = deque([])

    for letter in graph:
        if letter not in visited:
            visit(letter, graph, visited, order)

    return list(order)

def alien_letter_order(words):
    graph = create_graph(words)
    return toposort(graph)

### TEST
t1 = ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']
t2 = ['xww', 'wxyz', 'wxyw', 'ywxqrt', 'yawz']
print(alien_letter_order(t1)) # ['x', 'z', 'w', 'y']
print(alien_letter_order(t2)) # ['z', 'q', 'r', 'x', 'w', 'a', 'y', 't'] <-- doesn't handle incomparable letters
