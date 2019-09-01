"""
Author: Zach Stoebner
Created on: 8-10-2019
Descrip:

What does the below code snippet print out?
How can we fix the anonymous functions to behave as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())

"""

"""
let l{x} be a lambda function and its return value x

functions should look like this after first for loop:
functions = [l{0},...,l{9}]
but looks like [l{9}...l{9}] because lambda: i references i, not
passed by value so the entire list is set to the last eval of i which is 9

Therefore can bypass reference by creating nested lambdas and passing i as arg
to set inner lambda to outer arg and dereference during the for loop

"""
functions = []
for i in range(10):
    functions.append((lambda x: (lambda: x))(i))

for f in functions:
    print(f())

###ADMIN SOLUTION
functions = []
for i in range(10):
    functions.append(lambda i=i: i)

for f in functions:
    print(f())
