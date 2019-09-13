"""
@author Zach Stoebner
@date 9-12-2019
@descrip You have n fair coins and you flip them all at the same time.
          Any that come up tails you set aside. The ones that come up
          heads you flip again. How many rounds do you expect to play
          before only one coin remains?

          Write a function that, given n, returns the number of rounds
          you'd expect to play until one coin remains.
"""
import random

#flip_coin
#Note: emulates a fair coin flip, returns True if tails and False if heads
#Complexity: O(1)
def flip_coin():

    random.seed(42)

    while True:
        yield True if random.randint(0,1) == 1 else False

#rounds
#Note: recursively counts the number of rounds that occur for n coinflips
#Complexity: O(n)
count = 0
def rounds(n):

    global count

    if n == 0:
        return count

    count += 1
    if flip_coin():
        return rounds(n-1)
    else:
        return rounds(n)

### TESTS
print(rounds(0)) #0
print(rounds(1)) #1
print(rounds(30)) #31
print(rounds(40)) #71
print(rounds(300)) #371

### ADMIN SOLUTION

def coins(n):
    return log(n, 2)
