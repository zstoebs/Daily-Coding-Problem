"""
@author Zach Stoebner
@date 9-15-2019
@descrip Let's represent an integer in a linked list format
          by having each node represent a digit in the number.
          The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in
the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
"""
#like binary, any decimal num can be represented as the sum of 10^index (0-based) times the symbol (0-9)
#therefore, can easily compute the nums from the LLs, then convert to string, and add to list

#LL_sum
#Note: returns the LL representation of the sum of two given LL nums
#Complexity: O(n1 + n2) where n1 and n2 represent the number of digits in num1 and num2
def LL_sum(num1,num2):

    #helper function to convert nums to decimal
    def convert(num):
        total = 0
        for i,digit in enumerate(num):
            total += digit * (10**i)
        return total

    #summing and converting to LL
    dec1 = convert(num1)
    dec2 = convert(num2)
    str_sum = str(dec1+dec2)
    sum = list([])
    for char in str_sum[::-1]:
        value = ord(char) - 48
        sum.append(value)

    return sum

num1 = [9,9]
num2 = [5,2]
print(LL_sum(num1,num2)) #[4,2,1]

### ADMIN SOLUTION
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def add(node0, node1, carry=0):
    if not node0 and not node1 and not carry:
        return None

    node0_val = node0.val if node0 else 0
    node1_val = node1.val if node1 else 0
    total = node0_val + node1_val + carry

    node0_next = node0.next if node0 else None
    node1_next = node1.next if node1 else None
    carry_next = 1 if total >= 10 else 0


    return Node(total % 10, add(node0_next, node1_next, carry_next))
