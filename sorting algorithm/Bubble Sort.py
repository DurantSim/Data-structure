
"""
Bubble sort
Best case: O(n^2) , because each value in list will required comparing with the rest of value in list. After comparing loop is done,
                    greatest value in list will be found
Worst case: O(n^2) , because each value in list, will required comparing with the rest of value in list. If comparing loop determine swap
                     condition is meet, swap will be make and worst case is swap is happen for each comparing loop.
"""
def bubble_sort(list):
    for x in range(len(list)-1,0,-1):       #each outer loop, will find out the largest value in list
        for y in range(0,x):
            if list[y] > list[y+1]:         #compare value at current index with next index, and swap if current index value are greater
                temp = list[y+1]
                list[y+1] = list[y]
                list[y] = temp

    return list
