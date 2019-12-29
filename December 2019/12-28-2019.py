"""
@author Zach Stoebner
@date 12-28-2019
@descrip Given a string with repeated characters, rearrange the string so that no two
adjacent characters are the same. If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return None.
"""

# no_repeats
# Returns a rearranged string with no repeated letters
# Complexity: O(n) <-- on average, may be higher in worst case
def no_repeats(input=""):

    string = [c for c in input]

    place = None
    prev = None
    ind = 0
    n = len(string)
    while ind < n:
        cur = string[ind]
        if cur == prev:
            i = ind
            while i < n and string[i] == cur:
                i += 1
            if i == n:
                return None
            else:
                string[i], string[ind] = string[ind], string[i]
        prev = string[ind]
        ind += 1

    ret = ""
    for c in string:
        ret += c
    return ret

### TESTS
print(no_repeats("aaabbc")) #acabac
print(no_repeats("aaab")) #None
print(no_repeats("aaaabbc")) #ababaca

### ADMIN SOLUTION
from collections import defaultdict
import heapq

def rearrange(string):
    frequencies = defaultdict(int)
    for letter in string:
        frequencies[letter] += 1

    heap = []
    for char, count in frequencies.items():
        heapq.heappush(heap, (-count, char))

    count, char = heapq.heappop(heap)
    result = [char]

    while heap:
        last = (count + 1, char)
        count, char = heapq.heappop(heap)
        result.append(char)

        if last[0] < 0:
            heapq.heappush(heap, last)

    if len(result) == len(string):
        return "".join(result)
    else:
        return None
