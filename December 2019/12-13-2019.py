"""
@author Zach Stoebner
@date 12-13-2019
@descrip Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses subtractive
notation for numbers such as IV and XL.

For the input XIV, for instance, you should return 14.
"""

# roman_to_decimal
# Converts a number in Roman numerals to decimal
# Complexity: O(n)
def roman_to_decimal(roman=""):

    numerals = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    prev = 0
    count = 0
    for num in reversed(roman):
        if prev > numerals[num]:
            count -= numerals[num]
            prev = 0
        else:
            prev = numerals[num]
            count += prev

    return count

###TESTS
print(roman_to_decimal("X"))
print(roman_to_decimal("IX"))
print(roman_to_decimal("IV"))
print(roman_to_decimal("III"))
print(roman_to_decimal("XIV"))
print(roman_to_decimal("XL"))

"""
10
9
4
3
14
40
"""

### ADMIN SOLUTION
def decimate(s):
    decimal_map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    total = 0
    for i in range(len(s) - 1):
        if decimal_map[s[i]] >= decimal_map[s[i + 1]]:
            total += decimal_map[s[i]]
        else:
            total -= decimal_map[s[i]]
    total += decimal_map[s[-1]]

    return total
