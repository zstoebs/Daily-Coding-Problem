"""
Author: Zach Stoebner
Created on: 8-24-2019
Descrip:

Given a function f, and N return a
debounced f of N milliseconds.

That is, as long as the debounced
f continues to be invoked, f itself
will not be called for N milliseconds.

"""

import time

#debounce
#Note: executes f after N milliseconds (ms)
def debounce(f,N):

    ms = N/1000
    time.sleep(ms)
    return f

t1 = time.time()
print(debounce((lambda x:x)(0),10000)) #0
t2 = time.time()
print(t2-t1) #10.000496864318848
