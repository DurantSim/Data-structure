
"""
Selection sort
Best case : O(n^2) complexity , because it take outer loop through list, and compare with inner loop through list to check smallest value
Worst case: O(n^2) complexity , because it take outer loop through list, and compare with inner loop through list to find smallest value
"""
def selection_sort(list):

    for x in range(0,len(list)-1):
        least_ind = x                   #assume x hold the least value
        least_val = list[least_ind]

        for y in range(x+1,len(list)):
            compare = list[y]           #take value from list in index y
            if compare < least_val:
                least_val = compare     #update value if value of compare is greater than value in least val
                least_ind = y           #least will hold the index which contain the smallest value
        print(list)

        if least_ind != x:              #value swapping
            temp = list[x]
            list[x] = list[least_ind]
            list[least_ind] = temp

    return list