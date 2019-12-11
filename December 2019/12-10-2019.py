"""
@author Zach Stoebner
@date 12-10-2019
@descrip Given a string of digits, generate all possible
valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C,
and D are numbers between 0 and 255. Zero-prefixed numbers,
such as 01 and 065, are not allowed, except for 0 itself.

For example, given "2542540123", you should return
['254.25.40.123', '254.254.0.123'].
"""

#This is a stars and bars problem where the dots are the bars and the numbers are the stars

import itertools

# gen_ips
# Generates all IP addresses where each of 4 sections is b/w 0 and 255
# Complexity:
def gen_ips(digits=""):

    length = len(digits)

    # checks the number prior to each of three periods "." to validate if it's an IP
    # Complecity: O(n)
    def validate_ip(ip=""):

        count = 0
        prev = 0
        length = len(ip)
        while count < 4:
            if count == 3:
                i = length - 1
                sect = ip[prev:]
            else:
                i = ip.find(".",prev)
                sect = ip[prev:i]

            if sect != '' and sect != ' ':
                value = int(sect)
            else:
                return False

            # periods are right next to each other
            if len(sect) == 0 or sect.find('.') != -1:
                return False
            # zero prefix
            if len(sect) > 1 and sect[0] == '0':
                return False
            # not in valid range
            if not value >= 0 or not value <= 255:
                return False


            prev = i + 1
            count += 1

        return True

    # creating a list of digits for quick insert
    splits = [digit for digit in digits]

    # creating sorted order combinations of 3 indices for "." insertion
    inds = [ind for ind in range(length)]
    combs = itertools.combinations(inds,3)
    valid_ips = []
    for comb in combs:

        ip_list = splits.copy()

        # inserting in reverse order so that later elements are pushed back and prior inds don't change
        for i in reversed(comb):
            ip_list.insert(i,'.')

        # creating a string of digits and periods
        ip = ""
        for elem in ip_list:
            ip += elem
        if validate_ip(ip):
            valid_ips.append(ip)

    return valid_ips

### TESTS
digits = "2542540123"
print(gen_ips(digits)) #['254.25.40.123', '254.254.0.123']

### ADMIN SOLUTION

def generate_IP_addresses(s, parts=[]):
    addresses = []

    if len(parts) > 4:
        return []

    if not s:
        if len(parts) == 4:
            return [".".join(parts)]
        else:
            return []

    addresses += generate_IP_addresses(s[1:], parts + [s[:1]])

    if len(s) > 1 and 10 <= int(s[:2]) <= 99:
        addresses += generate_IP_addresses(s[2:], parts + [s[:2]])

    if len(s) > 2 and 100 <= int(s[:3]) <= 255:
        addresses += generate_IP_addresses(s[3:], parts + [s[:3]])

    return addresses
