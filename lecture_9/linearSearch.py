def linearSearch(L, x):
    count = 0
    for e in L: 
        count += 1
        if e == x:
            count += 1
            return count
    count += 1
    return  count



print linearSearch([21, 1, 25, 22, 30, 13, 7, 24, 12], 24)