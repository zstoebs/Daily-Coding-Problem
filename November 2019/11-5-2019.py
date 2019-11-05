"""
@author Zach Stoebner
@date 11-5-2019
@descrip Alice wants to join her school's Probability Student Club.
Membership dues are computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a
five followed by a six. Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five
followed by a five.

Which of the two games should Alice elect to play? Does it even matter?
Write a program to simulate the two games and calculate their expected value.
"""

# The first one is 6 given 5 P(6 | 5) and the second one is 5 given 5 P(5 | 5).
# But rolling any number is statistically independent b/w rolls
# and the sample space for two dice rolls is 6 x 6 b/c there are 6 ways
# after rolling one number to get any other number.

# The probability for the end condition for each is 1 / 36.
# Therefore it doesn't matter which game Alice plays.

import random

#six_five
#Return expected value of payment
def dice_rolls(n1,n2):

    count = 0
    def helper():
        nonlocal count, n1

        first = random.randint(1,6)
        count += 1
        while first != n1:
            first = random.randint(1,6)
            count += 1

        return True

    while helper():
        second = random.randint(1,6)
        count += 1
        if second == n2:
            return count

### TESTS

print("Game 1: ")
counts = 0
for i in range(36):
    counts += dice_rolls(6,5)
print(counts / 36)

print()

print("Game 2: ")
counts = 0
for i in range(36):
    counts += dice_rolls(5,5)
print(counts / 36)

"""
Game 1:
40.888888888888886

Game 2:
42.638888888888886

"""
# If you keep doing this you get pretty similar results for both
# I'd expect the averages of these up to infinity iterations would be nearly identical
