"""
@author Zach Stoebner
@date 12-9-2019
@descrip Spreadsheets often use this alphabetical encoding
for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ",
"AAA", "AAB", ....

Given a column number, return its alphabetical column id.
For example, given 1, return "A". Given 27, return "AA".
"""

# This is a base 26 numbering system essentially

# convert_number_to_alphabase
# Returns the alphabase number equivalent
# Complexity: O(n)
def convert_number_to_alphabase(number):

    alphabet = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "J",
    11: "K",
    12: "L",
    13: "M",
    14: "N",
    15: "O",
    16: "P",
    17: "Q",
    18: "R",
    19: "S",
    20: "T",
    21: "U",
    22: "V",
    23: "W",
    24: "X",
    25: "Y",
    26: "Z"
    }

    div = number - 1
    ret = ""
    while div > 0:
        rem = div % 26
        div = (div - 1) // 26
        ret = alphabet[rem] + ret

    return ret

### TESTS
num = 1
print(convert_number_to_alphabase(num))
num = 27
print(convert_number_to_alphabase(num))
num = 52
print(convert_number_to_alphabase(num))

### ADMIN SOLUTION
def encode(n):
    s = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        s = chr(65 + remainder) + s
    return s
