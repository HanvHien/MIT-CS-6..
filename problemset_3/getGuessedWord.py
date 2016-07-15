def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
   
    secretPrint = []
    for l in secretWord:
        if l  in lettersGuessed:
             secretPrint.append(l)
        else:
             secretPrint.append(' _ ')

    return ''.join(secretPrint)

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

print getGuessedWord(secretWord, lettersGuessed)