def prefix(list,i):
    node = list[i]
    print("index:" + str(i) + " value:"+str(node))              #can modify to return value in list
    left_node = i*2+1
    right_node = i*2+2

    if left_node > len(list) or right_node > len(list):
        return

    prefix(list,left_node)
    prefix(list,right_node)


def infix(list,i):
    node = list[i]
    left_node = i * 2 + 1
    right_node = i * 2 + 2

    if left_node > len(list) or right_node > len(list):
        print("index:" + str(i) + " value:" + str(node))        #can modify to return value in list
        return

    infix(list, left_node)
    print("index:" + str(i) + " value:" + str(node))            #can modify to return value in list
    infix(list, right_node)


def postfix(list,i):
    node = list[i]
    left_node = i * 2 + 1
    right_node = i * 2 + 2

    if left_node > len(list) or right_node > len(list):
        print("index:" + str(i) + " value:" + str(node))        #can modify to return value in list
        return

    postfix(list, left_node)
    postfix(list, right_node)
    print("index:" + str(i) + " value:" + str(node))            #can modify to return value in lists