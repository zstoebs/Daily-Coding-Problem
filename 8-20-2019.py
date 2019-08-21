"""
Author: Zach Stoebner
Created on: 8-20-2019
Descrip:

Given an even number (greater than 2),
return two prime numbers whose sum will
be equal to the given number.

If there are more than one solution
possible, return the lexicographically
smaller solution.

"""
#I love prime numbers so, so much
#know that there will always be a solution due to Goldbach's conjecture

#goldbach
#Note: returns two prime numbers that sum to passed number, assumes number > 2
#Complexity: O(n^2)
def goldbach(number):

    #isPrime
    #Note: checks if number is prime
    def isPrime(less):
        #if less is 1 or 2, passes loop, returns true
        for least in range(2,less):
            #if least divides less, not prime
            if less % least == 0:
                return False
        return True

    #finding two primes that add up to number
    for lesser in reversed(range(1,number)):
        if isPrime(lesser) and isPrime(number-lesser):
             return sorted([lesser,number-lesser])
             #automatically returns lexicographically smallest pair
             # because smallest differences
             # are visited first due to reversed range


### TESTS
print(goldbach(18)) #[1,17]
                    # could also be [7,11] but reversed ensures lexic. smallest
print(goldbach(4)) #[1,3]
print(goldbach(40)) #[3,37]
print(goldbach(100004)) #[1,100003]
print(goldbach(123468)) #[11,123457]


### ADMIN solution
def primesum(self, n):
    for i in xrange(2, n):
        if self.is_prime(i) and self.is_prime(n - i):
            return i, n - i

def is_prime(self, n):
    if n < 2:
        return False

    for i in xrange(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True
