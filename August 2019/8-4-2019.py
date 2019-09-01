"""
Author: Zach Stoebner
Created on: 8-4-2019
Descrip: 
Given three 32-bit integers x, y, and b, 
return x if b is 1 and y if b is 0, 
using only mathematical or bit operations. 
You can assume b can only be 1 or 0.

"""

def bitwiseOps(x,y,b):
    assert(b == 1 or b == 0)
    
    if (b & 1):
        return x
    else:
        return y

print(bitwiseOps(2,3,0))

###CORRECT SOLUTION
def switch(x, y, b):
    return (x * b) | (y * (1 - b))
#https://www.dailycodingproblem.com/solution/85?token=25b2b0a442aaaf4848bfbe9a28fd3c65594d8d23a47dc7e3c47a676db04ae729cd45ca76