"""
@author Zach Stoebner
@date 10-27-2019
@descrip Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.
"""

# without using Python's built-in sort methods

#list_sort
#Returns a sorted linked list in O(nlogn) time, implements merge sort
#Complexity: O(nlogn) time and O(n) space
def merge_sort(LL=list()):

    n = len(LL)
    if n == 1:
        return [LL[0]]
    elif n == 2:
        mx = max(LL)
        mn = min(LL)
        return [mn,mx]
    else:

        mid = int(n // 2)
        left = merge_sort(LL[:mid])
        right = merge_sort(LL[mid:])

        sort = list()
        input = 0
        i = 0
        j = 0
        while input < n:
            if i < mid and left[i] < right[j]:
                sort.append(left[i])
                i += 1
            else:
                sort.append(right[j])
                j += 1
            input += 1
        return sort    

### TESTS
t1 = [4,1,-3,99]
print(merge_sort(t1)) # [-3, 1, 4, 99]
