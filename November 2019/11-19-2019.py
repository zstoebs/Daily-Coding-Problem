"""
@author Zach Stoebner
@date 11-19-2019
@descrip You are given an array of nonnegative integers. Let's say you start
at the beginning of the array and are trying to advance to the end. You can advance
at most, the number of steps that you're currently on. Determine whether you can get
to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5,
so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
"""
#hopscotch
#Plays hopscotch on an array and determines if it's possible given the values
#Complexity: O(n)
def hopscotch(arr=list()):

    n = len(arr)

    cur = 0
    start = None
    while cur < n:
        start = arr[cur]
        if start == 0:
            return False

        try:
            mx = max(arr[cur+1:cur+start+1])
            # when it can jump past the end of the array
            if cur + start + 1 >= n:
                return True

        # occurs when at the last element and it's greater than 0
        except ValueError:
            return True

        cur += 1
        while arr[cur] != mx:
            cur += 1

    return True

### TESTS
t1 = [1, 3, 1, 2, 0, 1]
print(hopscotch(t1)) #True
t2 = [1, 2, 1, 0, 0]
print(hopscotch(t2)) #False
t3 = [5,0,0]
print(hopscotch(t3))
