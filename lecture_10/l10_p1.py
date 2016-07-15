for j in [0,1,3,5]:

    L = [2, 0, 1, 5, 3, 4]
    val = 0
    for i in range(0, j):
        print 'num', i
        val = L[L[val]]
        print L[val], L[L[val]]

    print 'val :' , val
    print '----'