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
