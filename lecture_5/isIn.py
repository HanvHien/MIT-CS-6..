def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    lo = 0
    up = len(aStr)
    h = (lo + up) / 2

    if (len(aStr)==1):
        if (char == aStr[h]):
            return True
           
        else:
            return False
    elif len(aStr) > 0:
        if (char == aStr[h]):
            return True
        elif (char < aStr[h]):
            up = h-1
            return (True and isIn(char, aStr[lo:h]))
        elif (char > aStr[h]):
            lo = h+1
            return (True and isIn(char, aStr[h:up]))
        else:
            return False
    else:
        return False

print isIn('g', 'adhjkz')
