def isPalindrome(aString):
    '''
    aString: a string
    '''
    # Your code here
    l = len(aString)
    retval = True
    for i in range(l):
        if aString[i] != aString[l-(i+1)]:
            retval = False

    return retval

print isPalindrome('parterretrap')
print isPalindrome('lepel')
print isPalindrome('astrind')
print isPalindrome('')