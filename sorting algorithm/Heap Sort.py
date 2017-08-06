"""
Heap sort
Best case & worst case: O(n log n) , since heapify require O(log n) time , and it run through N element in list once to pop from largest
                                     value
"""
def heap_sort(list):
    result = []
    list = heapify(list)  # initialize heap tree

    while len(list)>0:
        list[0],list[len(list)-1] = list[len(list)-1],list[0]   #swap largest parent node with last element in heap tree
        result.insert(0,list[len(list)-1])                            #append largest value found in heap tree to result list
        list.pop(len(list)-1)                                   #pop out largest value from list
        heapify(list)                                           #heapify tree again

    return result


def heapify(list):
    for root in range((len(list)-1)//2,-1,-1):
        root_val = list[root]
        left_child = 2*root+1
        while left_child < len(list):
            if len(list)==left_child+1 or list[left_child]>list[left_child+1] :     #compare which child node value is bigger
                bigger_child = left_child
            else:
                bigger_child = left_child+1

            if list[bigger_child]<=root_val:    #compare parent node value with bigger child node
                break
            else:
                list[bigger_child],list[root] = list[root],list[bigger_child]   #swap if child node value is greater than parent node value

            root = bigger_child                 #change parent node to biggest child node, to continuous heapify
            left_child = 2*bigger_child+1       #change child node to next child node, to continuous heapify

    return list