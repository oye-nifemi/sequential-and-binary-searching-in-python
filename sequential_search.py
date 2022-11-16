def finder(findee):
    the_list = [12,3,45,6,95,20,75,42]
    for i in the_list:
        if findee in the_list:
            return True
        else:
            return False
        
print(finder(6))

def finder2(findee):
    d = [0,1,3,6,9,15,27,49,68]
    for i in range(len(d)):
        if d[i] == findee:
            return True
        elif d[i] > findee:
            return False
    return False
print(finder2(10))