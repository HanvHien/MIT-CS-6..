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

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for l in secretWord:
        if l not in lettersGuessed:
            return False

    return True


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.
      len (secretword)
    * Ask the user to supply one guess (i.e. letter) per round.
      rawinput

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
      is guessing secretwrd
      getguessedword

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    # FILL IN YOUR CODE HERE...
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is {:} letters long.'.format(len(secretWord))
    print '-------------'
    # Some initialisations
    mistakesMade = 0
    lettersGuessed = []

    while (mistakesMade < 8 and not isWordGuessed(secretWord, lettersGuessed)):
        print 'You have {:} guesses left.'.format(8 - mistakesMade)
        availableLetters = getAvailableLetters(lettersGuessed)
        print 'Available Letters: {:}'.format(availableLetters)
        # raw_input
        s = raw_input('Please guess a letter: ').lower()
        # double input 
        if s in lettersGuessed:
            print "Oops! You've already guessed that letter: {:}".format(getGuessedWord(secretWord, lettersGuessed))
            # print '-------------'               
        else:
            lettersGuessed.append(s)
            if s in secretWord:
                print 'Good guess: {:}'.format(getGuessedWord(secretWord, lettersGuessed))

                # print '-------------'               
            else:
                print 'Oops! That letter is not in my word: {:}'.format(getGuessedWord(secretWord, lettersGuessed))
                mistakesMade += 1
        print '-------------'
        if isWordGuessed(secretWord, lettersGuessed):
            print 'Congratulations, you won!'
    if mistakesMade == 8:
        print 'Sorry, you ran out of guesses. The word was {:}.'.format(secretWord)


hangman('c')
