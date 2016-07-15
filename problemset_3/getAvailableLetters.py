def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string

    allAvailable = string.lowercase
    listAll = list(allAvailable)
    for l in lettersGuessed:
        listAll.remove(l)

    return ''.join(listAll)





lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

print getAvailableLetters(lettersGuessed)
