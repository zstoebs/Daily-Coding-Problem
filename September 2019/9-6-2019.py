"""
@author Zach Stoebner
@date 9-6-2019
@details Given a sorted list of integers,
          square the elements and give the output in sorted order.

          For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""

def square_sort(ints):

    for i,int in enumerate(ints):
        ints[i] = int**2

    return sorted(ints)

ints = [-9, -2, 0, 2, 3]
print(square_sort(ints))

### ADMIN SOLUTION

def square_sort(lst):
    negatives = [x for x in lst if x < 0]
    non_negatives = [x for x in lst if x >= 0]

    negatives_square_sorted = [x ** 2 for x in reversed(negatives)]
    non_negatives_square_sorted = [x ** 2 for x in non_negatives]

    return _merge(negatives_square_sorted, non_negatives_square_sorted)


def _merge(left_lst, right_lst):
    result = []

    i = j = 0

    while i < len(left_lst) and j < len(right_lst):
        if left_lst[i] < right_lst[j]:
            result.append(left_lst[i])
            i += 1
        elif left_lst[i] > right_lst[j]:
            result.append(right_lst[j])
            j += 1
        else:
            result.append(left_lst[i])
            result.append(right_lst[j])
            i += 1
            j += 1

    result.extend(left_lst[i:])
    result.extend(right_lst[j:])
    return result
