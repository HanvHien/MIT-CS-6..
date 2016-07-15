def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def search2(L, e):
    for i in L:
        if i == e:
            return True
        elif i > e:
            return False
    return False

def search3(L, e):
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)

print search([0, 1, 2, 3, 4], 2)
print search([0, 1, 2, 3, 4], 5)
print search([], 2)

print search2([0, 1, 2, 3, 4], 2)
print search2([0, 1, 2, 3, 4], 5)
print search2([], 2) 

print search3([0, 1, 2, 3, 4], 2)
print search3([0, 1, 2, 3, 4], 4)
print search3([], 2)
