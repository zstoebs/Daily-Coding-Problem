"""
@author Zach Stoebner
@date 10-21-2019
@descrip Given an arithmetic expression in Reverse Polish Notation,
write a program to evaluate it.

The expression is given as a list of numbers and operands.
For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
should return 5, since it is equivalent to
((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
"""

#Know from data structures course that reverse polish notation can be decoded using a stack or a binary tree
#Postfix notation can be evaluated w/ post-processing in a tree traversal

#reverse_polish
#Returns the answer to the reverse polish notation
#Traverses the expression and replaces initial values w/ their computed values
#Complexity: O(N^2)
def reverse_polish(expr=list()):

    ops = {'+' : lambda x,y : x + y,
    '-' : lambda x,y : x - y,
    '%' : lambda x,y : x % y,
    '*' : lambda x,y : x * y,
    '/' : lambda x,y : x / y,
    '//' : lambda x,y : x // y,
    '&' : lambda x,y : x & y,
    '|' : lambda x,y : x | y,
    '^' : lambda x,y : x ^ y,
    }

    while len(expr) > 1:
        i = 0
        while (expr[i] not in ops.keys()):
            i += 1
        op = ops[expr[i]]
        eval = op(expr[i-2],expr[i-1])
        expr.insert(i,eval)

        # popping operator
        expr.pop(i+1)
        # popping second operand
        expr.pop(i-1)
        # popping first operand
        expr.pop(i-2)

    return expr[0]

### TESTS
expr = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
print(reverse_polish(expr)) #5.0

# Using a tree would be faster b/c it would be O(nlogn) time to insert into the tree and then O(V+E) ~ O(n) time to evaluate
