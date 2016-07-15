
def testinput(guessedLetters):
    s = raw_input('Please guess a letter: ')
    while s in guessedLetters:
        print 'That letter is already given'
        s = raw_input('Please guess a letter: ')
    guessedLetters.append(s)

    return (guessedLetters , s)

