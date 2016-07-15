def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    t=min(a,b)

    while (t >= 1):
        if (t==1):
            return 1
        elif (a%t==0 and b%t==0):
            return t
        else:
            t -=1



print gcdIter(2,12)
print gcdIter(6,12)
print gcdIter(9,12)
print gcdIter(17,12)