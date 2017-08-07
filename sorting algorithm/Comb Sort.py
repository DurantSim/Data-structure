"""
Comb sort
Best case: O(n log n) , where in inner loop of element in list, it will compare with element between gap and the gap will keep decrease
                        and at 1 point it will become 1. When gap is 1, it perform bubble sort for 1 time. Gap comparing allow cutting down
                        comparison, making time complexity down to log n time.
Worst case: O(n^2) , where if shrink factor is nearly proportional to N length of list, making the comparison of elements between gap
                     does not significally help in reducing the "comb" sort
"""
def comb_sort(list):
    shrink_factor = 1.3
    gap = int(len(list)//shrink_factor)

    sorted = 1
    while sorted == 1:
        if gap == 1:
            sorted = 0       #indicate this will be last loop

        i=0
        while i + gap < len(list):      #bubble sort with gap increment
            if list[i] > list[i+gap]:
                list[i],list[i+gap] = list[i+gap],list[i]
            i+=1

        gap = int(gap//shrink_factor)
    return list