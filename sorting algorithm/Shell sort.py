def shell_sort(list):
    gap = len(list)//2      #the gap formula can be change to optimize computation speed

    while gap >0:
        for i in range(gap):
            list=gapInsertionSort(i,list,gap)

        gap = gap // 2      #the gap formula can be change to optimize computation speed

    return list

def gapInsertionSort(starting_index,list,gap):
    for item_index in range(starting_index,len(list),gap):
        current_position = item_index
        next_position = current_position+gap

        while next_position <len(list):     #insertion sort between numbers in gap
            if list[current_position] > list[next_position]:
                list[current_position],list[current_position+gap] = list[current_position+gap],list[current_position]
            current_position = next_position
            next_position = next_position+gap

    return list