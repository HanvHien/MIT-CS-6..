def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string

    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # Your code here
    l1 = len(str1)
    l2 = len(str2)
    if l1 != l2:
        return False
    else:
        if (str1[0:l1 - (l1 - 1)] == str2[l2 - 1:l2]):
            if (l1>0 and l2>0):
                return (True and semordnilap(str1[l1 - (l1 - 1):] , str2[:l2 - 1]))
            else:
                return True    
        else:
            return False


print semordnilap('rats live on', 'no evil star') 