"""
Cocktail sort:
Best case: O(n) , if first loop of bubble sort found out no swap action performed, it means list is sorted
Worst case: O(n^2) , looping backward and forward with bubble sort for entire list, until 1 of looping does not perform any swap
"""
def cocktail_sort(list):
    sorted = 0
    i = 0
    j = len(list)-1

    while sorted != 1:
        swap = 0
        for index in range(i,j):        #bubble sort forward
            if list[index]>list[index+1]:
                list[index],list[index+1] = list[index+1],list[index]
                swap +=1
        if swap == 0:       #if no swap action is performed, means list is sorted
            sorted = 1

        j-=1                #more bigger value will be found as looping forward
        swap = 0
        for index in range(j,i,-1):     #bubble sort backward
            if list[index]<list[index-1]:
                list[index],list[index-1] = list[index-1],list[index]
                swap +=1
            print(index)
        if swap == 0:
            sorted = 1

        i+=1                #more smaller value will be found as looping backward

    return list

