"""
@author Zach Stoebner
@date 10-10-2019
@descrip You are given n numbers as well as n probabilities
that sum up to 1. Write a function to generate one of the
numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities
[0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the
time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
"""

import random as rnd

rnd.seed(42)

def generate_w_prob(L,probs):

     while True:
        distr = rnd.random()
        print(distr)
        ind = 0
        value = None
        for prob in probs:
            if ind == 0 and distr <= prob:
                value = L[ind]
            elif distr > probs[ind] and distr <= prob:
                value = L[ind+1]
            if ind != 0:
                ind += 1
        yield value

### TESTS
L = [1,2,3,4]
p = [0.1, 0.5, 0.2, 0.2]
for _,num in zip(range(100),generate_w_prob(L,p)):
    print(num)

#My solution is wrong

### ADMIN SOLUTION
from random import random
from bisect import bisect_left

def preprocess(probs):
    lst = []

    current_val = 0
    for p in probs:
        current_val += p
        lst.append(current_val)

    return lst

def distribute(nums, arr):
    r = random()
    i = bisect_left(arr, r)
    return nums[i]
