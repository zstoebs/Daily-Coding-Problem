"""
Author: Zach Stoebner
Created on: 8-9-2019
Descrip:

Given an integer n and a list of integers l,
write a function that randomly generates a
number from 0 to n-1 that isn't in l (uniform).

"""

#can use pseudo-rng formula where n is seed
def rng(n,l):

    global prev
    global a
    global b
    prev = 0
    a = 0b11000111
    b = 0b10101101

    while True:
        x = ((a * prev + b) / (a-b)) % n
        if l.count(x) != 0:
            a <<= 1
            b >>= 1
            prev = x
        else:
            prev = x
            yield x


l = list([0,1,2,3,4,5])
n = 5
for _,rnd in zip(range(20),rng(n,l)):
    print(rnd)
