"""
Quick sort
Best case: O(n log n) , for simple partition with simple swap
Worst case: O(n^2) , when list is sorted and choose the largest value as pivot, in partition process it will move everything in front for each loop
"""
def quick_sort(list):
    left = 0
    right = len(list)-1

    splitpoint = partition(left,right,list)
    partition(left,splitpoint-1,list)
    partition(splitpoint+1,right,list)

    return list


def partition(left,right,list):
    pivot_val = list[len(list)-1]
    while True:
        while list[left] < pivot_val:   #move pointer to right and will stop if value is greater than pivot
            left +=1
        while list[right] >= pivot_val: #move pointer to left and will stop if value is smaller than pivot
            right -=1
        if left > right:                #if left pointer is greater than right pointer, values which smaller than pivot should be at front of right pointer
            break
        else:
            list[left] , list[right] = list[right],list[left]   #swap latest left pointer position value with latest right pointer position value

    list[left],list[len(list)-1]= list[len(list)-1],list[left]

    return left     #return splitpoint where pivot is in correct position