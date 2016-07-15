def flatten(aList):
#    import pdb; pdb.set_trace()   
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    if len(aList) == 0:
       return []
    if type(aList[0]) == list:
        return flatten(aList[0]) + flatten(aList[1:])
    return aList[:1] + flatten(aList[1:])




print flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])