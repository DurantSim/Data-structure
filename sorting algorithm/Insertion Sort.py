"""
Insertion sort
Best case: O(n), only go through for loop and check while loop condition only once when condition are no meet on first time
Worst case: O(n^2), go through for loop for list and check while loop all way back to index 0 of list
"""
def insertion_sort(list):
    for i in range(1,len(list)):
        temp_val = list[i]      #store value in tmp var
        j = i-1
        while j >= 0 and list[j] > temp_val:
            list[j+1] = list[j]
            j-=1
        list[j+1] = temp_val

    return list

