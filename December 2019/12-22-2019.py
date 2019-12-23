"""
@author Zach Stoebner
@date 12-22-2019
@descrip There are N prisoners standing in a circle, waiting to be executed.
The executions are carried out starting with the kth person, and removing every successive
kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand in order to
be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so
you should return 3.

Bonus: Find an O(log N) solution if k = 2.
"""

# I think the problem is taking into account the shrinking set of prisoners but I'm going to assume
# that we're using the original indices.
# Under this premise, for k=2, the last survivor will be the largest odd number which can be found
# in constant time.

# if N and k have gcd=1, then the graph is connected; otherwise, it's disconnected
def gcd(n,k):

    mod = n % k
    if mod == 0:
        return k
    else:
        return gcd(k,mod)

# last_survivor
# Given number of people N and k, returns the spot in the circle to discern the last survivor
# Complexity: O(N)
def last_survivor(N,k):

    kth = k
    order = []
    for _ in range(N):
        if kth == 0:
            order.append(N)
            kth = 1
        else:
            order.append(kth)
            kth = (kth + k) % N

    return order[-1]

###TESTS
print(last_survivor(5,2)) #5

###ADMIN SOLUTION
#Complexity: O(N)
def helper(n, k):
    if n == 0:
        return 0
    else:
        return (helper(n - 1, k) + k) % n

def last_one_standing(n, k):
    people = range(1, n + 1)
    return people[helper(n, k)]

print(last_one_standing(5,2)) #3


#Complexity: O(logN)
def last_one_standing1(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2 * last_one_standing1(n / 2) - 1
    else:
        return 2 * last_one_standing1(n / 2) + 1
