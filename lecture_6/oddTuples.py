def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    newTuple = ()
    for t in range(0,len(aTup),2):
        newTuple = newTuple + (aTup[t],)

    return newTuple      

print oddTuples(('I', 'am', 'a', 'test', 'tuple'))