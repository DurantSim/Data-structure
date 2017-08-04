"""
Merge Sort
Best case & worst case: O(n log n) , where process of breaking list to equal length 1 is a must, and comparison are only
                                     took maximum n length if in process of comparison, all small value are in left list
                                     and it will also loop through right list to append into final result list.
"""
def merge_sort(list):
    if len(list) <=1:
        return list

    left = []
    right = []
    for i in range(0,len(list)):        #splitting action happen
        if i < len(list)/2:
            left.append(list[i])
        else:
            right.append(list[i])

    left = merge_sort(left)             #recursive split list to smaller
    right = merge_sort(right)           #recursive split list to smaller

    return merge(left,right)


def merge(left,right):
    result = []

    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:          #if first value in list left is smaller than first val in list right,append to result list
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    while len(left)!=0:                 #if either left list or right list have component left, just append remainder to result list
        result.append(left[0])
        left.pop(0)

    while len(right)!=0:
        result.append(right[0])
        right.pop(0)

    return result
