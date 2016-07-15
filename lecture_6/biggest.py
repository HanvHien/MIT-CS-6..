def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    big = []   # b is a list 
    if aDict == {}:
        return 
    else:
        for k, v in aDict.items():
            big.append([len(v),k])

        m = max(big)
        big.sort()
        s = ''
        for l in big:
            if l[0]==m[0]:
                s= s+l[1]+' '
    return s.rstrip()


print biggest({'a': [14, 13, 20, 10, 8, 12, 17, 20], 'c': [20, 5, 6], 'b': [11, 6], 'd': [5, 15, 18, 6]})
print biggest({})