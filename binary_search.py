def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and found == False:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

test_list = [0,1,2,8,13,17,19,32,42]
print(binary_search(test_list, 0))